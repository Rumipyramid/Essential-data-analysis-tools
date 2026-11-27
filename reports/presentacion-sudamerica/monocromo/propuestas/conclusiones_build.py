import sys,os
D=sys.argv[1]
rows=[
("El freno es el seguro, no lo digital.","51,7% paga digital; seguro, 1,7% PBI.",
 "Dar un motivo para asegurarse donde ya es digital.",
 "¿Cómo pagó su última emergencia?","H: el seguro es gasto perdido."),
("El socio da tráfico, no demanda.","Yape: 17 M usuarios; embebido, <1%.",
 "Producto necesario, marca visible y siniestro pactado.",
 "¿Por qué la billetera no asegura?","H: al pagar no siente necesidad."),
("Vender al grupo, no a la persona.","Familia primero: 39,4%; seguro: 10,2%.",
 "Pólizas colectivas con cooperativas y gremios.",
 "¿En qué grupo ya paga una cuota?","Juntas, cooperativas, gremios."),
("Cobrar sin depender de la memoria.","Por defecto: 86% vs. 37%; TAPP en 2027.",
 "Diseñar ya un débito que el cliente elija.",
 "¿Aceptaría el cobro automático?","H: sí, con aviso previo y pausa."),
("Un canal para cada momento.","Consulta en app; urgencia, con persona.",
 "Lo omnicanal es el dato, no la oferta.",
 "¿Quién decide, paga y usa en casa?","H: son personas distintas."),
("La confianza es el espacio vacío.","Solo 2 de 82 casos la trabajan.",
 "Mostrar cuánto y qué tan rápido se paga.",
 "¿Qué le haría comprar sin asesor?","H: ver pagos rápidos y la marca."),
]
cols="48px 580px 440px 1fr"
head=(f'<div style="display:grid;grid-template-columns:{cols};column-gap:32px;border-bottom:4px solid #0F0F0E;padding-bottom:8px">'
      '<p></p><p class="k">Lo que concluimos</p><p class="k">Qué significa para RIMAC</p><p class="k">Qué validar en campo</p></div>')
body=''
for i,(c,d,r,q,h) in enumerate(rows,1):
    body+=(f'<div style="display:grid;grid-template-columns:{cols};column-gap:32px;border-bottom:2px solid #BDBCB6;padding:6px 0">'
           f'<p class="txt" style="font-weight:700">{i:02d}</p>'
           f'<div><p class="txt"><b>{c}</b></p><p class="dim">{d}</p></div>'
           f'<p class="txt">{r}</p>'
           f'<div><p class="txt">{q}</p><p class="dim">{h}</p></div></div>')
aside=("Qué decir (en la tabla, H es hipótesis): esta lámina cierra la presentación y conecta cada conclusión con lo que significa para RIMAC y con la pregunta que hay que llevar al campo para validarla. Las conclusiones son lectura nuestra a partir de los 82 casos del benchmark, el Global Findex y dos entrevistas. "
"Uno: el freno es el seguro, no lo digital. 51,7% de los adultos peruanos ya paga en digital, por encima de Colombia (49,2%) y Ecuador (43,3%) (Banco Mundial, 2025), pero el seguro voluntario más el SOAT es 1,7% del PBI, frente a 2,7% en América Latina, 2,6% en México y 2,2% en Colombia (MAPFRE Economics, 2025). Para RIMAC: no hay que digitalizar al cliente, hay que darle un motivo para tener seguro donde ya es digital. En campo: reconstruir cómo pagaron su última emergencia de salud; 16,3% pidió prestado para salud y para 27,2% los gastos médicos son su mayor preocupación (Banco Mundial, 2025). Hipótesis: la colecta familiar se percibe segura y el seguro, un gasto que no vuelve o algo que «llama la desgracia» (Orozco y Morales, 2022). Decide la propuesta de valor del producto de entrada. "
"Dos: el socio pone el tráfico, no la demanda. Yape tiene 17 millones de usuarios activos al mes y lo embebido es menos de 1% de la cartera de Pacífico (Gestión, 2026b); DaviPlata dejó de aceptar solicitudes de su seguro de vida (DaviPlata, s. f.); en los paquetes del banco o la tienda la marca de la aseguradora se pierde (RIMAC, 2026c). Para RIMAC: entrar a un ecosistema solo rinde con un producto que se necesite en ese momento, la marca visible y el contacto en el siniestro pactado con el socio; el éxito se mide en pólizas que se renuevan. En campo: entrevistas a usuarios de Yape o Plin expuestos a ofertas de seguro y una prueba A/B de mensajes. Decide si invertir en ecosistemas y con qué producto. "
"Tres: vender al grupo, no a la persona. Ante una emergencia, 39,4% acude primero a la familia o amigos y solo 10,2% paga un seguro; quien más depende de la familia menos se asegura: mujeres 46,5% y 7,2%; 40% de menores ingresos 43,9% y 3,8% (Banco Mundial, 2025). En Colombia, Café Seguro cubre a 39.589 productores con una póliza colectiva que contratan cooperativas (Seguros Bolívar, 2025). Para RIMAC: pólizas colectivas con cooperativas, asociaciones y gremios que ya cobran y ya tienen confianza; con aseguradora detrás, a diferencia de las AFOCAT. En campo: mapeo de juntas o panderos, cooperativas, asociaciones de mercado y gremios de mototaxistas en dos o tres ciudades. Decide con qué socios armar pólizas colectivas. "
"Cuatro: cobrar sin depender de la memoria. Con inscripción por defecto participa 86%, frente a 37% cuando hay que inscribirse (Madrian y Shea, 2001, en ahorro previsional); Pix Automático cobra R$ 1.200 millones al mes a un año de su lanzamiento (Let's Money, 2026b); TAPP opera en Perú desde 2027 (Vodanovic, 2026). Indecopi exige consentimiento expreso, así que el débito debe elegirlo el cliente. En campo: prueba de prototipos del consentimiento. Hipótesis: hoy paga desde su banco para tener el control y aceptaría el débito con aviso previo y opción de pausar. Decide el diseño del cobro con TAPP. "
"Cinco: un canal para cada momento; es la respuesta a omnicanalidad o mejor canal. Comprar con el socio o el corredor equipado; pagar por el banco o TAPP; consultar en la app, que retiene cuando muestra algo propio para decidir; y resolver lo urgente por WhatsApp o la app con la identidad ya cargada y una persona detrás. Un siniestro 100% digital tiene NPS de 42 frente a 27 cuando es solo humano (Bain & Company, 2022) y dos de cada tres prefieren un asesor para cerrar (Capgemini y LIMRA, 2026). Lo omnicanal es el dato del cliente, no la oferta. En campo: entrevistas en díada u hogar en NSE C y D, porque quien decide, quien paga y quien usa la app pueden ser personas distintas; una entrevistada depende de su pareja para ver su ahorro. Decide a quién se dirige cada canal. "
"Seis: la confianza es el espacio vacío. Solo 2 de los 82 casos trabajan la confianza y ninguno ataca la creencia de que el seguro llama la desgracia (RIMAC, 2026a); 17,5% de los peruanos menciona la desconfianza como razón para no tener cuenta, frente a 5,7% en Brasil (Banco Mundial, 2025). Para RIMAC: es el diferencial más defendible: mostrar cuánto y qué tan rápido se paga, hacer visible la marca en el canal del socio y apoyarse en la recomendación entre pares. En campo: encuesta de unas 800 personas que además mida lo visto en las dos entrevistas. Decide los mensajes y las pruebas de confianza del recorrido. "
"Prioridad sugerida para el campo: primero las preguntas 1, 3 y 5, porque definen producto, socio y destinatario; luego 2, 4 y 6, que se pueden probar con prototipos. Las cifras de casos son declaradas por las empresas; las entrevistas ilustran motivos y no miden frecuencias.")
s=f'''<section id="conclusiones" class="inv" data-transition="fade">
<h2 class="t">Seis apuestas por validar</h2>
<div style="display:flex;flex-direction:column">
{head}
{body}
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Validar primero 3, 5 y 1: definen socio, destinatario y producto.</p></div>
<p class="src">Banco Mundial (2025) · MAPFRE Economics (2025) · Gestión (2026b) · Madrian y Shea (2001) · RIMAC (2026a)</p>
<p class="foot">Conclusiones · 19 / 20</p>
<aside>{aside}</aside>
</section>
'''
open(os.path.join(D,'conclusiones.html'),'w').write(s)
