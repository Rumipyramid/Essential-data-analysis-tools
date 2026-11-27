import base64,sys
SP=sys.argv[1]; out=sys.argv[2]
logo=base64.b64encode(open(SP+'/rimacpdf/logo.png','rb').read()).decode()
rows=[
("¿Cómo pagó su última emergencia de salud?",
 "16,3% se endeudó por salud. H: el seguro se ve como un gasto que no vuelve.",
 "Reconstruir el último incidente con familias de NSE C y D.","El producto de entrada.","07"),
("¿En qué grupos ya confía y paga una cuota?",
 "H: juntas, cooperativas, mercados y gremios ya cobran y tienen confianza.",
 "Mapeo de grupos en Lima y dos ciudades del interior.","Socios para seguros colectivos.","07"),
("¿Quién decide, quién paga y quién usa el seguro en casa?",
 "H: son personas distintas; una entrevistada no ve su ahorro sin su pareja.",
 "Entrevistas en pareja o con el hogar completo.","A quién va cada canal y mensaje.","05"),
("¿Aceptaría el cobro automático? ¿Con qué condiciones?",
 "H: paga desde su banco por control; aceptaría con aviso previo y pausa.",
 "Prueba de prototipos del consentimiento del débito.","El diseño del cobro con TAPP.","01"),
("¿Por qué pagar con la billetera no lleva a asegurarse?",
 "H: al pagar no se siente la necesidad ni se sabe quién paga el siniestro.",
 "Entrevistas a usuarios de Yape o Plin y prueba A/B de mensajes.","Qué vender embebido y con qué socio.","04"),
("¿Qué le daría confianza para comprar sin un asesor?",
 "H: ver pagos rápidos, la marca detrás y la recomendación de un conocido.",
 "Encuesta a unas 800 personas que además mida lo visto en las entrevistas.","Mensajes y pruebas de confianza.","02 · 06"),
]
body=''.join(f'<div class="row{" pri" if i<=3 else ""}"><p class="n">{i:02d}</p><div><p class="h">{q}</p><p class="b">{h}</p></div><p class="i">{c}</p><p class="i">{d}</p><p class="v">{v}</p></div>' for i,(q,h,c,d,v) in enumerate(rows,1))
notes=("Qué decir: esta lámina dice qué falta saber antes de decidir. Son seis preguntas para el campo; cada una tiene la hipótesis que queremos poner a prueba, cómo investigarla, qué decisión desbloquea y qué insight de la lámina anterior valida. Las hipótesis son lectura nuestra a partir del Global Findex, el benchmark de 82 casos y dos entrevistas en profundidad; las entrevistas ilustran motivos y no miden frecuencias, por eso hay que ir a campo. Prioridad: primero las preguntas 1, 2 y 3, marcadas en rojo, porque definen el producto, el socio y el destinatario; las 4, 5 y 6 se pueden probar después con prototipos y una encuesta. "
"1. Cómo pagó su última emergencia de salud. 16,3% de los adultos pidió prestado para gastos médicos en el último año y para 27,2% la mayor preocupación financiera es pagar una enfermedad o un accidente graves (Banco Mundial, 2025). Hipótesis: la colecta familiar se percibe segura y el seguro, un gasto que no vuelve o algo que «llama la desgracia» (Orozco y Morales, 2022). Método: reconstrucción del último incidente crítico con familias de NSE C y D, en Lima y una ciudad del interior. Decide qué producto de entrada ofrecer, por ejemplo salud con uso frecuente frente a protección por catástrofe. Valida el insight 07. "
"2. En qué grupos ya confía y paga una cuota. 39,4% acude primero a la familia ante una emergencia y solo 10,2% paga un seguro (Banco Mundial, 2025). Hipótesis: juntas o panderos, cooperativas, asociaciones de mercado y gremios de mototaxistas ya cobran con regularidad y tienen la confianza de sus miembros, así que podrían contratar pólizas colectivas. Método: mapeo de grupos en Lima y dos ciudades del interior, con entrevistas a dirigentes y miembros. Decide con qué socios hacer pilotos. Valida el insight 07. "
"3. Quién decide, quién paga y quién usa el seguro en casa. Una entrevistada no ve su ahorro en la app sin ayuda de su pareja (RIMAC, 2026c). Hipótesis: quien decide, quien paga y quien usa son personas distintas. Método: entrevistas en pareja o con el hogar completo. Decide a quién va cada canal y cada mensaje. Valida el insight 05. "
"4. Si aceptaría el cobro automático y con qué condiciones. Las entrevistadas pagan desde su banco como un servicio más (RIMAC, 2026c); Indecopi exige consentimiento expreso y TAPP opera desde 2027 (Vodanovic, 2026). Hipótesis: hoy paga desde su banco para mantener el control y aceptaría el débito con aviso previo y opción de pausar. Método: prueba de prototipos del flujo de consentimiento. Decide el diseño del cobro con TAPP. Valida el insight 01. "
"5. Por qué pagar con la billetera no lleva a asegurarse. Yape tiene 17 millones de usuarios activos al mes y lo embebido es menos de 1% de la cartera de Pacífico (Gestión, 2026b). Hipótesis: al pagar no se siente la necesidad y no queda claro quién responde en el siniestro. Método: entrevistas a usuarios de Yape o Plin expuestos a ofertas de seguro y prueba A/B de mensajes. Decide qué vender embebido y con qué socio. Valida el insight 04. "
"6. Qué le daría confianza para comprar sin un asesor. Solo 2 de los 82 casos del benchmark trabajan la confianza (RIMAC, 2026a) y 17,5% de los peruanos menciona la desconfianza en las entidades financieras como razón para no tener cuenta (Banco Mundial, 2025). Hipótesis: ver que la aseguradora paga rápido, ver su marca detrás del banco o la tienda y la recomendación de un conocido. Método: encuesta a unas 800 personas que además mida en la población lo visto en las dos entrevistas. Decide los mensajes y las pruebas de confianza del recorrido. Valida los insights 02 y 06.")
html=f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Investigación de campo</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#ECEEFC;--ink:#0D1520;--grey:#6B7080;--red:#E4002B}}
html,body{{margin:0;height:100%;background:#d9dbe8;overflow:hidden}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center center}}
.slide{{position:absolute;inset:0;background:var(--bg);color:var(--ink);font-family:'Figtree',Arial,sans-serif;overflow:hidden}}
p{{margin:0}}
h1{{position:absolute;left:128px;top:128px;margin:0;font-family:'Poppins',Arial,sans-serif;font-weight:700;font-size:64px;letter-spacing:-2.5px;line-height:1}}
.sub{{position:absolute;left:128px;top:216px;font-size:26px;line-height:1.3}}
.tbl{{position:absolute;left:128px;top:282px;width:1664px;background:#fff}}
.hd,.row{{display:grid;grid-template-columns:48px 700px 400px 1fr 80px;column-gap:28px;align-items:start}}
.hd{{background:var(--ink);color:#fff;padding:13px 28px;font-size:17px;font-weight:700;letter-spacing:.3px}}
.row{{padding:12px 28px;border-top:1px solid #E1E3EE;position:relative}}
.row:first-of-type{{border-top:0}}
.row.pri::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:var(--red)}}
.n{{font-size:21px;font-weight:700;color:var(--ink);line-height:1.36}}
.pri .n{{color:var(--red)}}
.h{{font-size:21px;font-weight:700;line-height:1.36}}
.b{{font-size:20px;line-height:1.36;color:var(--grey)}}
.i{{font-size:20px;line-height:1.36}}
.v{{font-size:20px;line-height:1.36;font-weight:700}}
.src{{position:absolute;left:128px;top:943px;width:1664px;font-size:17px;color:var(--grey)}}
.foot{{position:absolute;left:128px;top:1004px;width:1664px;display:flex;align-items:center;font-size:16px;color:var(--grey)}}
.foot img{{height:18.5px}}
.foot .sep{{width:1px;height:28px;background:#C9CCDA;margin:0 22px}}
.foot .pg{{margin-left:auto}}
aside{{display:none}}
</style></head><body>
<div id="stage"><div class="slide">
<h1>Qué queda por investigar en campo</h1>
<p class="sub">Seis preguntas para pasar de hipótesis a decisión. <b>Primero 01, 02 y 03:</b> definen producto, socio y destinatario.</p>
<div class="tbl">
<div class="hd"><p></p><p>Pregunta e hipótesis</p><p>Cómo investigarlo</p><p>Qué decide</p><p>Insight</p></div>
{body}
</div>
<p class="src">Banco Mundial (2025), Global Findex, Perú 2024 · Orozco y Morales (2022) · Gestión (2026b) · RIMAC (2026a, 2026c) · H: hipótesis, lectura nuestra</p>
<div class="foot"><img alt="RIMAC" src="data:image/png;base64,{logo}"><span class="sep"></span><span>CoE de Experiencia - Behavioral Design</span><span class="pg">31 / 32</span></div>
<aside>{notes}</aside>
</div></div>
<script>
function fit(){{var s=Math.min(innerWidth/1920,innerHeight/1080);document.getElementById('stage').style.transform='translate(-50%,-50%) scale('+s+')';}}
addEventListener('resize',fit);fit();
</script>
</body></html>'''
open(out,'w').write(html)
