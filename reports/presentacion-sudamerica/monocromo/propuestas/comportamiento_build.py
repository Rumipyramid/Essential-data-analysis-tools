import sys,os
D=sys.argv[1]
W='#ECEBE6'; G='#8C8B85'; TR='#262622'; LG='#BDBCB6'
def f(v): return f"{v:.1f}".replace('.',',')
def hbar(label,v,scale=100,width=420,lw=400,color=W,vw=110,bold=False):
    return (f'<div style="display:flex;align-items:center;gap:20px"><p class="txt" style="width:{lw}px{";font-weight:700" if bold else ""}">{label}</p>'
            f'<svg width="{width}" height="22" viewBox="0 0 {width} 22" aria-hidden="true"><rect width="{width}" height="22" fill="{TR}"/><rect width="{v/scale*width:.1f}" height="22" fill="{color}"/></svg>'
            f'<p class="txt" style="width:{vw}px;font-weight:700">{f(v)}%</p></div>')
def refbar(label,v,vec,hor,width=440,lw=360):
    """barra de Perú + rango de vecinos (línea punteada) + rango del horizonte (línea sólida)"""
    sx=lambda x: x/100*width
    h=44
    svg=(f'<svg width="{width}" height="{h}" viewBox="0 0 {width} {h}" aria-hidden="true">'
         f'<rect y="0" width="{width}" height="20" fill="{TR}"/><rect y="0" width="{sx(v):.1f}" height="20" fill="{W}"/>'
         f'<line x1="{sx(vec[0]):.1f}" y1="29" x2="{sx(vec[1]):.1f}" y2="29" stroke="{LG}" stroke-width="4" stroke-dasharray="5 4"/>'
         f'<line x1="{sx(vec[0]):.1f}" y1="24" x2="{sx(vec[0]):.1f}" y2="34" stroke="{LG}" stroke-width="2"/><line x1="{sx(vec[1]):.1f}" y1="24" x2="{sx(vec[1]):.1f}" y2="34" stroke="{LG}" stroke-width="2"/>'
         f'<line x1="{sx(hor[0]):.1f}" y1="39" x2="{sx(hor[1]):.1f}" y2="39" stroke="{W}" stroke-width="4"/>'
         f'<line x1="{sx(hor[0]):.1f}" y1="34" x2="{sx(hor[0]):.1f}" y2="44" stroke="{W}" stroke-width="2"/><line x1="{sx(hor[1]):.1f}" y1="34" x2="{sx(hor[1]):.1f}" y2="44" stroke="{W}" stroke-width="2"/></svg>')
    return (f'<div style="display:flex;align-items:flex-start;gap:20px"><p class="txt" style="width:{lw}px">{label}</p>{svg}'
            f'<p class="txt" style="width:100px;font-weight:700">{f(v)}%</p></div>')

# ===== Lámina 1
s1=f'''<section id="comp-banca" data-transition="fade">
<h2 class="t">Entrar por la billetera</h2>
<div class="row" style="gap:64px">
<div style="width:960px;display:flex;flex-direction:column;gap:4px">
<p class="k">Perú frente a la región · % de adultos, 2024</p>
<div style="display:flex;flex-wrap:wrap;column-gap:28px;row-gap:2px;margin-bottom:8px"><p class="dim" style="display:flex;align-items:center;gap:8px"><svg width="32" height="14" aria-hidden="true"><rect width="32" height="14" fill="{W}"/></svg>Perú</p><p class="dim" style="display:flex;align-items:center;gap:8px"><svg width="32" height="14" aria-hidden="true"><line x1="0" y1="7" x2="32" y2="7" stroke="{LG}" stroke-width="4" stroke-dasharray="5 4"/></svg>Vecinos: Colombia, Ecuador</p><p class="dim" style="display:flex;align-items:center;gap:8px"><svg width="32" height="14" aria-hidden="true"><line x1="0" y1="7" x2="32" y2="7" stroke="{W}" stroke-width="4"/></svg>Horizonte: Chile, Brasil, Argentina, Uruguay</p></div>
{refbar("Tiene alguna cuenta",59.3,(57.1,64.5),(73.7,86.4))}
{refbar("Paga en digital",51.7,(43.3,49.2),(68.0,84.3))}
{refbar("Tiene billetera",42.5,(10.1,39.1),(56.7,58.2))}
{refbar("Paga servicios en línea",27.9,(18.9,19.6),(32.3,54.8))}
<div style="display:flex;gap:48px;margin-top:4px">
<div class="stat" style="width:440px"><p class="mid">1 de cada 10</p><p class="dim">tiene billetera, pero no cuenta bancaria (cálculo nuestro).</p></div>
<div class="stat" style="width:440px"><p class="mid">17,5%</p><p class="dim">menciona la desconfianza como razón para no tener cuenta. Brasil: 5,7%.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:6px">
<p class="k">Tiene cuenta, según grupo</p>
{hbar("Hasta primaria",35.9,width=180,lw=290,color=G,vw=90)}
{hbar("Secundaria",51.8,width=180,lw=290,color=G,vw=90)}
{hbar("Superior técnica",75.1,width=180,lw=290,vw=90)}
{hbar("Universitaria",84.7,width=180,lw=290,vw=90)}
<div style="border-top:2px solid #3A3A36"></div>
{hbar("Mujeres",56.2,width=180,lw=290,color=G,vw=90)}
{hbar("Hombres",62.5,width=180,lw=290,vw=90)}
<div style="border-top:2px solid #3A3A36"></div>
{hbar("40% menor ingreso",44.6,width=180,lw=290,color=G,vw=90)}
{hbar("60% mayor ingreso",69.1,width=180,lw=290,vw=90)}
<p class="dim">Educación: INEI, 18+. Sexo e ingreso: Findex, 15+.</p>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Perú supera a sus vecinos en billetera; usar el sistema sigue atado a la educación, el sexo y el ingreso.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, 2024 (Chile y Uruguay, 2021) · INEI (2025), ENAHO, oct.-dic. 2024</p>
<p class="foot">Dónde está Perú · Comportamiento · 1 / 3</p>
<aside>Qué decir: esta lámina describe cómo se relaciona el peruano con la banca, frente a la región. Datos del Global Findex 2025 del Banco Mundial, encuesta a unos 1.000 adultos por país con datos de 2024, en porcentaje de adultos de 15 años o más. La barra es Perú; la línea punteada es el rango de los vecinos más parecidos en estructura (Colombia y Ecuador); la línea sólida es el rango del horizonte (Chile, Brasil, Argentina y Uruguay; Chile y Uruguay con datos de 2021). Tiene alguna cuenta, en banco, financiera o billetera: Perú 59,3%; vecinos 57,1% a 64,5%; horizonte 73,7% a 86,4%. Paga en digital: Perú 51,7%; vecinos 43,3% a 49,2%; horizonte 68,0% a 84,3%. Tiene billetera de dinero móvil, como Yape o Plin: Perú 42,5%, por encima de Colombia (39,1%) y Ecuador (10,1%), y cerca del horizonte con dato, Argentina (56,7%) y Brasil (58,2%). Paga servicios en línea: Perú 27,9%; vecinos 18,9% a 19,6%; horizonte 32,3% a 54,8%. Cerca de 1 de cada 10 adultos tiene billetera pero no cuenta bancaria: es un cálculo nuestro, 59,3% con alguna cuenta menos 49,8% con cuenta bancaria. 17,5% de los adultos menciona la desconfianza en las instituciones financieras entre sus razones para no tener cuenta, frente a 5,7% en Brasil; la encuesta admite varias razones. Derecha: quién tiene cuenta. Por educación, con la ENAHO del INEI (adultos de 18 años o más, cuarto trimestre de 2024): hasta primaria 35,9%, secundaria 51,8%, superior no universitaria 75,1% y universitaria 84,7%. Por sexo, según el Findex: mujeres 56,2% y hombres 62,5%; las mujeres también tienen menos billetera (37,4% frente a 47,7%) y pagan menos en digital (46,6% frente a 56,9%). Por ingreso del hogar: 44,6% del 40% de menores ingresos, que equivale aproximadamente al NSE E y al tercio inferior del NSE D, frente a 69,1% del 60% restante. Ojo: INEI y Findex miden cuentas de forma distinta y no deben sumarse. Lectura nuestra: Perú ya supera a sus vecinos en billetera, pero usar el sistema sigue atado a la educación, el sexo y el ingreso.</aside>
</section>
'''
# ===== Lámina 2
seg=[("Familia",39.4,W),("Ahorros",17.8,LG),("Trabajar más",15.5,G),("Préstamo",9.8,'#5E5D59'),("Vender algo",5.7,'#45443F'),("No podría",9.8,'#33322F')]
Wst=1664; x=0; rects=f'<rect width="{Wst}" height="28" fill="#1F1F1D"/>'
for n,v,c in seg:
    w=v/100*Wst; rects+=f'<rect x="{x:.1f}" y="0" width="{w-4:.1f}" height="28" fill="{c}"/>'; x+=w
legend=''.join(f'<p class="txt" style="display:flex;align-items:center;gap:8px"><svg width="20" height="20" aria-hidden="true"><rect width="20" height="20" fill="{c}" stroke="#5E5D59" stroke-width="1"/></svg>{n} <b>{f(v)}</b></p>' for n,v,c in seg)
groups=[("Sexo",[("Hombres",32.2,13.4),("Mujeres",46.5,7.2)]),("Educación",[("Secundaria o más",38.1,11.9),("Primaria o menos",44.0,3.5)]),("Ingreso",[("60% mayores",36.4,14.5),("40% menores",43.9,3.8)]),("Trabajo",[("Trabaja o busca",36.1,13.6),("No trabaja",46.9,2.4)])]
BW=130
def cell(v,scale):
    return (f'<div style="display:flex;align-items:center;gap:10px"><svg width="{BW}" height="16" viewBox="0 0 {BW} 16" aria-hidden="true"><rect width="{BW}" height="16" fill="{TR}"/><rect width="{v/scale*BW:.1f}" height="16" fill="{W}"/></svg><p class="txt" style="width:70px;font-weight:700">{f(v)}</p></div>')
tab=('<div style="display:grid;grid-template-columns:130px 250px 1fr 1fr;column-gap:20px;row-gap:0px;align-items:center">'
     '<p></p><p></p><p class="k">Familia</p><p class="k">Paga seguro</p>')
for g,rows in groups:
    for i,(lab,a,b) in enumerate(rows):
        top='border-top:2px solid #3A3A36;padding-top:4px;' if i==0 else ''
        tab+=(f'<p class="dim" style="{top}">{g if i==0 else ""}</p><p class="txt" style="{top}">{lab}</p>'
              f'<div style="{top}">{cell(a,60)}</div><div style="{top}">{cell(b,20)}</div>')
tab+='</div>'
s2=f'''<section id="comp-riesgo" data-transition="fade">
<h2 class="t">Diseñar con la familia</h2>
<p class="k">Ante una emergencia, ¿de dónde sacaría el dinero en 30 días? · Principal fuente, adultos peruanos</p>
<svg style="flex-shrink:0" width="{Wst}" height="28" viewBox="0 0 {Wst} 28" aria-label="Barra apilada de la principal fuente de dinero ante una emergencia">{rects}</svg>
<div style="display:flex;gap:24px;flex-wrap:wrap">{legend}</div>
<p class="dim">Familia primero en la región: Colombia 45,1 · Ecuador 43,0 · Argentina 39,3 · Chile* 33,4 · Brasil 26,2</p>
<div class="row" style="gap:48px">
<div style="width:860px">{tab}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<div class="stat"><p class="k">La necesidad existe</p><p class="mid">16,3% · 27,2%</p><p class="dim">se endeudó por salud · teme gastos médicos</p></div>
<div class="stat"><p class="k">Lo compra en paquete: banco o tienda</p><p class="mid">67% → 21%</p><p class="dim">cotiza en digital → compra en línea</p></div>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Quien más depende de la familia menos se asegura, aunque la salud ya le cuesta deuda.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, 2024 · APESEG (2023) · *Chile, 2021 · Escalas: 0-60% y 0-20%</p>
<p class="foot">Dónde está Perú · Comportamiento · 2 / 3</p>
<aside>Qué decir: esta lámina describe cómo enfrenta el riesgo el peruano y cómo se relaciona con el seguro. Arriba, la pregunta del Global Findex: si tuviera una emergencia y necesitara una suma importante en 30 días, ¿cuál sería su principal fuente de dinero? En Perú, 39,4% acudiría primero a su familia o amigos; 17,8% a sus ahorros; 15,5% trabajaría más; 9,8% pediría un préstamo a un banco, su empleador o un prestamista; 5,7% vendería algo; 9,8% no podría conseguirlo; y 2,0% da otra respuesta (Banco Mundial, 2025, datos de 2024). En la región, la familia también va primero en Colombia (45,1%), Ecuador (43,0%) y Argentina (39,3%); en Chile pesa menos (33,4%, datos de 2021) y en Brasil la primera opción es trabajar más (31,5%; familia 26,2%). Tabla: familia primero y pago regular de un seguro, por grupo. Sexo: hombres 32,2% y 13,4%; mujeres 46,5% y 7,2%. Educación: secundaria o más 38,1% y 11,9%; primaria o menos 44,0% y 3,5%; el Findex solo publica estos dos niveles. Ingreso del hogar: 60% de mayores ingresos 36,4% y 14,5%; 40% de menores ingresos, que equivale aproximadamente al NSE E y al tercio inferior del NSE D, 43,9% y 3,8%. Trabajo: quienes trabajan o buscan trabajo 36,1% y 13,6%; quienes no trabajan 46,9% y 2,4%. En la región, Perú es tercero de siete en pago de un seguro (10,2%), detrás de Argentina (22,4%) y Brasil (13,9%), y por delante de Colombia (4,4%) y Ecuador (5,0%). Derecha: la necesidad existe. 16,3% de los adultos pidió prestado para gastos médicos en el último año, y para 27,2% la mayor preocupación financiera es pagar una enfermedad o un accidente graves (Banco Mundial, 2025); además, 7 de cada 10 peruanos que necesitaron atención de salud no la obtuvieron (Banco Mundial, citado en RIMAC, 2026a). Cómo compra el seguro: 67% prefiere buscar y cotizar en digital, pero solo 21% compra la póliza en línea (APESEG, 2023); en las entrevistas, los seguros llegaron en paquetes del banco o por llamadas de la tarjeta de tienda, y la marca de la aseguradora se pierde; 43% compraría un seguro integrado a otra compra (Gestión). Además, los seguros quedaron últimos entre 20 industrias en satisfacción del cliente en Perú (Centrum PUCP, 2022, citado en Craddock et al., 2023). Lectura nuestra: quien más depende de la familia es quien menos se asegura, aunque la salud ya le cuesta deuda; diseñar productos que se compren, se paguen o protejan en familia puede funcionar mejor que competir contra ella.</aside>
</section>
'''
# ===== Lámina 3
rows=[("Tiene billetera",14.3,42.5),("Ahorra en el sistema",15.3,31.4),("Paga con celular en tienda",21.3,32.5),("Paga servicios en línea",19.7,27.9),("Familia primero",42.0,39.4)]
Wd=420; SC=50
def dumb(label,a,b,bold=False):
    xa=a/SC*Wd; xb=b/SC*Wd; lo,hi=sorted([xa,xb]); ch=b-a; chs=("+" if ch>0 else "−")+f(abs(ch))
    return (f'<div style="display:flex;align-items:center;gap:20px"><p class="txt" style="width:400px{";font-weight:700" if bold else ""}">{label}</p>'
            f'<svg width="{Wd}" height="28" viewBox="0 0 {Wd} 28" aria-hidden="true"><line x1="0" y1="14" x2="{Wd}" y2="14" stroke="#3A3A36" stroke-width="2"/>'
            f'<line x1="{lo:.1f}" y1="14" x2="{hi:.1f}" y2="14" stroke="{W}" stroke-width="4"/><circle cx="{xa:.1f}" cy="14" r="9" fill="#0F0F0E" stroke="{LG}" stroke-width="3"/><circle cx="{xb:.1f}" cy="14" r="11" fill="{W}"/></svg>'
            f'<p class="txt" style="width:300px"><b>{chs}</b> <span style="color:#A3A29C">{f(a)} → {f(b)}</span></p></div>')
axis=(f'<div style="display:flex;gap:20px"><p class="txt" style="width:400px"></p><div style="width:{Wd}px;display:flex;justify-content:space-between">'+''.join(f'<p class="dim">{t}%</p>' for t in (0,25,50))+'</div></div>')
s3=f'''<section id="comp-digital" data-transition="fade">
<h2 class="t">Subirse a la infraestructura</h2>
<div class="row" style="gap:64px">
<div style="width:1180px;display:flex;flex-direction:column;gap:10px">
<p class="k">Adultos peruanos · ○ 2021 → ● 2024 · cambio en puntos</p>
{''.join(dumb(*r) for r in rows[:4])}
<div style="border-top:2px solid #3A3A36;padding-top:8px">{dumb(*rows[4],bold=True)}</div>
{axis}
<div style="display:flex;gap:44px;margin-top:4px">
<div class="stat" style="width:560px"><p class="mid">51,7%</p><p class="dim">paga en digital. Vecinos: 43% a 49%. Horizonte: 68% a 84%.</p></div>
<div class="stat" style="width:560px"><p class="mid">47,4% · 34,7%</p><p class="dim">de los jóvenes (15-24) tiene billetera · tiene cuenta bancaria.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<p class="k">En la app · 2 entrevistas</p>
<div class="card"><p class="txt"><b>Consultan</b></p><p class="dim">su ahorro, su cobertura, la clínica que les toca</p></div>
<div class="card"><p class="txt"><b>Pagan afuera</b></p><p class="dim">en su banco o con débito automático</p></div>
<div class="card"><p class="txt"><b>Lo urgente, por WhatsApp</b></p><p class="dim">«alguien respondiendo es la mejor opción»</p></div>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Lo digital sigue a la estructura, no a la cultura: Chile y Perú comparten perfil cultural, pero pagan en digital 84% y 52%.</p></div>
<p class="src">Banco Mundial (2025), Global Findex · The Culture Factor Group (s. f.) · RIMAC (2026c) · Chile y Uruguay: 2021</p>
<p class="foot">Dónde está Perú · Comportamiento · 3 / 3</p>
<aside>Qué decir: esta lámina describe la digitalización del peruano y por qué cambia. Izquierda: el mismo hábito en 2021 (círculo vacío) y en 2024 (círculo lleno), según el Global Findex del Banco Mundial, en porcentaje de adultos. Tener billetera pasó de 14,3% a 42,5% (+28,2 puntos); ahorrar en un banco, financiera o billetera, de 15,3% a 31,4%; pagar con celular o tarjeta en una tienda, de 21,3% a 32,5%; pagar servicios en línea, de 19,7% a 27,9%. En cambio, acudir primero a la familia ante una emergencia apenas bajó, de 42,0% a 39,4%. Los hábitos digitales cambiaron en tres años, con Yape y la interoperabilidad entre billeteras; la red familiar casi no se movió. Abajo: 51,7% de los peruanos paga en digital, por encima de sus vecinos Colombia (49,2%) y Ecuador (43,3%) y por debajo del horizonte: Uruguay 68,0%, Argentina 72,2%, Brasil 77,4% y Chile 84,3% (Uruguay y Chile, 2021). Los jóvenes de 15 a 24 años entran al sistema por la billetera: 47,4% tiene una, pero solo 34,7% tiene cuenta bancaria, y solo 7,0% paga un seguro. Derecha: lo que vimos en dos entrevistas a usuarias de apps de aseguradoras; son dos personas e ilustran motivos, no frecuencias. Entran a la app para consultar su ahorro (Mapfre), su cobertura o qué clínica les corresponde (RIMAC); pagan desde su banco o con débito automático; y resuelven lo urgente con una llamada y un enlace por WhatsApp, como el reporte de un choque en menos de 10 minutos. Lectura: los hábitos digitales siguen a la estructura del país, no a su cultura. Chile y Perú tienen casi el mismo perfil cultural en Hofstede (distancia al poder 63 y 64; aversión a la incertidumbre 86 y 87; The Culture Factor Group), pero en Chile 84,3% paga en digital y en Perú 51,7%; lo que los separa es la estructura: empleo formal de 74% frente a 30% y una cuenta universal en el banco estatal desde 2006. En nuestro análisis de 8 a 10 países, el parecido en hábitos digitales con Perú sigue al parecido estructural (correlación de 0,65 a 0,71) y no al cultural (−0,15 a 0,37). Implicación: TAPP, la plataforma de pagos inmediatos prevista para 2027, puede acelerar el cobro digital de seguros.</aside>
</section>
'''
# ===== Lámina 4: interna
gest=[("Consulta de póliza",95.8),("Gestión de pago",92.0),("Renovación",35.1),("Buscar una clínica",23.7),("Pedir una grúa",15.0),("Reportar un choque",2.0),("Médico a domicilio",0.0)]
s4=f'''<section id="comp-rimac" data-transition="fade">
<h2 class="t">Llevar lo urgente a la app</h2>
<p class="k">USO INTERNO · Cliente digital RIMAC, julio de 2026</p>
<div class="row" style="gap:64px">
<div style="width:760px;display:flex;flex-direction:column;gap:12px">
<div class="stat"><p class="mid">28,9%</p><p class="dim">de los 2,4 millones de clientes gestionables está registrado en canales digitales.</p></div>
<div class="stat"><p class="mid">77% · 71%</p><p class="dim">del cliente digital es NSE A o B · vive en Lima. El peruano de las láminas anteriores es otro.</p></div>
<div class="stat"><p class="mid">80,7% · 21,2%</p><p class="dim">es digital si llegó por la fuerza de ventas · si llegó por bancos y retail.</p></div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<p class="k">Participación digital, por gestión</p>
{''.join(hbar(n,v,width=380,lw=360,color=(W if v>=50 else G),vw=110) for n,v in gest)}
<p class="dim">Médico a domicilio: 7.706 pedidos por teléfono; no está en la app. Con siniestro, 61% es digital; sin siniestro, 28%.</p>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · La app ya resuelve la consulta; lo urgente y el cliente de NSE C, D y E siguen afuera.</p></div>
<p class="src">RIMAC (2026d), radiografía digital, corte de julio de 2026 · Uso interno, no compartir fuera de la compañía</p>
<p class="foot">Dónde está Perú · Comportamiento · Anexo interno</p>
<aside>Qué decir: lámina de uso interno con la radiografía digital de RIMAC, corte de julio de 2026. De 2.440.910 clientes gestionables, 705.407 están registrados en canales digitales: 28,9%. El cliente digital es de mediana edad (61% tiene entre 29 y 50 años), de NSE A o B (77%) y de Lima (71%): es lo contrario del peruano descrito en las láminas anteriores, donde la oportunidad está en los NSE C, D y E, en provincias, en las mujeres y en los informales. Lo digital depende de cómo llegó el cliente: 80,7% de quienes compraron con la fuerza de ventas multiproducto es digital, frente a 21,2% de quienes compraron en bancos y retail. Participación digital por gestión: consulta de póliza 95,8%, gestión de pago 92,0%, renovación 35,1%, buscar una clínica 23,7%, pedir una grúa 15,0%, reportar un choque 2,0% (157 de 7.809) y médico a domicilio 0% (7.706 pedidos, todos por teléfono, porque no está en la app). El siniestro empuja el uso digital: 61% de los clientes con siniestro es digital, frente a 28% de los demás. Coincide con las entrevistas: la app sirve para consultar, y lo urgente y el pago ocurren afuera. Lectura nuestra: la app ya resuelve la consulta; la oportunidad es llevar lo urgente (médico a domicilio, choque, grúa) a la app con una persona detrás, y llegar al cliente de NSE C, D y E por los canales que ya usa. Uso interno: no compartir fuera de la compañía.</aside>
</section>
'''
for n,s in [('comp-banca',s1),('comp-riesgo',s2),('comp-digital',s3),('comp-rimac',s4)]:
    open(os.path.join(D,n+'.html'),'w').write(s)
