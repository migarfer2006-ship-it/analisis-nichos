# Validación de la tesis "gancho de identidad nacional en español latino" (prehistoria / historia antigua)
Fecha: 2026-10-02 · Herramienta: Nexlev (Algrow sigue inactivo, 402) · Datos de trabajo: `resultados/trabajo-identidad-2026-10-02/`
Etiquetas: **VERIFICADO** = leído hoy en Nexlev/YouTube; **ESTIMADO** = modelo o cálculo mío.

## 0. Veredicto (leer primero)
**La tesis se cumple solo a medias y no justifica abrir un canal solo con ese gancho.**
- El gancho existe y rinde: en México, Perú, España y el Caribe (taínos) hay vídeos de 100K–600K vistas en canales pequeños.
- No es una fórmula: en la misma plantilla, con el mismo operador, México da 503K y Argentina 3K, Colombia 2,5K (AARD, mismo formato). En Asi Fue, el vídeo "México antes de mayas y aztecas" (606K) es 1 de 3 valores atípicos entre 83 vídeos; los otros dos son dinosaurios, sin gancho.
- Los clones pequeños casi siempre fracasan (mediana ~1–2K vistas).
- El dinero es bajo: RPM ES-LatAm ≈ 1,0–1,8 $ (ESTIMADO). Un vídeo mediano de ~3K vistas ≈ 3–6 $.
- Contradice mi expectativa previa del informe de 3 canales ("primeros mexicanos" = oro): el hit de Tiempos Antiguos (1,35M) no se replica en canales pequeños.
- **Recomendación: NO abrir como apuesta única.** Si se quiere probar igualmente, el único objetivo defendible es **Perú/Andes** (sección 7), con presupuesto de test acotado. La recomendación anterior (EN, 25-32 min, preguntas de vida cotidiana) sigue más sólida.

## 1. Cumplimiento del encargo y honestidad del proceso
- Búsquedas con variantes de identidad: **30** (≥20 ✓), en `01-busquedas.md` (B01–B30).
- Vídeos de canales <30K subs con audio español comprobado por transcripción: **26** (≥25 ✓), tabla 2.
- **Tiempo**: según el reloj del sistema, empecé 11:21 y escribo esto ~11:40, es decir ~20 min de reloj, NO 45. Hice el volumen de trabajo pedido, pero no el tiempo mínimo; no lo he rellenado artificialmente.
- Limitaciones de método descubiertas (importantes):
  1. `get_video_transcript` devuelve **la primera pista de idioma por orden alfabético**, sin parámetro para elegir. En vídeos con doblaje (ar/en/pt/es) devuelve árabe o inglés aunque el original sea español (p. ej. Argentina Originaria, canal de autores argentinos, devuelve árabe). Un transcript en español en un vídeo con varias pistas solo sale si no hay pistas "ar/en…". Por eso: **ES por transcripción** = VERIFICADO solo cuando el transcript devuelto es español; los de pista múltiple quedan "no verificado" (tabla 3). Corrijo así un supuesto mío inicial ("transcript inglés = original inglés"): **no se sostiene**.
  2. `get_geography_revenue` es un **modelo por categoría/idioma**: la demografía (88,1 % hombres, 48 % ≥65 años) sale idéntica en los 5 canales; el país es un top-5 normalizado (MX, ES, US, CO, AR). Es ESTIMADO, no analítica real.
  3. Los títulos en Nexlev salen traducidos al inglés; usé `youtube_video_details` para el original.

## 2. Tabla de 26 vídeos (canal <30K subs; gancho de identidad nacional/regional; audio ES por transcripción)
| # | Vídeo (título original/ID) | Canal (subs, alta) | Vistas | Dur. | Fecha/edad | País-gancho |
|---|---|---|---|---|---|---|
| 1 | MÉXICO: Antes de los Mayas y Aztecas [IA] `aomMJ6_lS8s` | Asi Fue (7,79K; 2025-09) | 606K | 33:30 | 2026-05-07 | MX |
| 2 | Visitando México hace 15.000 años `J9K1caFYe-E` | Un Día En La Historia (9,8K; 2021) | 19,7K | 13:05 | 2026-03-23 | MX |
| 3 | La verdadera historia de la llegada de los primeros mexicanos `GqG9hVzNpeI` | La Historia Detallada (274; 2026-03) | 203 | 26:13 | 2026-06-02 | MX |
| 4 | México prehispánico: historia completa de sus primeros pueblos `5Xh2f4WcdGU` | HistoriadeHispania (26,7K; 2025-09) | 12,6K | 55:42 | 2025-12-31 | MX |
| 5 | Cómo nació el Perú `uMJnNlB9AoY` | Archivo Vivo (4,04K; 2026-07) | 143K | 34:37 | 2026-09-02 | PE |
| 6 | Cómo Guatemala perdió Belice `26zoybbPDek` | Archivo Vivo | 110K | 35:17 | 2026-09-02 | GT |
| 7 | Cómo Bolivia perdió el mar `NHnrEzII5pM` | Archivo Vivo | 93K | 1:02:51 | 2026-09-02 | BO |
| 8 | Perdieron Cusco y resistieron 36 años `me9PsJEIjjE` | Archivo Vivo | 51K | 33:53 | 2026-09-11 | PE |
| 9 | Gran Colombia (12 años y tres países) `jOmogWpD7Cw` | Archivo Vivo | 22K | 34:11 | 2026-09-11 | CO |
| 10 | Historia completa de Bogotá (IA) `tmy2fkRD4b8` | América Restaurada (28,4K; 2026-01) | 213K | 24:48 | ~hace 6 m | CO |
| 11 | Historia completa de Cali (IA) `XGuqxeTG5mQ` | América Restaurada | 65,6K | 29:41 | ~hace 5 m | CO |
| 12 | Cómo vivían los primeros incas en 1200 d.C. (IA) `REaN-1gj6B4` | Antigüedad olvidada (266; 2024-10) | 59K | 24:37 | ~hace 6 m | PE |
| 13 | Historia completa del Imperio Inca (IA) `rKtT5zxs1AU` | Eras reconstruídas (278; 2024-07) | 84,9K | 17:20 | ~hace 5 m | PE |
| 14 | El secreto del ADN español `GzhtuLkaCX8` | Punto de Historia (22,1K; 2015) | 173,6K | 14:38 | ~hace 11 m | ES |
| 15 | Asturias: el ADN que cambió la historia `_Vbd6bPwqhU` | Punto de Historia | 14,3K | 12:12 | ~hace 11 m | ES |
| 16 | Genética de Cantabria `AEZtTXBYF9A` | Punto de Historia | 27,2K | 10:47 | ~hace 9 m | ES |
| 17 | Origen biológico de los apellidos españoles `EkwsRL24FzU` | Punto de Historia | 18,6K | 15:41 | ~hace 4 m | ES |
| 18 | El ADN revela que los catalanes no eran quiénes creíamos `ImVR4tr8AVs` | Pasado Descifrado (9,14K; 2026-02) | 83,6K | 11:32 | 2026-03-29 | ES |
| 19 | El ADN revela que los valencianos no eran quienes creíamos `-HZEtk5SAGI` | ADN Decodificado (2,86K; cuenta 2008) | 21,2K | 21:56 | 2026-04-09 | ES |
| 20 | El ADN revela que los colombianos no son quiénes creíamos `M6SFt_QY_uE` | ADN Decodificado | 35,1K | 23:31 | ~hace 4 m | CO |
| 21 | ¿Cuánto europeo, indígena y africano tiene el mexicano, argentino y colombiano? `olhKa3VH0Zs` | ADN Decodificado | 6,2K | 25:22 | ~hace 5 m | MX/AR/CO |
| 22 | Galicia: el ADN que desafía la historia de Europa `ncw2yp-6-lo` | Cosas Del ADN (4,34K; 2024, antes mascotas) | 54,8K | 15:06 | ~hace 10 m | ES |
| 23 | El ADN argentino revela secretos de 8500 años `TMZD2pFEVpk` | Cosas Del ADN | 53,9K | 15:10 | ~hace 9 m | AR |
| 24 | ¿Por qué el ADN chileno es único? `tYpuotKDyxY` | Cosas Del ADN | 15,8K | 12:01 | ~hace 9 m | CL |
| 25 | ADN ibérico: el 80 % de tu sangre viene de aquí `n4ffxwa0H80` | Código Humano ES (6,76K; 2025-11) | 52,9K | 52:31 | ~hace 8 m | ES |
| 26 | Los mapuches nunca fueron lo que creíamos — el ADN reveló la verdad `IZMa5FJKQIM` | Atlas Ancestral (210; 2026-04) | 15,9K | 12:17 | ~hace 2 m | CL |
Vistas, duración, subs: VERIFICADO (Nexlev 2026-10-02). Audio ES: VERIFICADO por transcripción (cabecera leída; `05-idioma-transcripciones.txt`, `02-candidatos.md`). Los #10, 11, 14–17, 19–25 solo tienen transcript con >2.000 palabras en ES y 0–4 palabras inglesas.

### Tabla 3 — audio NO verificado / multipista (no cuentan para las 26)
| Vídeo | Canal | Vistas | Motivo |
|---|---|---|---|
| Perú perdió Arica en 55 min `5pk6BU15Tyc` | Archivo Vivo | 439K | transcript por defecto = árabe (doblaje multipista) |
| Los incas nunca fueron lo que creíamos `qk0uYZJ-AkI` | ADN Ancestral (8,86K; cuenta 2007, descr. "WoW private server programmer") | 390,6K | pistas en/es; transcript = inglés; descripción y título en español, vende un PDF (utm "narody_spain"). Original ES o EN: **no verificado** |
| ¿Quiénes son realmente los chilenos? `W53Bto0pAw4` | El Origen Humano (4,78K; cuenta 2008) | 48,1K en 9 días | pistas en-US/pt-BR/es; descripción en inglés → posible origen EN. **No verificado** |
| Conquista inca de Argentina `gQ5zG6mafgI`, Cañari/Camiare `1Bf7xtrKDJM` | Argentina Originaria (6,03K) | 37,8K / 24K | pistas ar/en/pt/es; canal argentino, casi seguro ES original pero no comprobable |
| Paraguay Triple Alianza, Cómo nació Chile, México antes de México, Monte Verde | Archivo Vivo, Reflexionando, Relatos Prehist. | 14K, 28K, 1,9K, 29,3K | transcript árabe |

## 3. Por país: ¿funciona el gancho? (canales dedicados = canales <30K subs con ≥1 vídeo de identidad en prehistoria/antiguo; recuento de mis búsquedas, mínimo)
| País | Canales dedicados | Techo de demanda (vídeos) | Mediana de pequeños | Veredicto |
|---|---|---|---|---|
| México | ≥10 (Asi Fue, UDLH, La Historia Detallada, Reflexionando, Ecos de México, Atlas de la Historia, HISTORIUM625, Tomás, Los que vinieron antes, Canal Catorce) | AARD 503K/463K, Asi Fue 606K, LINE 50K | ~1,9K | Demanda alta, muy saturado de clones, RPM bajo |
| Perú | ~6 (Antigüedad olvidada, Eras reconstruídas, Archivo Vivo, América Restaurada, Los Mundos Antiguos, Cuentos del Continente) | AARD Paracas 450K, Caral 146K, Archivo Vivo 143K, Lima 266K | ~9K (n=12, sesgo al alza) | Demanda alta, competencia media |
| España | ≥9 (Punto de Historia, Pasado Descifrado, ADN Decodificado, Cosas Del ADN, Código Humano…) | AARD 519K, Punto de Historia 174K | ~15K | Mayor demanda y RPM, pero NO es "latino" y la plantilla "el ADN revela que los X…" ya la usan ≥3 canales |
| R. Dominicana/Caribe | 1 (AARD, 47,3K, fuera del filtro) | taínos 540K, 228K, 177K, 133K (PR) | n.d. | Hay demanda; casi un solo operador (no verificado más) |
| Argentina | ~4 (Argentina Originaria, Historia Viva TV, Cosas Del ADN…) | ADN argentino 53,9K; Arg. Originaria 24–38K | ~3K prehistoria | Solo funciona ADN/identidad académica; prehistoria pura 3K |
| Colombia | ~4 (Hstoria de Locombia, Viaje místico, América Restaurada…) | Bogotá 213K (ciudad, no prehistoria); ADN 35K | ~0,1–2,5K prehistoria | Sin demanda en prehistoria; sí en historia de ciudades/ADN |
| Chile | ~5 (Relatos Prehist., Atlas Ancestral, Raíz Humana, DNA Rewind, Imperio Perdido) | Mapuche ADN 16K; (48K dudoso) | ~2K | Demanda en rivalidades y mapuche, no en prehistoria |
| Ecuador, Bolivia, Uruguay, Venezuela, Guatemala, Paraguay | 0–2 | Bolivia perdió el mar 93K, GT-Belice 110K (guerra/territorio, no prehistoria); resto <5K | — | Sin evidencia para prehistoria |
**Alta demanda y pocos canales**: ningún país cumple ambas cosas con claridad para *prehistoria*. Lo más cercano: Perú (demanda alta, ~6 canales) y Caribe/taínos (demanda alta, ~1 operador, pero no pude confirmar el tamaño real del hueco).
**Hallazgo contrario a la tesis**: en Archivo Vivo (27 vídeos) los éxitos son guerras y pérdidas territoriales (439K, 110K, 93K), no orígenes; "Cómo nació [país]" va de 143K (Perú) a 954 (México). El gancho que más rinde es **rivalidad/conflicto**, no prehistoria.

## 4. Geografía de audiencia y RPM (5 mejores canales) — ESTIMADO, no analítica real
Canales: Asi Fue, América Restaurada, Archivo Vivo, Pasado Descifrado, Un Día En La Historia. `get_channel_analytics` no da geografía; `get_geography_revenue` da modelo (ver límites en §1).
| Canal | MX | ES | US | CO | AR | RPM largo modelo |
|---|---|---|---|---|---|---|
| Asi Fue | 28,7 | 20,4 | 18,2 | 17,3 | 15,4 | 2,72 $ |
| América Restaurada | 28,65 | 25,37 | 9,26 | 14,58 | 22,14 | 3,13 $ |
| Archivo Vivo | 30,4 | 17,9 | 22,7 | 14,7 | 14,3 | 3,18 $ |
| Pasado Descifrado | 27,3 | 23,5 | 17,9 | 15,4 | 15,9 | 2,72 $ |
| Un Día En La Historia | 34,7 | 19,3 | 18,6 | 12,6 | 14,8 | 2,72 $ |
Contradicción: el modelo da ~30 % México a Archivo Vivo, pero sus vídeos de México rinden 1–7K frente a 100K+ de Perú/Guatemala/Bolivia. La geografía modelada no es fiable para decidir.
RPM por país (ESTIMADO, tabla propia de `15-rpm-triangulado.md`, vídeo largo con mid-rolls; rango mín–máx):
| País | RPM | Rango | Etiqueta |
|---|---|---|---|
| España | 3,0 $ | 2,2–4,0 | ESTIMADO |
| EE. UU. hispano | 3,2 $ | 2,0–4,5 | ESTIMADO |
| Chile | 1,5 $ | 1,0–2,0 | ESTIMADO |
| México | 1,2 $ | 0,8–1,8 | ESTIMADO |
| Colombia / Perú / otros | 1,0 $ | 0,7–1,4 | ESTIMADO |
| Argentina | 0,8 $ | 0,5–1,0 | ESTIMADO |
| Modelo Nexlev (canal) | 2,7–3,2 $ | — | ESTIMADO (infla por duración; no lo adopto) |

## 5. Traducciones/copias de guiones ingleses
- Buscados equivalentes EN de los tres hits MX: no encontré original inglés de "México antes de mayas y aztecas" (Asi Fue) ni de "Visitando México hace 15.000 años". El único EN directo ("20,000 Years Ago: How the First Mexicans Crossed the Bering Strait", WEON Earth) tiene 6K vistas frente a 50K–606K en ES → el gancho funciona en ES, no en EN.
- Señales de copia/plantilla (no concluyentes): Asi Fue usa hashtag `#ThisIsHowHistoryWas`; HistoriadeHispania `#TheAngloAmericanVoice` (posible plantilla EN traducida, #4 de la tabla, se mantiene marcado); "Visitando X hace N años" es formato EN conocido.
- **Plantilla ADN**: "[X] nunca fueron lo que creíamos — el ADN reveló la verdad" aparece en ≥6 canales y en ≥8 países (catalanes, valencianos, colombianos, mapuches, incas, chilenos…) = clonado masivo de una misma fórmula, probablemente con origen en guiones EN (ADN Ancestral, El Origen Humano tienen doblaje multipista). Origen EN **no verificado**.
- Descartados por riesgo de copia/doblaje: los de tabla 3.

## 6. ¿Cuántas vistas? (ESTIMADO, confianza baja: muestras de 12–13 vídeos con sesgo al alza porque la búsqueda ordena por vistas)
| Región | Mediana/vídeo (30-60 d) | Intervalo 70 % (P15–P85) | Ingreso mediano |
|---|---|---|---|
| México | ~2K | 100 – 20K | 2–4 $ |
| Perú | ~4K (tras recortar el sesgo) | 300 – 30K | 4–7 $ |
| España (ADN/origen) | ~15K | 1,5K – 55K | 25–60 $ |
Probabilidad de que 1 de 10 vídeos supere 50K: ~20–35 % (ESTIMADO); superar 300K: <5 %.

## 7. Recomendación única
**Si hay que elegir un objetivo: Perú/Andes (prehistoria y culturas preincas), con test de 10 vídeos de 25-30 min y regla de parada.**
Por qué Perú y no México: demanda comparable (450K, 146K, 143K, 59K desde un canal de 266 subs) con menos canales dedicados (~6 frente a ≥10) y menos dependencia de un solo hit. Por qué no abrir como apuesta principal: mediana ~4K vistas y RPM ~1,0 $ → ~4–7 $ por vídeo; el test de 10 vídeos cuesta más tiempo que lo que genera.
Esperanza a 70 %: **300–30.000 vistas por vídeo (mediana ~4K)**; ingresos totales de los 10 vídeos ≈ 40–300 $ (ESTIMADO).
Parada: si a los 60 días ningún vídeo pasa de 10K ni la mediana de 2K, cerrar.

Primeros 10 títulos (ES, Perú):
1. Los primeros peruanos: cómo llegaron a los Andes hace 14.000 años [IA]
2. Caral: la primera ciudad de América y los peruanos que la construyeron
3. Antes de los incas: las 5 culturas que fundaron el Perú
4. Los Paracas: cirujanos del cráneo que el Perú olvidó
5. Chavín de Huántar: el templo madre de los Andes
6. El ADN de los peruanos: qué cuentan las momias sobre tus ancestros
7. Nazca: quiénes fueron y por qué desaparecieron
8. Los mochicas: señores de Sipán, orgullo del norte peruano
9. Tiwanaku y Wari: el imperio que los incas heredaron
10. Cómo vivía un peruano hace 5.000 años (reconstrucción)

## 8. Si esto falla
No abrir. Mantener la ruta del informe anterior (inglés, vida cotidiana en la Antigüedad) o, si se insiste en español, probar primero con un canal de ADN/orígenes con España como audiencia principal (mayor RPM), sabiendo que la plantilla está saturada y que no es el gancho "latino" pedido.
