# -*- coding: utf-8 -*-
"""
Genera el libro de trabajo del ejercicio de taxonomías para la
Matriz de Expertiz Research & Behavioral Design.

Entrada:  Propuesta_Matriz_expertiz_1.xlsx (columna "Capacidades incluidas")
Salida:   Propuesta_Matriz_expertiz_taxonomias.xlsx

El ejercicio se aplica ÚNICAMENTE a la columna "Capacidades incluidas".
El resto de columnas de la matriz original se conserva sin cambios.
"""

import os
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(HERE, "Propuesta_Matriz_expertiz_taxonomias.xlsx")

# ---------------------------------------------------------------- estilos ---

AZUL = "1F3864"
AZUL_CLARO = "D9E2F3"
GRIS = "F2F2F2"
AMBAR = "FFF2CC"
VERDE = "E2EFDA"
NARANJA = "F8CBAD"
CELESTE = "DDEBF7"

TITULO = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
CABECERA = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
NEGRITA = Font(name="Calibri", size=10, bold=True)
NORMAL = Font(name="Calibri", size=10)
FILL_TITULO = PatternFill("solid", fgColor=AZUL)
FILL_CABECERA = PatternFill("solid", fgColor=AZUL)
FILL_SUAVE = PatternFill("solid", fgColor=AZUL_CLARO)
FILL_GRIS = PatternFill("solid", fgColor=GRIS)
FILL_AMBAR = PatternFill("solid", fgColor=AMBAR)
FILL_VERDE = PatternFill("solid", fgColor=VERDE)

_linea = Side(style="thin", color="BFBFBF")
BORDE = Border(left=_linea, right=_linea, top=_linea, bottom=_linea)

TOP_WRAP = Alignment(vertical="top", wrap_text=True)
TOP_WRAP_CENTER = Alignment(vertical="top", horizontal="center", wrap_text=True)


def encabezar(ws, titulo, subtitulo, ncols):
    """Escribe título + subtítulo fusionados y devuelve la fila de cabecera."""
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=titulo)
    c.font = TITULO
    c.fill = FILL_TITULO
    c.alignment = Alignment(vertical="center", horizontal="left")
    ws.row_dimensions[1].height = 30

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c = ws.cell(row=2, column=1, value=subtitulo)
    c.font = NORMAL
    c.fill = FILL_GRIS
    c.alignment = TOP_WRAP
    ws.row_dimensions[2].height = 45
    return 4


def escribir_tabla(ws, fila_cabecera, columnas, filas, anchos):
    """columnas: lista de nombres. filas: lista de listas. anchos: lista de int."""
    for j, nombre in enumerate(columnas, start=1):
        c = ws.cell(row=fila_cabecera, column=j, value=nombre)
        c.font = CABECERA
        c.fill = FILL_CABECERA
        c.alignment = TOP_WRAP_CENTER
        c.border = BORDE
    ws.row_dimensions[fila_cabecera].height = 30

    for i, fila in enumerate(filas, start=fila_cabecera + 1):
        for j, valor in enumerate(fila, start=1):
            c = ws.cell(row=i, column=j, value=valor)
            c.font = NORMAL
            c.alignment = TOP_WRAP
            c.border = BORDE

    for j, ancho in enumerate(anchos, start=1):
        ws.column_dimensions[get_column_letter(j)].width = ancho

    ws.freeze_panes = ws.cell(row=fila_cabecera + 1, column=1)
    return fila_cabecera + len(filas)


# ------------------------------------------------------- 1. taxonomías ------

TAXONOMIAS = [
    ("EJES TRANSVERSALES — encuadran la matriz completa; no se evalúan como capacidad suelta",
     None, None, None, None),
    ("E1. Campo de investigación",
     "¿Dónde ocurre el comportamiento que estudiamos?",
     "El entorno o canal en el que se observa y se interviene. Es un eje, no una capacidad: "
     "toda metodología y toda técnica se instancia en uno o más campos.",
     "Digital (UX) · Físico (presencial) · Híbrido (omnicanal)",
     "Columna nueva / etiqueta transversal. Sale de «Capacidades incluidas»."),
    ("E2. Sujeto de estudio",
     "¿A quién estudiamos?",
     "La población cuyo comportamiento se investiga. Se confunde con frecuencia con el campo; "
     "conviene mantenerlo como eje separado para no duplicar campos.",
     "Cliente / usuario · No cliente y mercado · Colaborador · Asesor o intermediario",
     "Eje transversal (opcional, recomendado)."),
    ("E3. Especialidad de diseño",
     "¿Qué disciplina de diseño evalúa esta matriz?",
     "Única especialidad contemplada: Diseño Conductual. Product Design y Service Design NO se "
     "evalúan aquí: aparecen solo como modelo de colaboración.",
     "Diseño Conductual (única)",
     "Declaración de alcance en la cabecera de la matriz."),
    ("NIVELES DE LA CAPACIDAD — T0 gobierna la composición; T1 a T4 son secuencia; T5 a T9, transversales",
     None, None, None, None),
    ("T0. Meta-capacidad",
     "¿Sabe elegir, no solo ejecutar?",
     "La capacidad de COMPONER los niveles T1–T4 de forma coherente con la decisión que hay que tomar: "
     "elegir el objetivo correcto, el enfoque proporcionado, la metodología que la decisión exige y la "
     "técnica que corresponde. Es lo que distingue a un Specialist de un Expert: no ejecutar mejor, "
     "elegir mejor. Cada dimensión tiene la suya.",
     "D1 Estrategia de investigación · D2 Juicio estratégico · D3 Criterio de intervención · "
     "D4 Criterio de evidencia · D5 Criterio de escalamiento y liderazgo",
     "Encabeza cada dimensión, por encima de T1. Ver hoja «3. Meta-capacidades»."),
    ("T1. Objetivo",
     "¿Para qué investigamos o intervenimos?",
     "La intención de conocimiento o de cambio. Define el tipo de pregunta, no el modo de responderla. "
     "Es el nivel más alto: primero se decide el objetivo, después todo lo demás.",
     "Diagnóstico conductual · Diagnóstico sistémico · Exploración / discovery · Validación (UX validation) · "
     "Evaluación de impacto · Problem framing · Opportunity framing",
     "Encabeza la columna «Capacidades incluidas» de cada dimensión."),
    ("T2. Enfoque",
     "¿Con qué lógica de evidencia?",
     "El paradigma que gobierna la evidencia. Tres cortes independientes: naturaleza del dato "
     "(cuali / cuanti / mixto), origen (primaria / secundaria) y control (observacional / experimental).",
     "Cualitativo · Cuantitativo · Mixto · Primario / secundario · Observacional / experimental",
     "Segundo bloque de la columna."),
    ("T3. Metodología",
     "¿Cómo se estructura el estudio?",
     "El diseño global de la investigación: qué se compara, con quién, en cuántos momentos y bajo qué "
     "control. Una metodología admite varias técnicas.",
     "Desk research · Etnografía / investigación en campo · Estudio longitudinal · Diseño experimental · "
     "RCT · Cuasi-experimento · Pre-post con control · Encuesta poblacional",
     "Tercer bloque de la columna."),
    ("T4. Técnica / instrumento",
     "¿Con qué herramienta concreta se recoge o se analiza?",
     "El instrumento operativo. Se subdivide en técnicas de recolección y técnicas de análisis. "
     "Una misma técnica sirve a metodologías distintas: por eso no puede ir al mismo nivel que la metodología.",
     "Recolección: entrevista · observación estructurada · diario · encuesta · intercept · mystery shopping · "
     "usability test · concept & prototype testing · A/B test · analytics.   "
     "Análisis: diseño muestral · codificación · triangulación · síntesis · análisis estadístico",
     "Cuarto bloque de la columna."),
    ("T5. Marco conceptual",
     "¿Con qué lente interpretamos?",
     "Modelos y teorías que ordenan la lectura del comportamiento y del sistema. No son métodos: "
     "no dicen cómo recoger datos, dicen cómo leerlos.",
     "Frameworks de ciencias del comportamiento (COM-B, EAST, MINDSPACE) · Systems thinking · "
     "Journey thinking · Arquitectura de decisiones · Inferencia causal · Teoría del cambio",
     "Bloque transversal dentro de la columna."),
    ("T6. Artefacto / output",
     "¿Qué produce la capacidad?",
     "El entregable observable. Es lo que permite evidenciar el nivel en la evaluación; "
     "hoy está mezclado con los métodos que lo producen.",
     "Insight · Hipótesis priorizada · Principios y criterios de diseño · Métricas y criterios de éxito · "
     "Concepto de intervención · Prototipo conceptual · Repositorio de evidencia",
     "Bloque transversal; conecta directo con la columna «Evidencias sugeridas»."),
    ("T7. Calidad y ética",
     "¿Bajo qué estándar es válido?",
     "Criterios que hacen la evidencia, la intervención y el ejercicio del liderazgo defendibles. "
     "Deben aparecer en las cinco dimensiones, no solo en una. Donde hay liderazgo, la ética deja de "
     "ser solo ética de la evidencia y pasa a ser también ética del trato con el equipo.",
     "Calidad y suficiencia de evidencia · Gestión de sesgos · Validez interna y externa · "
     "Control de variables · Potencia y tamaño muestral · Ética de la investigación y de la influencia · "
     "Privacidad y trazabilidad · Ética del liderazgo (ver hoja «4. Ética del liderazgo»)",
     "Bloque transversal en las 5 dimensiones. En D5 y en los niveles 3–4 de todas las dimensiones "
     "incluye la ética del liderazgo."),
    ("T8. Práctica operativa (Ops)",
     "¿Cómo se sostiene y escala en el tiempo?",
     "Sistemas, procesos y activos que convierten estudios sueltos en capacidad organizacional acumulativa.",
     "ResearchOps · BehavioralOps · KnowledgeOps · Gobernanza y estándares · Capability building · "
     "Mejora continua · Automatización",
     "Concentrado en la Dimensión 5."),
    ("T9. Competencia transversal",
     "¿Qué habilidad profesional lo hace posible?",
     "Habilidades no metodológicas que atraviesan todas las dimensiones. No son research ni diseño: "
     "son el vehículo. Conviene declararlas aparte para no inflar las dimensiones técnicas.",
     "Pensamiento crítico · Business acumen · Storytelling estratégico · Facilitación · Influencia · "
     "Stakeholder management · Mentoring · Priorización · Comunicación estratégica",
     "Bloque de cierre en cada dimensión, o columna propia."),
    ("CATEGORÍAS DE CONTROL — lo que NO es capacidad y hoy está dentro de la columna",
     None, None, None, None),
    ("X. Modelo de colaboración",
     "¿Con quién se trabaja y en qué rol?",
     "Describe el alcance de la relación con otros equipos (PD/SD, Data, Negocio). No es una habilidad "
     "evaluable: su progresión ya está descrita en los niveles 1 a 4.",
     "Acompañamiento a Product / Service Design · Trabajo con Data & Analytics · Interlocución con negocio",
     "Sacar de «Capacidades incluidas» → describir en la definición del rol y en los niveles."),
    ("Y. Resultado organizacional",
     "¿Qué efecto buscamos en la organización?",
     "Estados deseados de la organización, no capacidades de una persona. Evaluarlos como capacidad "
     "individual genera ambigüedad.",
     "Cultura de evidencia · Continuous learning · Reconocimiento de la capacidad",
     "Sacar de «Capacidades incluidas» → propósito de la dimensión."),
]

# ------------------------------------------------- 2. ejes transversales ----

CAMPOS = [
    ("Digital (UX)",
     "Recomendado",
     "El comportamiento ocurre en un producto o interfaz digital: app, web, onboarding, "
     "flujos de compra, cotización y siniestros, notificaciones.",
     "UX Research, usability testing, analytics de producto, A/B testing, concept & prototype testing.",
     "Hoy la matriz está escrita casi por completo desde este campo."),
    ("Físico (presencial)",
     "Recomendado",
     "El comportamiento ocurre en un entorno físico: sucursal, clínica, punto de venta, "
     "atención presencial, visita domiciliaria.",
     "Etnografía y observación estructurada, intercept, mystery shopping, shadowing, "
     "pilotos en campo, cuasi-experimentos por sede.",
     "GAP: hoy no hay ninguna metodología ni técnica de este campo en la columna."),
    ("Híbrido (omnicanal)",
     "Recomendado",
     "El comportamiento cruza canales dentro de un mismo journey: empieza en la app y termina "
     "presencial, o se resuelve por teléfono o con un asesor.",
     "Journey research multicanal, diarios longitudinales, service safaris, "
     "reconstrucción de trayectorias combinando datos y cualitativo.",
     "Debe declararse como campo propio, no como la suma de los dos anteriores: "
     "su unidad de análisis es la transición entre canales."),
    ("Sistémico / contextual",
     "A decidir — 4.º campo candidato",
     "El objeto no está situado en un canal: mercado, regulación, actores del ecosistema, "
     "normas sociales, evidencia publicada.",
     "Desk research, revisión de literatura y evidencia, análisis de políticas, "
     "social listening, mapeo de actores.",
     "Es el único cuarto campo con criterio propio. Si no se abre, «desk research» y el "
     "«diagnóstico sistémico» que ya están en la matriz quedan sin campo asignable."),
    ("Organizacional / interno",
     "NO abrir como campo",
     "Investigación con colaboradores, asesores o áreas internas.",
     "Las mismas metodologías de los campos anteriores.",
     "No es un campo: es un SUJETO. Abrirlo como campo mezcla dos ejes y obliga a duplicar "
     "todas las metodologías. Va en el eje E2."),
    ("Conversacional / asistido",
     "NO abrir como campo",
     "Contact center, WhatsApp, asesor humano.",
     "Análisis de conversaciones, escucha de llamadas, observación de la interacción.",
     "Cae dentro de Híbrido. Abrirlo por separado fragmenta el eje sin ganancia evaluativa."),
]

# ------------------------------------------------ 3. meta-capacidades -------
# Una por dimensión. La meta-capacidad no es "otra capacidad más": es la que
# gobierna cómo se componen las demás. (Dimensión, nombre, qué compone,
# pregunta que resuelve, progresión 1→4, cómo se evidencia, cambio por campo)

META_CAPACIDADES = [
    ("1. Discovery e Insights",
     "Estrategia de investigación",
     "T1 objetivo + T2 enfoque + T3 metodología + T4 técnica",
     "¿Es esta la investigación que esta decisión necesita, o solo la que sabemos hacer?",
     "1 Professional: ejecuta la estrategia que otro definió y reconoce sus límites.  "
     "2 Specialist: elige metodología y técnicas para un objetivo dado.  "
     "3 Expert: define el objetivo y combina métodos para problemas ambiguos o mal formulados.  "
     "4 Master: define qué preguntas merece hacerse la organización antes de que alguien las pida.",
     "Plan de investigación con la justificación del método frente a alternativas descartadas, "
     "y no solo el método elegido.",
     "En Digital el sesgo es sobrerrepresentar lo instrumentable; en Físico, el acceso al campo "
     "condiciona el diseño; en Híbrido, la unidad de análisis es la transición entre canales."),

    ("2. Estrategia y Problem Solving",
     "Juicio estratégico",
     "T1 framing + T5 marco + T7 criterio de suficiencia + T9 lectura de negocio",
     "¿Qué problema merece resolverse, y con cuánta evidencia basta para decidirlo?",
     "1 Professional: interpreta insights dentro de un encuadre dado.  "
     "2 Specialist: reencuadra el problema e integra usuario, conducta y negocio.  "
     "3 Expert: sostiene la decisión bajo evidencia incompleta y hace explícito el riesgo de "
     "equivocarse.  "
     "4 Master: cambia el encuadre con el que la organización lee sus propios problemas.",
     "Una decisión tomada con evidencia parcial, con el umbral de suficiencia declarado por "
     "adelantado y revisado después.",
     "El campo condiciona el costo de equivocarse: en Físico la corrección es lenta y cara, "
     "lo que sube el estándar de evidencia exigible antes de decidir."),

    ("3. Diseño y Orquestación de Experiencias",
     "Criterio de intervención",
     "T1 conducta objetivo + T5 palanca + T7 ética de la influencia",
     "¿Cuánta intervención pide esta conducta — y cuándo lo correcto es no intervenir?",
     "1 Professional: aplica palancas conocidas a problemas acotados.  "
     "2 Specialist: elige la palanca proporcional al problema y la justifica.  "
     "3 Expert: orquesta intervenciones múltiples anticipando efectos de segundo orden.  "
     "4 Master: define qué está y qué no está permitido intervenir, y por qué.",
     "Una intervención descartada por desproporcionada o por riesgo ético, con el razonamiento "
     "escrito. Saber no intervenir es evidencia de nivel, no ausencia de trabajo.",
     "En Físico la intervención es más difícil de revertir y afecta a terceros presentes; "
     "en Híbrido el riesgo es que la palanca funcione en un canal y rompa el otro."),

    ("4. Experimentación, Medición e Impacto",
     "Criterio de evidencia",
     "T1 objetivo evaluativo + T2 control + T3 metodología + T7 validez",
     "¿Cuánto rigor exige esta decisión — y cuánto sería desperdiciarlo?",
     "1 Professional: ejecuta la validación definida y lee sus límites.  "
     "2 Specialist: elige el diseño según la evidencia que la decisión necesita.  "
     "3 Expert: ajusta rigor, costo, reversibilidad y riesgo, y defiende la causalidad que afirma.  "
     "4 Master: define el estándar de evidencia por tipo de decisión para toda la organización.",
     "Dos decisiones resueltas con distinto nivel de rigor y la justificación de por qué cada una "
     "merecía el suyo.",
     "En Digital el experimento es barato y reversible; en Físico rara vez hay aleatorización "
     "posible, y el cuasi-experimento por sede pasa a ser el diseño de referencia."),

    ("5. Escalamiento y Liderazgo",
     "Criterio de escalamiento y liderazgo",
     "T8 práctica operativa + T7 gobernanza y ética del liderazgo + T9 influencia",
     "¿Qué se estandariza, qué se deja variar, y a qué ritmo se le puede exigir a un equipo?",
     "1 Professional: usa los procesos y documenta para otros.  "
     "2 Specialist: mejora prácticas y acompaña a personas.  "
     "3 Expert: decide qué se vuelve estándar y sostiene el equilibrio entre lo que el equipo "
     "produce y lo que el equipo puede sostener.  "
     "4 Master: responde por que ese equilibrio esté instrumentado y auditado, no solo declarado.",
     "Un estándar adoptado sin imposición, y el resultado del feedback ascendente del equipo "
     "junto a su indicador de entrega en el mismo periodo.",
     "Transversal a los campos. Lo que cambia con el campo es el costo operativo de cada "
     "estándar, no el criterio."),
]

# ----------------------------------------------- 4. ética del liderazgo -----

ETICA_PARTES = [
    ("A. El equilibrio",
     "Productividad del equipo ↔ satisfacción del equipo con la persona que lidera.",
     "Se mide y se pondera. Ninguno de los dos se lee solo.",
     "Un líder con alta entrega y baja satisfacción está quemando al equipo y la matriz debe "
     "verlo. Un líder muy valorado con el equipo estancado tampoco está en nivel. El nivel "
     "está en sostener ambos a la vez, no en maximizar uno."),
    ("B. El umbral",
     "Respeto básico: sin acoso, sin mansplaining, sin conductas excluyentes en el trato cotidiano.",
     "Se verifica, NO se pondera. Es un piso, no una variable.",
     "Si el respeto básico entrara en la balanza, la matriz estaría diciendo que un buen "
     "resultado puede compensarlo. No puede. El incumplimiento verificado bloquea el nivel, "
     "por alto que sea el equilibrio de la parte A y por alto que sea el puntaje en las otras "
     "cuatro dimensiones."),
]

ETICA_INDICADORES = [
    ("A · Productividad del equipo",
     "Estudios e intervenciones entregados Y usados en una decisión",
     "ResearchOps / KnowledgeOps",
     "Entregado sin uso no cuenta: mide actividad, no valor."),
    ("A · Productividad del equipo",
     "Tiempo de ciclo de la evidencia: de pregunta a decisión",
     "ResearchOps",
     "Es el indicador que más tienta a forzar al equipo. Por eso nunca se lee sin el bloque de "
     "satisfacción."),
    ("A · Productividad del equipo",
     "Reutilización del conocimiento y cumplimiento del estándar metodológico",
     "KnowledgeOps / gestión de calidad",
     "Distingue producir mucho de producir capacidad acumulativa."),
    ("A · Satisfacción con quien lidera",
     "Feedback ascendente anónimo: claridad de dirección, apoyo al desarrollo, seguridad "
     "psicológica para discrepar",
     "Encuesta al equipo directo, anónima",
     "n mínimo de 5 respuestas para publicar cualquier resultado. Por debajo, se reporta "
     "agregado o no se reporta."),
    ("A · Satisfacción con quien lidera",
     "Intención declarada de volver a trabajar con esa persona",
     "Encuesta al equipo directo, anónima",
     "Es el indicador que mejor resiste la deseabilidad social: pregunta por conducta futura, "
     "no por opinión."),
    ("A · Satisfacción con quien lidera",
     "Rotación voluntaria del equipo y motivo declarado en la salida",
     "Personas / entrevista de salida",
     "Indicador rezagado: confirma, no anticipa. Nunca se usa solo."),
    ("B · Respeto básico (umbral)",
     "Distribución del habla, de las interrupciones y de la atribución de ideas en reuniones",
     "Observación estructurada de sesiones reales",
     "Es la medición directa del mansplaining: quién es interrumpido y a quién se le atribuye "
     "después la idea. Es conducta observable, no percepción — y es exactamente la técnica que "
     "este equipo ya sabe aplicar."),
    ("B · Respeto básico (umbral)",
     "Equidad en la asignación de oportunidades visibles: quién presenta al comité, quién lleva "
     "el estudio estratégico",
     "Registro de asignaciones del periodo",
     "El trato desigual aparece antes en el reparto de oportunidades que en un reporte formal."),
    ("B · Respeto básico (umbral)",
     "Atribución de autoría en entregables y presentaciones",
     "Repositorio de evidencia",
     "Trazable sin necesidad de encuesta."),
    ("B · Respeto básico (umbral)",
     "Casos abiertos o sostenidos en el canal formal de reporte",
     "Canal de la organización",
     "Es la verificación final, no la primera señal. Una matriz que solo mira aquí llega tarde "
     "siempre."),
]

ETICA_NIVELES = [
    ("1 — Professional",
     "No lidera equipo: no hay equilibrio que medir.",
     "El umbral aplica igual, a su conducta como integrante: respeto, escucha, atribución de "
     "ideas ajenas."),
    ("2 — Specialist",
     "Lidera estudios y acompaña a otras personas. Primeras señales del equilibrio: satisfacción "
     "de quienes acompaña, junto al avance de lo que lidera.",
     "Umbral verificado con las personas a las que acompaña, no solo con su jefatura."),
    ("3 — Expert",
     "Lidera personas y prácticas. El equilibrio se mide formalmente: feedback ascendente anónimo "
     "y entrega del equipo, leídos en el mismo periodo y juntos.",
     "Umbral verificado con el equipo directo. Un incumplimiento verificado impide alcanzar o "
     "mantener este nivel."),
    ("4 — Master",
     "Define la gobernanza. Además de sostener su propio equilibrio, responde por que exista el "
     "sistema: los indicadores, el canal, el anonimato y la consecuencia.",
     "Umbral verificado y, además, instrumentado para toda la capacidad. Un Master no alcanza el "
     "nivel si el sistema de medición no existe, aunque su equipo esté satisfecho."),
]

ETICA_CAUTELAS = [
    ("Anonimato con n mínimo",
     "Por debajo de 5 respuestas no se publica resultado desagregado. Medir satisfacción con el "
     "líder en un equipo de tres personas sin protección es exponer a quien responde."),
    ("Sin represalia, y verificable",
     "El acceso al resultado desagregado y el momento de entrega deben estar definidos antes de "
     "la primera medición, no después de conocer el resultado."),
    ("La percepción de la jefatura no sustituye la del equipo",
     "El umbral se verifica con las personas que reciben el trato, no con quien supervisa a "
     "quien lo da. Es el error de diseño más común de estos sistemas."),
    ("El equilibrio se lee en el mismo periodo",
     "Productividad de un trimestre contra satisfacción de otro permite justificar cualquier "
     "cosa. Misma ventana temporal o no se lee."),
    ("Umbral incumplido no se compensa",
     "No entra en la ponderación 30/20/15/20/15. Bloquea el nivel con independencia del puntaje "
     "de las otras cuatro dimensiones."),
]

# --------------------------------------------- 5. desglose de la columna ----
# (Dimensión, ítem tal como está hoy, taxonomía, ítem normalizado, decisión, nota)

DESGLOSE = [
    # ---- D1
    ("1. Discovery e Insights", "Problem framing", "T1. Objetivo",
     "Problem framing: traducir una decisión de negocio en pregunta de investigación y conducta objetivo",
     "Reubicar",
     "Es el acto de fijar el objetivo del estudio, no un método. Debe encabezar la lista."),
    ("1. Discovery e Insights", "Research Strategy", "T0. Meta-capacidad",
     "Estrategia de investigación: componer objetivo, enfoque, metodología y técnicas de forma coherente",
     "Renombrar",
     "Es la capacidad de ARTICULAR los niveles T1–T4. Ponerla como un ítem más de la lista la iguala "
     "a una técnica. Es la única meta-capacidad que la matriz ya tenía, aunque sin nombrarla como tal."),
    ("1. Discovery e Insights", "estrategia de investigación", "T0. Meta-capacidad",
     "(absorbido por «Research Strategy»)", "Eliminar",
     "Duplicado literal dentro de la misma celda."),
    ("1. Discovery e Insights", "investigación cualitativa, cuantitativa y mixta", "T2. Enfoque",
     "Enfoque cualitativo, cuantitativo y mixto", "Mantener",
     "Correcto, pero hoy convive en la misma frase con campos, metodologías y técnicas."),
    ("1. Discovery e Insights", "UX Research", "E1. Campo de investigación",
     "Campo: Digital (UX)", "Mover a eje transversal",
     "No es una metodología ni una capacidad: es el campo de aplicación. Con la unificación de roles "
     "debe salir de la columna y convertirse en etiqueta transversal."),
    ("1. Discovery e Insights", "Behavioral Research", "E1 / T1 — lente transversal",
     "Lente conductual: aplicable a los tres campos", "Mover a eje transversal",
     "Al unificar UX Research y Behavioral Design, «behavioral» deja de ser un campo paralelo a UX y "
     "pasa a ser objetivo y lente transversal. Mantenerlo en la lista reproduce la separación de roles "
     "que la matriz busca eliminar."),
    ("1. Discovery e Insights", "desk research", "T3. Metodología",
     "Desk research (evidencia secundaria)", "Mantener",
     "Metodología definida por el ORIGEN del dato. Su campo natural es «Sistémico / contextual»."),
    ("1. Discovery e Insights", "muestreo", "T4. Técnica (diseño y análisis)",
     "Diseño muestral", "Mantener",
     "Instrumento, no metodología. Baja un nivel."),
    ("1. Discovery e Insights", "diagnóstico conductual y sistémico", "T1. Objetivo",
     "Diagnóstico conductual / Diagnóstico sistémico", "Reubicar y desagregar",
     "Son dos objetivos distintos (conducta individual frente a sistema de actores) hoy fusionados en "
     "un mismo ítem y listados como si fueran métodos."),
    ("1. Discovery e Insights", "triangulación", "T4. Técnica (análisis)",
     "Triangulación de métodos y fuentes", "Mantener — resolver duplicado",
     "Aparece también en la Dimensión 4. Recomendación: vive en D1 como técnica de análisis; "
     "en D4 solo como criterio de robustez (T7)."),
    ("1. Discovery e Insights", "síntesis", "T4. Técnica (análisis)",
     "Síntesis y construcción de patrones", "Mantener", ""),
    ("1. Discovery e Insights", "generación de insights", "T6. Artefacto / output",
     "Insight (output de la dimensión)", "Reubicar",
     "Es el resultado del proceso, no una capacidad paralela a «desk research». "
     "Conecta directo con «Evidencias sugeridas»."),
    ("1. Discovery e Insights", "calidad de evidencia", "T7. Calidad y ética",
     "Calidad y suficiencia de la evidencia; gestión de sesgos; límites de validez", "Reubicar",
     "Criterio, no capacidad metodológica. Debe repetirse en las 5 dimensiones."),
    ("1. Discovery e Insights", "— ausente —", "T3 / T4 — campo físico",
     "Etnografía y observación en campo; intercept; mystery shopping; shadowing", "Añadir (gap)",
     "GAP CRÍTICO: la visión declara tres campos, pero no hay una sola metodología ni técnica de "
     "contexto físico o híbrido en toda la columna."),

    # ---- D2
    ("2. Estrategia y Problem Solving", "síntesis estratégica", "T4. Técnica (análisis)",
     "Síntesis estratégica", "Mantener",
     "Distinguir de la «síntesis» de D1: allí produce insights, aquí produce direcciones estratégicas."),
    ("2. Estrategia y Problem Solving", "problem reframing", "T1. Objetivo",
     "Problem reframing", "Mantener", ""),
    ("2. Estrategia y Problem Solving", "frameworks de Research, Design y Behavioral Science",
     "T5. Marco conceptual",
     "Frameworks de Research, Design y Behavioral Science", "Mantener — precisar",
     "Conviene nombrar los frameworks conductuales de referencia (COM-B, EAST, MINDSPACE) "
     "para que el ítem sea evaluable."),
    ("2. Estrategia y Problem Solving", "system thinking", "T5. Marco conceptual",
     "Systems thinking", "Mantener — unificar nomenclatura",
     "Aparece también en D3 como «journey & systems thinking». Unificar."),
    ("2. Estrategia y Problem Solving", "business acumen", "T9. Competencia transversal",
     "Business acumen", "Reubicar", ""),
    ("2. Estrategia y Problem Solving", "opportunity framing", "T1. Objetivo",
     "Opportunity framing", "Mantener", ""),
    ("2. Estrategia y Problem Solving", "formulación y priorización de hipótesis", "T1 + T6",
     "Formulación de hipótesis (proceso) / Hipótesis priorizada (artefacto)", "Desagregar",
     "Mezcla la acción y su entregable. Separarlos aclara qué se evalúa."),
    ("2. Estrategia y Problem Solving", "evaluación de valor y viabilidad", "T7. Criterio",
     "Criterios de valor, viabilidad, riesgo y esfuerzo", "Reubicar",
     "Es el criterio con el que se prioriza, no una capacidad independiente."),
    ("2. Estrategia y Problem Solving", "pensamiento crítico", "T9. Competencia transversal",
     "Pensamiento crítico", "Reubicar", ""),
    ("2. Estrategia y Problem Solving", "ética", "T7. Calidad y ética",
     "Ética de la investigación y de la intervención", "Reubicar — declarar transversal",
     "Hoy solo figura en D2. Con el diseño conductual como única especialidad, la ética de la influencia "
     "es un criterio obligatorio también en D3 y D4."),
    ("2. Estrategia y Problem Solving", "storytelling estratégico", "T9. Competencia transversal",
     "Storytelling estratégico", "Reubicar", ""),
    ("2. Estrategia y Problem Solving", "— ausente —", "T0. Meta-capacidad",
     "Juicio estratégico: qué problema merece resolverse y con cuánta evidencia basta para decidirlo",
     "Añadir (gap)",
     "La dimensión enumera técnicas de encuadre pero no la capacidad de elegir entre ellas. "
     "Sin meta-capacidad, la progresión Specialist→Expert se lee como «conoce más frameworks»."),

    # ---- D3
    ("3. Diseño y Orquestación de Experiencias", "diseño de intervenciones conductuales",
     "T1. Objetivo + E3. Especialidad",
     "Diseño conductual: intervenir sobre una conducta objetivo", "Mantener — elevar",
     "Es el núcleo de la única especialidad de diseño de la matriz. Debe encabezar la dimensión, "
     "no aparecer como un ítem más de una enumeración."),
    ("3. Diseño y Orquestación de Experiencias", "arquitectura de decisiones", "T5. Marco conceptual",
     "Arquitectura de decisiones", "Mantener", ""),
    ("3. Diseño y Orquestación de Experiencias", "traducción de insights a diseño", "T4. Técnica (proceso)",
     "Traducción de insights y evidencia a criterios de diseño", "Mantener", ""),
    ("3. Diseño y Orquestación de Experiencias", "principios y criterios de diseño", "T6. Artefacto / output",
     "Principios y criterios de diseño", "Reubicar", ""),
    ("3. Diseño y Orquestación de Experiencias", "ideación y conceptualización", "T4. Técnica",
     "Ideación y conceptualización", "Mantener", ""),
    ("3. Diseño y Orquestación de Experiencias", "acompañamiento a PD/SD", "X. Modelo de colaboración",
     "Acompañamiento a Product / Service Design", "Sacar de la columna",
     "No es una capacidad técnica sino un modelo de trabajo. Además es lo único que introduce otras "
     "especialidades de diseño en una matriz que decidió evaluar solo diseño conductual. "
     "Va en la definición del rol."),
    ("3. Diseño y Orquestación de Experiencias", "prototipado conceptual", "T4. Técnica",
     "Prototipado conceptual", "Mantener", ""),
    ("3. Diseño y Orquestación de Experiencias", "journey & systems thinking", "T5. Marco conceptual",
     "Journey thinking / Systems thinking", "Desagregar y unificar",
     "Son dos lentes distintos, y «systems thinking» ya está en D2. Definir un único hogar."),
    ("3. Diseño y Orquestación de Experiencias", "orquestación de experiencias", "T1. Objetivo / alcance",
     "Orquestación de la experiencia a través de touchpoints y canales", "Reubicar",
     "Es el alcance del objetivo (una intervención frente a un sistema de intervenciones), "
     "y es donde entra de forma natural el campo Híbrido."),
    ("3. Diseño y Orquestación de Experiencias",
     "personalización, comunicación y contenido conductual", "T5b. Palanca de intervención",
     "Palancas conductuales: fricción, defaults, timing y saliencia, framing y comunicación, "
     "incentivos, normas sociales, personalización", "Desagregar y completar",
     "Hoy se nombran tres palancas sueltas mezcladas con marcos. Conviene una taxonomía explícita "
     "de palancas: es lo que hace evaluable el diseño conductual."),
    ("3. Diseño y Orquestación de Experiencias", "— ausente —", "T0. Meta-capacidad",
     "Criterio de intervención: cuánta intervención pide la conducta, qué palanca es proporcional "
     "y cuándo lo correcto es no intervenir", "Añadir (gap)",
     "Es la meta-capacidad más importante de un rol que diseña conducta. Sin ella, la matriz premia "
     "intervenir y no tiene forma de reconocer la decisión de no hacerlo."),

    # ---- D4
    ("4. Experimentación, Medición e Impacto", "Formulación y validación de hipótesis", "T1 + T4",
     "Formulación operacional de hipótesis y variables", "Desagregar",
     "«Formular» es técnica; «validar» es el objetivo de toda la dimensión."),
    ("4. Experimentación, Medición e Impacto", "UX Validatio [sic]", "T1. Objetivo (evaluativo)",
     "UX validation: validar concepto, prototipo o experiencia en campo digital", "Corregir y reubicar",
     "Erratum en el archivo original («UX Validatio»). Además es un objetivo, no una técnica: "
     "las técnicas que lo sirven son usability y prototype testing."),
    ("4. Experimentación, Medición e Impacto", "concept & prototype testing", "T4. Técnica",
     "Concept & prototype testing", "Mantener", ""),
    ("4. Experimentación, Medición e Impacto", "experimentación conductual", "T3. Metodología",
     "Experimentación conductual", "Mantener", ""),
    ("4. Experimentación, Medición e Impacto", "diseño experimental", "T3. Metodología",
     "Diseño experimental", "Mantener", ""),
    ("4. Experimentación, Medición e Impacto", "métricas y criterios de éxito", "T6. Artefacto / output",
     "Métricas y criterios de éxito", "Reubicar", ""),
    ("4. Experimentación, Medición e Impacto", "A/B testing", "T4. Técnica",
     "A/B testing y multivariante", "Reubicar",
     "Es una técnica DENTRO del diseño experimental. Hoy está al mismo nivel que «diseño experimental» "
     "y que «RCT», lo que impide graduar la progresión de niveles."),
    ("4. Experimentación, Medición e Impacto", "RCT y cuasi-experimentos", "T3. Metodología",
     "RCT · Cuasi-experimentos · Pre-post con grupo de control", "Mantener — desagregar",
     "RCT y cuasi-experimento tienen exigencias de validez muy distintas: separarlos permite "
     "diferenciar Specialist de Expert."),
    ("4. Experimentación, Medición e Impacto", "métodos cuantitativos", "T2. Enfoque",
     "Enfoque cuantitativo", "Reubicar",
     "Es un enfoque, y ya está declarado en D1. Aquí genera redundancia entre dimensiones."),
    ("4. Experimentación, Medición e Impacto", "analytics", "T4. Técnica / fuente de datos",
     "Analytics e instrumentación de producto", "Mantener", ""),
    ("4. Experimentación, Medición e Impacto", "control de variables", "T7. Calidad",
     "Control de variables; validez interna", "Reubicar",
     "Es un criterio de validez, no una técnica autónoma."),
    ("4. Experimentación, Medición e Impacto", "inferencia causal", "T5. Marco conceptual",
     "Inferencia causal", "Reubicar",
     "Es la lógica que justifica el diseño, no un método aplicable por sí solo."),
    ("4. Experimentación, Medición e Impacto", "triangulación", "T7. Calidad (aquí) / T4 (en D1)",
     "Triangulación como criterio de robustez de resultados", "Resolver duplicado",
     "Segunda aparición. Definir un único hogar y, si se repite, que sea con función distinta y explícita."),
    ("4. Experimentación, Medición e Impacto", "evaluación de impacto", "T1. Objetivo",
     "Evaluación de impacto", "Reubicar",
     "Objetivo de máxima exigencia causal. Debe encabezar la dimensión junto a «validación»."),
    ("4. Experimentación, Medición e Impacto", "continuous learning", "Y. Resultado organizacional",
     "Evidencia acumulativa y aprendizaje continuo", "Sacar de la columna",
     "Es un estado deseado de la organización, no una capacidad individual evaluable. "
     "Su hogar natural es la Dimensión 5."),
    ("4. Experimentación, Medición e Impacto", "— ausente —", "T7. Ética",
     "Ética experimental: consentimiento, grupos de control, reversibilidad de la intervención",
     "Añadir (gap)",
     "GAP: experimentar con la conducta real de clientes sin criterio ético explícito es el mayor "
     "riesgo reputacional de la unificación de roles."),
    ("4. Experimentación, Medición e Impacto", "— ausente —", "T3. Metodología — campo físico",
     "Piloto en campo; cuasi-experimento por sede o territorio", "Añadir (gap)",
     "GAP: toda la dimensión está escrita desde el campo digital."),
    ("4. Experimentación, Medición e Impacto", "— ausente —", "T0. Meta-capacidad",
     "Criterio de evidencia: cuánto rigor exige cada decisión y cuánto sería desperdiciarlo",
     "Añadir (gap)",
     "Sin esta meta-capacidad, «más rigor» se lee siempre como «mejor», y la matriz no puede "
     "reconocer el juicio de proporcionalidad, que es justo lo que distingue a un Expert."),

    # ---- D5
    ("5. Escalamiento y Liderazgo", "ResearchOps", "T8. Práctica operativa",
     "ResearchOps", "Mantener", ""),
    ("5. Escalamiento y Liderazgo", "BehavioralOps", "T8. Práctica operativa",
     "BehavioralOps", "Mantener — definir",
     "Es el término menos estandarizado de la matriz. Conviene definirlo explícitamente (catálogo de "
     "intervenciones, reutilización, medición acumulada) para que sea evaluable."),
    ("5. Escalamiento y Liderazgo", "KnowledgeOps", "T8. Práctica operativa",
     "KnowledgeOps", "Mantener", ""),
    ("5. Escalamiento y Liderazgo", "gestión y activación del conocimiento", "T8. Práctica operativa",
     "Gestión y activación del conocimiento", "Mantener — posible absorción",
     "Se solapa con KnowledgeOps: decidir si es su contenido o una práctica distinta."),
    ("5. Escalamiento y Liderazgo", "estándares y gobernanza", "T7 + T8",
     "Estándares metodológicos; gobernanza de datos y privacidad", "Desagregar",
     "Estándar (calidad) y gobernanza (decisión y control) son cosas distintas."),
    ("5. Escalamiento y Liderazgo", "stakeholder management", "T9. Competencia transversal",
     "Stakeholder management", "Reubicar", ""),
    ("5. Escalamiento y Liderazgo", "influencia", "T9. Competencia transversal",
     "Influencia", "Reubicar", ""),
    ("5. Escalamiento y Liderazgo", "facilitación", "T9. Competencia transversal",
     "Facilitación", "Reubicar", ""),
    ("5. Escalamiento y Liderazgo", "mentoring", "T9. Competencia transversal",
     "Mentoring", "Reubicar", ""),
    ("5. Escalamiento y Liderazgo", "capability building", "T8. Práctica operativa",
     "Capability building", "Mantener",
     "Distinguir de «mentoring»: mentoring es uno a uno, capability building es sistémico."),
    ("5. Escalamiento y Liderazgo", "gestión de calidad", "T7. Calidad",
     "Gestión de calidad", "Reubicar", ""),
    ("5. Escalamiento y Liderazgo", "priorización", "T9. Competencia transversal",
     "Priorización de portafolio de estudios e intervenciones", "Reubicar — precisar",
     "«Priorización» a secas ya aparece implícita en D2. Aquí debe significar priorización de portafolio."),
    ("5. Escalamiento y Liderazgo", "comunicación estratégica", "T9. Competencia transversal",
     "Comunicación estratégica", "Reubicar",
     "Se solapa con «storytelling estratégico» de D2: definir un único hogar."),
    ("5. Escalamiento y Liderazgo", "cultura de evidencia", "Y. Resultado organizacional",
     "Cultura de decisión basada en evidencia", "Sacar de la columna",
     "Es el propósito de la dimensión, no una capacidad. Ya está dicho en «Definición para el rol»."),
    ("5. Escalamiento y Liderazgo", "mejora continua", "T8. Práctica operativa",
     "Mejora continua", "Mantener", ""),
    ("5. Escalamiento y Liderazgo", "— ausente —", "T0. Meta-capacidad",
     "Criterio de escalamiento y liderazgo: qué se estandariza, qué se deja variar y a qué ritmo se "
     "le puede exigir a un equipo", "Añadir (gap)",
     "La dimensión enumera prácticas de Ops y competencias, pero no la capacidad de decidir entre "
     "ellas ni de calibrar la exigencia sobre el equipo."),
    ("5. Escalamiento y Liderazgo", "— ausente —", "T7b. Ética del liderazgo — EQUILIBRIO",
     "Productividad del equipo ↔ satisfacción del equipo con la persona que lidera, leídas en el "
     "mismo periodo", "Añadir (gap)",
     "La dimensión mide lo que el liderazgo PRODUCE (estándares, gobernanza, capacidades) pero no "
     "cómo trata a quienes lo hacen posible. Sin el contrapeso de la satisfacción, «capability "
     "building» y «mejora continua» premian a quien exprime al equipo."),
    ("5. Escalamiento y Liderazgo", "— ausente —", "T7b. Ética del liderazgo — UMBRAL",
     "Respeto básico: sin acoso, sin mansplaining, sin conductas excluyentes. Se verifica; no se "
     "pondera", "Añadir (gap)",
     "No es una variable del equilibrio: es un piso. Si entrara en la ponderación 30/20/15/20/15, "
     "la matriz estaría diciendo que un buen resultado puede compensarlo. Su incumplimiento "
     "verificado bloquea el nivel."),
]

# ------------------------------------- 4. columna C reescrita por niveles ---

COLUMNA_C_NUEVA = {
    "1. Discovery e Insights":
        "T0 META-CAPACIDAD · Estrategia de investigación: componer objetivo, enfoque, metodología y "
        "técnicas de forma coherente con la decisión que se necesita tomar. ¿Es esta la investigación "
        "que la decisión necesita, o solo la que sabemos hacer?\n\n"
        "T1 OBJETIVO · Problem framing (de decisión de negocio a pregunta de investigación y conducta "
        "objetivo); exploración de necesidades, experiencias y contexto; diagnóstico conductual; "
        "diagnóstico sistémico.\n\n"
        "T2 ENFOQUE · Cualitativo, cuantitativo y mixto; evidencia primaria y secundaria.\n\n"
        "T3 METODOLOGÍA · Desk research (evidencia secundaria); investigación en campo / etnográfica; "
        "estudios longitudinales y de seguimiento.\n\n"
        "T4 TÉCNICA · Recolección: entrevistas, observación estructurada, diarios, encuestas, intercept y "
        "mystery shopping (campo físico), analítica de comportamiento. "
        "Análisis: diseño muestral, codificación, triangulación de métodos y fuentes, síntesis.\n\n"
        "T5 MARCO · Frameworks de ciencias del comportamiento para leer conducta (COM-B, EAST); "
        "systems thinking.\n\n"
        "T6 ARTEFACTO · Insight; plan y estrategia de investigación.\n\n"
        "T7 CALIDAD Y ÉTICA · Calidad y suficiencia de la evidencia; gestión de sesgos; límites de validez; "
        "consentimiento y privacidad.\n\n"
        "T9 COMPETENCIA · Pensamiento crítico.",

    "2. Estrategia y Problem Solving":
        "T0 META-CAPACIDAD · Juicio estratégico: decidir qué problema merece resolverse y con cuánta "
        "evidencia basta para decidirlo, haciendo explícito el riesgo de equivocarse.\n\n"
        "T1 OBJETIVO · Problem reframing; opportunity framing; formulación y priorización de hipótesis "
        "estratégicas.\n\n"
        "T5 MARCO · Frameworks de Research, Design y Behavioral Science (COM-B, EAST, MINDSPACE); "
        "systems thinking; teoría del cambio.\n\n"
        "T4 TÉCNICA (análisis y decisión) · Síntesis estratégica; evaluación de valor, viabilidad, riesgo y "
        "esfuerzo; matrices de priorización; exploración de escenarios y trade-offs.\n\n"
        "T6 ARTEFACTO · Problema reencuadrado; mapa de oportunidades; hipótesis priorizadas; "
        "narrativa estratégica.\n\n"
        "T7 CALIDAD Y ÉTICA · Supuestos explícitos; estándar de evidencia exigible según el tipo de "
        "decisión; ética de la intervención.\n\n"
        "T9 COMPETENCIA · Pensamiento crítico; business acumen; storytelling estratégico.",

    "3. Diseño y Orquestación de Experiencias":
        "E3 ESPECIALIDAD · Diseño conductual (única especialidad de diseño evaluada por esta matriz).\n\n"
        "T0 META-CAPACIDAD · Criterio de intervención: decidir cuánta intervención pide una conducta, "
        "elegir la palanca proporcional al problema y al riesgo ético, y reconocer cuándo lo correcto "
        "es no intervenir.\n\n"
        "T1 OBJETIVO · Traducir evidencia y estrategia en principios, conceptos e intervenciones; "
        "intervenir sobre una conducta objetivo; orquestar la experiencia a través de touchpoints y canales.\n\n"
        "T5 MARCO · Arquitectura de decisiones; journey thinking; systems thinking.\n\n"
        "T5b PALANCAS DE INTERVENCIÓN · Fricción y esfuerzo; defaults; timing y saliencia; framing y "
        "comunicación conductual; incentivos; normas sociales; personalización.\n\n"
        "T4 TÉCNICA · Ideación y conceptualización; traducción de insights a criterios de diseño; "
        "prototipado conceptual; behavioral walkthrough; diseño de contenido conductual.\n\n"
        "T6 ARTEFACTO · Principios y criterios de diseño; concepto de intervención; blueprint de orquestación.\n\n"
        "T7 CALIDAD Y ÉTICA · Ética de la influencia (transparencia, autonomía de la persona, no explotación "
        "de sesgos); testeabilidad de la intervención.\n\n"
        "X MODELO DE COLABORACIÓN (no es capacidad; describe alcance) · Acompañamiento a Product y Service "
        "Design en la conceptualización y orquestación de la experiencia.",

    "4. Experimentación, Medición e Impacto":
        "T0 META-CAPACIDAD · Criterio de evidencia: decidir cuánto rigor exige cada decisión y cuánto "
        "sería desperdiciarlo, ajustando el diseño al costo, al riesgo y a la reversibilidad.\n\n"
        "T1 OBJETIVO · UX validation (concepto, prototipo, experiencia); evaluación del efecto de "
        "intervenciones conductuales; evaluación de impacto; decisión de iterar, escalar o detener.\n\n"
        "T2 ENFOQUE · Observacional frente a experimental; cuantitativo, cualitativo de validación y mixto.\n\n"
        "T3 METODOLOGÍA · Diseño experimental; RCT; cuasi-experimentos; pre-post con grupo de control; "
        "pruebas de concepto y prototipo; piloto en campo (físico) y en producto (digital).\n\n"
        "T4 TÉCNICA · Formulación operacional de hipótesis y variables; A/B testing y multivariante; "
        "concept & prototype testing; usability testing; analytics e instrumentación; análisis estadístico.\n\n"
        "T5 MARCO · Inferencia causal; teoría del cambio; jerarquía de evidencia.\n\n"
        "T6 ARTEFACTO · Hipótesis operacionalizada; métricas y criterios de éxito; lectura de resultados y "
        "recomendación de decisión.\n\n"
        "T7 CALIDAD Y ÉTICA · Validez interna y externa; control de variables; potencia y tamaño muestral; "
        "triangulación como criterio de robustez; ética experimental (consentimiento, grupos de control, "
        "reversibilidad).",

    "5. Escalamiento y Liderazgo":
        "T0 META-CAPACIDAD · Criterio de escalamiento y liderazgo: decidir qué se estandariza, qué se "
        "deja variar y a qué ritmo se le puede exigir a un equipo, sosteniendo el equilibrio entre lo "
        "que el equipo produce y lo que el equipo puede sostener.\n\n"
        "T1 OBJETIVO · Escalar conocimiento, prácticas y capacidades; sostener la decisión basada en "
        "evidencia.\n\n"
        "T8 PRÁCTICA OPERATIVA · ResearchOps; BehavioralOps; KnowledgeOps; gestión y activación del "
        "conocimiento; repositorios y trazabilidad; automatización; capability building; mejora continua.\n\n"
        "T7 GOBERNANZA, CALIDAD Y ÉTICA · Estándares metodológicos; gobernanza de datos y privacidad; "
        "gestión de calidad; ética aplicada.\n\n"
        "T7b ÉTICA DEL LIDERAZGO · Se mide en dos partes que no se mezclan. "
        "EQUILIBRIO (se pondera): productividad del equipo ↔ satisfacción del equipo con la persona "
        "que lidera, leídas en el mismo periodo y nunca por separado. "
        "UMBRAL (se verifica, no se pondera): respeto básico — sin acoso, sin mansplaining, sin "
        "conductas excluyentes. El umbral no entra en la ponderación: su incumplimiento verificado "
        "bloquea el nivel. Ver hoja «4. Ética del liderazgo».\n\n"
        "T6 ARTEFACTO · Estándares y playbooks; repositorio de evidencia; catálogo de intervenciones "
        "reutilizables; modelo de capacidades del Council.\n\n"
        "T9 COMPETENCIA · Stakeholder management; influencia; comunicación estratégica; facilitación; "
        "mentoring; priorización de portafolio.",
}

# ------------------------------------------- 6. hallazgos y decisiones ------

HALLAZGOS = [
    ("H1", "Mezcla de niveles de abstracción", "Transversal — las 5 dimensiones",
     "Cada celda enumera en un mismo plano objetivos, enfoques, metodologías, técnicas, artefactos, "
     "criterios y competencias. Ejemplo literal en D1: «desk research» (metodología), «muestreo» (técnica), "
     "«diagnóstico conductual» (objetivo) y «calidad de evidencia» (criterio), separados solo por comas.",
     "Impide comparar personas: dos evaluadores leen la misma lista con jerarquías distintas.",
     "Ordenar cada celda por los niveles T1→T9 (ver hoja «6. Columna C propuesta»)."),
    ("H2", "«UX Research» y «Behavioral Research» aparecen como capacidades", "D1",
     "Están listados entre metodologías, cuando en la nueva visión son el CAMPO y la LENTE.",
     "Reproduce dentro de la matriz la separación de roles que la unificación busca eliminar.",
     "Sacarlos de la columna y convertirlos en ejes transversales (E1 campo; lente conductual)."),
    ("H3", "Ausencia total del campo físico e híbrido", "D1 y D4 sobre todo",
     "No hay una sola metodología ni técnica de contexto presencial: ni etnografía en sucursal, ni "
     "observación estructurada, ni intercept, ni mystery shopping, ni piloto en campo.",
     "La visión declara tres campos pero la matriz solo permite evidenciar uno. Un perfil fuerte en "
     "campo físico no podría demostrar nivel.",
     "Añadir metodologías y técnicas de campo físico e híbrido en T3 y T4 de D1 y D4."),
    ("H4", "Duplicados entre dimensiones", "D1 y D4; D2 y D3; D2 y D5",
     "«Triangulación» (D1 y D4), «systems thinking» (D2 y D3), «storytelling estratégico» frente a "
     "«comunicación estratégica» (D2 y D5), «métodos cuantitativos» frente al enfoque ya declarado en D1.",
     "Con pesos por dimensión (30/20/15/20/15), un duplicado puntúa dos veces.",
     "Un hogar único por ítem. Si se repite, debe repetirse con FUNCIÓN distinta y explícita "
     "(p. ej. triangulación = técnica en D1, criterio de robustez en D4)."),
    ("H5", "Objetivos escritos como si fueran métodos", "D1, D3, D4",
     "«diagnóstico conductual y sistémico», «evaluación de impacto», «UX Validation» y «diseño de "
     "intervenciones conductuales» son objetivos o propósitos, no procedimientos.",
     "Confunde el «para qué» con el «cómo», que es justo lo que la progresión de niveles necesita separar.",
     "Elevarlos a T1 y encabezar con ellos cada dimensión."),
    ("H6", "Metodología y técnica al mismo nivel", "D4",
     "«diseño experimental» y «RCT y cuasi-experimentos» (metodologías) conviven en la misma línea con "
     "«A/B testing» y «analytics» (técnicas).",
     "Un Professional que corre A/B tests podría leerse al mismo nivel que un Expert que diseña un "
     "cuasi-experimento con inferencia causal.",
     "Separar T3 y T4, y anclar la progresión 1→4 al nivel metodológico, no al número de técnicas."),
    ("H7", "Contenido que no es capacidad", "D3, D4, D5",
     "«acompañamiento a PD/SD» es un modelo de colaboración; «continuous learning» y «cultura de "
     "evidencia» son resultados organizacionales.",
     "Infla las dimensiones y hace que se evalúe algo que no depende solo de la persona. Además "
     "«acompañamiento a PD/SD» es lo único que introduce otras especialidades de diseño en una matriz "
     "que decidió evaluar solo diseño conductual.",
     "Sacarlos de la columna: el primero a la definición del rol y a los niveles; los otros dos al "
     "propósito de la Dimensión 5."),
    ("H8", "La ética aparece en una sola dimensión", "D2 (y ausente en D3 y D4)",
     "«ética» figura suelta en D2 y «gobernanza» en D5, pero no hay criterio ético en el diseño de "
     "intervenciones (D3) ni en la experimentación con clientes reales (D4).",
     "Es el punto de mayor riesgo de un rol que diseña intervenciones conductuales y experimenta con "
     "conducta real.",
     "Declarar T7 (calidad y ética) como bloque obligatorio en las cinco dimensiones."),
    ("H9", "Términos sin definición operativa", "D5",
     "«BehavioralOps» no tiene definición estándar en la industria; «gestión y activación del "
     "conocimiento» se solapa con KnowledgeOps; «priorización» es ambiguo.",
     "No son evaluables de forma consistente entre evaluadores.",
     "Definir cada uno en una línea dentro del diccionario de taxonomías."),
    ("H10", "Erratum", "D4",
     "«UX Validatio» (falta la «n») en el archivo original.", "Menor.",
     "Corregido en la propuesta."),
    ("H11", "La meta-capacidad existía en una sola dimensión", "D1 la tenía; D2, D3, D4 y D5 no",
     "«Research Strategy» es lo único parecido a una meta-capacidad en toda la matriz, y aun así "
     "está escrito como un ítem más de la enumeración, al lado de «muestreo».",
     "Sin meta-capacidad, la progresión Professional→Master se lee como acumulación: «conoce más "
     "frameworks», «sabe más técnicas», «usa más rigor». Lo que separa a un Expert no es ejecutar "
     "más, es elegir mejor — y eso no estaba en ninguna parte.",
     "Declarar una meta-capacidad por dimensión (T0), por encima de T1, y anclar en ella la "
     "progresión Specialist→Expert. Ver hoja «3. Meta-capacidades»."),
    ("H12", "El liderazgo se mide por lo que produce, no por cómo trata al equipo",
     "D5 y niveles 3–4 de todas las dimensiones",
     "D5 evalúa estándares, gobernanza, capability building y mejora continua. No hay un solo "
     "indicador sobre la experiencia de las personas lideradas.",
     "Tal como está, «capability building» y «mejora continua» premian a quien exprime al equipo "
     "igual que a quien lo desarrolla: el resultado se ve, el costo humano no. Y en una matriz de "
     "un rol que diseña conducta ajena, no medir la propia conducta hacia el equipo es una "
     "contradicción difícil de sostener.",
     "Añadir T7b en dos partes: EQUILIBRIO productividad ↔ satisfacción del equipo (se pondera) "
     "sobre un UMBRAL de respeto básico (se verifica, bloquea el nivel). Ver hoja «4. Ética del "
     "liderazgo»."),
]

PREGUNTAS = [
    ("P1", "¿Se abre un cuarto campo «Sistémico / contextual»?",
     "Es el único candidato con criterio propio: cubre lo que no ocurre en un canal (mercado, regulación, "
     "ecosistema, evidencia publicada). Sin él, «desk research» y el «diagnóstico sistémico» que ya están "
     "en la matriz quedan sin campo asignable. «Organizacional» y «conversacional» NO deberían abrirse: "
     "el primero es un sujeto, el segundo cae dentro de híbrido.",
     "Recomendación: abrirlo, y mantener el sujeto (cliente / colaborador / asesor) como eje separado."),
    ("P2", "¿La progresión 1→4 se ancla en metodología o en técnica?",
     "Hoy la columna mezcla ambas, así que la progresión se puede leer como «sabe más técnicas». "
     "Un modelo más defendible: el nivel sube con la exigencia metodológica y con la ambigüedad del "
     "problema, no con el número de herramientas.",
     "Recomendación: anclar en T1 (complejidad del objetivo) y T3 (exigencia metodológica)."),
    ("P3", "¿«Estrategia de investigación» es un ítem o una meta-capacidad?",
     "Es la capacidad de componer objetivo + enfoque + metodología + técnica. Listarla junto a «muestreo» "
     "la iguala a un instrumento.",
     "Recomendación: declararla meta-capacidad de D1 y hacerla el eje de la progresión Specialist→Expert."),
    ("P4", "¿Las competencias transversales (T9) viven dentro de las dimensiones o en un eje propio?",
     "Hoy están repartidas: pensamiento crítico y business acumen en D2; influencia y facilitación en D5. "
     "Con pesos por dimensión, su valor depende de dónde caigan.",
     "Recomendación: mantenerlas dentro de cada dimensión pero marcadas como T9, para que se vea que no "
     "compiten con la capacidad metodológica."),
    ("P5", "¿El campo (E1) se evalúa o solo se declara?",
     "Si el campo es solo una etiqueta, la matriz sigue siendo digital-first. Si se evalúa, hay que "
     "decidir si un Expert debe demostrar solvencia en más de un campo.",
     "Recomendación: exigir un campo a Specialist, dos a Expert, y visión híbrida a Master."),
    ("P6", "¿Quién administra la medición de la ética del liderazgo, y quién ve el resultado?",
     "Es la decisión que hace que el sistema funcione o se vuelva decorativo. El acceso al resultado "
     "desagregado, el n mínimo para publicar y el momento de entrega tienen que quedar definidos "
     "ANTES de la primera medición: si se deciden después de conocer los resultados, el instrumento "
     "pierde credibilidad ante el equipo y nadie vuelve a responder con honestidad.",
     "Recomendación: Personas administra el instrumento y custodia el anonimato; el Council define "
     "los indicadores; el resultado agregado se comparte con el equipo que respondió. El n mínimo "
     "(≥5) y la regla de bloqueo se publican de antemano."),
]

BLOQUES_LEEME = [
    ("Alcance del ejercicio",
     "Se trabaja ÚNICAMENTE la columna «Capacidades incluidas». Las columnas Dimensión, Peso, "
     "«Definición para el rol», los cuatro niveles (Professional a Master), «Evidencias sugeridas» "
     "e «IA integrada» se conservan sin modificar respecto del archivo original."),
    ("Qué significa «ordenar por niveles y taxonomía»",
     "Son dos operaciones distintas:\n"
     "  (a) TAXONOMÍA — a qué clase pertenece cada ítem: un objetivo no es una metodología, una "
     "metodología no es una técnica, y un criterio de calidad no es ninguna de las tres.\n"
     "  (b) NIVEL — qué va antes que qué. La lectura correcta es de arriba abajo: primero el objetivo "
     "(para qué), después el enfoque (con qué lógica), después la metodología (cómo se estructura el "
     "estudio) y por último la técnica (con qué instrumento). Los marcos, artefactos, criterios de "
     "calidad y competencias son transversales y cierran cada bloque."),
    ("Ejemplos tomados del propio archivo",
     "«desk research» = metodología (define el origen de la evidencia).\n"
     "«diagnóstico conductual» = objetivo (define la pregunta, no el procedimiento).\n"
     "«muestreo» = técnica (instrumento al servicio de una metodología).\n"
     "«generación de insights» = artefacto (el resultado, no la capacidad).\n"
     "«calidad de evidencia» = criterio (el estándar bajo el cual lo anterior es válido).\n"
     "Hoy los cinco conviven en la misma celda separados por comas."),
    ("Cómo leer este libro",
     "1. Taxonomías — el diccionario: la meta-capacidad (T0), nueve clases (T1 a T9), tres ejes "
     "transversales (E1 a E3) y dos categorías de control (X, Y) para lo que hoy está en la columna "
     "sin ser una capacidad.\n"
     "2. Ejes transversales — campos de investigación (incluye la respuesta a «¿alguna más?»), sujetos "
     "y especialidad de diseño.\n"
     "3. Meta-capacidades — una por dimensión: qué compone, qué pregunta resuelve, cómo progresa de "
     "Professional a Master y cómo cambia según el campo.\n"
     "4. Ética del liderazgo — el modelo de medición de T7b: el equilibrio que se pondera, el umbral "
     "que se verifica, los indicadores, la aplicación por nivel y las cautelas del instrumento.\n"
     "5. Desglose capacidades — los ítems actuales, uno por fila, con su clase, su nombre normalizado "
     "y la decisión propuesta.\n"
     "6. Columna C propuesta — la columna reescrita y ordenada por niveles, lista para pegar.\n"
     "7. Matriz propuesta — la matriz completa con la columna C nueva y el resto intacto.\n"
     "8. Hallazgos y decisiones — los problemas detectados y las preguntas abiertas para cerrar con "
     "los dos leads."),
    ("Criterio de ordenamiento aplicado a cada celda",
     "T0 Meta-capacidad → T1 Objetivo → T2 Enfoque → T3 Metodología → T4 Técnica → "
     "T5 Marco conceptual → T6 Artefacto → T7 Calidad y ética (T7b Ética del liderazgo donde "
     "corresponde) → T8 Práctica operativa → T9 Competencia transversal."),
    ("Dos incorporaciones sobre la primera versión",
     "(a) META-CAPACIDAD EN TODAS LAS DIMENSIONES. Antes existía solo en D1 y sin nombrarse como tal. "
     "Ahora cada dimensión declara la suya: es lo que distingue elegir bien de ejecutar mucho, y es "
     "donde debe anclarse la progresión Specialist→Expert.\n"
     "(b) ÉTICA DEL LIDERAZGO (T7b). Donde hay liderazgo, la ética se mide como el equilibrio entre "
     "la productividad del equipo y su satisfacción con quien lidera. El respeto básico —sin acoso, "
     "sin mansplaining, sin conductas excluyentes— NO forma parte de ese equilibrio: es un umbral "
     "que se verifica y que bloquea el nivel. Ponerlo en la balanza equivaldría a decir que un buen "
     "resultado puede compensarlo."),
]

SUJETOS = [
    ("Cliente / usuario", "Sujeto por defecto de la matriz actual."),
    ("No cliente y mercado", "Habilita el discovery de mercado y la evidencia sistémica."),
    ("Colaborador", "Hoy se confunde con un «campo organizacional». Es un sujeto: se investiga con las "
                    "mismas metodologías, en cualquiera de los tres campos."),
    ("Asesor / intermediario", "Relevante en seguros: su conducta media la del cliente final."),
]

ESPECIALIDADES = [
    ("Diseño Conductual",
     "ÚNICA especialidad de diseño evaluada por esta matriz. Es el núcleo de la Dimensión 3 y debe "
     "encabezarla."),
    ("Product Design / Service Design",
     "NO se evalúan. Aparecen solo como modelo de colaboración (categoría X). Hoy están dentro de "
     "«Capacidades incluidas» como «acompañamiento a PD/SD», lo que contradice la decisión de alcance."),
]

CAMPOS_POR_DIMENSION = {
    "1. Discovery e Insights": "Digital · Físico · Híbrido · Sistémico",
    "2. Estrategia y Problem Solving": "Transversal a todos los campos",
    "3. Diseño y Orquestación de Experiencias": "Digital · Físico · Híbrido",
    "4. Experimentación, Medición e Impacto": "Digital · Físico · Híbrido",
    "5. Escalamiento y Liderazgo": "Transversal a todos los campos",
}

COLORES_DECISION = [
    ("Mantener", VERDE),
    ("Reubicar", AMBAR),
    ("Renombrar", AMBAR),
    ("Desagregar", AMBAR),
    ("Corregir y reubicar", AMBAR),
    ("Eliminar", NARANJA),
    ("Sacar de la columna", NARANJA),
    ("Mover a eje transversal", NARANJA),
    ("Resolver duplicado", NARANJA),
    ("Añadir (gap)", CELESTE),
]


def subtitulo_bloque(ws, fila, texto, ncols):
    c = ws.cell(row=fila, column=1, value=texto)
    c.font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
    c.fill = FILL_TITULO
    c.alignment = Alignment(vertical="center")
    ws.merge_cells(start_row=fila, start_column=1, end_row=fila, end_column=ncols)
    ws.row_dimensions[fila].height = 22


def par_etiqueta_nota(ws, fila, etiqueta, nota, ncols):
    c = ws.cell(row=fila, column=1, value=etiqueta)
    c.font = NEGRITA
    c.alignment = TOP_WRAP
    c.border = BORDE
    c = ws.cell(row=fila, column=2, value=nota)
    c.font = NORMAL
    c.alignment = TOP_WRAP
    c.border = BORDE
    ws.merge_cells(start_row=fila, start_column=2, end_row=fila, end_column=ncols)
    for j in range(3, ncols + 1):
        ws.cell(row=fila, column=j).border = BORDE
    ws.row_dimensions[fila].height = 32


def main():
    origen = None
    for arg in sys.argv[1:]:
        if arg.endswith(".xlsx"):
            origen = arg
    if origen is None:
        origen = os.path.join(HERE, "Propuesta_Matriz_expertiz_1.xlsx")

    wb_in = load_workbook(origen, data_only=True)
    ws_in = wb_in[wb_in.sheetnames[0]]
    titulo_rol = ws_in["A1"].value
    proposito = ws_in["A2"].value
    cabeceras = [ws_in.cell(row=4, column=j).value for j in range(1, 11)]
    matriz = [[ws_in.cell(row=i, column=j).value for j in range(1, 11)]
              for i in range(5, 10)]

    wb = Workbook()

    # ---------------------------------------------------------- 0. Léeme ---
    ws = wb.active
    ws.title = "0. Lee me"
    ws.column_dimensions["A"].width = 120
    c = ws.cell(row=1, column=1,
                value="Ejercicio de taxonomías — Matriz de Expertiz Research & Behavioral Design")
    c.font = TITULO
    c.fill = FILL_TITULO
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 30

    fila = 3
    for titulo, cuerpo in BLOQUES_LEEME:
        c = ws.cell(row=fila, column=1, value=titulo)
        c.font = Font(name="Calibri", size=11, bold=True, color=AZUL)
        c.fill = FILL_SUAVE
        c.alignment = TOP_WRAP
        fila += 1
        c = ws.cell(row=fila, column=1, value=cuerpo)
        c.font = NORMAL
        c.alignment = TOP_WRAP
        n_lineas = sum(1 + len(l) // 115 for l in cuerpo.split("\n"))
        ws.row_dimensions[fila].height = 15 * n_lineas + 6
        fila += 2

    # ----------------------------------------------------- 1. Taxonomías ---
    ws = wb.create_sheet("1. Taxonomias")
    fc = encabezar(
        ws, "Diccionario de taxonomías",
        "Nueve clases de capacidad (T1–T9) ordenadas de más abstracta a más concreta, tres ejes que "
        "encuadran la matriz (E1–E3) y dos categorías de control (X, Y) para el contenido que hoy está "
        "en la columna sin ser una capacidad evaluable.", 5)
    ultima = escribir_tabla(
        ws, fc,
        ["Clase", "Pregunta que responde", "Definición", "Ejemplos (tomados de la matriz actual)",
         "Dónde vive en la matriz"],
        [list(x) for x in TAXONOMIAS], [26, 34, 52, 58, 42])
    for i in range(fc + 1, ultima + 1):
        if ws.cell(row=i, column=2).value is None:
            for j in range(1, 6):
                ws.cell(row=i, column=j).fill = FILL_SUAVE
                ws.cell(row=i, column=j).font = NEGRITA
            ws.row_dimensions[i].height = 22

    # ---------------------------------------------- 2. Ejes transversales ---
    ws = wb.create_sheet("2. Ejes transversales")
    fc = encabezar(
        ws, "Eje E1 — Campos de investigación",
        "Criterio de corte propuesto: el ENTORNO en el que ocurre el comportamiento que se estudia o en "
        "el que se interviene. Con ese criterio los campos son mutuamente excluyentes y toda metodología "
        "se puede asignar a uno o más. Incluye la respuesta a «¿alguna más?».", 5)
    ultima = escribir_tabla(
        ws, fc,
        ["Campo", "Recomendación", "Qué cubre", "Metodologías y técnicas típicas", "Nota"],
        [list(x) for x in CAMPOS], [24, 26, 46, 50, 54])
    for i in range(fc + 1, ultima + 1):
        rec = ws.cell(row=i, column=2).value or ""
        if rec.startswith("Recomendado"):
            ws.cell(row=i, column=2).fill = FILL_VERDE
        elif rec.startswith("A decidir"):
            ws.cell(row=i, column=2).fill = FILL_AMBAR
        elif rec.startswith("NO"):
            ws.cell(row=i, column=2).fill = PatternFill("solid", fgColor=NARANJA)

    fila = ultima + 3
    subtitulo_bloque(ws, fila, "Eje E2 — Sujeto de estudio (recomendado como eje separado)", 5)
    fila += 1
    for sujeto, nota in SUJETOS:
        par_etiqueta_nota(ws, fila, sujeto, nota, 5)
        fila += 1

    fila += 2
    subtitulo_bloque(ws, fila, "Eje E3 — Especialidad de diseño", 5)
    fila += 1
    for esp, nota in ESPECIALIDADES:
        par_etiqueta_nota(ws, fila, esp, nota, 5)
        fila += 1

    # ------------------------------------------- 3. Meta-capacidades -------
    ws = wb.create_sheet("3. Meta-capacidades")
    fc = encabezar(
        ws, "T0 — Una meta-capacidad por dimensión",
        "La meta-capacidad no es una capacidad más: es la que gobierna cómo se componen las demás. "
        "Responde a «¿sabe elegir, no solo ejecutar?» y es donde debe anclarse la progresión "
        "Specialist→Expert. Antes existía solo en D1, y sin nombrarse como tal.", 7)
    ultima = escribir_tabla(
        ws, fc,
        ["Dimensión", "Meta-capacidad", "Qué compone", "La pregunta que resuelve",
         "Cómo progresa (1 → 4)", "Cómo se evidencia", "Cómo cambia según el campo (E1)"],
        [list(x) for x in META_CAPACIDADES], [26, 26, 30, 40, 62, 46, 46])
    for i in range(fc + 1, ultima + 1):
        ws.row_dimensions[i].height = 118
        ws.cell(row=i, column=2).font = NEGRITA
        ws.cell(row=i, column=2).fill = FILL_VERDE
        ws.cell(row=i, column=4).font = Font(name="Calibri", size=10, italic=True, color=AZUL)

    # ------------------------------------------ 4. Ética del liderazgo -----
    ws = wb.create_sheet("4. Etica del liderazgo")
    fc = encabezar(
        ws, "T7b — Ética del liderazgo",
        "Aplica en la Dimensión 5 y como condición de los niveles 3 y 4 de todas las dimensiones, "
        "que es donde la matriz ya describe liderar, orientar y desarrollar personas. Se mide en dos "
        "partes que NO se mezclan.", 4)
    ultima = escribir_tabla(
        ws, fc,
        ["Parte", "Qué es", "Cómo se trata", "Por qué así"],
        [list(x) for x in ETICA_PARTES], [22, 54, 40, 78])
    for i in range(fc + 1, ultima + 1):
        ws.row_dimensions[i].height = 92
        ws.cell(row=i, column=1).font = NEGRITA
        ws.cell(row=i, column=1).fill = FILL_VERDE if i == fc + 1 else FILL_AMBAR

    fila = ultima + 3
    subtitulo_bloque(ws, fila, "Indicadores sugeridos", 4)
    fila += 1
    for j, nombre in enumerate(["Componente", "Indicador", "Fuente", "Nota"], start=1):
        c = ws.cell(row=fila, column=j, value=nombre)
        c.font = CABECERA
        c.fill = FILL_CABECERA
        c.alignment = TOP_WRAP_CENTER
        c.border = BORDE
    fila += 1
    for comp, ind, fuente, nota in ETICA_INDICADORES:
        for j, valor in enumerate([comp, ind, fuente, nota], start=1):
            c = ws.cell(row=fila, column=j, value=valor)
            c.font = NORMAL
            c.alignment = TOP_WRAP
            c.border = BORDE
        ws.cell(row=fila, column=1).font = NEGRITA
        ws.cell(row=fila, column=1).fill = (
            FILL_AMBAR if comp.startswith("B") else FILL_VERDE)
        ws.row_dimensions[fila].height = 46
        fila += 1

    fila += 2
    subtitulo_bloque(ws, fila, "Cómo se aplica en cada nivel", 4)
    fila += 1
    for j, nombre in enumerate(["Nivel", "Equilibrio (se pondera)", "Umbral (se verifica)", ""],
                               start=1):
        c = ws.cell(row=fila, column=j, value=nombre)
        c.font = CABECERA
        c.fill = FILL_CABECERA
        c.alignment = TOP_WRAP_CENTER
        c.border = BORDE
    fila += 1
    for nivel, equilibrio, umbral in ETICA_NIVELES:
        for j, valor in enumerate([nivel, equilibrio, umbral], start=1):
            c = ws.cell(row=fila, column=j, value=valor)
            c.font = NORMAL
            c.alignment = TOP_WRAP
            c.border = BORDE
        ws.cell(row=fila, column=1).font = NEGRITA
        ws.merge_cells(start_row=fila, start_column=3, end_row=fila, end_column=4)
        ws.cell(row=fila, column=4).border = BORDE
        ws.cell(row=fila, column=3).fill = FILL_AMBAR
        ws.cell(row=fila, column=4).fill = FILL_AMBAR
        ws.row_dimensions[fila].height = 62
        fila += 1

    fila += 2
    subtitulo_bloque(ws, fila, "Cautelas del instrumento — medir esto mal hace más daño que no medirlo", 4)
    fila += 1
    for cautela, detalle in ETICA_CAUTELAS:
        par_etiqueta_nota(ws, fila, cautela, detalle, 4)
        ws.cell(row=fila, column=1).fill = PatternFill("solid", fgColor=NARANJA)
        ws.row_dimensions[fila].height = 46
        fila += 1
    ws.column_dimensions["A"].width = 34

    # ------------------------------------------ 5. Desglose de la columna ---
    ws = wb.create_sheet("5. Desglose capacidades")
    fc = encabezar(
        ws, "Desglose ítem por ítem de «Capacidades incluidas»",
        "Cada ítem de la columna original, tal como está escrito hoy, con la clase taxonómica que le "
        "corresponde, su nombre normalizado y la decisión propuesta. Las filas marcadas «— ausente —» "
        "son gaps detectados, no contenido del archivo original.", 6)
    ultima = escribir_tabla(
        ws, fc,
        ["Dimensión", "Ítem tal como está hoy", "Clase taxonómica", "Ítem normalizado",
         "Decisión", "Por qué"],
        [list(x) for x in DESGLOSE], [30, 34, 28, 46, 24, 64])
    for i in range(fc + 1, ultima + 1):
        dec = (ws.cell(row=i, column=5).value or "").strip()
        for clave, color in COLORES_DECISION:
            if dec.startswith(clave):
                ws.cell(row=i, column=5).fill = PatternFill("solid", fgColor=color)
                break
        ws.cell(row=i, column=3).font = NEGRITA
    ws.auto_filter.ref = "A%d:F%d" % (fc, ultima)

    # ------------------------------------------- 6. Columna C propuesta ----
    ws = wb.create_sheet("6. Columna C propuesta")
    fc = encabezar(
        ws, "Columna «Capacidades incluidas» reescrita y ordenada",
        "Mismo contenido, ordenado por niveles. Orden aplicado: META-CAPACIDAD → T1 Objetivo → "
        "T2 Enfoque → T3 Metodología → T4 Técnica → T5 Marco → T6 Artefacto → T7 Calidad y ética → "
        "T8 Ops → T9 Competencia. Lista para pegar en la matriz.", 4)
    filas = []
    for fila_m in matriz:
        filas.append([fila_m[0], fila_m[1], fila_m[2], COLUMNA_C_NUEVA.get(fila_m[0], "")])
    ultima = escribir_tabla(
        ws, fc,
        ["Dimensión", "Peso", "Capacidades incluidas — ORIGINAL",
         "Capacidades incluidas — PROPUESTA ordenada por niveles"],
        filas, [30, 8, 62, 100])
    for i in range(fc + 1, ultima + 1):
        ws.row_dimensions[i].height = 255
        ws.cell(row=i, column=2).number_format = "0%"
        ws.cell(row=i, column=3).fill = FILL_GRIS
        ws.cell(row=i, column=4).fill = FILL_VERDE

    # ---------------------------------------------- 7. Matriz propuesta ----
    ws = wb.create_sheet("7. Matriz propuesta")
    ncols = 12
    c = ws.cell(row=1, column=1, value=titulo_rol)
    c.font = TITULO
    c.fill = FILL_TITULO
    c.alignment = Alignment(vertical="center")
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws.row_dimensions[1].height = 28

    c = ws.cell(row=2, column=1, value=proposito)
    c.font = NORMAL
    c.fill = FILL_GRIS
    c.alignment = TOP_WRAP
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    ws.row_dimensions[2].height = 40

    c = ws.cell(row=3, column=1,
                value="Alcance — Campos de investigación: Digital (UX) · Físico · Híbrido "
                      "[· Sistémico / contextual, a decidir].     "
                      "Única especialidad de diseño evaluada: Diseño Conductual.     "
                      "Product Design y Service Design aparecen solo como modelo de colaboración.")
    c.font = NEGRITA
    c.fill = FILL_SUAVE
    c.alignment = TOP_WRAP
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=ncols)
    ws.row_dimensions[3].height = 30

    cab = cabeceras[:3] + ["Campos aplicables (E1)", "Especialidad (E3)"] + cabeceras[3:]
    filas = []
    for fila_m in matriz:
        nuevo = COLUMNA_C_NUEVA.get(fila_m[0], fila_m[2])
        esp = "Diseño Conductual" if fila_m[0].startswith("3.") else "—"
        filas.append([fila_m[0], fila_m[1], nuevo,
                      CAMPOS_POR_DIMENSION.get(fila_m[0], ""), esp] + fila_m[3:])
    ultima = escribir_tabla(
        ws, 5, cab, filas, [26, 7, 94, 22, 18, 44, 40, 40, 40, 40, 44, 48])
    for i in range(6, ultima + 1):
        ws.row_dimensions[i].height = 265
        ws.cell(row=i, column=2).number_format = "0%"
        ws.cell(row=i, column=3).fill = FILL_VERDE

    # ---------------------------------------- 8. Hallazgos y decisiones ----
    ws = wb.create_sheet("8. Hallazgos y decisiones")
    fc = encabezar(
        ws, "Hallazgos del ejercicio y decisiones pendientes",
        "Problemas detectados al separar taxonomías en la columna «Capacidades incluidas», y preguntas "
        "que conviene cerrar con el lead de Research y el de Behavioral Design.", 6)
    ultima = escribir_tabla(
        ws, fc,
        ["#", "Hallazgo", "Dónde", "Evidencia en el archivo actual", "Por qué importa", "Propuesta"],
        [list(x) for x in HALLAZGOS], [6, 34, 26, 68, 54, 56])
    for i in range(fc + 1, ultima + 1):
        ws.cell(row=i, column=2).font = NEGRITA
        ws.cell(row=i, column=6).fill = FILL_VERDE

    fila = ultima + 3
    subtitulo_bloque(ws, fila, "Decisiones pendientes para cerrar con los leads", 6)
    fila += 1
    for j, nombre in enumerate(["#", "Pregunta", "Contexto", "", "Recomendación", ""], start=1):
        c = ws.cell(row=fila, column=j, value=nombre)
        c.font = CABECERA
        c.fill = FILL_CABECERA
        c.alignment = TOP_WRAP_CENTER
        c.border = BORDE
    fila += 1
    for pid, preg, ctx, rec in PREGUNTAS:
        c = ws.cell(row=fila, column=1, value=pid)
        c.font = NEGRITA
        c.alignment = TOP_WRAP
        c.border = BORDE
        c = ws.cell(row=fila, column=2, value=preg)
        c.font = NEGRITA
        c.alignment = TOP_WRAP
        c.border = BORDE
        c = ws.cell(row=fila, column=3, value=ctx)
        c.font = NORMAL
        c.alignment = TOP_WRAP
        c.border = BORDE
        ws.merge_cells(start_row=fila, start_column=3, end_row=fila, end_column=4)
        ws.cell(row=fila, column=4).border = BORDE
        c = ws.cell(row=fila, column=5, value=rec)
        c.font = NORMAL
        c.alignment = TOP_WRAP
        c.border = BORDE
        c.fill = FILL_AMBAR
        ws.merge_cells(start_row=fila, start_column=5, end_row=fila, end_column=6)
        ws.cell(row=fila, column=6).border = BORDE
        ws.cell(row=fila, column=6).fill = FILL_AMBAR
        ws.row_dimensions[fila].height = 100
        fila += 1

    wb.save(SALIDA)
    print("Escrito: %s" % SALIDA)
    print("Hojas: %s" % ", ".join(wb.sheetnames))
    print("Ítems desglosados: %d" % len(DESGLOSE))
    faltan = [d for d in matriz if d[0] not in COLUMNA_C_NUEVA]
    if faltan:
        raise SystemExit("Dimensiones sin columna C nueva: %s" % [d[0] for d in faltan])


if __name__ == "__main__":
    main()
