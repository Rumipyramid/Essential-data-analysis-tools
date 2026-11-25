import sys
OUT=sys.argv[1]
N={'PER':'Perú','ECU':'Ecuador','COL':'Colombia','BOL':'Bolivia','PRY':'Paraguay','ARG':'Argentina','BRA':'Brasil','CHL':'Chile','URY':'Uruguay'}
old={'CHL','URY'}
groups=[
 ('Uso del seguro',[
  ('Voluntario + SOAT, % PBI',{'BRA':3.3,'CHL':2.8,'ARG':2.3,'COL':2.2,'ECU':1.8,'PER':1.7,'BOL':1.6,'URY':1.5,'PRY':1.2},'%',set()),
  ('Paga un seguro, % adultos',{'ARG':22.4,'BRA':13.9,'PER':10.2,'PRY':8.0,'BOL':6.9,'ECU':5.0,'COL':4.4},'%',set()),
 ]),
 ('Hábitos digitales',[
  ('Pago digital, % adultos',{'CHL':84.3,'BRA':77.4,'ARG':72.2,'URY':68.0,'PRY':55.5,'PER':51.7,'COL':49.2,'BOL':43.6,'ECU':43.3},'%',old),
  ('Billetera móvil, % adultos',{'BRA':58.2,'ARG':56.7,'PER':42.5,'COL':39.1,'PRY':35.9,'BOL':20.0,'ECU':10.1},'%',set()),
 ]),
 ('Ante una emergencia',[
  ('Familia primero, % adultos',{'COL':45.1,'ECU':43.0,'PER':39.4,'ARG':39.3,'CHL':33.4,'PRY':28.8,'BOL':28.1,'URY':27.1,'BRA':26.2},'%',old),
 ]),
]
W=800;H=69;X0=24;X1=W-24;Y=49
def fmt(v): return (f"{v:.1f}").replace('.',',')
def row(name,d,unit,o):
    vals=sorted(d.values()); lo,hi=vals[0],vals[-1]; pad=(hi-lo)*0.04
    sx=lambda v: X0+(v-lo+pad)/(hi-lo+2*pad)*(X1-X0)
    n=len(vals); med=vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2
    rank=sorted(d,key=lambda c:-d[c]).index('PER')+1
    top=max(d,key=d.get)
    svg=[f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="#4A4A45" stroke-width="2"/>',
         f'<line x1="{sx(med):.1f}" y1="{Y-16}" x2="{sx(med):.1f}" y2="{Y+16}" stroke="#A3A29C" stroke-width="3"/>']
    for c,v in sorted(d.items(),key=lambda x:x[0]=='PER'):
        if c=='PER': continue
        dash=' stroke-dasharray="4 4"' if c in o else ''
        svg.append(f'<circle cx="{sx(v):.1f}" cy="{Y}" r="10" fill="#2A2A27" stroke="#A3A29C" stroke-width="3"{dash}/>')
    px=sx(d['PER'])
    svg.append(f'<circle cx="{px:.1f}" cy="{Y}" r="14" fill="#ECEBE6" stroke="#0F0F0E" stroke-width="3"/>')
    lw=200; left=min(max(px-lw/2,0),W-lw)
    return f'''<div style="display:flex;flex-direction:row;align-items:center;gap:32px">
<p class="txt" style="width:460px">{name}</p>
<div class="host" style="width:{W}px;height:{H}px">
<svg aria-label="{name}: Perú {fmt(d['PER'])}, puesto {rank} de {n}" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{''.join(svg)}</svg>
<p class="labpe" style="left:{left:.0f}px;top:-4px;width:{lw}px;text-align:center">PERÚ {fmt(d['PER'])}{unit}</p>
</div>
<div style="width:330px;display:flex;flex-direction:column;gap:0px"><p class="txt" style="font-weight:700">{rank}.º de {n}</p><p class="dim">Máx.: {N[top]}, {fmt(d[top])}{unit}</p></div>
</div>'''
body=[]
for gi,(g,rows) in enumerate(groups):
    leg='<p class="dim" style="font-size:24px">● Perú&nbsp;&nbsp;○ otro país&nbsp;&nbsp;┃ mediana&nbsp;&nbsp;◌ punteado: 2021</p>' if gi==0 else ''
    body.append(f'<div style="display:flex;flex-direction:column;gap:0px;border-top:4px solid #ECEBE6;padding-top:6px"><div style="display:flex;justify-content:space-between"><p class="k">{g}</p>{leg}</div>'+''.join(row(*r) for r in rows)+'</div>')
html=f'''<section id="peru-seguro-digital" data-transition="fade">
<h2 class="t">Billetera sí, seguro aún no</h2>
<div style="display:flex;flex-direction:column;gap:8px">
{''.join(body)}
</div>
<div class="spacer"></div>
<div class="strip"><p class="txt"><b>LECTURA NUESTRA</b> · Perú es 3.º en billetera y en pagar un seguro, pero 6.º en penetración y en pago digital, y de los que más acude a la familia. El canal existe; el seguro aún no entra por él.</p></div>
<p class="src">Banco Mundial (2025), Global Findex, datos de 2024 · MAPFRE Economics (2025) · ◌ Chile y Uruguay: 2021</p>
<p class="foot">Dónde está Perú · Propuesta</p>
<aside>Qué decir: esta lámina condensa dónde está Perú frente a los otros ocho países de Sudamérica con datos comparables, en cinco indicadores agrupados en tres bloques. Cada línea es un indicador; cada punto, un país; el punto blanco es Perú; la raya vertical es la mediana de Sudamérica; los puntos punteados son Chile y Uruguay, con datos de 2021 porque no entraron en la encuesta de 2024. Uso del seguro: las primas de seguros voluntarios más el SOAT son 1,7% del PBI en Perú, sexto de nueve; Brasil tiene 3,3% (MAPFRE Economics, 2025). En cambio, 10,2% de los adultos peruanos paga con regularidad un seguro, tercero de siete con dato, detrás de Argentina (22,4%) y Brasil (13,9%) (Banco Mundial, 2025). Hábitos digitales: 51,7% hizo o recibió un pago digital, sexto de nueve, lejos de Chile (84,3%, 2021), Brasil (77,4%), Argentina (72,2%) y Uruguay (68,0%, 2021); pero 42,5% tiene una billetera de dinero móvil, tercero de siete, detrás de Brasil (58,2%) y Argentina (56,7%). Ante una emergencia: 39,4% acudiría primero a su familia o amigos, tercero de nueve, detrás de Colombia (45,1%) y Ecuador (43,0%); Brasil (26,2%) y Uruguay (27,1%) son los que menos. Lectura nuestra: Perú ya tiene el canal, porque la billetera es masiva, pero el seguro todavía no entra por él, y la familia sigue siendo la primera red ante un golpe. Por eso la oportunidad no es solo digitalizar la venta, sino diseñar seguros que convivan con esa red, por ejemplo seguros que un hijo paga para sus padres. Definiciones: «Voluntario + SOAT» son las primas de seguros sin las de seguridad social como % del PBI; «Paga un seguro» es el porcentaje de adultos que hace pagos regulares a un agente o compañía de seguros; «Pago digital» es haber hecho o recibido un pago digital en el último año; «Billetera móvil» es tener una cuenta de dinero móvil; «Familia primero» es decir que la familia o los amigos serían la principal fuente de dinero para una emergencia en 30 días. Nota: la penetración es un dato del mercado (MAPFRE Economics, 2025); los demás son de la encuesta Global Findex 2025 del Banco Mundial, con datos de 2024. Chile y Uruguay no tienen datos de billetera ni de pago de seguros.</aside>
</section>
'''
open(OUT,'w').write(html)
