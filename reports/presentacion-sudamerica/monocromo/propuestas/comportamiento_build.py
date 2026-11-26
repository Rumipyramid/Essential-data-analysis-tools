import sys,os
D=sys.argv[1]
W='#ECEBE6'; G='#8C8B85'; T='#26262299'; TR='#262622'
def f(v): return f"{v:.1f}".replace('.',',')
def hbar(label,v,scale=100,width=420,lw=400,color=W,vw=110,bold=False,unit='%'):
    w=v/scale*width
    return (f'<div style="display:flex;align-items:center;gap:20px">'
            f'<p class="txt" style="width:{lw}px{";font-weight:700" if bold else ""}">{label}</p>'
            f'<svg width="{width}" height="24" viewBox="0 0 {width} 24" aria-hidden="true"><rect width="{width}" height="24" fill="{TR}"/><rect width="{w:.1f}" height="24" fill="{color}"/></svg>'
            f'<p class="txt" style="width:{vw}px;font-weight:700">{f(v)}{unit}</p></div>')
def pairrow(label,a_lab,a,b_lab,b,scale,width=300,lw=230):
    """two bars: a (gris) vs b (blanco), each with its own small label"""
    def one(l,v,c,bold):
        return (f'<div style="display:flex;align-items:center;gap:12px"><p class="dim" style="width:170px">{l}</p>'
                f'<svg width="{width}" height="20" viewBox="0 0 {width} 20" aria-hidden="true"><rect width="{width}" height="20" fill="{TR}"/><rect width="{v/scale*width:.1f}" height="20" fill="{c}"/></svg>'
                f'<p class="txt" style="width:80px{";font-weight:700" if bold else ""}">{f(v)}</p></div>')
    return (f'<div style="display:flex;flex-direction:column;gap:4px;border-top:2px solid #3A3A36;padding-top:8px">'
            f'<p class="k" style="font-size:24px;letter-spacing:1px">{label}</p>{one(a_lab,a,G,False)}{one(b_lab,b,W,True)}</div>')

# ===== Lámina 1: banca
s1=f'''<section id="comp-banca" data-transition="fade">
<h2 class="t">Billetera sí, banco a medias</h2>
<div class="row" style="gap:72px">
<div style="width:960px;display:flex;flex-direction:column;gap:10px">
<p class="k">Qué hacen los adultos peruanos · 2024</p>
{hbar("Tiene alguna cuenta",59.3)}
{hbar("Paga en digital",51.7)}
{hbar("Tiene billetera",42.5)}
{hbar("Ahorra en el sistema",31.4)}
{hbar("Paga servicios en línea",27.9)}
<p class="dim">Billetera: Yape, Plin. Sistema: banco, financiera o billetera.</p>
<div style="display:flex;gap:48px">
<div class="stat" style="width:440px"><p class="mid">1 de cada 10</p><p class="dim">tiene billetera, pero no cuenta bancaria.</p></div>
<div class="stat" style="width:440px"><p class="mid">17,5%</p><p class="dim">no tiene cuenta por desconfianza. En Brasil, 5,7%.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:14px">
<p class="k">Tiene cuenta, según educación</p>
{hbar("Hasta primaria",35.9,width=220,lw=250,color=G,vw=90)}
{hbar("Secundaria",51.8,width=220,lw=250,color=G,vw=90)}
{hbar("Superior técnica",75.1,width=220,lw=250,vw=90)}
{hbar("Universitaria",84.7,width=220,lw=250,vw=90)}
<p class="dim">Adultos de 18 años o más, ENAHO, oct.-dic. 2024.</p>
<div class="stat" style="margin-top:4px"><p class="mid">44,6% · 69,1%</p><p class="dim">tiene cuenta en el 40% de menores ingresos (≈ NSE E y parte del D) · en el 60% restante.</p></div>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · La billetera abrió la puerta; usar el sistema sigue atado a la educación y al ingreso.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, adultos de 15+ · INEI (2025), ENAHO, adultos de 18+</p>
<p class="foot">Dónde está Perú · Comportamiento · 1 / 3</p>
<aside>Qué decir: esta lámina describe cómo se relaciona el peruano con la banca. A la izquierda, datos del Global Findex 2025 del Banco Mundial, una encuesta a unos 1.000 adultos por país con datos de 2024, como porcentaje de adultos de 15 años o más: 59,3% tiene alguna cuenta, en un banco, financiera o billetera; 51,7% hizo o recibió un pago digital en el último año; 42,5% tiene una billetera de dinero móvil, como Yape o Plin, frente a 14,3% en 2021; 31,4% ahorró en un banco, financiera o billetera; y solo 27,9% paga sus servicios, como luz o teléfono, por celular o internet. Tener una cuenta no es usarla. Cerca de 1 de cada 10 adultos tiene billetera pero no cuenta bancaria (cálculo nuestro: 59,3% con alguna cuenta menos 49,8% con cuenta bancaria); McKinsey reporta que en 2023 Yape tenía 2,6 millones de usuarios sin cuenta bancaria previa (Craddock et al., 2023). 17,5% de los adultos no tiene cuenta y menciona la desconfianza en las instituciones financieras entre sus razones, frente a 5,7% en Brasil. A la derecha, la brecha por educación, con la ENAHO del INEI (cuarto trimestre de 2024, adultos de 18 años o más, cuentas de ahorro, sueldo, plazo fijo o corrientes): tiene cuenta 35,9% de quienes llegaron hasta primaria, 51,8% con secundaria, 75,1% con superior no universitaria y 84,7% con superior universitaria (INEI, 2025). Por ingreso del hogar, según el Findex, tiene alguna cuenta 44,6% del 40% de menores ingresos, que equivale aproximadamente al NSE E y al tercio inferior del NSE D, frente a 69,1% del 60% restante. Ojo: el INEI y el Findex miden cuentas de forma distinta, por eso sus totales no coinciden. Lectura nuestra: la billetera abrió la puerta, pero usar el sistema para pagar y ahorrar sigue atado a la educación y al ingreso.</aside>
</section>
'''
# ===== Lámina 2: riesgo y seguros
seg=[("Familia",39.4,W,'#0F0F0E'),("Sus ahorros",17.8,'#BDBCB6','#0F0F0E'),("Trabajar más",15.5,'#8C8B85','#0F0F0E'),("Préstamo",9.8,'#5E5D59',W),("Vender algo",5.7,'#45443F',W),("No podría",9.8,'#33322F',W)]
Wst=1664; x=0; rects=f'<rect x="0" y="0" width="{Wst}" height="60" fill="#1F1F1D"/>'; labs=''
tot=100.0
for n,v,c,tc in seg:
    w=v/tot*Wst
    rects+=f'<rect x="{x:.1f}" y="0" width="{w-4:.1f}" height="60" fill="{c}"/>'
    x+=w
legend=''.join(f'<p class="txt" style="display:flex;align-items:center;gap:10px"><svg width="22" height="22" aria-hidden="true"><rect width="22" height="22" fill="{c}" stroke="#5E5D59" stroke-width="1"/></svg>{n} <b>{f(v)}</b></p>' for n,v,c,_ in seg)
fam=[("Sexo","Hombres",32.2,"Mujeres",46.5),("Educación","Secundaria o más",38.1,"Primaria o menos",44.0),("Ingreso del hogar","60% de mayores",36.4,"40% de menores",43.9),("Trabajo","Trabaja o busca",36.1,"No trabaja",46.9)]
seg_ins=[("Sexo","Mujeres",7.2,"Hombres",13.4),("Educación","Primaria o menos",3.5,"Secundaria o más",11.9),("Ingreso del hogar","40% de menores",3.8,"60% de mayores",14.5),("Trabajo","No trabaja",2.4,"Trabaja o busca",13.6)]
def table2():
    groups=[("Sexo",[("Hombres",32.2,13.4),("Mujeres",46.5,7.2)]),("Educación",[("Secundaria o más",38.1,11.9),("Primaria o menos",44.0,3.5)]),("Ingreso",[("60% de mayores ingresos",36.4,14.5),("40% de menores ingresos",43.9,3.8)]),("Trabajo",[("Trabaja o busca",36.1,13.6),("No trabaja",46.9,2.4)])]
    BW=400
    def cell(v,scale,c):
        return (f'<div style="display:flex;align-items:center;gap:14px"><svg width="{BW}" height="18" viewBox="0 0 {BW} 18" aria-hidden="true"><rect width="{BW}" height="18" fill="{TR}"/><rect width="{v/scale*BW:.1f}" height="18" fill="{c}"/></svg><p class="txt" style="width:80px;font-weight:700">{f(v)}</p></div>')
    h=('<div style="display:grid;grid-template-columns:170px 360px 1fr 1fr;column-gap:24px;row-gap:2px;align-items:center;margin-top:6px">'
       '<p class="k"></p><p class="k"></p><p class="k">Familia primero · 39,4%</p><p class="k">Paga un seguro · 10,2%</p>')
    for g,rows in groups:
        for i,(lab,a,b) in enumerate(rows):
            top='border-top:2px solid #3A3A36;padding-top:6px;' if i==0 else ''
            gl=f'<p class="dim" style="{top}">{g}</p>' if i==0 else '<p class="dim"></p>'
            h+=gl+f'<p class="txt" style="{top}">{lab}</p><div style="{top}">{cell(a,60,W)}</div><div style="{top}">{cell(b,20,W)}</div>'
    return h+'</div>'
def grid(rows,scale):
    return ''.join(pairrow(*r,scale=scale) for r in rows)
T2=table2()
s2=f'''<section id="comp-riesgo" data-transition="fade">
<h2 class="t">La familia es la aseguradora</h2>
<p class="k">Ante una emergencia, ¿de dónde sacaría el dinero en 30 días? · Principal fuente, adultos peruanos</p>
<svg style="flex-shrink:0" width="{Wst}" height="56" viewBox="0 0 {Wst} 60" preserveAspectRatio="none" aria-label="Barra apilada: principal fuente de dinero ante una emergencia">{rects}</svg>
<div style="display:flex;gap:26px;flex-wrap:wrap">{legend}</div>
{T2}
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Quien más depende de la familia es quien menos se asegura.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, adultos de 15+ · Otra respuesta: 2,0% · Escalas: 0-60% y 0-20%</p>
<p class="foot">Dónde está Perú · Comportamiento · 2 / 3</p>
<aside>Qué decir: esta lámina describe cómo enfrenta el riesgo el peruano. La pregunta del Global Findex es: si tuviera una emergencia y necesitara una suma importante en 30 días, ¿cuál sería su principal fuente de dinero? En Perú, 39,4% acudiría primero a su familia o amigos; 17,8% usaría sus ahorros; 15,5% trabajaría más; 9,8% pediría un préstamo a un banco, su empleador o un prestamista; 5,7% vendería algo; y 9,8% no podría conseguirlo; el resto da otra respuesta (Banco Mundial, 2025, datos de 2024). Abajo, dos comparaciones con los mismos cuatro cortes. Familia primero: mujeres 46,5% frente a hombres 32,2%; primaria o menos 44,0% frente a secundaria o más 38,1%; 40% de menores ingresos del hogar, que equivale aproximadamente al NSE E y al tercio inferior del NSE D, 43,9% frente a 36,4% del 60% de mayores ingresos; y quienes no trabajan ni buscan trabajo 46,9% frente a 36,1% de quienes trabajan o buscan. Paga con regularidad un seguro: hombres 13,4% frente a mujeres 7,2%; secundaria o más 11,9% frente a primaria o menos 3,5%; 60% de mayores ingresos 14,5% frente a 3,8% del 40% de menores; quienes trabajan o buscan 13,6% frente a 2,4% de quienes no trabajan. El Findex solo publica dos niveles de educación; para ver más niveles hay que trabajar sus microdatos. En la región, la familia también va primero en Colombia (45,1%), Ecuador (43,0%) y Argentina (39,3%); en Brasil la primera opción es trabajar más (31,5%) y en Uruguay un préstamo (27,4%, datos de 2021). Y la categoría arrastra poca confianza: en un ranking de experiencia del cliente con 20 industrias en Perú, los seguros quedaron últimos (Centrum PUCP, 2022, citado en Craddock et al., 2023). Lectura nuestra: quien más depende de la familia es quien menos se asegura; el seguro compite con la familia, y puede funcionar mejor diseñarlo para comprarse, pagarse o proteger en familia.</aside>
</section>
'''
# ===== Lámina 3: digital
rows=[("Tiene billetera",14.3,42.5),("Ahorra en el sistema",15.3,31.4),("Paga con celular en tienda",21.3,32.5),("Paga servicios en línea",19.7,27.9),("Familia primero",42.0,39.4)]
Wd=440; SC=50
def dumb(label,a,b,bold=False):
    xa=a/SC*Wd; xb=b/SC*Wd; lo,hi=sorted([xa,xb]); ch=b-a
    chs=("+" if ch>0 else "−")+f(abs(ch))
    return (f'<div style="display:flex;align-items:center;gap:20px"><p class="txt" style="width:400px{";font-weight:700" if bold else ""}">{label}</p>'
            f'<svg width="{Wd}" height="30" viewBox="0 0 {Wd} 30" aria-hidden="true"><line x1="0" y1="15" x2="{Wd}" y2="15" stroke="#3A3A36" stroke-width="2"/>'
            f'<line x1="{lo:.1f}" y1="15" x2="{hi:.1f}" y2="15" stroke="{W}" stroke-width="4"/><circle cx="{xa:.1f}" cy="15" r="9" fill="#0F0F0E" stroke="#BDBCB6" stroke-width="3"/><circle cx="{xb:.1f}" cy="15" r="11" fill="{W}"/></svg>'
            f'<p class="txt" style="width:290px"><b>{chs}</b> <span style="color:#A3A29C">{f(a)} → {f(b)}</span></p></div>')
axis=(f'<div style="display:flex;gap:20px"><p class="txt" style="width:400px"></p><div style="width:{Wd}px;display:flex;justify-content:space-between">'
      + ''.join(f'<p class="dim">{t}%</p>' for t in (0,25,50)) + '</div></div>')
s3=f'''<section id="comp-digital" data-transition="fade">
<h2 class="t">Lo digital cambia rápido</h2>
<div class="row" style="gap:72px">
<div style="width:1190px;display:flex;flex-direction:column;gap:12px">
<p class="k">Adultos peruanos · ○ 2021 → ● 2024 · cambio en puntos</p>
{''.join(dumb(*r) for r in rows[:4])}
<div style="border-top:2px solid #3A3A36;padding-top:10px">{dumb(*rows[4],bold=True)}</div>
{axis}
<div style="display:flex;gap:48px;margin-top:8px">
<div class="stat" style="width:560px"><p class="mid">51,7%</p><p class="dim">paga en digital. Chile, Brasil, Argentina y Uruguay: 68% a 84%.</p></div>
<div class="stat" style="width:560px"><p class="mid">67% → 21%</p><p class="dim">cotiza seguros en digital → compra la póliza en línea.</p></div>
</div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:14px">
<p class="k">En la app de seguros</p>
<div class="card"><p class="txt"><b>Consultan</b></p><p class="dim">su ahorro, su cobertura, la clínica que les toca</p></div>
<div class="card"><p class="txt"><b>Pagan afuera</b></p><p class="dim">en su banco o con débito automático</p></div>
<div class="card"><p class="txt"><b>Lo urgente, por WhatsApp</b></p><p class="dim">«alguien respondiendo es la mejor opción»</p></div>
</div>
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Los hábitos digitales siguen a la infraestructura. La app gana consultando, no cobrando.</p></div>
<p class="src">Banco Mundial (2025), Global Findex · APESEG (2023) · RIMAC (2026c), dos entrevistas · Chile y Uruguay: 2021</p>
<p class="foot">Dónde está Perú · Comportamiento · 3 / 3</p>
<aside>Qué decir: esta lámina describe la digitalización del peruano y qué tan rápido cambia. Izquierda: el mismo hábito en 2021 (círculo vacío) y en 2024 (círculo lleno), según el Global Findex del Banco Mundial, en porcentaje de adultos. Tener billetera pasó de 14,3% a 42,5% (+28,2 puntos); ahorrar en un banco, financiera o billetera, de 15,3% a 31,4%; pagar con celular o tarjeta en una tienda, de 21,3% a 32,5%; pagar servicios en línea, de 19,7% a 27,9%. En cambio, acudir primero a la familia ante una emergencia apenas bajó, de 42,0% a 39,4%. Los hábitos digitales cambiaron en tres años, con Yape y la interoperabilidad entre billeteras; la red familiar casi no se movió. En la región, 51,7% de los peruanos paga en digital, frente a 68% a 84% en Chile, Brasil, Argentina y Uruguay, los países con más empleo formal, más cuentas y mejores instituciones. En seguros, 67% prefiere buscar y cotizar en digital, pero solo 21% compra la póliza en línea (APESEG, 2023). Derecha: lo que vimos en dos entrevistas a usuarias de apps de aseguradoras. Entran a la app para consultar su ahorro (Mapfre), su cobertura o qué clínica les corresponde (RIMAC); pagan desde su banco o con débito automático; y resuelven lo urgente con una llamada y un enlace por WhatsApp, como el reporte de un choque en menos de 10 minutos. Son dos personas: ilustran motivos, no frecuencias. Lectura nuestra: los hábitos digitales siguen a la infraestructura, así que TAPP, la plataforma de pagos inmediatos prevista para 2027, puede acelerar el cobro digital; la red familiar cambia lento y hay que diseñar para ella.</aside>
</section>
'''
for n,s in [('comp-banca',s1),('comp-riesgo',s2),('comp-digital',s3)]:
    open(os.path.join(D,n+'.html'),'w').write(s)
