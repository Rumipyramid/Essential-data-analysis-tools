# Narrativa de un deck monolito

Un deck monolito es un argumento, no un catálogo. Lo que lo hace convincente es el orden: cada lámina responde la
pregunta que dejó abierta la anterior.

## Arco por defecto (manifiesto o propuesta de equipo)

| Parte | Pregunta que responde | Láminas típicas |
|---|---|---|
| 1 · El problema | ¿Qué dejó de funcionar? | Portada con un título que nombra el problema · la evidencia de la falla · el límite que nos afecta a nosotros |
| 2 · Cómo evoluciona el campo | ¿Hacia dónde va? | Quién más lo ve (precedentes) · qué dice la vanguardia · lo que ya hacemos (logros reales, con cifras del repo) |
| 3 · Cómo vemos el problema | ¿Qué entendemos que otros no? | La idea fuerza · el mecanismo (ciclos, entornos, capas) · un ejemplo que lo junta todo |
| 4 · Lo que está en juego | ¿Por qué importa ahora? | La batalla de fondo · la novedad que lo vuelve urgente · la posición ética |
| 5 · Dónde lo probamos | ¿Cómo se ve en concreto? | El canal o terreno · un caso real con cifras · el método aplicado al caso · el alcance |
| 6 · Lo que proponemos | ¿Qué hacemos el lunes? | Qué existe hoy · definición · qué aprender · pasos · opciones para decidir juntos (por ejemplo, el nombre) · manifiesto de cierre |

**Empieza por el problema** (preferencia del usuario, 2026-10-20). El título de portada nombra lo que dejó de
funcionar y deja ver la salida, como en «El diseño conductual ha muerto. Larga vida al diseño conductual.». Lo que
el equipo debe decidir (un nombre, una prioridad) se presenta como opciones con criterios, sin recomendación,
cuando el usuario así lo pide.

Adáptalo al propósito. Para una decisión, la parte 4 puede ser «opciones y recomendación». Para una
investigación, la parte 1 puede ser «la pregunta» y la parte 3 «lo que encontramos».

## Reglas del hilo

1. **Escribe primero los títulos, en orden, y léelos solos.** Deben contar la historia completa sin el resto del texto.
2. **Cada parte tiene nombre** y aparece en el pie de cada lámina (`Parte 3 · Cómo vemos la conducta · 07 / 30`).
3. **Cada nota del orador termina con un puente**: una frase que plantea la pregunta de la lámina siguiente
   («Puente: el problema, para nosotros, es que nuestra definición sigue describiendo ese empujón»).
4. **Un caso concreto vuelve tangible lo abstracto.** Antes del cierre, aplica el argumento a un caso real del
   contexto del usuario, con cifras citadas y rotulado como propuesta si no está en marcha.
5. **Cierra con lo que se puede repetir sin la presentación**: el manifiesto (seis principios y un propósito) o una
   frase que resuma la propuesta.

## Evidencia y honestidad

- **Logros propios:** solo con fuente del proyecto (tablero de proyectos, notas de investigación, perfil; en el repo de origen, `TABLERO_BEHOLDER.md`) o dados por el usuario. Si un
  número es estimado («est.» en el tablero), dilo o no lo uses.
- **Fuentes externas:** autor y año en la lámina; en las notas, qué encontraron, dónde se publicó y qué tan sólido es.
  Registra cada fuente nueva en el registro de fuentes del proyecto, si lo tiene.
- **Evidencia débil:** si un caso famoso no tiene evaluación independiente, úsalo como ejemplo y dilo en la lámina.
- **Posición propia:** rotúlala en el pie («Es nuestra posición, no un hallazgo»).
- **Propuestas:** rotúlalas como tales («Propuestas del informe, no proyectos en marcha»).
- **Referencias:** cierra con un anexo de referencias por parte (formato en `layouts.md`) y deja la lista completa en el
  repo. Las fuentes de la lámina de vanguardia deben ser recientes (últimos dos o tres años); lo anterior va como base.

## El propósito sin sonar ingenuo

Un propósito amplio («aportar a las personas, la ciudad, el país, el planeta») se vuelve creíble cuando se ata a una
forma de demostrarlo: «…y demostrarlo con evidencia, no con promesas». Evita verbos de salvación («transformar el
mundo») y prefiere verbos de oficio («ampliar», «medir», «diseñar», «demostrar»).

## Revisión crítica final (preguntas)

1. ¿Hay alguna afirmación que el usuario o su equipo podría desmentir con un ejemplo propio?
2. ¿Cada término técnico se explica la primera vez que aparece?
3. ¿Alguna lámina tiene dos ideas?
4. ¿Las figuras centrales coinciden con la estructura de la idea (3, 4, ciclo o jerarquía)?
5. ¿El orden obliga a pasar a la siguiente lámina, o se podría barajar sin perder nada? Si se puede barajar, falta hilo.
