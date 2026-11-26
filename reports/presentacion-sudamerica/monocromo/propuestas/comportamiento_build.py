import sys,os
D=sys.argv[1]
W='#ECEBE6'; G='#A3A29C'; T='#2A2A27'
def fmt(v): return f"{v:.1f}".replace('.',',')
def bar(label,v,width=470,color=W,lw=360,sub=None):
    w=v/100*width
    lab=f'<p class="txt" style="width:{lw}px">{label}</p>' if sub is None else f'<div style="width:{lw}px"><p class="txt">{label}</p></div>'
    return (f'<div style="display:flex;align-items:center;gap:16px">{lab}'
            f'<svg width="{width}" height="26" viewBox="0 0 {width} 26" aria-hidden="true"><rect x="0" y="0" width="{width}" height="26" fill="{T}"/><rect x="0" y="0" width="{w:.1f}" height="26" fill="{color}"/></svg>'
            f'<p class="txt" style="font-weight:700;width:90px">{fmt(v)}%</p></div>')
def pair(label,a,b,width=290,lw=230):
    # a = grupo bajo (gris), b = grupo alto (blanco)
    return (f'<div style="display:flex;align-items:center;gap:16px"><p class="txt" style="width:{lw}px">{label}</p>'
            f'<div style="display:flex;flex-direction:column;gap:4px">'
            f'<div style="display:flex;align-items:center;gap:10px"><svg width="{width}" height="18" viewBox="0 0 {width} 18" aria-hidden="true"><rect width="{width}" height="18" fill="{T}"/><rect width="{a/100*width:.1f}" height="18" fill="{G}"/></svg><p class="dim" style="width:80px">{fmt(a)}</p></div>'
            f'<div style="display:flex;align-items:center;gap:10px"><svg width="{width}" height="18" viewBox="0 0 {width} 18" aria-hidden="true"><rect width="{width}" height="18" fill="{T}"/><rect width="{b/100*width:.1f}" height="18" fill="{W}"/></svg><p class="txt" style="width:80px;font-weight:700">{fmt(b)}</p></div>'
            f'</div></div>')

# ---------- Lámina 1: banca
s1=f'''<section id="comp-banca" data-transition="fade">
<h2 class="t">Billetera sí, banco a medias</h2>
<div class="row" style="gap:64px">
<div style="width:900px;display:flex;flex-direction:column;gap:9px">
<p class="k">Adultos peruanos, 2024</p>
{bar("Tiene alguna cuenta",59.3)}
{bar("Paga en digital",51.7)}
{bar("Tiene billetera (Yape, Plin)",42.5)}
{bar("Ahorra en banco o billetera",31.4)}
{bar("Paga servicios en línea",27.9)}
<div style="display:flex;gap:40px;margin-top:10px">
<div class="stat" style="width:420px"><p class="mid">1 de 10</p><p class="dim">tiene billetera, pero no cuenta bancaria.</p></div>
<div class="stat" style="width:420px"><p class="mid">17,5%</p><p class="dim">no tiene cuenta por desconfianza. Brasil: 5,7%.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<p class="k">La brecha es educativa</p>
<p class="dim">Gris: primaria o menos<br>Blanco: secundaria o más</p>
{pair("Tiene cuenta",29.6,66.5)}
{pair("Paga en digital",20.2,59.3)}
{pair("Tiene billetera",13.3,49.5)}
<p class="dim" style="margin-top:6px">Por ingreso del hogar: tiene cuenta 44,6% del 40% de menores ingresos (≈ NSE E y parte del D) y 69,1% del resto.</p>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · La billetera abrió la puerta, pero pagar y ahorrar en el sistema sigue siendo de quien tiene más educación.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, % de adultos de 15 años o más, datos de 2024</p>
<p class="foot">Dónde está Perú · Comportamiento · Propuesta</p>
<aside>Qué decir: esta lámina describe cómo se relaciona el peruano con la banca. Todos los datos son del Global Findex 2025 del Banco Mundial, una encuesta a unos 1.000 adultos por país, con datos de 2024, y se leen como porcentaje de adultos de 15 años o más. Izquierda, cuánto usan el sistema: 59,3% tiene alguna cuenta, sea en un banco o en una billetera; 51,7% hizo o recibió un pago digital en el último año; 42,5% tiene una billetera de dinero móvil, como Yape o Plin, frente a 14,3% en 2021; 31,4% ahorró en un banco o billetera; y solo 27,9% paga sus servicios, como luz o teléfono, por celular o internet. Tener cuenta no es usarla. Cerca de 1 de cada 10 adultos tiene billetera pero no cuenta bancaria (cálculo nuestro: 59,3% con alguna cuenta menos 49,8% con cuenta bancaria); en 2023, Yape tenía 2,6 millones de usuarios sin cuenta bancaria previa (Craddock et al., 2023, McKinsey). 17,5% de los adultos no tiene cuenta y menciona entre sus razones la desconfianza en las instituciones financieras, frente a 5,7% en Brasil; si se pregunta por la razón principal, gana la falta de ingresos (BCRP). Derecha, la brecha por educación: entre adultos con primaria o menos, 29,6% tiene cuenta, 20,2% paga en digital y 13,3% tiene billetera; con secundaria o más, 66,5%, 59,3% y 49,5%. La misma brecha aparece por ingreso del hogar: en el 40% de menores ingresos, que equivale aproximadamente al NSE E y al tercio inferior del NSE D, 44,6% tiene cuenta, frente a 69,1% en el 60% de mayores ingresos. Lectura nuestra: la billetera abrió la puerta, pero usar el sistema para pagar y ahorrar sigue concentrado en quienes tienen más educación e ingreso.</aside>
</section>
'''
# ---------- Lámina 2: riesgo y seguros
seg=[("Familia o amigos",39.4,W),("Sus ahorros",17.8,'#C9C8C2'),("Trabajar más",15.5,G),("Préstamo",9.8,'#6E6D68'),("Vender algo",5.7,'#4A4A45'),("No podría",9.8,'#2E2E2B'),("Otro",2.0,'#1F1F1D')]
Wst=1664; x=0; rects=''
for n,v,c in seg:
    w=v/100*Wst; rects+=f'<rect x="{x:.1f}" y="0" width="{w-3:.1f}" height="56" fill="{c}"/>'; x+=w
s2=f'''<section id="comp-riesgo" data-transition="fade">
<h2 class="t">La familia es la aseguradora</h2>
<p class="k">Si tuviera una emergencia, ¿de dónde sacaría el dinero? · Principal fuente, adultos peruanos</p>
<svg width="{Wst}" height="56" viewBox="0 0 {Wst} 56" aria-label="Barra apilada de la principal fuente de dinero ante una emergencia">{rects}</svg>
<div style="display:flex;gap:28px;flex-wrap:wrap"><p class="txt"><b>Familia 39,4</b></p><p class="dim">Ahorros 17,8</p><p class="dim">Trabajar más 15,5</p><p class="dim">Préstamo 9,8</p><p class="dim">Vender algo 5,7</p><p class="dim">No podría 9,8</p><p class="dim">Otro 2,0</p></div>
<div class="row" style="gap:64px;margin-top:8px">
<div style="width:800px;display:flex;flex-direction:column;gap:12px">
<p class="k">Familia primero, por grupo</p>
{bar("Mujeres",46.5,width=330,lw=330)}
{bar("Hombres",32.2,width=330,lw=330,color=G)}
{bar("Primaria o menos",44.0,width=330,lw=330)}
{bar("Secundaria o más",38.1,width=330,lw=330,color=G)}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<p class="k">Paga un seguro con regularidad</p>
{bar("Total",10.2,width=330,lw=330)}
{bar("Mujeres",7.2,width=330,lw=330,color=G)}
{bar("Primaria o menos",3.5,width=330,lw=330,color=G)}
{bar("No trabaja",2.4,width=330,lw=330,color=G)}
</div>
</div>
<p class="dim" style="margin-top:6px"><b style="color:#ECEBE6">En la región,</b> la familia también va primero en Colombia (45,1), Ecuador (43,0) y Argentina (39,3). En Brasil se trabaja más (31,5) y en Uruguay* se pide prestado (27,4).</p>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · El seguro compite con la familia. Mujeres, menos educados y quien no trabaja dependen más de ella y casi no se aseguran.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, % de adultos de 15 años o más, datos de 2024 · *Uruguay: 2021</p>
<p class="foot">Dónde está Perú · Comportamiento · Propuesta</p>
<aside>Qué decir: esta lámina describe cómo enfrenta el riesgo el peruano. La pregunta del Global Findex es: si tuviera una emergencia y necesitara una suma importante en 30 días, ¿cuál sería su principal fuente de dinero? En Perú, 39,4% acudiría primero a su familia o amigos; 17,8% usaría sus ahorros; 15,5% trabajaría más; 9,8% pediría un préstamo a un banco, su empleador o un prestamista; 5,7% vendería algo; y 9,8% no podría conseguirlo (Banco Mundial, 2025, datos de 2024). La familia pesa más entre las mujeres (46,5%, frente a 32,2% de los hombres), entre quienes tienen primaria o menos (44,0%, frente a 38,1% con secundaria o más), entre quienes no trabajan ni buscan trabajo (46,9%) y en el 40% de menores ingresos (43,9%). Del otro lado, solo 10,2% de los adultos paga con regularidad algún seguro: 7,2% de las mujeres, 3,5% de quienes tienen primaria o menos y 2,4% de quienes no trabajan. En la región, la familia primero también domina en Colombia (45,1%), Ecuador (43,0%) y Argentina (39,3%), mientras en Brasil la primera opción es trabajar más (31,5%) y en Uruguay un préstamo (27,4%, datos de 2021). La compra de seguros también es particular: 67% de los peruanos prefiere cotizar en digital, pero solo 21% compra en línea (APESEG, 2023), y en un ranking de experiencia del cliente con 20 industrias, los seguros quedaron últimos (Centrum PUCP, 2022, citado en Craddock et al., 2023). Lectura nuestra: el seguro compite con la familia; diseñar productos que se compren, se paguen o protejan en familia puede funcionar mejor que competir contra ella.</aside>
</section>
'''
# ---------- Lámina 3: digitalización
rows=[("Tiene billetera",14.3,42.5),("Ahorra en banco o billetera",15.3,31.4),("Paga con celular en tienda",21.3,32.5),("Paga servicios en línea",19.7,27.9),("Familia primero en emergencia",42.0,39.4)]
Wd=460
def dumb(label,a,b,bold=False):
    xa=a/60*Wd; xb=b/60*Wd
    lo,hi=sorted([xa,xb])
    ch=b-a; chs=("+" if ch>0 else "−")+fmt(abs(ch))
    return (f'<div style="display:flex;align-items:center;gap:16px"><p class="txt" style="width:380px{";font-weight:700" if bold else ""}">{label}</p>'
            f'<svg width="{Wd}" height="30" viewBox="0 0 {Wd} 30" aria-hidden="true"><line x1="0" y1="15" x2="{Wd}" y2="15" stroke="#2A2A27" stroke-width="2"/>'
            f'<line x1="{lo:.1f}" y1="15" x2="{hi:.1f}" y2="15" stroke="{W}" stroke-width="4"/><circle cx="{xa:.1f}" cy="15" r="9" fill="#0F0F0E" stroke="{G}" stroke-width="3"/><circle cx="{xb:.1f}" cy="15" r="11" fill="{W}"/></svg>'
            f'<p class="txt" style="width:300px"><b>{chs}</b> <span style="color:#A3A29C">({fmt(a)} → {fmt(b)})</span></p></div>')
s3=f'''<section id="comp-digital" data-transition="fade">
<h2 class="t">Lo digital cambia rápido</h2>
<div class="row" style="gap:56px">
<div style="width:1190px;display:flex;flex-direction:column;gap:8px">
<p class="k">Adultos peruanos · ○ 2021 · ● 2024 · cambio en puntos</p>
{''.join(dumb(*r) for r in rows[:4])}
{dumb(*rows[4],bold=True)}
<div style="display:flex;gap:36px;margin-top:10px">
<div class="stat" style="width:540px"><p class="mid">51,7%</p><p class="dim">paga en digital. Chile, Brasil, Argentina y Uruguay: 68% a 84%.</p></div>
<div class="stat" style="width:540px"><p class="mid">67% / 21%</p><p class="dim">cotiza seguros en digital / compra la póliza en línea.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<p class="k">En la app de seguros</p>
<div class="card"><p class="txt"><b>Consultan</b></p><p class="dim">ahorro, cobertura, clínicas</p></div>
<div class="card"><p class="txt"><b>Pagan afuera</b></p><p class="dim">banco o débito automático</p></div>
<div class="card"><p class="txt"><b>Resuelven por WhatsApp</b></p><p class="dim">«alguien respondiendo es la mejor opción»</p></div>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Los hábitos digitales siguen a la infraestructura. La app gana consultando, no cobrando.</p></div>
<p class="src">Banco Mundial (2025) · APESEG (2023) · RIMAC (2026c), dos entrevistas · Chile y Uruguay: 2021</p>
<p class="foot">Dónde está Perú · Comportamiento · Propuesta</p>
<aside>Qué decir: esta lámina describe la digitalización del peruano y qué tan rápido cambia. Izquierda, el mismo indicador en 2021 (círculo vacío) y en 2024 (círculo lleno), según el Global Findex del Banco Mundial: tener billetera pasó de 14,3% a 42,5% de los adultos (+28,2 puntos); ahorrar en un banco o billetera, de 15,3% a 31,4%; pagar con celular o tarjeta en una tienda, de 21,3% a 32,5%; pagar servicios en línea, de 19,7% a 27,9%. En cambio, acudir primero a la familia ante una emergencia apenas bajó, de 42,0% a 39,4%. Los hábitos digitales cambiaron en tres años, con Yape y la interoperabilidad entre billeteras; la red familiar casi no se movió. En la comparación con la región, los países con más empleo formal, más cuentas y mejores instituciones son también los que más pagan en digital: 51,7% de los peruanos paga en digital, frente a 68% a 84% en Chile, Brasil, Argentina y Uruguay. En seguros, 67% prefiere cotizar en digital, pero solo 21% compra en línea (APESEG, 2023). Derecha, lo que vimos en dos entrevistas a usuarias de apps de aseguradoras: entran a la app para consultar su ahorro (Mapfre), su cobertura o qué clínica les corresponde (RIMAC); pagan desde su banco o con débito automático; y resuelven lo urgente con una llamada y un enlace por WhatsApp, como el reporte de un choque en menos de 10 minutos. Son dos personas: ilustran motivos, no frecuencias. Lectura nuestra: los hábitos digitales siguen a la infraestructura, así que TAPP, en 2027, puede acelerar el cobro digital; la red familiar cambia lento y hay que diseñar para ella.</aside>
</section>
'''
for n,s in [('comp-banca',s1),('comp-riesgo',s2),('comp-digital',s3)]:
    open(os.path.join(D,n+'.html'),'w').write(s)
