# Verificación final: e-bikes y movilidad para mayores de 60 (español) — 2026-10-01

Complementa `nichos-2026-10-01.md`. Fuentes: 16 búsquedas nuevas con `youtube_search` (ES, MX, AR, US), 2 con `search_niche_finder_channels` (idioma es), `get_video_rpm` en 15 vídeos y `get_batch_channel_metrics_v2` en 10 canales.

## 0. Corrección al informe anterior

**Los vídeos con título en español de Tech Charge, Ebiker, E Biking Today, E Bike Nation y Gr8fully Tedicated son los mismos vídeos en inglés con el título localizado.** Las vistas no son vistas en español:

- "¿Pensando en una bicicleta eléctrica a los 60 años o más?" (Tech Charge): 206.992 vistas. `get_video_rpm` lo devuelve como "Thinking About an E-Bike at 60+?", con 206.992 vistas.
- "10 cosas que a los adultos mayores les habría gustado saber…" (Ebiker): 75.000 vistas, igual que el vídeo en inglés.

Consecuencias:

1. Las cifras de "demanda en español" del informe anterior (33.411 vistas de E Biking Today, 16.390 de Tech Charge) **no demuestran demanda en español**.
2. Esos canales ya ocupan los primeros puestos de la búsqueda en español para este ángulo. Tech Charge sube los vídeos con título en español desde hace 1 a 3 meses. En "bicicleta eléctrica después de los 60 años" (MX) salen Tech Charge en 1.º y 4.º lugar y E Biking Today en 6.º, 7.º y 8.º.
3. Probablemente hay doblaje automático. Un vídeo de Tech Charge tiene RPM limitado por geografía (`geoCapped`, 11,5 antes del tope y 4,34 después), lo que indica audiencia de países de menor RPM. No lo he podido comprobar.

**La competencia pasa de BAJA a MEDIA.** Sigue siendo BAJA solo entre canales nativos en español.

## 1. Test de competencia en español: 16 búsquedas nuevas

| # | Búsqueda (país) | Resultados totales | Qué hay |
|---|---|---|---|
| 1 | bicicleta eléctrica para personas mayores (ES) | 764.319 | Listicles de afiliación. El nativo más alto es innova, con 4.636 vistas. Sin canal editorial para mayores |
| 2 | errores al comprar una bici eléctrica (MX) | 307.292 | Tema genérico con tracción: Mammoth Bikes 296.937 vistas (2024), MP Bicis y Más 116.747 (2022), BANZAI 9.620. Ninguno para mayores |
| 3 | triciclo eléctrico para jubilados (ES) | **43** | Entreruedasespaña (2.372 vistas) y sixthreezero (marca de EE. UU. con títulos en español). El resto es irrelevante |
| 4 | bici eléctrica para abuelos Argentina (AR) | 2.903 | Spots de producto: Tutiendaenergetica 60.604 (2023), ETNNIC 57.839. Sin editorial |
| 5 | bicicleta eléctrica después de los 60 años (MX) | 26.008 | Títulos localizados de Tech Charge (×2) y E Biking Today (×3). Ningún nativo |
| 6 | me arrepentí de comprar una bicicleta eléctrica (ES) | 286 | Reseñas genéricas (el buscador usó resultados de respaldo). Ningún vídeo para mayores |
| 7 | triciclo eléctrico adultos mayores equilibrio (MX) | 387 | Listicles: Rafito Ofertas 7.947, TechZone, Gear Geek, Gadgetron, innova, Consíguelo ahora. Más sixthreezero y TrikeBike Australia (3.426) |
| 8 | qué bicicleta eléctrica comprar si tengo 70 años (AR) | 39.821 | Guías genéricas (Alex Medina MTB 227.415, Mammoth 110.060). Para mayores solo sixthreezero y E Biking Today |
| 9 | bicicleta eléctrica para mayores de 70 consejos seguridad (ES, último año) | 355 | Ebiker, Tech Charge ×3, E Bike Nation ×2, Gr8fully Tedicated: todos títulos localizados. Ningún nativo |
| 10 | marcas de bicicletas eléctricas que quebraron (MX) | 90 | Solo tutoriales de reparación y "15 peores bicis" de Tech Charge (45.262 vistas, localizado). Nada nativo |
| 11 | scooter eléctrico para personas con movilidad reducida (ES) | 4.750 | ~6 tiendas de ortopedia más 4 canales de listicles. El máximo es 28.734 |
| 12 | bicicleta eléctrica plegable para viajar en autocaravana (ES) | 1.981 | Al menos 8 canales nativos de vanlife (Nómadas Charlatanes, viajeros_perrunos, Kinito Spiti, PACA stories, Con Destino Al Mundo…) |
| 13 | triciclo eléctrico para pensionados jubilados bici de tres ruedas (AR) | **9** | Todo irrelevante (consulta larga y apilada) |
| 14 | bici eléctrica abuela tercera edad cómo elegir (MX) | 232 | Casi todo irrelevante (dramas cortos, música) |
| 15 | canal bicicletas eléctricas mayores de 60 (US, canales) | 14 | Ningún canal dedicado. bici.mayor60 es de rutas urbanas |
| 16 | bicicleta eléctrica para jubilados en Estados Unidos hispanos (US) | 15 | Solo noticias de Univision y Telemundo. Ningún creador |

Además, `search_niche_finder_channels` (idioma es, con y sin filtro de EE. UU.) no devuelve ningún canal dedicado a bicis o triciclos para mayores. Devuelve unos 35 canales faceless registrados en septiembre-octubre de 2026 sobre mayores (belleza, finanzas, salud) o motos y coches, así que el público mayor hispano se está poblando, pero con otros temas.

**Sobre las dos búsquedas que antes devolvieron pocos resultados:** el informe no recoge cuáles eran, así que no puedo asegurar cuáles. Con los mismos patrones de hoy, **el problema era la formulación en gran parte**:

- Una consulta apilada ("triciclo eléctrico para pensionados jubilados bici de tres ruedas") da 9 resultados, todos irrelevantes. La versión corta ("triciclo eléctrico para jubilados") da 43. Con "adultos mayores" da 387.
- "Jubilados" casi no lo usan los creadores. Dicen "personas mayores", "adultos mayores", "mayores de 60", "tercera edad".
- Cuando una búsqueda devuelve pocos resultados irrelevantes, significa que ningún vídeo coincide con esa redacción, no que no haya oferta.

## 2. RPM en español

Medido con `get_video_rpm` y `get_batch_channel_metrics_v2`:

| Audiencia | Evidencia | RPM |
|---|---|---|
| Inglés, EE. UU. (referencia) | Ebiker: vídeo 11,5; canal 11,02. Tech Charge: vídeo de 207k vistas 11,21 | 11 |
| Canal con mezcla EN + localizados | Tech Charge canal: 3,93. E Biking Today canal: 3,72 | La mezcla con audiencia de RPM bajo hunde el canal de ~11 a ~4 |
| **España** (nativos) | Eliges Bien 3,29; innova 3,22; Mammoth 2,70; Decisión Informada 2,43 | **2,4 a 3,3** |
| **México / Chile** (nativos) | Escuela de Ebikes (MX) 2,37; MP Bicis y Más (CL) 2,02 | **2,0 a 2,4** |
| Vídeos nativos en español, tier 2 | Mammoth 3,17; innova 3,17; Giordano 3,17; MP Bicis 3,95 (tope geográfico). **Máximo del rango en todos: 4,5** | **3,2 a 4,0, techo 4,5** |
| Vídeo en español de LatAm (tier 3) | Rafito Ofertas 1,58 | 1,6 |
| Hispanos de EE. UU. | No hay canal nativo en español medible. Único dato: vídeo con título en español de sixthreezero (audiencia tier 1): 3,47, rango 0 a 7,28 | **Estimación 4 a 7. No verificado** |

**Conclusión:**

- España y México: **2,4 a 4,5 USD, mediana 3,2**. Tu suelo de 3 se cumple por poco y tu prioridad de 8 a 10 no.
- Hispanos de EE. UU.: **4 a 7 USD, sin verificar.** No hay datos propios que lo respalden, solo que el sistema los clasifica como tier 1.
- ¿Compensa? Por vídeo de 20.000 vistas, serían unos 64 USD (España/México) frente a unos 110 USD (EE. UU. hispano), frente a unos 220 USD de Ebiker en inglés.
- La audiencia no se elige. Depende de dónde vean el vídeo, y solo se puede inclinar con precios en dólares, marcas de EE. UU. (Aventon, Rad, Amazon.com) y ejemplos de Florida o Texas. Eso es una apuesta, no una garantía.

## 3. Tres ángulos cercanos

| Ángulo | Competencia ES | RPM ES | Veredicto |
|---|---|---|---|
| **Triciclos eléctricos para adultos mayores** (estabilidad, equilibrio, seguridad) | **BAJA-MEDIA.** Solo listicles (innova 4.636, Rafito 7.947, Gear Geek, Gadgetron, TechZone), marcas (sixthreezero, ETNNIC, TrikeBike) y spots de 2023 (Tutiendaenergetica 60.604, javi vlogs 171.010). Ningún canal editorial | 3,2 (innova), 1,6 (Rafito) | **El mejor. Sin ventaja de RPM** |
| **Scooters de movilidad reducida** (4 ruedas, plegables) | **MEDIA.** ~6 tiendas de ortopedia, 4 canales de listicles, máximo 28.734 vistas. Alta en España | 2,4 (Decisión Informada), 3,17 (vídeo) | Peor. Sector médico-adyacente: hay que evitar afirmaciones. No verifiqué su evidencia en inglés |
| **Bicis plegables para viajar / autocaravana** | **ALTA.** Al menos 8 canales nativos con cara y comunidad | 3,17 | **Descartado** |

Ningún sub-nicho mejora el RPM. En español, el RPM lo marca la geografía de la audiencia, no el tema.

## 4. Recomendación: abrir, sí, como test pequeño

**Ángulo:** "Errores y arrepentimientos al comprar una bici o triciclo eléctrico después de los 60", en español neutro, con vídeos de 15 a 25 minutos. Los primeros 4 de 8 vídeos, centrados en triciclos eléctricos, que es donde hay menos competencia.

**Por qué ese:**

- El formato "errores/desventajas" ya mueve 117.000 a 297.000 vistas en español para el tema general (MP Bicis y Más, Mammoth Bikes).
- Ningún nativo lo aplica a mayores ni a triciclos.
- Los competidores son canales en inglés con títulos localizados, de los que un canal nativo se diferencia con guion, voz y ejemplos propios en español.

**Audiencia:** hispanohablantes de México y EE. UU., mayores de 50 y sus hijos adultos. Precios en dólares y marcas de EE. UU. para inclinar la audiencia hacia el RPM de 4 a 7. La base esperada, si no sale así, es 3 a 4.

**Lo que no cumple:** tu prioridad de RPM de 8 a 10. En español este nicho no llega ahí. Si ese es el objetivo principal, la única vía medida es abrirlo en inglés (11 USD), y eso es otro proyecto.

**Límites:**

- Parar si tras 8 vídeos la media está por debajo de 1.500 vistas.
- Escalar si supera 8.000 de media.
- Evitar consejos médicos y promesas de seguridad.
- Hay que comprobar el doblaje automático de Tech Charge y Ebiker abriendo uno de sus vídeos con título en español.

## 5. Límites de esta verificación

- No hay medición propia de RPM de hispanos de EE. UU.
- No he comprobado si hay doblaje real en los canales con títulos localizados.
- Los dos resultados con pocos vídeos de la ronda anterior no se pueden identificar con certeza.
- Las fechas de creación de algunos canales de `search_niche_finder_channels` no son fiables: "Camino de los Ancianos" aparece con 55.700 suscriptores y fecha de creación 2026-09-30.
- Los RPM de Nexlev para canales en español dependen de la geografía de la audiencia, no del idioma.
