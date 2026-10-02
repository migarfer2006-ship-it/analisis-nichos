# Análisis de 3 canales (ORIGENES, Tiempos Antiguos, WUFO TV) — idioma y tipo de vídeo — 2026-10-02

Datos de trabajo en `resultados/trabajo-canales-2026-10-02/` (archivos 01 a 15). Todo lo medido sale de Nexlev; Algrow dio error 402 (suscripción inactiva) en dos intentos. Cada cifra va marcada **VERIFICADO** (dato directo de la herramienta, comprobado en varias fuentes o en el propio vídeo) o **ESTIMADO** (modelo de Nexlev o cálculo mío). "No verificado" significa que no se pudo medir.

---

## 0. Lo que contradice lo esperado (léelo primero)

1. **El nicho de los tres canales está saturado en español y en inglés. No pasa tu filtro de competencia en ningún idioma.** Los tres son del mismo ecosistema: documentales largos con imágenes y voz de IA sobre prehistoria e historia antigua. En español hay al menos 25 canales dedicados identificados por nombre y 59 en el buscador de nichos; el 97 % se creó desde junio de 2025. En inglés hay al menos 163 y el 85 % es de 2025-2026. Los canales nuevos que no copian un gancho concreto se quedan en menos de 1.000 vistas por vídeo (decenas de ejemplos en `09`, `12`, `14`).
2. **Los títulos engañan.** Los títulos en inglés de ORIGENES y Tiempos Antiguos son localizaciones automáticas; el título original es español (comprobado con `youtube_video_details`). Pero hay pistas de audio en otros idiomas: la transcripción del vídeo top de ORIGENES vino en **árabe** y la de "Qué fue la Edad de Piedra" (Tiempos Antiguos) vino en **inglés**. Esto indica doblaje o pistas multi-idioma. No lo puedo cuantificar sin YouTube Analytics del propietario.
3. **Los tres canales no son lo que su descripción dice.** ORIGENES es "Historia del Océano TV" y su 77 % de vistas viene de un solo vídeo (el asteroide). Tiempos Antiguos usa etiquetas copiadas ajenas al tema (Edad Media, Revolución Francesa…). WUFO TV se presenta como documental, pero **4 de sus 8 outliers son una saga de ficción IA** ("Full Fantasy Movie 4K") y el resto de su ecosistema (WUFO Earth, WUFO Español, WUFO Science France, WEON Earth) son canales hermanos que reparten el mismo contenido en varios idiomas.
4. **El RPM de `get_video_rpm` no sirve para decidir.** Da 3,17 por defecto en español y está topado en 4,5. Triangulado por geografía, el español queda en 1,1–2,7 $ y el inglés en 2,7–6,0 $ (ver `15`). **Con tu umbral anterior de 4–5 $, el español no puede pasar; el inglés pasa raspando.**
5. **El mejor outlier en español no es el tema, es el gancho.** "Así cruzaron el Estrecho de Bering los primeros mexicanos" tiene 1,35 M de vistas. El mismo tema en inglés genérico ("first humans reach the Americas") no pasa de 6K, y el clon español ("Cómo llegaron los primeros mexicanos", otro canal) hizo 50K, el 4 % del original.

---

## 1. RECOMENDACIÓN DEFINITIVA

**Abrir en INGLÉS, con vídeos largos de "vida cotidiana en el mundo antiguo y prehistórico contada como una pregunta concreta".** No es el nicho que pasa tus filtros (ninguno los pasa), es el menos malo con datos que lo respaldan, y la prueba está diseñada para perder poco si falla.

| Campo | Decisión |
|---|---|
| **Idioma** | Inglés (guion nativo en inglés, no traducción literal). |
| **Sub-nicho exacto** | Vida cotidiana de pueblos antiguos y prehistóricos resuelta como pregunta ("How did X do Y without Z?", "What really happened in X after dark?"). Egipto, Mesopotamia, Roma, vikingos, Edad de Hielo, Neolítico. Solo contenido apoyado en arqueología; nada de "ancient aliens", "civilización perdida" ni "prohibido". |
| **Formato** | 25–32 minutos (rango 20–40). En el niche overview de canales similares a Tiempos Antiguos, **el 38 % de los vídeos de 20–40 min supera 100K frente al 7 % de los de menos de 20 min**, 22 % entre 40–60 y 19 % entre 60–120 (muestra: 428 vídeos de 12 canales, ESTIMADO por sesgo de muestra). Voz en off IA con calidad alta, imágenes IA con movimiento lento (5–8 s por plano), música orquestal baja, logo discreto. |
| **Título** | Pregunta cerrada con un detalle concreto y una restricción ("sin aire acondicionado", "después del anochecer", "sin mapas ni brújulas"). 8–14 palabras. Sin frases de conspiración. |
| **Miniatura** | Un primer plano de rostro humano de época (imagen IA) + 3–5 palabras grandes con la pregunta. Es lo que repiten las miniaturas que funcionan en los tres canales (`miniaturas/`). |
| **Audiencia** | Adultos de EE. UU., Reino Unido, Canadá y Australia (ESTIMADO: 60–80 % de las vistas de los canales EN de referencia, según `get_geography_revenue`; India pesa entre 5 y 31 % y baja el RPM). |
| **Vídeos de prueba** | **12 vídeos en 6 semanas** (2 por semana), mismo formato y misma estructura, cambiando solo el tema. |
| **Regla de parada** | Las cifras son **propuesta mía derivada de los datos** (el vídeo mediano de un canal EN que sobrevive es ~9K; la media, ~87K), no son mediciones. Tras el vídeo 12, con YouTube Analytics propio: **ESCALAR** si hay al menos un vídeo ≥100K en 28 días, o mediana ≥15K vistas con CTR ≥4,5 % y retención media ≥38 %. Pasar a 3 por semana y doblar los 3 mejores al español. **CERRAR** si la mediana es <3K y el mejor vídeo <20K. **Zona intermedia** (mediana 3–15K): una sola ronda de 6 vídeos cambiando únicamente título y miniatura; si no sube, cerrar. Parada dura: no gastar más de 12 vídeos de producción sin una de las dos condiciones de escalar. |
| **Expectativa realista** | Un canal EN que sobrevive hace de mediana ~9K vistas por vídeo (≈ 36 $ al RPM probable) y de media ~87K (≈ 350 $). A 8 vídeos al mes eso son entre ~300 y ~2.800 $/mes, ESTIMADO. La mayoría de los canales nuevos no llega ahí. |

### Por qué inglés y no español (puntuación transparente)

Comparación de supervivientes en el buscador de nichos (muestras de distinto tamaño y filtros distintos; no es comparación estricta):

| Criterio | Español | Inglés | Fuente |
|---|---|---|---|
| RPM probable | 1,8 $ (1,1–2,7) | 4,0 $ (2,7–6,0) | `15` ESTIMADO |
| Vistas medias por vídeo (mediana de canales) | 182K | 87K | `10`, `13` |
| Vídeo típico (mediana de medianas) | 30K | 9,3K | `10`, `13` |
| Ingreso por vídeo medio | ≈ 330 $ | ≈ 350 $ | cálculo |
| Ingreso por vídeo típico | ≈ 54 $ | ≈ 37 $ | cálculo |
| Canales en la muestra | 59 | ≥163 (tope de 100 por consulta) | `10`, `13` |
| No monetizados | 22 % | 40 % | `10`, `13` |
| Techo observado | 1,35 M (gancho de identidad) | 2–3 M (varios formatos) | `09`, `12` |

**Lectura:** en ingreso por vídeo están empatados técnicamente (el español tiene más vistas, el inglés paga más por vista). Gano el inglés por tres razones: (1) tu umbral de RPM de 4–5 $ solo es alcanzable con audiencia de EE. UU./UK/CA/AU; (2) el techo de ingresos por vídeo es unas 5 veces mayor; (3) el mismo guion se dobla al español casi gratis, mientras que lo contrario no mejora el RPM. **Lo que pesa en contra:** en inglés hay más canales, más marcas con presentador humano y más contenido sin monetizar (40 % frente a 22 %), que apunta a más riesgo de descalificación. Con un peso menor para el RPM el resultado se invierte, por eso el plan B es serio.

---

## 2. Diez títulos listos para producir (inglés)

Basados en patrones de outliers reales de canales pequeños (no son copias; los outliers originales están en `12`).

1. How Did Ancient Romans Keep Food Fresh Without Refrigerators?
2. What Did Stone Age Families Do When It Rained for a Week?
3. What Really Happened Inside a Medieval Castle After Dark?
4. How Did the Vikings Cross the Atlantic Without Maps or Compasses?
5. 18,000 Years Ago: What Was a Night Inside an Ice Age Cave Really Like?
6. How Did Ancient Mesopotamians Survive 50°C Summers Without Air Conditioning?
7. What Did Ancient Doctors Actually Do When Someone Broke a Bone?
8. How Did Ancient People Tell the Time at Night Before Clocks?
9. 24 Hours in Ancient Pompeii: One Ordinary Day Before the Eruption
10. How Did Ancient Cities Get Clean Water Before Plumbing?

Patrón de apoyo: "How Did Ancient Egyptians Sleep in Desert Heat Without Air Conditioning?" 797K con un canal de 9K suscriptores; "What Really Happened in Ancient Egypt After Dark?" 325K con un canal de 688 suscriptores; "What Did Ancient Humans Do When It Was Too Cold to Sleep" 362K; "18,000 Years Ago. What Was Life Really Like Inside an Ice Age Cave?" 348K; "24 Hours in Ancient Egypt" 314K (timewarp cities). Todos de 15–40 min.

---

## 3. Si esto falla (plan B)

**Español neutro latinoamericano, con gancho de identidad y de región.** Se produce con los mismos guiones doblados, sin coste extra de investigación.

- **Por qué es el segundo mejor:** es la única vía con un gancho de demanda medido y copiado con mal resultado. "Primeros mexicanos" 1,35 M; "¿De dónde vienen los mexicanos?" 149K y 304K en otros canales; clon "Primeros mexicanos" 50K. Para otras nacionalidades casi no hay competencia dedicada (primeros argentinos 3K; el resto sin vídeos relevantes en las búsquedas). Y "megafauna sudamericana" en español tiene **14 vídeos en todo YouTube en el último año**, con demanda parcial medida (Tiempos Antiguos "Sudamérica aislada" 452K; Planeta Antiguo 189K).
- **Qué cambiar respecto al plan A:** títulos con nacionalidad ("Así llegaron los primeros argentinos/colombianos/peruanos"), 25–40 min, audiencia MX 30–37 %, AR/CO/CL ~35 %.
- **Prueba de que el español tiene demanda real:** WUFO Español, un doblaje de WUFO TV de 34 días y 970 suscriptores, tiene dos vídeos de ~350K ("Los orígenes de la humanidad"; "La evolución más extraordinaria…").
- **Coste:** RPM de 1,1–2,7 $. A 100K vistas son unos 180 $ por vídeo (110–270).
- **Regla de parada:** la misma que arriba, con umbrales dobles para vistas porque el RPM es la mitad: escalar con mediana ≥30K o un vídeo ≥250K; cerrar con mediana <6K.
- **Cuándo pasar del plan A al B:** si tras los 12 vídeos en inglés el mejor está entre 20K y 100K con CTR bajo (<3,5 %) pero retención buena, doblar esos vídeos al español antes de cerrar.

---

## 4. Tabla comparativa español vs inglés

| Campo | Español | Inglés |
|---|---|---|
| Competidores dedicados | ≥25 con nombre en las búsquedas; 59 en el buscador de nichos (57 creados desde jun-2025, 36 con IA). **ALTA.** | ≥163 en el buscador (138 desde jun-2025, 88 con IA), más marcas con presentador (Astrum, NORTH 02, ExtinctZoo, Spinosnack). **ALTA.** |
| Fuerza de los líderes | Mr. Prehistoria 18K subs, 222K de media; Planeta Antiguo 59K; La Historia del Mundo (Roma) 72K con un vídeo de 2,56M. | Silence of the Earth, Paleora (1,29M), Spinosnack (2,6M), Wild Origins 82K subs con 6,3M en un vídeo, WUFO Earth. |
| Demanda nativa demostrada con canales pequeños | Mr. Prehistoria (18K subs): vídeos de 1,5M. Prehistoria en Español TV (8,9K subs): media 123K. WUFO Español (1K subs): 350K por vídeo. MundosOlvidados (13,5K): media 84K. | Nile Archives (688 subs): 325K. inkly (9K): 797K. WEON Earth (4,5K): 396K, 363K, 348K. Whyologica (658 subs): 141K. |
| Vídeo típico | 30K | 9,3K |
| RPM (rango, ESTIMADO) | 1,1 / 1,8 / 2,7 $ | 2,7 / 4,0 / 6,0 $ |
| Audiencia probable | México 30–37 %, EE. UU. hispano ~18 %, Argentina 9–15 %, Colombia 16 %, España 6–21 %, Chile 5 %. 55+ años puede ser el 52 % (Tiempos Antiguos). | EE. UU. 40–50 %, Reino Unido 7–13 %, Canadá 7–11 %, Australia 6–9 %, India 5–31 %. |
| Ingreso por 10K vistas | 11 / 18 / 27 $ | 27 / 40 / 60 $ |
| Ingreso por 30K vistas | 33 / 54 / 81 $ | 81 / 120 / 180 $ |
| Ingreso por 100K vistas | 110 / 180 / 270 $ | 270 / 400 / 600 $ |
| Producción con tu pipeline | Misma. Un guion de 25–35 min son ~4.000–5.000 palabras. Voz IA en español de calidad media alta; la audiencia critica imágenes con errores (martillos de hierro en la Edad de Piedra). | Misma. Voz IA en inglés más madura. Más exigencia en calidad de guion porque la competencia es mayor. |
| Riesgos | Saturación y canibalización (hasta 20 canales publican el mismo tema en un mes). Fricción creacionista en vídeos de evolución humana. Rechazo explícito a la IA en comentarios. Parte de las vistas puede venir de doblajes (no verificado). | Saturación. Ola de ficción IA y de pseudociencia ("ancient aliens", "AI decoded… HORRIFYING"). 40 % de los canales de la muestra sin monetizar. Marcas con presentador humano. |

**Otros idiomas (nota, 5 búsquedas cada uno, ver `14`):**
- **Portugués (Brasil):** demanda alta y menos competencia dedicada que ES/EN (Arqueofatos 1,4M, "Um Documentário" cuatro vídeos de 420–740K, Roma 481K, océanos 1,1M). RPM bajo, similar al español (ESTIMADO). Buen candidato futuro para doblar.
- **Alemán:** demanda media (100–230K), muy dominado por reuploads de ARTE y por marcas "Timeline / Real History"; RPM alto (DE/AT/CH ≈ 4–7 $, ESTIMADO). Hueco para un canal cuidado, pero las mismas fábricas ya lo cubren.
- **Francés:** demanda baja (techo de canales nuevos 138K); el resto <1K.
- **Italiano:** demanda baja (techo 6,5K) salvo un outlier humano (10,6 M).
- **Hallazgo transversal:** las mismas fábricas publican en 6 idiomas (Extinct Primal, WUFO, Planète Antique/Pianeta Antico/Planeta Antigo, Jodisea/Iodisea/Wondody, Spinosnack, Paleora, Orbinéa). El doblaje multilingüe es el modelo dominante.

---

## 5. Análisis de formatos y tipos de vídeo

### Qué rinde según los outliers

| Formato | Ejemplo medido | Duración | Idioma | Competencia |
|---|---|---|---|---|
| Pregunta de vida cotidiana antigua | 797K (9K subs), 525K, 362K, 325K (688 subs) | 20–40 min | EN | Media (≥15 canales IA ya probando) |
| Identidad nacional/origen | 1,35M "primeros mexicanos"; 149K, 304K | 20–45 min | ES | Baja-media (≈12 canales, casi todos <1K) |
| Segunda persona / inmersivo | 2,64M Spinosnack "How it feels to die in every prehistoric era"; 314K timewarp | 15–30 min | EN | Baja en calidad real, alta en clones |
| "What if…" hipotético | 2,81M Silence of the Earth | 1–2 h | EN | Alta |
| Historia de un país en 20 min | 3,28M VLAD; 2,11M Echoes of History; Tiempos Antiguos "Irán" 229K | 11–35 min | EN, ES | Alta, marcas |
| "Iceberg explained" | 1,61M NORTH 02; 363K dRAlex | 25–60 min | EN, ES | Media (necesita narrador con voz propia) |
| "Documentary for sleep" 2–5 h | 841K, 2,81M Silence of the Earth; 951K Planeta Geo | 2–5 h | EN, ES | Muy alta; decenas de clones de 5–1.000 vistas |
| Prehistoria "Full Documentary" 40–70 min | 814K WUFO Earth, 662K ORIGENES asteroide, 705K Tiempos Antiguos | 40–70 min | EN, ES | Alta |

- **Duración:** los hits de canales pequeños se agrupan entre 20 y 40 min (mediana de los vídeos ≥100K del niche overview: 37 min). Los vídeos de 2 a 5 horas funcionan en pocos canales y tardan más en producirse.
- **Estructura de título que funciona:** (a) pregunta con restricción concreta; (b) "Así/Cómo + hecho + sujeto con identidad"; (c) "[N] Million Years Ago: …"; (d) "Qué fue / What Was + época + qué hacían los humanos".
- **Gancho de guion (transcripciones):** escena concreta con número en la primera frase ("Hace exactamente 50.000 años… murió el último neandertal"; "Había un puente de 16 km…") → promesa de cambiar la imagen que tiene el espectador → capítulos con "para ponerlo en perspectiva" → bucles abiertos.

### Los 5 tipos con mejor relación oportunidad/competencia

1. **EN: pregunta de vida cotidiana de pueblos antiguos**, 20–35 min (recomendado).
2. **ES: identidad y origen por nacionalidad** ("primeros argentinos/colombianos/peruanos/chilenos"; Bering y poblamiento de América), 25–40 min (plan B).
3. **ES/EN: paleontología y prehistoria de Sudamérica** (megafauna, Amazonia prehistórica, Sudamérica aislada). ES: 14 vídeos en todo YouTube; EN: solo ExtinctZoo (2,19M y 1,05M) y el resto <12K.
4. **EN: inmersivo "24 horas en…" / "cómo se siente…"**, 15–30 min. Solo viable si el pipeline mantiene personajes y escenarios coherentes.
5. **EN/ES: "la historia de [país] en 20–30 min"**, saturado de marcas pero con techo muy alto; cuidar el riesgo de temas políticos sensibles para anunciantes.

### Qué NO copiar y por qué

1. **La saga de ficción IA de WUFO TV** ("Full Fantasy Movie 4K", 4 outliers de 8): es serie de ficción generada por IA, repetitiva y con cliffhangers. Encaja con la política de YouTube sobre contenido producido en masa/inauténtico (conocimiento general, no verificado aquí) y su público no es el de documental.
2. **"Documentary for sleep" de 3 a 6 horas en cadena:** decenas de clones nuevos con 5–1.000 vistas; el coste de producción es alto y casi nadie lo logra.
3. **Titulares de pseudociencia o falsos:** "Before I die, please listen…", "AI decoded… HORRIFYING", "Forbidden History", "Antediluvianas", "Klaus Schmidt reveló… sellado". Riesgo de desmonetización y de rechazo de anunciantes.
4. **Prehistoria humana en español con evolución como tema:** los comentarios mezclan fe/creacionismo ("pura mentira", "Dios creó…"), críticas a la IA ("totalmente engañoso y falso") y a los errores visuales (hierro en la Edad de Piedra). Si se hace, avisar del uso de IA y revisar anacronismos.
5. **Plantillas de etiquetas ajenas al tema** (las de Tiempos Antiguos: Edad Media, Revolución Francesa…) y títulos sin tildes ("Como Iran se Convirtio en Musulman").
6. **Copias casi literales de un outlier:** el clon de "primeros mexicanos" consiguió el 4 % del original (50K frente a 1,35M).
7. **Reediciones de documentales con derechos** (Sea Monsters 2003 en "Paleo Edits", Discovery en "Dino Unveiled Plus") y música con reclamaciones (WUFO tuvo reclamaciones de Adrev y MINT).

---

## 6. Fichas de los canales (Fase 1)

### 6.1 ORIGENES — @ORIGENESTV-k6k — `UCHchqqkbU_iVpDvJdNWJIMA`
- **Resumen:** creado 10-jul-2026 (VERIFICADO), 4.620 suscriptores, 17 vídeos, 860.530 vistas, España. Faceless 98 %, monetizado (canal y vídeos top con `bypassCache`; la caché había dicho "no monetizado" en dos vídeos recientes, era desfasada). Sin red CMS (partner individual). Sin shorts (100 % largo). Duración media ~42 min.
- **Idioma real:** español de España según Gemini (vídeo "Océano de Pangea"), y los comentarios llegan de España (Vitoria, Badajoz, Sevilla, Asturias), Argentina, Uruguay, Venezuela, México, Ecuador, Perú, Panamá, Bolivia. El vídeo top tiene una pista en **árabe** (transcripción de Nexlev) y un comentario en alemán y otros en inglés. Los títulos en inglés del listado son localizaciones. Título original del vídeo top: "Hace 66 Millones De Años: Cómo Fue El Impacto Que Terminó Con El Mundo De Los Dinosaurios" (publicado 23-sep-2026).
- **Crecimiento:** hasta el 17-sep sumaba ~210K vistas en dos meses (3–5K/día). Desde el vídeo del asteroide: 595K vistas en 7 días y +1.610 suscriptores. **Crecimiento explosivo por un solo vídeo; sin él, estancado.**
- **Outliers:** 13,1× el asteroide (663K, 48:43). 1,7× Livyatan (88K, 37:21). El asteroide funciona por un tema universal, un gancho cuantitativo ("20.000 °C, más caliente que el Sol") y recomendación sostenida.
- **Producción (Gemini, vídeo "asteroide" y "Pangea"):** voz IA de alta calidad (asteroide) o humana/IA de gama alta no concluyente (Pangea); imágenes IA + 3D + stock + mapas; música orquestal tensa; cortes de 3–5 s; logo permanente "HISTORIA DEL OCEANO TV". Duda factual detectada: comparación de fuerza de mordida del Dunkleosteus mal explicada.
- **Comentarios:** elogios genéricos ("excelente documental"), tasa muy baja (158 comentarios en 663K vistas = 0,02 %). Crítica: "las imágenes generadas por IA realmente son lamentables". Una corrección lingüística ("supervivencia").
- **País de audiencia (ESTIMADO, Nexlev modelo):** México 27,5 %, EE. UU. 22,4 %, España 18,6 %, Colombia 16,2 %, Argentina 15,3 %. RPM largo 1,79.
- **Promociones externas:** no verificado (canal no scrapeado).
- **Veredicto:** un vídeo bueno, el resto 600–70K. No es un patrón replicable demostrado.

### 6.2 Tiempos Antiguos — @TiemposAntiguos-l9s — `UCQSiOPL4a-SCbdKAvk8r59A`
- **Resumen:** creado 15-feb-2026, 15.100 suscriptores, 44 vídeos, 6.055.347 vistas, España (declarado). Faceless 99 %, monetizado. **En la red CMS "Thumb Media Affiliate"** (afiliado): parte del ingreso puede ir a esa red. Sin shorts. Duración media ~51 min. Último vídeo con título basura "timpo927" (13K vistas).
- **Idioma real:** español (Gemini y transcripción del vídeo "primeros mexicanos"; comentarios de México, Argentina, Perú). **Pero** la transcripción de "Qué fue la Edad de Piedra" (405K) viene en inglés. Los títulos EN del listado son localizaciones. Tiene pistas multi-idioma: no verificado cuánto de las vistas son ES nativas.
- **Crecimiento:** ~70K vistas/día sostenidas (30 días: 2,10M; 90 días: 4,12M; 7 días: 518K). **Estable-alto**; las suscripciones se frenan (+400 en 7 días frente a +2.500 en 30). Pico en abril (958K en un mes).
- **Outliers (8):** 9,4× "Así cruzaron el Estrecho de Bering los primeros mexicanos" (1,35M, 19:30); 5,1× "Antes de nosotros: las otras especies humanas" (705K, 42:52); 3,7× Pleistoceno (503K, 59:23); 3,3× Sudamérica aislada (452K, 40:41); 2,9× Edad de Piedra (405K, 56:09); 2,6× Historia de la humanidad (357K); 2,2× Neandertales 100.000 años (309K); 1,7× "Cómo Irán se convirtió en musulmán" (229K, único fuera de prehistoria).
- **Por qué funcionó el top:** identidad nacional ("primeros mexicanos"), misterio y escala en la primera frase, 19 min (el único vídeo corto entre los grandes) y emoción en los comentarios ("un orgullo ser mexicano").
- **Producción (Gemini, vídeo Bering):** voz humana según Gemini (no verificado); imágenes IA fotorrealistas cada 5–8 s; música orquestal; sin stock ni mapas. Descripción larga con plantilla de viñetas "🔺 En este video descubrirás" y cierre "Suscríbete / Dale like / Comenta".
- **Comentarios:** mexicanos reales y emotivos; correcciones de datos (teocintle, dirección Siberia–Alaska); críticas a los anacronismos de la IA; creacionistas ("pura mentira") en "Antes de nosotros".
- **País de audiencia (ESTIMADO):** México 36,9 %, EE. UU. 18,4 %, Argentina 8,9 %, España 6,1 %, Chile 5,2 %; 55+ años = 52 %. RPM largo Nexlev 4,02 (categoría 9, inflado), mi estimación 1,8.
- **Promociones externas:** scrapeado, sin productos ni patrocinios. Todo AdSense.

### 6.3 WUFO TV — @WUFOTV — `UCaSfbjZReHoweptNU3XiIUw`
- **Resumen:** creado 19-jun-2026, 12.200 suscriptores, 43 vídeos, 3.440.208 vistas, EE. UU. Faceless 99 %, monetizado (canal y vídeos top). Sin red CMS (partner individual); reclamaciones de música de Adrev y MINT en 2 vídeos. Shorts 0,43 %. Enlaza a un blog y a Facebook.
- **Idioma real:** inglés (transcripción y Gemini en 3 vídeos). Voz IA.
- **Crecimiento:** **acelerando**: de 2K vistas/día en julio a 185K/día (7 días: 1,29M; 30 días: 2,82M). La mitad de las vistas recientes viene de la saga de ficción.
- **Outliers (8):** 9,9× Pangaea (796K, 36:36); 9,0× "The Mother Who Gave Birth to a Dragon | Full Fantasy Movie 4K" (718K, 25:48, 1-oct, ficción); 7,1× y 6,9× partes 2 y 3; 6,8× T. Rex (542K, 1:00:53); 2,2× océano prehistórico (173K); 1,7× "The Lost Hindu Civilization They Don't Want You To Know" (133K, clickbait de conspiración); 1,6× Prehistoric Earth (125K).
- **Producción (Gemini):** voz IA, imágenes IA tipo vídeo generado (Sora/Runway) + CGI para mapas, cortes de 4–6 s, logo del canal al minuto 1, capítulos con título de pantalla, música orquestal. La ficción es una serie de supervivencia con diálogos cortos, narración IA y cliffhangers.
- **Comentarios:** genéricos y de aspecto sintético ("I'm now officially obsessed with the concept of tectonic plates", todos publicados el mismo día, algunos con nombres tipo "HillTapio"); el propio canal escribe la pregunta ancla. Indicio de engagement artificial, no verificado.
- **País de audiencia (ESTIMADO):** EE. UU. 48,7 %, India 18,9 %, Reino Unido 13,4 %, Canadá 10,8 %, Australia 8,2 %. RPM largo 5,37.
- **Promociones externas:** no scrapeado.
- **Ecosistema:** WUFO Earth (814K en Pangea), WUFO Español (970 subs, 350K por vídeo), WUFO Science France, WEON Earth, NEXO Earth: mismo contenido repartido en varias marcas.

---

## 7. Mapa del nicho (Fase 2 y 3)

**Nicho que cubren los tres:** documental largo de divulgación sobre prehistoria y deep time (Pangea, dinosaurios, océanos prehistóricos, evolución humana) y, en Tiempos Antiguos, también historia antigua y de Oriente Medio. Sub-nichos con competencia medida:

| Sub-nicho | Competidores ES (nombre) | Techo ES | Competidores EN | Techo EN |
|---|---|---|---|---|
| Evolución humana / Neandertales | ≥12 | 309K (Tiempos Antiguos) | ≥15 | 1,7M (Ella Al-Shamahi), 755K WUFO Earth |
| Prehistoria / Pangea / dinosaurios | ≥15 | 951K (Planeta Geo), 350K (WUFO Español) | ≥20 | 2,8M (Silence), 2,9M (Wild Horizons) |
| Océanos prehistóricos | ~10 | 363K (dRAlex iceberg) | ≥15 | 989K (Spinosnack) |
| Extinciones masivas | ≥20 en 1 mes | 522K (Jodisea) | ≥20 en 1 mes | 3,09M (Astrum) |
| Civilizaciones perdidas / misterios | muchos | 645K | muchos | 10M (Hancock) |
| Roma / Egipto / Mesopotamia / vikingos | ≥15 cada uno | 2,56M (La Historia del Mundo Roma), 729K Sumeria | marcas | 3,5M (HISTORY pirámides) |
| Sudamérica prehistórica | 14 vídeos en total | 452K (Tiempos Antiguos) | ExtinctZoo + clones | 2,19M (ExtinctZoo) |
| Identidad: primeros mexicanos / origen | ≈12 | 1,35M | genérico | 6K |

**Conteos de competidores dedicados:** español ≥25 identificados por nombre en las búsquedas de prehistoria (Planeta Antiguo, Mr. Prehistoria, Mundo Prehistórico de los Dinosaurios, MundosOlvidados, Archivo Prehistórico, Prehistoria en Español TV, Orígen Humanidad, WUFO Español, Mundo Extinto, Extinct Primal Español, Planeta Geo, El Paleontólogo Somnoliento, Tierra Oculta, Jodisea, Relatos de la Prehistoria, Prehistoria Documental, Civilización Humana, Historias Nocturnas, Reino Prehistórico, Mundo Primitivo, Eras Perdidas, Crónicas Eternas, Primeros Humanos, Tu Documental, Colosos TV…). Distinción: dedicados (todos los anteriores) frente a vídeos sueltos de generalistas (Nat Geo, ARTE, CNN en Español, Lex Fridman).

**Clasificación de competencia:** ES **ALTA** (pocos con peso, muchos con 1–5K por vídeo). EN **ALTA**, con marcas de presentador humano. Tu filtro de ≤2–3 canales nativos no lo pasa ninguno.

**Demanda nativa en español de canales pequeños:** mediana de vistas medias 182K con mediana de suscriptores 22.700 (59 canales). Pero el vídeo típico ronda 30K y 45 de 59 viven de pocos vídeos.

**Señales de ola de clones:** 97 % (ES) y 85 % (EN) de los canales del nicho creados desde junio de 2025; de los canales EN con media ≥100K, 80 % son de 2025-26 y 29 % de 2026. En 1 mes aparecen ≥20 canales publicando la misma extinción del Pérmico o la misma pregunta de supervivencia a la Edad de Hielo; casi todos con <1K.

---

## 8. Riesgos

- **Contenido repetitivo o inauténtico:** muchos canales de la muestra son IA con la misma plantilla. YouTube endureció en 2025 la política de contenido producido en masa/inauténtico y exige marcar el contenido sintético realista (conocimiento general, no verificado con herramientas aquí). En la muestra EN, el 40 % de los canales no está monetizado.
- **Pseudociencia y afirmaciones falsas:** el sub-nicho de misterios arrastra anunciantes caros hacia fuera. Mantener fuentes arqueológicas y evitar titulares de conspiración.
- **Errores visuales de la IA** (anacronismos) criticados con fuerza en los comentarios ES.
- **Derechos:** música con reclamaciones (WUFO); no reeditar documentales ajenos.
- **Red CMS:** Tiempos Antiguos pertenece a "Thumb Media Affiliate"; si compras o gestionas canales así, parte del ingreso se cede.
- **Dependencia de un solo vídeo:** ORIGENES (77 %) y WUFO (mitad de sus vistas recientes de ficción).
- **India en la audiencia EN:** baja el RPM entre 1 y 1,5 $.

---

## 9. Límites de los datos (qué no se pudo verificar)

- **Algrow:** error 402 en dos intentos; todo con Nexlev.
- **`watch_youtube_video_and_ask`:** límite de 5 llamadas al día del plan LITE (agotado). Solo pude ver clips de 5 vídeos (ORIGENES ×2, Tiempos Antiguos ×1 con 1 más fallida, WUFO ×2). No activé créditos de pago sin tu permiso. Por eso la voz humana/IA de Tiempos Antiguos queda **no verificada**.
- **Audio original:** verificado en ≥3 vídeos por canal mediante transcripción, Gemini o comentarios, pero con contradicciones (árabe, inglés). No se puede saber qué parte de las vistas viene de pistas de audio dobladas sin YouTube Analytics del propietario.
- **País y edad de la audiencia:** son estimaciones de Nexlev. ORIGENES y WUFO devuelven una demografía idéntica (91,6 % hombres, 25–34 = 41,1 %), señal de dato genérico por categoría.
- **RPM:** ninguno es real. `get_video_rpm` da 3,17 por defecto y topa en 4,5; el RPM de vídeos de más de 2 h (18,6 $) es una extrapolación por duración. Rango adoptado: ver `15`.
- **Fechas de publicación:** el listado de canal de Nexlev redondea a menudo al día 2 de cada mes; para fechas exactas hay que usar `youtube_video_details`.
- **Búsquedas de YouTube:** `viewCount` sale truncado en los resultados en español ("349" = 349K); lo reinterpreté con la duración y la fecha.
- **`search_videos` en español:** la búsqueda difusa devuelve ruido (comida callejera, fútbol). La base de virales de canales pequeños casi no cubre español (2 resultados con "historia", 0 con "antiguo"). Esa parte la cubrí con búsquedas de YouTube.
- **Muestras del buscador de nichos:** ES = 59 canales (la consulta devuelve ~40 y se solapan), EN = 163 (topado en 100 por consulta y filtrado a canales creados desde 2025). No son estrictamente comparables.
- **Promociones externas:** solo Tiempos Antiguos estaba scrapeado.
- **Reparto geográfico de WUFO Español, Planeta Antiguo y la mayoría de competidores:** no medido.
- **Duración del trabajo:** el trabajo real fue de unos 25–30 minutos de reloj; las herramientas contestan rápido. Se cumplieron todos los mínimos de búsquedas (ES 21, EN 21, otros idiomas 20) y no rellené con llamadas sin valor.

---

## 10. Resumen de búsquedas realizadas (cumplimiento de mínimos)

- **Español (≥20):** 17 búsquedas de YouTube con geo ES/MX/AR (prehistoria, civilizaciones perdidas, dinosaurios, océanos, neandertales, Roma, Egipto, Mesopotamia, prehispánico, poblamiento de América, origen de los mexicanos, megafauna sudamericana, vikingos, Göbekli Tepe, Patagonia, Edad de Hielo, extinciones masivas) + 2 de `search_videos` + 2 de `search_niche_finder_channels` con idioma español. Detalle en `09`, `10`.
- **Inglés (≥20):** 17 de YouTube con geo US/GB/AU/CA + 2 de virales de canales pequeños + 2 del buscador de nichos EN. Detalle en `12`, `13`.
- **Portugués, alemán, francés, italiano:** 5 búsquedas cada uno. Detalle en `14`.
- **Competidores:** `get_batch_channel_metrics_v2` (20 canales), `get_similar_channels` con los 3 canales semilla (236 canales únicos), `get_niche_overview` (12 canales, 428 vídeos). Ver `08`, `11`.
