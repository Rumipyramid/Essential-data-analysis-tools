#!/usr/bin/env python3
"""Genera el SVG y las cajas de etiqueta de las figuras centrales de un deck monolito.

Cada figura se imprime como HTML listo para pegar dentro de un <section> del tipo Slides
(lienzo de 1920x1080, márgenes de 128 px). Las etiquetas quedan con marcadores [..] para
reemplazar por el texto real. Solo stdlib.

Uso:
  python figuras.py circulo --pasos 4
  python figuras.py triangulo --modo tres
  python figuras.py triangulo --modo jerarquia --base 3
  python figuras.py rombo --base 3
  python figuras.py cuadrado
  Opciones comunes: --color "#B9A2FF" --tenue "#8F7CC9"
"""
import argparse
import math

IZQ, DER, ABAJO = 128, 1792, 920  # límites útiles del lienzo (margen y pie)


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def caja(left, top, width, align, titulo, texto, color_tenue, h3_style):
    a = f";text-align:{align}" if align != "left" else ""
    return (
        f'<div style="position:absolute;left:{round(left)}px;top:{round(top)}px;width:{round(width)}px;'
        f'display:flex;flex-direction:column;gap:6px">\n'
        f'<h3 style="{h3_style}{a}">{titulo}</h3>\n'
        f'<p style="font-size:24px;line-height:1.4;color:{color_tenue}{a}">{texto}</p>\n</div>'
    )


H3_GRANDE = "font-family:'Archivo Black', Arial, sans-serif;font-size:36px;font-weight:400;text-transform:uppercase"
H3_MONO = "font-size:30px;font-weight:700"


def circulo(n, color, tenue, cx=960, cy=600, r=160):
    """Ciclo de n pasos en sentido horario, empezando arriba."""
    lado = 2 * (r + 20)
    c = lado / 2
    left, top = cx - c, cy - c
    partes = [f'<circle cx="{f(c)}" cy="{f(c)}" r="{r}" fill="none" stroke="{color}" stroke-width="8"/>']
    nodos = []
    for k in range(n):
        th = math.radians(-90 + 360 * k / n)
        x, y = c + r * math.cos(th), c + r * math.sin(th)
        partes.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="14" fill="{color}"/>')
        nodos.append((th, cx + r * math.cos(th), cy + r * math.sin(th)))
        # flecha a mitad de camino hacia el paso siguiente
        tf = th + math.pi / n
        px, py = c + r * math.cos(tf), c + r * math.sin(tf)
        tx, ty = -math.sin(tf), math.cos(tf)          # tangente (sentido horario en pantalla)
        nx, ny = math.cos(tf), math.sin(tf)           # normal hacia afuera
        punta = (px + 14 * tx, py + 14 * ty)
        bx, by = px - 8 * tx, py - 8 * ty
        a1, a2 = (bx + 10 * nx, by + 10 * ny), (bx - 10 * nx, by - 10 * ny)
        pts = " ".join(f"{f(a)},{f(b)}" for a, b in (punta, a1, a2))
        partes.append(f'<polygon points="{pts}" fill="{color}"/>')
    svg = (
        f'<svg aria-label="Círculo con {n} pasos y flechas en sentido horario: un ciclo" '
        f'style="position:absolute;left:{round(left)}px;top:{round(top)}px;width:{round(lado)}px;height:{round(lado)}px" '
        f'width="{round(lado)}" height="{round(lado)}" viewBox="0 0 {round(lado)} {round(lado)}">' + "".join(partes) + "</svg>"
    )
    centro = (
        f'<p style="position:absolute;left:{round(cx - 140)}px;top:{round(cy - 38)}px;width:280px;'
        f'font-size:26px;line-height:1.25;font-weight:700;text-align:center">[Idea del ciclo, 2 líneas]</p>'
    )
    cajas = []
    for i, (th, x, y) in enumerate(nodos, 1):
        s, co = math.sin(th), math.cos(th)
        t = f"{i:02d} · [Paso {i}]"
        if s < -0.7:      # arriba
            cajas.append(caja(x - 400, y - 204, 800, "center", t, "[Una o dos frases, máx. ~150 caracteres]", tenue, H3_GRANDE))
        elif s > 0.7:     # abajo
            cajas.append(caja(x - 450, y + 30, 900, "center", t, "[Máx. ~120 caracteres: aquí queda poco alto]", tenue, H3_GRANDE))
        elif co > 0:      # derecha
            l = x + 40
            cajas.append(caja(l, y - 60, DER - l, "left", t, "[Máx. ~130 caracteres]", tenue, H3_GRANDE))
        else:             # izquierda
            cajas.append(caja(IZQ, y - 60, x - 40 - IZQ, "right", t, "[Máx. ~130 caracteres]", tenue, H3_GRANDE))
    return "\n".join([svg, centro] + cajas)


def triangulo_tres(color, tenue):
    """Tres ideas que se relacionan entre sí, con una palabra al centro."""
    svg = (
        f'<svg aria-label="Triángulo: tres ideas relacionadas" style="position:absolute;left:660px;top:250px;width:600px;height:560px" '
        f'width="600" height="560" viewBox="0 0 600 560"><polygon points="300,12 588,548 12,548" fill="none" stroke="{color}" stroke-width="8"/>'
        f'<circle cx="300" cy="12" r="12" fill="{color}"/><circle cx="12" cy="548" r="12" fill="{color}"/><circle cx="588" cy="548" r="12" fill="{color}"/></svg>'
    )
    centro = ('<p style="position:absolute;left:810px;top:600px;width:300px;font-size:26px;line-height:1.2;'
              'font-weight:700;text-align:center">[Lo que las une]</p>')
    return "\n".join([
        svg, centro,
        caja(1090, 250, 702, "left", "[Idea 1 · vértice superior]", "[Máx. ~140 caracteres]", tenue, H3_MONO),
        caja(128, 700, 500, "right", "[Idea 2 · base izquierda]", "[Máx. ~150 caracteres]", tenue, H3_MONO),
        caja(1292, 700, 500, "left", "[Idea 3 · base derecha]", "[Máx. ~150 caracteres]", tenue, H3_MONO),
    ])


def triangulo_jerarquia(n, color, tenue):
    """Una idea arriba que ordena varias ideas de la base (2 a 4)."""
    svg = (
        f'<svg aria-label="Triángulo: una idea en el vértice y {n} en la base" style="position:absolute;left:700px;top:240px;width:520px;height:440px" '
        f'width="520" height="440" viewBox="0 0 520 440"><polygon points="260,12 508,428 12,428" fill="none" stroke="{color}" stroke-width="8"/></svg>'
    )
    centro = ('<p style="position:absolute;left:810px;top:508px;width:300px;font-size:26px;line-height:1.2;'
              'font-weight:700;text-align:center">[Nombre de la idea que manda]</p>')
    cima = caja(1080, 236, 712, "left", "[Lo que la idea de arriba afirma]", "[Máx. ~140 caracteres]", tenue, H3_MONO)
    largo = {2: 150, 3: 100, 4: 70}[n]
    items = "\n".join(
        '<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
        f'<h3 style="font-size:30px;font-weight:700">[Base {i}]</h3>'
        f'<p style="font-size:24px;line-height:1.35;color:{tenue}">[Máx. ~{largo} caracteres]</p></div>'
        for i in range(1, n + 1)
    )
    base = (f'<div style="position:absolute;left:{IZQ}px;top:704px;width:{DER - IZQ}px;display:flex;flex-direction:row;gap:48px;'
            f'border-top:4px solid {color};padding:24px 0px 0px 0px">\n{items}\n</div>')
    return "\n".join([svg, centro, cima, base])


def rombo(n, color, tenue):
    """Un concepto general (rombo) que ordena varias partes de la base (2 a 4).

    Se prefiere al triángulo jerárquico cuando la base usa íconos ○ □ △: el rombo no se
    confunde con ninguna de las partes."""
    svg = (
        f'<svg aria-label="Rombo: un concepto general sobre {n} partes" style="position:absolute;left:760px;top:250px;width:400px;height:400px" '
        f'width="400" height="400" viewBox="0 0 400 400"><polygon points="200,8 392,200 200,392 8,200" fill="none" stroke="{color}" stroke-width="8"/></svg>'
    )
    centro = ('<p style="position:absolute;left:810px;top:419px;width:300px;font-size:26px;line-height:1.2;'
              'font-weight:700;text-align:center">[Concepto general, 2 líneas]</p>')
    cima = caja(1200, 250, 592, "left", "[Lo que el concepto afirma]", "[Máx. ~130 caracteres]", tenue, H3_MONO)
    largo = {2: 150, 3: 100, 4: 70}[n]
    items = "\n".join(
        '<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
        f'<h3 style="font-size:30px;font-weight:700">[Parte {i}]</h3>'
        f'<p style="font-size:24px;line-height:1.35;color:{tenue}">[Máx. ~{largo} caracteres]</p></div>'
        for i in range(1, n + 1)
    )
    base = (f'<div style="position:absolute;left:{IZQ}px;top:704px;width:{DER - IZQ}px;display:flex;flex-direction:row;gap:48px;'
            f'border-top:4px solid {color};padding:24px 0px 0px 0px">\n{items}\n</div>')
    return "\n".join([svg, centro, cima, base])


def cuadrado(color, tenue):
    """Cuatro ideas, una por esquina, con una palabra al centro."""
    svg = (
        f'<svg aria-label="Cuadrado con un punto en cada esquina: cuatro ideas" style="position:absolute;left:740px;top:280px;width:440px;height:440px" '
        f'width="440" height="440" viewBox="-20 -20 440 440"><rect x="0" y="0" width="400" height="400" fill="none" stroke="{color}" stroke-width="8"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="14" fill="{color}"/>' for x, y in ((0, 0), (400, 0), (0, 400), (400, 400)))
        + "</svg>"
    )
    centro = ('<p style="position:absolute;left:780px;top:476px;width:360px;font-size:30px;line-height:1.2;'
              'font-weight:700;text-align:center">[Lo que las une]</p>')

    def esquina(left, top, align, i):
        a = f";text-align:{align}" if align != "left" else ""
        return (f'<div style="position:absolute;left:{left}px;top:{top}px;width:590px;display:flex;flex-direction:column;gap:6px">\n'
                f'<p style="font-size:24px;color:{tenue};text-transform:uppercase;letter-spacing:2px{a}">[Etiqueta {i}]</p>\n'
                f'<h3 style="font-size:30px;font-weight:700{a}">[Idea {i}]</h3>\n'
                f'<p style="font-size:24px;line-height:1.4{a}">[Máx. ~120 caracteres]</p>\n</div>')
    return "\n".join([svg, centro, esquina(128, 262, "right", 1), esquina(1202, 262, "left", 2),
                      esquina(128, 584, "right", 3), esquina(1202, 584, "left", 4)])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("figura", choices=["circulo", "triangulo", "cuadrado", "rombo"])
    ap.add_argument("--pasos", type=int, default=4, help="círculo: número de pasos (3 a 6)")
    ap.add_argument("--modo", choices=["tres", "jerarquia"], default="tres", help="triángulo: tres ideas o jerarquía")
    ap.add_argument("--base", type=int, default=3, help="triángulo jerárquico o rombo: partes en la base (2 a 4)")
    ap.add_argument("--color", default="#B9A2FF")
    ap.add_argument("--tenue", default="#8F7CC9")
    a = ap.parse_args()
    if a.figura == "circulo":
        if not 3 <= a.pasos <= 6:
            ap.error("el círculo admite de 3 a 6 pasos; con más, el texto no cabe")
        print(circulo(a.pasos, a.color, a.tenue))
    elif a.figura == "triangulo":
        if a.modo == "tres":
            print(triangulo_tres(a.color, a.tenue))
        else:
            if not 2 <= a.base <= 4:
                ap.error("la base admite de 2 a 4 ideas")
            print(triangulo_jerarquia(a.base, a.color, a.tenue))
    elif a.figura == "rombo":
        if not 2 <= a.base <= 4:
            ap.error("la base admite de 2 a 4 partes")
        print(rombo(a.base, a.color, a.tenue))
    else:
        print(cuadrado(a.color, a.tenue))


if __name__ == "__main__":
    main()
