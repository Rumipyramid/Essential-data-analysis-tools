import base64,sys
SP=sys.argv[1]; out=sys.argv[2]
logo=base64.b64encode(open(SP+'/rimacpdf/logo.png','rb').read()).decode()
L=[
("En Perú ya hay hábito digital; el freno es el seguro.",
 "51,7% paga en digital, más que Colombia y Ecuador; el seguro es 1,7% del PBI.",
 "Dar un motivo para asegurarse donde el cliente ya es digital."),
("La venta embebida trae tráfico, no demanda.",
 "Yape tiene 17 M de usuarios al mes; lo embebido es menos de 1% de Pacífico.",
 "Entrar con un producto que se necesite, marca visible y siniestro pactado."),
("Vender al grupo, no a la persona.",
 "39,4% acude primero a la familia ante una emergencia; solo 10,2% paga un seguro.",
 "Pólizas colectivas con cooperativas y gremios, como Café Seguro."),
("El cobro automático llega a Perú en 2027.",
 "Con el cobro por defecto participa 86%, frente a 37%; TAPP opera desde 2027.",
 "Diseñar ya un débito que el cliente elija, con consentimiento expreso."),
("Omnicanal en el dato; el mejor canal en cada momento.",
 "App para consultar, WhatsApp con persona para lo urgente, asesor para cerrar.",
 "Equipar al corredor y compartir la identidad del cliente entre canales."),
("La confianza es el espacio vacío.",
 "Solo 2 de 82 casos la trabajan; 17,5% desconfía de las entidades financieras.",
 "Mostrar cuánto y qué tan rápido se paga, con la marca a la vista."),
]
R=[
("¿Cómo pagó su última emergencia de salud?",
 "16,3% se endeudó por salud. Hipótesis: la colecta familiar se siente segura y el seguro, un gasto que no vuelve."),
("¿Quién decide, quién paga y quién usa el seguro en casa?",
 "Hipótesis: son personas distintas; una entrevistada no ve su ahorro sin su pareja."),
("¿En qué grupos ya confía y paga una cuota?",
 "Juntas, cooperativas, mercados y gremios de mototaxis: posibles tomadores de pólizas colectivas."),
("¿Por qué la billetera no se convierte en seguro?",
 "Hipótesis: al pagar no se siente la necesidad y no queda claro quién paga el siniestro."),
("¿Aceptaría el cobro automático? ¿Con qué condiciones?",
 "Hipótesis: paga desde su banco por control; aceptaría con aviso previo y pausa."),
("¿Qué le daría confianza para comprar sin un asesor?",
 "Hipótesis: ver pagos rápidos, la marca detrás del banco y la recomendación de un conocido."),
]
left=''.join(f'<div class="item"><p class="h">{a}</p><p class="b">{b}</p><p class="i"><span class="ar">→</span> {c}</p></div>' for a,b,c in L)
right=''.join(f'<div class="item"><p class="h">{a}</p><p class="g">{b}</p></div>' for a,b in R)
notes=("Qué decir: la lámina tiene dos mitades. A la izquierda, seis conclusiones; cada una con el dato que la sostiene y, tras la flecha, lo que significa para RIMAC. A la derecha, seis preguntas para investigar en Perú antes de decidir, cada una con su hipótesis. Las conclusiones son lectura nuestra a partir de los 82 casos del benchmark, el Global Findex y dos entrevistas. "
"1. 51,7% de los adultos paga en digital, frente a 49,2% en Colombia y 43,3% en Ecuador (Banco Mundial, 2025); el seguro voluntario más el SOAT es 1,7% del PBI, frente a 2,6% en México, 2,2% en Colombia y 2,7% en América Latina (MAPFRE Economics, 2025). "
"2. Yape tiene 17 millones de usuarios activos al mes y lo embebido es menos de 1% de la cartera de Pacífico; bancaseguros pesa 35% (Gestión, 2026b, 2026c). DaviPlata dejó de aceptar solicitudes de su seguro de vida. Hay que medir pólizas que se renuevan, no usuarios. "
"3. 39,4% acude primero a la familia o amigos y 10,2% paga un seguro; quien más depende de la familia menos se asegura: mujeres 46,5% y 7,2%; 40% de menores ingresos 43,9% y 3,8% (Banco Mundial, 2025). Café Seguro, de Seguros Bolívar en Colombia, es una póliza colectiva que contratan cooperativas: 39.589 productores y 52.222 hectáreas a septiembre de 2024 (Seguros Bolívar, 2025). "
"4. Con inscripción por defecto participa 86%, frente a 37% cuando hay que inscribirse (Madrian y Shea, 2001, en ahorro previsional). Pix Automático cobra R$ 1.200 millones al mes (Let's Money, 2026b). TAPP opera desde 2027 (Vodanovic, 2026) e Indecopi exige consentimiento expreso. "
"5. Responde a omnicanalidad frente a mejor canal: lo omnicanal es el dato del cliente; la oferta va por el mejor canal de cada momento. Las entrevistadas consultan en la app, pagan en su banco y prefieren WhatsApp con una persona para lo urgente (RIMAC, 2026c); dos de cada tres prefieren un asesor para cerrar (Capgemini y LIMRA, 2026); Bradesco atiende a más de 1.200 corredores con IA y especialistas (CQCS, 2026a). "
"6. Solo 2 de 82 casos trabajan la confianza y ninguno ataca la creencia de que el seguro llama la desgracia (RIMAC, 2026a; Orozco y Morales, 2022). 17,5% de los peruanos menciona la desconfianza en las entidades financieras como razón para no tener cuenta, frente a 5,7% en Brasil (Banco Mundial, 2025). "
"Preguntas: 1, reconstruir la última emergencia de salud (16,3% pidió prestado para salud; para 27,2% es su mayor preocupación). 2, entrevistas en pareja u hogar en NSE C y D. 3, mapeo de grupos con cuota y confianza en dos o tres ciudades. 4, entrevistas a usuarios de Yape o Plin expuestos a ofertas de seguro y prueba A/B. 5, prototipos del consentimiento del débito antes de 2027. 6, encuesta de unas 800 personas que además mida lo visto en las dos entrevistas. Prioridad: 1, 2 y 3, porque definen producto, destinatario y socio.")
html=f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Conclusiones RIMAC</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#ECEEFC;--ink:#0D1520;--grey:#6B7080;--red:#E4002B;--rule:#0D1520}}
html,body{{margin:0;height:100%;background:#d9dbe8;overflow:hidden}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:0 0}}
.slide{{position:absolute;inset:0;background:var(--bg);color:var(--ink);font-family:'Figtree',Arial,sans-serif;overflow:hidden}}
h1{{position:absolute;left:128px;top:128px;margin:0;font-family:'Poppins',Arial,sans-serif;font-weight:700;font-size:64px;letter-spacing:-2.5px;line-height:1}}
.col{{position:absolute;top:231px;border-top:4px solid var(--rule);padding-top:22px}}
.c1{{left:128px;width:800px}} .c2{{left:984px;width:808px}}
.lab{{margin:0 0 16px;font-size:17px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase}}
.item{{margin-bottom:13px;min-height:85.7px}}
p{{margin:0}}
.h{{font-size:21px;font-weight:700;line-height:1.36}}
.b{{font-size:21px;line-height:1.36}}
.i{{font-size:21px;line-height:1.36;color:#3A4150}}
.ar{{color:var(--red);font-weight:700;display:inline-block;transform:translateY(-1px)}}
.g{{font-size:21px;line-height:1.36;color:var(--grey)}}
.src{{position:absolute;left:128px;top:932px;width:1664px;font-size:17px;color:var(--grey)}}
.foot{{position:absolute;left:128px;top:1004px;width:1664px;display:flex;align-items:center;font-size:16px;color:var(--grey)}}
.foot img{{height:18.5px}}
.foot .sep{{width:1px;height:28px;background:#C9CCDA;margin:0 22px}}
.foot .pg{{margin-left:auto}}
aside{{display:none}}
</style></head><body>
<div id="stage"><div class="slide">
<h1>Conclusiones</h1>
<div class="col c1"><p class="lab">Lo que concluimos</p>{left}</div>
<div class="col c2"><p class="lab">Qué investigar en Perú antes de decidir</p>{right}</div>
<p class="src">Banco Mundial (2025), Global Findex, Perú 2024 · MAPFRE Economics (2025) · Gestión (2026b) · Madrian y Shea (2001) · Seguros Bolívar (2025) · RIMAC (2026a, 2026c) · Lectura nuestra</p>
<div class="foot"><img alt="RIMAC" src="data:image/png;base64,{logo}"><span class="sep"></span><span>CoE de Experiencia - Behavioral Design</span><span class="pg">30 / 31</span></div>
<aside>{notes}</aside>
</div></div>
<script>
function fit(){{var s=Math.min(innerWidth/1920,innerHeight/1080),st=document.getElementById('stage');st.style.transform='scale('+s+') translate(-50%,-50%)';st.style.transformOrigin='0 0';st.style.left='50%';st.style.top='50%';st.style.transform='translate(-50%,-50%) scale('+s+')';st.style.transformOrigin='center center';}}
addEventListener('resize',fit);fit();
</script>
</body></html>'''
open(out,'w').write(html)
