# Matriz de Expertiz — Research & Behavioral Design

Ejercicio de **diferenciación de taxonomías** sobre la propuesta de matriz que unifica el rol de
UX Research con el de Behavioral Design.

## Alcance

El ejercicio se aplica **únicamente a la columna «Capacidades incluidas»**. Las columnas Dimensión,
Peso, «Definición para el rol», los cuatro niveles (Professional → Master), «Evidencias sugeridas»
e «IA integrada» se conservan sin modificar respecto del archivo original.

## Archivos

| Archivo | Qué es |
| --- | --- |
| `Propuesta_Matriz_expertiz_1.xlsx` | Propuesta original recibida (entrada, sin modificar). |
| `Propuesta_Matriz_expertiz_taxonomias.xlsx` | Libro de trabajo generado (salida). |
| `build_matriz_taxonomias.py` | Script que genera la salida a partir de la entrada. |

Regenerar la salida:

```bash
python3 build_matriz_taxonomias.py            # usa Propuesta_Matriz_expertiz_1.xlsx
python3 build_matriz_taxonomias.py otro.xlsx  # o un archivo de entrada distinto
```

Requiere `openpyxl`.

## Hojas del libro generado

| Hoja | Contenido |
| --- | --- |
| 0. Lee me | Alcance, qué significa «ordenar por niveles y taxonomía», criterio de ordenamiento. |
| 1. Taxonomías | Diccionario: la meta-capacidad (T0), 9 clases (T1–T9), 3 ejes transversales (E1–E3), 2 categorías de control (X, Y). |
| 2. Ejes transversales | Campos de investigación (incluye la respuesta a «¿alguna más?»), sujetos y especialidad de diseño. |
| 3. Meta-capacidades | Una por dimensión: qué compone, qué pregunta resuelve, cómo progresa 1→4 y cómo cambia según el campo. |
| 4. Ética del liderazgo | Modelo de medición de T7b: el equilibrio que se pondera, el umbral que se verifica, indicadores, aplicación por nivel y cautelas. |
| 5. Desglose capacidades | Los ítems actuales de la columna, uno por fila, con clase, nombre normalizado y decisión. |
| 6. Columna C propuesta | La columna reescrita y ordenada por niveles, lista para pegar. |
| 7. Matriz propuesta | La matriz completa con la columna C nueva y el resto intacto. |
| 8. Hallazgos y decisiones | Problemas detectados y preguntas abiertas para cerrar con los dos leads. |

## El modelo en una línea

Dentro de cada dimensión, la columna se lee de más abstracto a más concreto:

```
T0 Meta-capacidad → T1 Objetivo → T2 Enfoque → T3 Metodología → T4 Técnica
                    → T5 Marco → T6 Artefacto → T7 Calidad y ética
                    → T8 Práctica operativa → T9 Competencia transversal
```

**T0** existe en las cinco dimensiones: es la capacidad de *elegir* bien, no de ejecutar mucho, y es
donde se ancla la progresión Specialist → Expert.

**T7b — Ética del liderazgo** aplica en la Dimensión 5 y como condición de los niveles 3 y 4 de todas
las dimensiones. Se mide en dos partes que no se mezclan:

- **Equilibrio** (se pondera): productividad del equipo ↔ satisfacción del equipo con quien lidera,
  leídas en el mismo periodo y nunca por separado.
- **Umbral** (se verifica, no se pondera): respeto básico — sin acoso, sin mansplaining, sin conductas
  excluyentes. No entra en la ponderación 30/20/15/20/15; su incumplimiento verificado bloquea el nivel.

Y tres ejes encuadran la matriz completa sin ser capacidades evaluables:
**E1 Campo** (Digital / Físico / Híbrido [/ Sistémico]), **E2 Sujeto**,
**E3 Especialidad de diseño** (Diseño Conductual, única).
