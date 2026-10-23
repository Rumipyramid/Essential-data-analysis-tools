# El códice: memoria aislada de Orfeo

Orfeo guarda lo que trabaja. Sin memoria no hay serie, y la serie es el terreno donde este método es
menos especulativo. Pero un diario de sueños es material íntimo, así que la memoria vive en un
espacio **aislado por diseño**, separado tanto del resto del repositorio como del resto de los
skills.

## Las dos capas, y por qué están separadas

| | Dónde vive | ¿Se versiona? | Qué contiene |
|---|---|---|---|
| **Maquinaria** | `.claude/skills/orfeo/` | Sí | El método: lentes, convergencia, claves, este archivo. Ningún dato personal. |
| **Códice** | `codice/` en la raíz del proyecto | **Nunca** | Los sueños, las lecturas, la serie codificada. |

La separación no es estética: permite **compartir el método sin compartir los sueños**. El skill se
puede publicar, copiar a otro proyecto o enseñar a alguien; el códice no sale de la máquina.

## Regla de aislamiento

**Orfeo escribe en `codice/` y en ningún otro sitio.** No toca `docs/`, ni el README, ni
`.claude/settings.json`, ni ningún archivo de otro skill, ni añade hooks. No hay estado compartido
con nada más: cualquier otro skill del proyecto funciona exactamente igual exista o no el códice, y
Orfeo funciona exactamente igual exista o no el códice.

Antes de escribir nada por primera vez en un proyecto, comprueba y, si falta, establece el
aislamiento con **dos mecanismos independientes**, porque uno solo se borra por accidente:

```bash
# 1. regla en el .gitignore de la raíz
printf '\n# Códice Orfeo — bitácora de sueños. Contenido personal sensible.\ncodice/\n' >> .gitignore

# 2. .gitignore propio dentro del directorio, que sobrevive al borrado del anterior
mkdir -p codice/bitacora
printf '# Todo este directorio queda fuera de git. Sin excepciones.\n*\n!.gitignore\n' > codice/.gitignore

# comprobación — debe nombrar la regla, y codice/ no debe aparecer en status
git check-ignore -v codice/bitacora
git status --short
```

**Comprueba la visibilidad del repositorio antes de escribir el primer sueño.** Si es público, dilo
en voz alta al soñante: no es un detalle técnico, es la diferencia entre un diario y una publicación.
Un repositorio privado no cambia la regla —el códice sigue sin versionarse— pero sí cambia la
urgencia con la que hay que explicarla.

Si `codice/` aparece alguna vez en `git status`, **no hagas commit**: el aislamiento está roto.
Restáuralo y dilo.

## Qué no entra en el códice, nunca

- **Nombres propios de terceros.** Las personas que aparecen en los sueños de alguien no han
  consentido figurar en ningún archivo. Se guardan por su relación —"mi jefa", "mi novia", "una
  compañera de trabajo"— y nunca con nombre, apellido, cargo, empresa o contacto. Si el soñante los
  menciona, se registran igualmente por la relación.
- **Datos identificativos del soñante** más allá de lo que la lectura necesita.
- **Conclusiones presentadas como hechos.** Todo lo que sea inferencia o construcción se guarda
  etiquetado como tal, igual que en el informe. Un archivo se lee dentro de un año sin el contexto
  de la conversación, y una hipótesis sin etiqueta se habrá convertido en un dato.

## Estructura

```
codice/
├── README.md                    reglas de aislamiento y persistencia
├── bitacora/AAAA-MM-DD-motivo.md una entrada por sueño
├── serie.csv                    codificación ligera, una fila por sueño
└── serie.md                     la deriva: qué se repite, qué muta, qué desaparece
```

## La entrada: cabecera obligatoria

La cabecera es lo que hace posible la serie, así que se rellena siempre, incluso con `?`. Son los
campos que han mostrado capacidad de discriminar; añadir más columnas "por si acaso" degrada el
análisis en vez de mejorarlo.

| Campo | Valores |
|---|---|
| `fecha_relato` | Cuándo se contó. Dato seguro. |
| `fecha_sueno` | Cuándo se soñó. `~` si es aproximada: no inventes precisión. |
| `motivo` | Una palabra para el nombre del archivo. |
| `escenario` · `figuras` · `custodia` | Descriptivos. En `figuras`, marca cuáles son personas reales. |
| `amenaza` | ambiental / autoridad / colectiva / interna / ninguna |
| `agencia` | 0 ninguna · 1 un acto · 2 acción intencional · 3 acción + iniciativa agresiva |
| `actos_propios` | Cuántas cosas hace el soñante. Contadas, no estimadas. |
| `conoce_la_causa` | sí / no / parcial |
| `afecto_en_relato` | sí / no. Si el relato declara emociones, no si tú se las supones. |
| `desenlace` | sin lisis / veredicto / lisis falsa / resuelto |
| `lentes_ciegas` · `hallazgo_central` · `pendiente` | Las ciegas con su motivo; el hallazgo en una frase; el pendiente con su estado. |

El cuerpo de la entrada lleva el **relato literal entre comillas, textual, con las vacilaciones del
soñante intactas**. La gramática de la duda —"me da la impresión", "o quizás", "o al menos"— ha
resultado ser dato en más de un sueño; pasarla a limpio la destruye.

## Rutina de cada sesión

1. Si existe `codice/`, **lee `serie.md` y `serie.csv` antes de aplicar las lentes**. La serie
   cambia qué es notable en el sueño nuevo: un rasgo que parece banal en una pieza puede ser el
   tercer caso de un invariante.
2. Aplica el método normal (SKILL.md).
3. Escribe la entrada nueva, añade su fila al CSV y **actualiza `serie.md`**: tabla, invariantes,
   derivas, pendientes.
4. Revisa los **pendientes abiertos** de sesiones anteriores y pregunta por ellos una vez. Una
   acción verificable que nadie comprueba convierte el método en entretenimiento.
5. Comprueba el aislamiento (`git status --short`) y **entrega los archivos al soñante** para que
   tenga copia: el contenedor es efímero y el códice no se versiona, así que sin descarga se pierde.

## Series: lo que hay que mirar

Con n ≥ 3 el objeto es la **deriva**, no la pieza:

- **Lo invariante** — qué sale igual en todos. Es el hallazgo más fuerte que una serie puede dar.
- **Lo que se mueve** — los campos con variación son los únicos informativos; vigílalos y di en qué
  dirección van.
- **El punto de corte** — en sueños que se repiten, el cambio suele estar en dónde termina.
- **El artefacto del reporte** — si los relatos se alargan, parte de la "intensificación" es que el
  soñante está contando mejor, no que esté soñando peor. Descuéntalo explícitamente.

Y la advertencia que debe quedar escrita **dentro** del propio códice, no solo en el informe: una
serie corta construye narrativas coherentes con facilidad, y este método las fabrica mejor que
ninguna otra cosa. La coherencia de un archivo no es evidencia de que sea cierto.
