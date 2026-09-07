# Playbook de investigacion - Dashboard Nichos YouTube Faceless

Este documento es el procedimiento que debe seguir el agente (Claude Code, via
herramientas MCP `mcp__claude_ai_Nexlev__*`) en cada pasada, sea manual o
disparada por el cron job. El script `scripts/build_dashboard.py` NO llama a
ninguna API: solo renderiza el HTML a partir de `data/latest.json`. Toda la
recoleccion de datos la hace el agente siguiendo estos pasos.

Todos los umbrales y pesos citados aqui viven en `config.json` — leerlo antes
de empezar y usar sus valores, no los numeros de este documento como fuente
de verdad si difieren.

## 0. Cargar configuracion

Leer `config.json`. De ahi salen: `target_channels_per_section`, los
`criteria` de cada seccion, la `rpm_table_usd_per_1000_views`, los
`ranking_weights` y el `dedup_priority_order`.

## 1. Descubrimiento por seccion

Para cada seccion, lanzar varias queries de categoria/nicho (finanzas,
salud, tecnologia, historia, curiosidades, negocios, true crime, etc.) con:

- `search_niche_finder_channels` (contenido long-form) y
- `search_shorts_niche_finder_channels` (si la seccion admite shorts-driven channels)

Usar `query: "*"` cuando el criterio es puramente numerico (vistas, subs) y
aplicar los filtros numericos que la propia herramienta soporte para reducir
candidatos antes de gastar llamadas de verificacion.

Objetivo: reunir suficientes candidatos brutos para que, tras filtrar, cada
seccion llegue a `target_channels_per_section` (o al minimo de 30 si se ha
escalado el config a produccion completa).

## 2. Verificacion por canal candidato

`search_niche_finder_channels` ya devuelve, por canal, un payload rico:
`channelCreationDate`, `isFaceless`, `isAiChannel`, `isMonetizationEnabled`,
`stats.monthlyViews`, `stats.avgVideoLength`, `stats.uploadsPerWeek`,
`stats.subscribers` y los ultimos videos con vistas/fecha. Repetir
`get_channel_analytics` + `get_daily_analytics` + `check_faceless_channel` +
`check_channel_monetization` para cada candidato del pool de descubrimiento
duplicaria datos que ya tenemos y dispararia el gasto de cuota que motivo la
conversacion de cadencia — así que **el filtrado y el ranking (pasos 3-5) se
hacen primero, solo con el payload del descubrimiento**, y las llamadas de
verificacion por canal se reservan para los finalistas que de verdad van a
salir en el dashboard (el `target_channels_per_section` de `config.json`, no
todo el pool bruto).

Para cada canal finalista, en este orden:

1. `get_channel_analytics` / `get_daily_analytics` / `check_faceless_channel`
   / `check_channel_monetization` — usar SOLO como respaldo si algun campo del
   payload de descubrimiento viene ambiguo o vacio para ese canal en concreto
   (p.ej. `channelCreationDate` ausente). En el resto de casos el dato de
   descubrimiento ya es la fuente de verdad y estas llamadas se omiten.
2. `get_channel_promotions` (`query: "channelProfile"`) — este es el dato que
   el descubrimiento NO trae: ingresos externos (sponsors, afiliados,
   productos propios). Presencia de esto (`sells`, `sponsorCount`,
   `selfPromoCount` > 0) es señal de nicho maduro, no descarta al canal pero
   se guarda como `external_monetization_signals`. Si `scraped: false` el
   canal aun no ha sido rastreado por Nexlev — se guarda como "sin datos" en
   vez de asumir que no vende nada.

Descartar el candidato si no cumple los `criteria` numericos de la seccion en
`config.json` (duracion media de video, vistas/30d, antiguedad, vistas/mes).

**Resultado real de la pasada piloto (2026-09-07):** 4 llamadas de
descubrimiento + 48 llamadas `get_channel_promotions` = 52 llamadas Nexlev en
total para 48 canales finales — muy por debajo de la estimacion inicial de
~570, precisamente por reusar el payload del descubrimiento en vez de
reverificar cada candidato con las 5 herramientas.

Para "senales de produccion por IA" (solo seccion `ia_nichos`): cadencia de
subida alta desde el primer video (>= ~1 video/dia de media en sus primeras
semanas) + consistencia visual de miniaturas (mismo estilo/plantilla en las
ultimas 10-15 miniaturas, revisable con `get_channel_videos`/metadatos de
miniatura si estan disponibles).

## 3. Deduplicacion entre secciones

Un mismo canal (identificado por su **channel_id real**, no por nombre) solo
puede aparecer en la primera seccion de `dedup_priority_order` en la que
califica: `ia_nichos > long_form > faceless_nuevos > faceless_establecidos`.
Si un canal calificaria para varias, se queda solo en la de mayor prioridad y
se descarta de las demas.

## 4. Estimacion de ingresos

Clasificar el canal en una de las 4 categorias de
`rpm_table_usd_per_1000_views` segun su tematica dominante. Calcular:

```
vistas_mensuales_estimadas = views_30d
ingreso_min = vistas_mensuales_estimadas / 1000 * rpm.min
ingreso_max = vistas_mensuales_estimadas / 1000 * rpm.max
```

Guardar siempre con etiqueta "estimado" — nunca presentar como cifra exacta.
`get_video_rpm` puede usarse si esta disponible para afinar el RPM real de
categoria en vez del rango generico de la tabla.

## 5. Ranking 1-10

Para cada canal, normalizar 0-10 estos 4 componentes y combinarlos con los
pesos de `ranking_weights` (documentados en `config.json`, suman 1.0):

- **views_subscribers_ratio** (35%): vistas_30d / subscribers. Ratio alto =
  canal creciendo por SEO/algoritmo, no por marca — puntua mejor.
- **sustained_vph_last_5_10_videos** (30%): vistas-por-hora media de los
  ultimos 5-10 videos (no el pico de un solo video viral).
- **upload_consistency** (20%): regularidad de la cadencia de subida
  (desviacion baja entre intervalos = mejor puntuacion).
- **estimated_revenue** (15%): ingreso estimado medio del rango, normalizado
  contra el resto de candidatos de la misma seccion.

`ranking = round(sum(componente_normalizado * peso))`, acotado a [1, 10].

## 6. Guardar snapshot y generar HTML

Escribir el resultado en `data/latest.json` con este esquema exacto:

```json
{
  "generated_at": "<ISO 8601 UTC>",
  "sections": {
    "ia_nichos": [ {ChannelRecord}, ... ],
    "long_form": [ ... ],
    "faceless_nuevos": [ ... ],
    "faceless_establecidos": [ ... ]
  }
}
```

`ChannelRecord`:

```json
{
  "channel_id": "UC...",
  "name": "...",
  "url": "https://www.youtube.com/channel/UC...",
  "days_since_creation": 0,
  "views_30d": 0,
  "subscribers": 0,
  "category": "finanzas_legal_seguros_salud|tecnologia_negocios|entretenimiento_historia_curiosidades|otros",
  "est_revenue_min_usd": 0,
  "est_revenue_max_usd": 0,
  "is_monetized": true,
  "external_monetization_signals": false,
  "is_faceless": true,
  "avg_video_duration_min": 0,
  "upload_cadence_per_week": 0,
  "vph_recent_avg": 0,
  "views_subscribers_ratio": 0.0,
  "ranking": 0
}
```

Despues ejecutar:

```
python3 scripts/build_dashboard.py
```

Esto sobrescribe `dashboard.html` en la raiz del proyecto. No editar el HTML
a mano — siempre regenerar desde el JSON.

## 7. Cadencia

La cadencia de ejecucion vive **solo** en la definicion del cron job
(`CronCreate`), no en este playbook ni en el codigo. Cambiar de 2x/semana a
diario es editar esa unica expresion cron, sin tocar nada de lo anterior.
