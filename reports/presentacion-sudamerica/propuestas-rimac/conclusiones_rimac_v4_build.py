import base64,sys
SP=sys.argv[1]; out=sys.argv[2]
logo=base64.b64encode(open(SP+'/rimacpdf/logo.png','rb').read()).decode()
rows=[
("Muchas pólizas se caen por olvido, no por decisión.",
 "Por defecto participa 86% vs. 37%; Justos cobra por Pix contra el olvido.",
 "Débito autorizado en un clic al contratar, con aviso previo y pausa; listo para TAPP en 2027.",3,"Fuerte"),
("El siniestro es el momento de la verdad: ahí se gana o se pierde al cliente.",
 "NPS de 42 si es digital vs. 27 solo humano; lo mejor: el choque por WhatsApp.",
 "Siniestro por app o WhatsApp con una persona detrás, y pago en días, no en semanas.",3,"Fuerte"),
("La IA debe estar al servicio primero de la operación.",
 "SURA: de 20 h a 8 min; Bradesco equipa a 1.200 corredores; Pier falló.",
 "Automatizar documentos, triaje y fraude; asistente de IA para corredores y asesores.",2,"Media"),
("El seguro se compra junto a lo que protege, no por sí solo.",
 "SOAT y compra protegida escalan; salud en Yape pesa menos de 1%; DaviPlata cerró.",
 "Seguros dentro de compras con riesgo (viajes, electro, movilidad, crédito), con marca visible.",2,"Mixta"),
("Las personas tienen hábitos de canal definidos para cada tarea.",
 "Pagan desde el banco, avisan por WhatsApp y consultan en la app (n = 2).",
 "Información del seguro y sus servicios en todos los canales: banco, WhatsApp, app y corredor.",2,"Media"),
("La app no es el fin: se vuelve a ella por lo propio y lo urgente.",
 "Retiene ver el ahorro o la clínica; los sorteos solo «obligan» a entrar.",
 "Mostrar ahorro, cobertura y clínicas, y resolver lo urgente; medir momentos resueltos.",2,"Mixta"),
("Las personas confían más en sus grupos que en bancos y aseguradoras.",
 "39,4% acude primero a la familia; solo 10,2% paga un seguro.",
 "Seguros colectivos para grupos no registrados (cooperativas, familias, barrios, juntas).",1,"Indirecta"),
]
def dots(n):
    return ''.join(f'<span class="dot{" on" if i<n else ""}"></span>' for i in range(3))
body=''.join(f'<div class="row"><p class="n">{i:02d}</p><div><p class="h">{a}</p><p class="b">{b}</p></div><p class="i">{c}</p><div class="ev"><div class="dots">{dots(n)}</div><p class="evl">{e}</p></div></div>' for i,(a,b,c,n,e) in enumerate(rows,1))
notes=("Qué decir: siete insights ordenados por la solidez de la evidencia y por cuánto control tiene RIMAC sobre la palanca. Primero lo que se puede hacer ya; al final, lo que hay que probar. Cada fila trae el insight, el dato que lo sostiene, el accionable y qué tan fuerte es la evidencia. Punto de partida: el freno en Perú no es lo digital sino la demanda de seguro: 51,7% de los adultos paga en digital (Banco Mundial, 2025), pero el seguro voluntario más el SOAT es 1,7% del PBI, frente a 2,6% en México y 2,2% en Colombia (MAPFRE Economics, 2025). "
"1. Muchas pólizas se caen por olvido, no por decisión. Con inscripción por defecto participa 86%, frente a 37% cuando hay que inscribirse (Madrian y Shea, 2001); el efecto se repite en un mercado emergente con dinero móvil (Blumenstock et al., 2018). Pix Automático cobra R$ 1.200 millones al mes a un año de su lanzamiento (Let's Money, 2026b) y Justos lo usa para evitar la cancelación por olvido (Justos, 2026). Las entrevistadas pagan a mano desde su banco (RIMAC, 2026c). Crítica: la evidencia viene del ahorro, no del seguro, e Indecopi exige consentimiento expreso, así que no vale una casilla premarcada: autorización en un clic al contratar, aviso antes de cada cobro y opción de pausar. TAPP opera desde 2027 (Vodanovic, 2026). Medir persistencia a 12 meses y caída por impago. El pago en un clic evita el olvido; la compra en un clic no crea necesidad. "
"2. El siniestro es el momento de la verdad. Un siniestro 100% digital tiene NPS de 42, frente a 27 cuando es solo humano (Bain & Company, 2022, Brasil); Quálitas resolvió 28% de sus siniestros de 2024 con fotos, con 94,1% de satisfacción (Quálitas, 2025); Porto canaliza 70% de los avisos por WhatsApp (Revista Apólice, 2026). En las entrevistas, el choque por WhatsApp fue la mejor experiencia y el médico a domicilio por teléfono, la peor. Crítica: digitalizar solo el aviso no basta si la reparación o el pago siguen lentos; las cifras son declaradas por las empresas. "
"3. La IA debe estar al servicio primero de la operación. SURA México bajó la respuesta a correos de agentes de 20 horas a 8 minutos (Darío Celis, 2026); Allianz Türkiye declara más de 20 millones de euros de valor sobre 15 invertidos (Allianz Türkiye, 2026); Bradesco atiende con IA y especialistas a más de 1.200 corredores (CQCS, 2026a) y Río Uruguay subió 67% los corredores que cotizan (Prensa Aseguradora, 2026). Pier, que quiso competir con el corredor, despidió a 39% de su equipo (Startups.com.br, 2023); dos de cada tres prefieren un asesor para cerrar (Capgemini y LIMRA, 2026). Crítica: casi nadie publica el retorno y el cliente no lo ve; es eficiencia, no diferencial. "
"4. El seguro se compra junto a lo que protege, no por sí solo. Escalan el SOAT dentro de apps (Seguros Mundial, 1,8 millones de pólizas con aliados; Semana, 2026) y la compra protegida; en cambio, la salud en Yape pesa menos de 1% de la cartera de Pacífico (Gestión, 2026b) y DaviPlata dejó de aceptar solicitudes. Crítica: Mercado Pago, con 11 millones de clientes de seguros de vida, contradice en parte la regla porque el socio da crédito y empuja el producto; es lectura nuestra por validar. El socio se queda con la relación y la marca se pierde. Yape es del grupo de Pacífico: RIMAC debe elegir socios cuya transacción ya trae un riesgo, como retail, viajes, movilidad o crédito. "
"5. Las personas tienen hábitos de canal definidos para cada tarea: las entrevistadas pagan desde su banco como un servicio más, avisan lo urgente por WhatsApp porque «alguien respondiendo es la mejor opción» y entran a la app para consultar (RIMAC, 2026c). En la radiografía digital de RIMAC (uso interno), la consulta de póliza es 95,8% digital y reportar un choque, 2%. Crítica: son dos entrevistas y datos internos; ilustran el patrón, no lo miden en la población. Accionable: no forzar a la persona a cambiar de canal sino llevar la información del seguro y sus servicios a todos los canales que ya usa, como el banco, WhatsApp, la app y el corredor, con el mismo dato del cliente detrás; lo omnicanal es el dato. 6. La app no es el fin: se vuelve a ella por lo propio y lo urgente. Las entrevistadas vuelven a la app que muestra algo suyo, como el ahorro en Mapfre o las clínicas en RIMAC; los sorteos producen un «me obligan» y la app se borra cuando el SOAT se paga solo (RIMAC, 2026c). Los clientes digitales de Interseguro bajaron de 580 mil a unos 540 mil y Betterfly cerró en cinco países (RIMAC, 2026b; Forbes Chile, 2025). Crítica: son dos entrevistas; ilustran motivos, no frecuencias. Un canal para cada momento: comprar con socio o corredor, pagar por banco o TAPP, consultar en la app y lo urgente con una persona. "
"7. Las personas confían más en sus grupos que en bancos y aseguradoras; 17,5% menciona la desconfianza en las entidades financieras como razón para no tener cuenta, frente a 5,7% en Brasil (Banco Mundial, 2025). 39,4% acude primero a la familia y 10,2% paga un seguro; quienes más dependen de la familia menos se aseguran (Banco Mundial, 2025). Café Seguro es una póliza colectiva que contratan cooperativas, con 39.589 productores (Seguros Bolívar, 2025). Crítica: la evidencia es rural o de microfinanzas; en grupos urbanos informales de Perú no hay pruebas, y las AFOCAT muestran el riesgo de un grupo sin aseguradora. Accionable: seguros colectivos para grupos que no están registrados como clientes, como cooperativas, familias, barrios o juntas, con la aseguradora detrás; empezar con pilotos, no a escala. "
"Salud como producto de entrada y confianza como diferencial quedan como preguntas para el campo, porque aún son hipótesis. Lo que el benchmark no prueba: las cifras son declaradas por las empresas, no hay grupo de control y los fracasos rara vez se publican.")
html=f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Conclusiones RIMAC</title>
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
.hd,.row{{display:grid;grid-template-columns:48px 790px 1fr 130px;column-gap:28px;align-items:start}}
.hd{{background:var(--ink);color:#fff;padding:13px 28px;font-size:17px;font-weight:700;letter-spacing:.3px}}
.row{{padding:9px 28px;border-top:1px solid #E1E3EE}}
.row:first-of-type{{border-top:0}}
.n{{font-size:21px;font-weight:700;color:var(--red);line-height:1.36}}
.h{{font-size:21px;font-weight:700;line-height:1.36}}
.b{{font-size:20px;line-height:1.36;color:#3A4150}}
.i{{font-size:20px;line-height:1.36;color:var(--ink)}}
.ev{{display:flex;flex-direction:column;gap:6px;padding-top:6px}}
.dots{{display:flex;gap:6px}}
.dot{{width:14px;height:14px;border-radius:50%;border:2px solid var(--ink);box-sizing:border-box}}
.dot.on{{background:var(--ink)}}
.evl{{font-size:17px;color:var(--grey)}}
.note{{position:absolute;left:128px;top:876px;width:1664px;box-sizing:border-box;background:#fff;border-left:6px solid var(--red);padding:16px 28px;font-size:20px;line-height:1.36}}
.src{{position:absolute;left:128px;top:943px;width:1664px;font-size:17px;color:var(--grey)}}
.foot{{position:absolute;left:128px;top:1004px;width:1664px;display:flex;align-items:center;font-size:16px;color:var(--grey)}}
.foot img{{height:18.5px}}
.foot .sep{{width:1px;height:28px;background:#C9CCDA;margin:0 22px}}
.foot .pg{{margin-left:auto}}
aside{{display:none}}
</style></head><body>
<div id="stage"><div class="slide">
<h1>Conclusiones</h1>
<p class="sub">El freno no es lo digital: 51,7% ya paga en digital, pero el seguro es solo 1,7% del PBI.</p>
<div class="tbl">
<div class="hd"><p></p><p>Insight</p><p>Accionable</p><p>Evidencia</p></div>
{body}
</div>
<p class="src">Banco Mundial (2025) · MAPFRE Economics (2025) · Madrian y Shea (2001) · Justos (2026) · Bain & Company (2022) · Darío Celis (2026) · CQCS (2026a) · Gestión (2026b) · RIMAC (2026c)</p>
<div class="foot"><img alt="RIMAC" src="data:image/png;base64,{logo}"><span class="sep"></span><span>CoE de Experiencia - Behavioral Design</span><span class="pg">30 / 31</span></div>
<aside>{notes}</aside>
</div></div>
<script>
function fit(){{var s=Math.min(innerWidth/1920,innerHeight/1080);document.getElementById('stage').style.transform='translate(-50%,-50%) scale('+s+')';}}
addEventListener('resize',fit);fit();
</script>
</body></html>'''
open(out,'w').write(html)
