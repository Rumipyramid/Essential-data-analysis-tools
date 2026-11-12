---
name: monolito
description: Crea presentaciones brutalistas, minimalistas y low-fi (fondo casi negro, texto violeta, Archivo Black + Space Mono, reglas gruesas) que funcionan como manifiesto o propuesta de equipo, con un hilo narrativo en partes, redacción de experto, evidencia citada y láminas con una figura central (triángulo, cuadrado, círculo o rombo). Úsala cuando el usuario invoque /monolito o pida "una presentación brutalista", "un deck low-fi negro y violeta", "un manifiesto en slides", "una presentación como la de El diseño conductual ha muerto" (antes "Diseño de agencia"), o quiera convertir una argumentación en un deck con este estilo. No la uses cuando una marca o identidad propia manda sobre el estilo (en el repo de origen, la marca Rimac, que tiene `presentaciones-rimac` y `rimac-slides`, y la identidad de Mu).
---

# Monolito — presentaciones brutalistas que argumentan

Un deck monolito no decora: **argumenta**. Cada diapositiva dice una sola idea, en frases cortas que se entienden sin
haber estado en la conversación. El estilo es brutalista y austero para que el texto y las figuras hagan todo el
trabajo. El ejemplo de referencia es el deck «El diseño conductual ha muerto. Larga vida al diseño conductual.»:
ocho de sus láminas están en `references/ejemplo/` (portada, cifras, grilla con habilitador, círculo, rombo,
cuadrado, manifiesto y referencias), listas para copiar como modelo.

Las rutas de esta guía son relativas a la carpeta de la skill (la que contiene este `SKILL.md`).

## Cuándo usarla

- El usuario quiere convencer a un equipo, presentar una tesis, un manifiesto, una propuesta de rol o una estrategia.
- El usuario pide explícitamente el estilo brutalista, low-fi, negro y violeta, o `/monolito`.
- **No** cuando una marca propia manda sobre el estilo (ver la descripción). Si el usuario pide otros colores, cambia solo los tokens
  de color (§3); todo lo demás se mantiene.

## 1. Proceso en seis pasos

1. **Entiende el mensaje antes de escribir.** Escribe en una frase la idea que el público debe llevarse. Identifica
   al público (qué sabe, qué no) y el propósito (inspirar, decidir, alinear). Lee lo que el proyecto ya sabe del tema:
   su índice de conocimiento, sus notas de investigación, el tablero de proyectos del equipo y el perfil del usuario,
   si existen (en el repo de origen: `research/alma.md`, `research/_nodes/`, `TABLERO_BEHOLDER.md` y
   `research/yopersona/perfil.md`). **Nunca inventes logros, cifras ni proyectos**: si no están en el proyecto ni los
   dio el usuario, pregunta o deja `[por confirmar]`.
2. **Arma el hilo antes que las diapositivas.** Divide el deck en 3 a 6 partes con nombre. Cada diapositiva tiene una
   sola idea y una frase puente (en las notas) que abre la siguiente. Para manifiestos o propuestas usa por defecto el
   arco de `references/narrativa.md`, que empieza por el problema: lo que dejó de funcionar → cómo evoluciona el campo
   (y lo que ya hacemos) → cómo vemos el problema → lo que está en juego → dónde lo probamos (un caso concreto) →
   qué proponemos → cierre con el manifiesto. El título de portada nombra el problema, no la solución.
3. **Elige el formato por la naturaleza de cada idea**, no por variedad (tabla de §4). Si hay 3, 4 ideas o un ciclo,
   usa una figura central (§5).
4. **Redacta como experto en redacción** (§2). Rotula lo que es posición propia frente a lo que es hallazgo.
5. **Construye y publica con el tipo de Artifact "Slides"** (§6). Escribe primero `project/deck.json` y la portada,
   publica, y luego el resto en tandas.
6. **Revisa con mirada crítica antes de entregar** (§7) y guarda en el repo lo que corresponda (§8).

## 2. Redacción

Sigue `references/redaccion.md` (y la guía de redacción del proyecto, si tiene una). En resumen:

- **Primero la conclusión.** El título de la diapositiva ya afirma algo ("El límite está en la definición"), no
  anuncia un tema ("Limitaciones").
- **Una idea por frase; frases de 25 palabras o menos.** Primera persona del plural si es un manifiesto ("diseñamos",
  "medimos").
- **Nada que solo el sistema conozca.** Explica cada término técnico en la misma frase ("capitación: un pago fijo por
  afiliado a la red médica"). Presenta a cada actor ("la petrolera BP", "el laboratorio del Ministerio de Educación").
- **Las fuentes se cuentan**: autor y año en la diapositiva; revista, tamaño de muestra y matices en las notas.
- **Rotula la posición propia**: "Es nuestra posición, no un hallazgo" en el pie, cuando la idea es una tesis.
- **Nunca afirmes de más.** Si la evidencia es débil, dilo en la propia diapositiva ("Ojo: nunca se evaluó de forma
  independiente").
- **Listas detalladas, ideas fuerza sintéticas.** Las listas pueden tener frases completas; los enunciados grandes,
  no más de diez palabras.

## 3. Sistema visual

| Token | Valor | Uso |
|---|---|---|
| Fondo principal | `#0E0B14` | Casi todas las diapositivas |
| Fondo secundario | `#17121F` | Enunciados, aperturas, definición y manifiesto |
| Acento (fondo) | `#B9A2FF` con texto `#0E0B14` | Una sola diapositiva de quiebre por deck (o una por parte, como máximo) |
| Texto | `#B9A2FF` | Títulos y texto principal |
| Texto tenue | `#8F7CC9` | Descripciones, pies, notas en pantalla |
| Display | `Archivo Black`, mayúsculas, peso 400 | Títulos (80 px), enunciados (130-200 px), cifras (88 px) |
| Texto | `Space Mono` 400/700 | Todo lo demás |
| Escala | 200 · 150 · 80 · 44 · 30-36 · 24-28 | Portada · enunciado · título · frase fuerte · subtítulo · texto (mínimo 24 px) |
| Reglas | 8 px (divisiones mayores) · 4 px (tarjetas) · 2 px (tablas) | Siempre del color del texto |
| Márgenes | `padding:128px 128px 160px` | Zona útil: x 128-1792, y 128-920 |
| Pie | `Parte N · Nombre de la parte · NN / TT`, 24 px, mayúsculas, `bottom:64px` | En todas menos la portada; puede sumar una nota corta |

Contraste: violeta sobre casi negro supera 7:1; el tono tenue supera 5:1. Esquinas rectas, sin sombras ni gradientes.

## 4. Formatos por tipo de idea

Las plantillas completas están en `references/layouts.md`.

| La idea es… | Formato |
|---|---|
| Una frase fuerza que debe quedar | **Enunciado**: título gigante + una frase (fondo secundario) |
| Lo que ya se logró o un contraste | **Dos columnas** con regla superior de 8 px |
| Comparar opciones en varias dimensiones | **Tabla** de 2 a 5 columnas, 24-26 px |
| Una lista de 6 a 8 elementos paralelos | **Grilla** 2×4 o 3×2 de tarjetas con regla de 4 px |
| Tres cifras que cuentan un caso | **Cifras grandes** (88 px) con leyenda |
| Tres conceptos distintos con significado | **Tres figuras** (○ □ △) en fila |
| Algo pequeño dentro de algo grande | **Punto en cuadrado** (lo que se mide frente a lo que importa) |
| Tres ideas relacionadas | **Triángulo central** (§5) |
| Cuatro ideas | **Cuadrado central** (§5) |
| Un ciclo, un loop, algo que vuelve | **Círculo central** (§5) |
| Un concepto general sobre varias partes | **Rombo central** (§5) |
| Una lista con un elemento que atraviesa a los demás | **Grilla con franja de habilitador transversal** |
| Las fuentes de todo el deck | **Referencias** (anexo final, por parte) |
| Cambio de parte o quiebre emocional | **Diapositiva acento** (fondo violeta) |
| El cierre | **Manifiesto**: 6 principios en grilla + propósito |

## 5. Figuras centrales: triángulo, cuadrado, círculo y rombo

La figura va **en el centro** de la lámina, grande y de línea gruesa (8 px). Las ideas van **alrededor**, junto a
cada vértice, esquina o punto. Dentro de la figura va una o dos palabras que nombran lo que une a las ideas.

- **Triángulo, modo «tres»:** tres ideas que se relacionan entre sí (ninguna manda). Una idea por vértice.
- **Rombo:** un concepto general que ordena varias partes (2 a 4). Las partes van en una fila horizontal bajo el
  rombo, separada por una regla de 4 px. Usa el rombo, y no el triángulo, cuando la base lleva íconos ○ □ △: así el
  concepto general no se confunde con una de sus partes (regla del usuario, 2026-10-20).
- **Triángulo, modo «jerarquía»:** igual que el rombo, pero solo si ninguna parte de la base usa el △.
- **Cuadrado:** exactamente cuatro ideas, una por esquina (marcada con un punto).
- **Círculo:** un ciclo de 3 a 6 pasos en sentido horario, con flechas entre pasos. Úsalo cuando algo vuelve, se
  repite o se retroalimenta. Si el orden no es fijo, dilo en las notas.

**No calcules las coordenadas a mano.** Genera la figura con el script y pega el resultado en la diapositiva:

```bash
python scripts/figuras.py circulo --pasos 4
python scripts/figuras.py triangulo --modo tres
python scripts/figuras.py triangulo --modo jerarquia --base 3
python scripts/figuras.py cuadrado
python scripts/figuras.py rombo --base 3
# sobre fondo acento: --color "#0E0B14" --tenue "#0E0B14"
```

El script imprime el SVG y las cajas de texto ya posicionadas, con marcadores `[..]` y el largo máximo de cada una.
El título de la lámina debe caber en una sola línea (unos 22 caracteres a 80 px), porque la figura empieza en y≈240.

**Dos gramáticas, no las mezcles.** La figura central dice **cuántas ideas hay y cómo se relacionan**. Si el deck
además usa íconos pequeños con significado (en el deck de referencia: ○ persona, □ entorno, △ sistema, ◇ concepto general), decláralos
una vez en una leyenda y mantenlos pequeños (36-64 px) para que no se confundan con la figura central.

## 6. Construir y publicar con el tipo «Slides»

Si no tienes la herramienta `Artifact` con el tipo «Slides», entrega un solo archivo HTML con una `<section>` de
1920×1080 por lámina y las mismas reglas (estilos en línea, tipografías de Google Fonts, notas en un `<aside>`).

1. Llama a `Artifact` con `action: "quickstart"`, `intent: "slides"` y `design_systems: false` (el estilo ya está
   definido aquí). Crea el deck con el `type_url` que devuelve, un `title` y `auto_open: "after_first_write"`.
2. Trabaja en una carpeta del scratchpad (`<scratchpad>/deck/`) con `project/deck.json` y
   `project/slides/<id>.html`. Ejemplo de `deck.json` en `references/layouts.md`.
3. Escribe `deck.json` completo (con `order`, `sections` por parte y `faces` de Archivo Black y Space Mono) y la
   portada; publica ambos en una llamada (`url`, `root`, `file_path` = deck.json, `files` = portada).
4. Escribe el resto **de a tres diapositivas** y publica cada tanda (`file_path` = una, `files` = las otras).
5. Cada diapositiva lleva notas del orador en un `<aside>` final: qué decir, la fuente completa y la frase puente a
   la siguiente.
6. **Al revisar un deck ya publicado:** lee primero los archivos con `action: "read"`, porque el usuario puede
   haberlos editado en la página. Si una publicación se rechaza porque alguien guardó antes, vuelve a leer ese
   archivo, aplica tu cambio sobre su versión (conserva lo que el usuario cambió) y publica de nuevo.
7. Para quitar diapositivas, sácalas de `order` y manda `"project/slides/<id>.html": null`.
8. El artifact es privado: avisa al usuario que debe compartirlo desde el menú Compartir para que otros lo abran.

## 7. Revisión crítica antes de entregar

- **Verdad:** ¿cada cifra y cada proyecto tiene fuente (repo o usuario)? ¿Hay alguna afirmación que el usuario
  podría desmentir ("solo cambiamos conductas", "solo dentro de la empresa")? Corrígela antes de que la vea.
- **Hilo:** lee solo los títulos en orden. ¿Cuentan la historia completa? ¿Cada nota termina con un puente?
- **Una idea por diapositiva:** si una lámina tiene dos ideas, son dos láminas.
- **Jerga:** busca términos sin explicar (sigla, autor sin presentar, concepto técnico).
- **Que quepa:** calcula el alto antes de publicar (fórmulas en `references/layouts.md`). Nada debe pasar de y=920.
- **Figuras:** ¿la figura central coincide con la estructura de la idea (3, 4, ciclo, jerarquía)?
- **Posición frente a hallazgo:** ¿las tesis propias están rotuladas como tales?
- No hace falta renderizar ni tomar capturas salvo que el usuario lo pida; si dudas de que algo quepa, acórtalo.

## 8. Guardar lo aprendido

- Si el proyecto lleva un registro de fuentes, cada fuente nueva del deck se anota ahí, y la idea vive en una nota
  de investigación (en el repo de origen: el códice de `cronista` en `research/fuentes/codice.md`, los nodes de
  `research/_nodes/` y el índice `research/alma.md`, donde el deck se registra como output).
- La lista completa de referencias (título, revista, rigor, enlace) se guarda como documento junto al deck; la lámina
  final muestra solo autor y año.
- Las decisiones de contenido que el usuario corrige (un dato, un nombre, un propósito) se anotan en el node para que
  la próxima versión no repita el error.

## 9. Archivos de la skill

| Archivo | Qué contiene |
|---|---|
| `SKILL.md` | Este manual |
| `LEEME.md` | Cómo instalar la skill en Claude Code o claude.ai y qué necesita |
| `references/layouts.md` | Plantillas HTML de cada formato, `deck.json` de ejemplo y fórmulas para que el texto quepa |
| `references/narrativa.md` | Arco narrativo por defecto, frases puente, manifiesto y cómo rotular evidencia |
| `references/redaccion.md` | Reglas de redacción para que cada lámina se entienda sola |
| `references/ejemplo/` | Ocho láminas reales del deck de referencia y su `deck.json`, para copiar como modelo |
| `scripts/figuras.py` | Genera triángulo, cuadrado, círculo y rombo con sus etiquetas posicionadas (solo stdlib) |
