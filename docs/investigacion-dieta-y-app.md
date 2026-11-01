# Investigación: dieta para bajar de peso + plan técnico de la app (Perú)

Fecha: 2026-11-01 · Estado: borrador v1

> **Nota de rigor.** Lo marcado ✅ se apoya en fuentes consultadas en esta sesión. Lo marcado ⚠️ viene de conocimiento general y **debe verificarse** antes de construir. Este documento no es consejo médico; la app debe incluir descargo y derivar a un profesional en casos de riesgo.

---

## 1. Dieta que funciona para la mayoría

### Conclusión
No existe una "dieta mágica". La evidencia apunta a que **lo que determina el éxito es el déficit calórico sostenido y la adherencia**, no el nombre de la dieta.

- ✅ Un *umbrella review* (Dinu et al., *Advances in Nutrition*, 2020; 495 meta-análisis de ensayos aleatorizados) encontró que la **dieta mediterránea** tiene la evidencia más consistente (mejora de peso, IMC, colesterol, glucosa y presión). Dietas bajas en carbohidratos, altas en proteína, bajas en grasa y de bajo índice glucémico mostraron evidencia sugestiva o débil. La calidad metodológica de la mayoría de los estudios fue baja o críticamente baja, por lo que la certeza es limitada. [PubMed 32059053](https://pubmed.ncbi.nlm.nih.gov/32059053/) · [Manuscrito](https://air.unimi.it/retrieve/dfa8b9a1-cd19-748b-e053-3a05fe0a3a96/Manuscript_DInu_AdvNutr.pdf)
- ✅ A largo plazo, distintas dietas producen pérdidas similares y el mejor predictor es la adherencia (varias fuentes secundarias; observacional, sin causalidad probada).
- ⚠️ Las demás cifras (proteína, ayuno, etc.) deben contrastarse con los trabajos originales antes de ponerlas en la app.

### Propuesta: "Mediterránea-peruana" de déficit moderado
| Parámetro | Valor propuesto ⚠️ (verificar con nutricionista) |
|---|---|
| Déficit | 15–25 % bajo el gasto total (≈ 300–600 kcal/día) |
| Ritmo esperado | 0,25–0,75 kg/semana |
| Proteína | ≈ 1,2–1,6 g/kg/día |
| Fibra | ≥ 25–30 g/día |
| Grasas | Predominio insaturadas (pescado, palta, aceite de oliva, frutos secos) |
| Calorías mínimas | Nunca por debajo de ~1 200 kcal (mujeres) / ~1 500 kcal (hombres) sin supervisión |
| Cálculo del gasto | Mifflin-St Jeor × factor de actividad |

### Base alimentaria local (barata y disponible en supermercado/mercado)
- **Proteínas:** pollo, pescado (jurel, caballa, bonito, pota), huevos, atún en agua, menestras (lentejas, frejoles, pallares, garbanzos), queso fresco, yogur natural.
- **Carbohidratos de calidad:** quinua, kiwicha, avena, camote, papa (cocida y fría), choclo, arroz integral, pan integral.
- **Verduras/frutas:** tomate, cebolla, zanahoria, zapallo, espinaca, brócoli, plátano, papaya, naranja, mandarina.
- **Grasas:** palta, aceite de oliva, maní, nueces.
- **Limitar:** gaseosas, jugos azucarados, frituras, embutidos, pastelería.

Esto es importante para el producto: una dieta con ingredientes locales hace que el **costo semanal sea bajo**, y eso mejora la adherencia (el diferencial de la app).

### Contraindicaciones / seguridad
Embarazo y lactancia, menores de 18, trastornos de conducta alimentaria, diabetes con insulina o sulfonilureas, enfermedad renal, IMC < 18,5. La app debe filtrarlos en el onboarding y recomendar consulta médica.

### Datos nutricionales
⚠️ Usar la **Tabla Peruana de Composición de Alimentos** (CENAN / INS) como base de macros, complementada con USDA FoodData Central o Open Food Facts para productos envasados. No pude verificar la versión vigente en esta sesión.

---

## 2. Precios de supermercados peruanos

### Mercado
✅ Los grupos son: **InRetail/Intercorp** (Plaza Vea, Vivanda, Mass, Makro), **Cencosud** (Wong, Metro) y **Falabella** (Tottus). Esto significa que Wong y Metro (y Plaza Vea/Vivanda) probablemente comparten plataforma y catálogo similar. Fuentes: [peru-retail.com](https://www.peru-retail.com/indecopi-metro-plaza-vea-tottus-vivanda-wong-precios/), [kom.pe](https://kom.pe/las-mejores-paginas-web-de-supermercados-en-peru/).

### Vías para obtener precios (de mejor a peor)
| Opción | Ventaja | Riesgo |
|---|---|---|
| **1. Convenios / afiliación con los comercios** (API o feed) | Datos oficiales, legales, estables | Lento; negociar con 3 grupos (Intercorp, Cencosud, Falabella) |
| **2. Agregador/proveedor de datos de precios** | Rápido | Costo; cobertura incierta |
| **3. Consulta de los catálogos públicos de las tiendas online** ⚠️ | Rápido para prototipo | Términos de uso, cambios sin aviso, bloqueos |
| **4. Colaborativo** (usuarios suben precios/tickets con OCR) | Complementa vacíos, mercados y bodegas | Calidad variable |
| **5. Datos abiertos oficiales** (p. ej. precios referenciales del Estado) | Legal | No son precios de góndola |

⚠️ **Hipótesis a verificar:** varias de estas tiendas online usan plataformas de comercio con endpoints de catálogo (p. ej. VTEX en algunas). Mi búsqueda **no confirmó** qué plataforma usa cada cadena ni si el acceso es permitido. Esto requiere revisión técnica y de términos de cada sitio.

### Aspectos legales (Perú)
- ✅ Ley 29733 de Protección de Datos Personales y su reglamento (se reporta un reglamento modernizado, D.S. 016-2024-JUS, vigente desde marzo de 2025; **verificar en El Peruano**). Aplica sobre todo a los datos de los usuarios de la app, incluidos los de salud, que son **datos sensibles**.
- ✅ Fuentes indican que el scraping no tiene jurisprudencia específica en Perú; el riesgo está en términos de uso, derechos de autor y datos personales. **Requiere consulta con un abogado.**
- Recomendación: empezar con convenios + aportes de usuarios, y usar consulta pública solo con asesoría legal, respetando robots.txt y frecuencia baja.
- ✅ INDECOPI sancionó a varias cadenas por no respetar el precio exhibido (artículo de 2017). La app debe mostrar **"precio referencial, fecha y hora de actualización"**, y nunca prometer el precio de caja.

### Modelo de datos de precios
`Producto(ean, nombre, marca, unidad, contenido)` · `Precio(producto, tienda, sucursal/distrito, precio, promo, fecha)` · `Equivalencia(ingrediente genérico → productos)`.
Clave: mapear **ingrediente genérico** ("pechuga de pollo 1 kg") a productos concretos para comparar entre tiendas por **precio por kg/litro**.

---

## 3. Integración con salud

✅ El paquete [`health`](https://docs.carp.dk/packages/flutter-health-plugin) de Flutter ofrece una API unificada para **Apple HealthKit** y **Google Health Connect**, incluyendo peso, mediciones corporales y nutrición (calorías, macros, agua). Alternativa más nueva: `health_connector`. El soporte de tipos difiere por plataforma. Android requiere SDK mínimo 26 en `flutter_health_connect`. En iOS hay que activar la capability **HealthKit** en Xcode.

| Dato | Leer | Escribir |
|---|---|---|
| Peso, % grasa, IMC | ✅ (seguimiento de progreso) | ✅ (si el usuario lo registra en la app) |
| Pasos / energía activa | ✅ (ajustar gasto calórico) | — |
| Nutrición (kcal, macros, agua) | — | ✅ (comidas registradas en la app) |

Puntos a tener en cuenta ⚠️:
- Permisos granulares por tipo de dato; el usuario puede negarlos y la app debe funcionar igual.
- Apple y Google revisan el uso de datos de salud: se exige política de privacidad clara, y **prohíben usar datos de salud para publicidad**.
- Health Connect es el estándar actual de Android (Google Fit está en retiro); verificar el estado vigente.
- Los datos de salud se procesan **en el dispositivo** siempre que sea posible.

---

## 4. Producto (MVP)

1. **Onboarding:** edad, sexo, talla, peso, meta, actividad, restricciones/alergias, presupuesto semanal, distrito.
2. **Plan:** calorías y macros objetivo; menú semanal (desayuno/almuerzo/cena/snacks) con recetas peruanas simples.
3. **Lista de compras** consolidada por ingredientes y cantidades (considerando rendimiento y mermas).
4. **Calculadora de precios:** costo total por tienda, "mejor tienda" o "mejor combinación", costo por porción y por día; sustitutos más baratos con igual aporte nutricional.
5. **Seguimiento:** peso, registro de comidas, sincronización con Salud/Health Connect.
6. **Ajuste semanal** del déficit según la tendencia real de peso.

Fuera del MVP: escaneo de códigos de barras, tickets con OCR, compra directa en tienda, comunidad, suscripción.

---

## 5. Arquitectura propuesta

- **App:** Flutter (un código para iOS y Android; plugin `health`). React Native es alternativa viable.
- **Backend:** API (Node/TypeScript o Python/FastAPI) + PostgreSQL. Servicio de ingesta de precios (jobs programados), normalización y emparejamiento de productos.
- **Optimizador:** dado un menú, encuentra la combinación de tiendas más barata (problema de lista de compras con costo de desplazamiento opcional).
- **Offline:** caché local de menú y última lista.
- **Seguridad/privacidad:** consentimiento explícito, cifrado en tránsito y reposo, datos de salud minimizados, borrado de cuenta.

### Roadmap sugerido
| Fase | Contenido |
|---|---|
| 0 (2–4 sem) | Validar con nutricionista; decisión legal sobre precios; contactar cadenas |
| 1 (6–8 sem) | MVP con catálogo de ~300 ingredientes, 1–2 tiendas, menú semanal, calculadora |
| 2 (4–6 sem) | Salud/Health Connect, seguimiento y ajuste semanal |
| 3 | Más tiendas (Makro, Tottus, mercados), colaborativo, beta cerrada en Lima |
| 4 | Publicación en App Store / Google Play |

---

## 6. Riesgos principales
1. **Acceso a precios** (legal/técnico): el mayor riesgo del proyecto.
2. **Responsabilidad sanitaria:** requiere revisión de un nutricionista colegiado y descargos claros.
3. **Revisión de tiendas de apps** por datos de salud.
4. **Precios desactualizados:** mostrar siempre fecha de actualización.
5. **Retención:** el seguimiento diario tiende a abandonarse; la compra semanal automática ayuda.

## 7. Próximos pasos recomendados
1. Validar con un nutricionista el plan y los límites calóricos.
2. Consultar a un abogado sobre el acceso a precios y el tratamiento de datos de salud.
3. Hacer una revisión técnica manual de cada tienda online y contactar a los grupos comerciales.
4. Elegir Flutter vs React Native y armar un prototipo.
5. Definir el modelo de negocio (suscripción, afiliados con tiendas).

## Fuentes
- Dinu et al., *Adv Nutr* 2020: https://pubmed.ncbi.nlm.nih.gov/32059053/
- Plugin `health`: https://docs.carp.dk/packages/flutter-health-plugin
- Flutter Health Connect: https://pub.dev/documentation/flutter_health_connect/latest/
- Supermercados Perú: https://www.peru-retail.com/indecopi-metro-plaza-vea-tottus-vivanda-wong-precios/
- Ley 29733: https://lpderecho.pe/ley-proteccion-datos-personales-ley-29733-actualizada/
