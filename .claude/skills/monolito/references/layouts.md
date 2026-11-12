# Plantillas de láminas monolito

Todas las plantillas siguen el formato del tipo «Slides»: un único `<section id="…">` por archivo, estilos en
línea, lienzo de 1920×1080. Reemplaza lo que está entre `[corchetes]`. El pie `[Parte N · Nombre · NN / TT]` va en
todas las láminas menos la portada.

## Estilo base de una sección

```
background:#0E0B14;color:#B9A2FF;font-family:'Space Mono', 'Courier New', monospace;padding:128px 128px 160px;display:flex;flex-direction:column;gap:48px
```

- Título de lámina: `<h2 style="font-family:'Archivo Black', Arial, sans-serif;font-size:80px;font-weight:400;line-height:1.0;text-transform:uppercase">`
- Pie: `<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#8F7CC9;text-transform:uppercase;letter-spacing:2px">[Parte N · Nombre · NN / TT]</p>`
- Notas: `<aside>[Qué decir. Fuentes completas. Puente: frase que abre la siguiente lámina.]</aside>` como último hijo.

## `deck.json` de ejemplo

```json
{"v":4,"createdOnFiles":{"v":1,"at":"[AAAA-MM-DDTHH:MM:SSZ]"},"lists":"css","title":"[Nombre del deck]","cover":"cover",
 "order":["cover","[id-2]","[id-3]"],
 "sections":{"s1":{"description":"Parte 1 · [Nombre]: [una frase]","start":"cover"},"s2":{"description":"Parte 2 · [Nombre]: [una frase]","start":"[id]"}},
 "faces":{"archivo-black":{"family":"Archivo Black","href":"https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap"},
          "space-mono":{"family":"Space Mono","href":"https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap"}},
 "designSystems":[]}
```

## Portada

```html
<section id="cover" data-transition="fade" style="background:#0E0B14;color:#B9A2FF;font-family:'Space Mono', 'Courier New', monospace;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:space-between;gap:48px">
<p style="font-size:24px;color:#8F7CC9;text-transform:uppercase;letter-spacing:4px">[Tipo de documento · fecha]</p>
<div style="display:flex;flex-direction:column;gap:40px">
<hr style="border-top:8px solid #B9A2FF;width:1664px">
<h1 style="font-family:'Archivo Black', Arial, sans-serif;font-size:200px;font-weight:400;line-height:0.95;text-transform:uppercase">[Dos<br>palabras]</h1>
<hr style="border-top:8px solid #B9A2FF;width:1664px">
</div>
<p style="font-size:30px;line-height:1.4;width:1664px">[La promesa del documento en una o dos frases.]</p>
<aside>[El hilo en partes, dicho en una línea cada una.]</aside>
</section>
```

## Enunciado (idea fuerza)

Fondo secundario, contenido centrado verticalmente. Título de 130-150 px y no más de diez palabras.

```html
<section id="[id]" data-transition="fade" style="background:#17121F;color:#B9A2FF;font-family:'Space Mono', 'Courier New', monospace;padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:44px">
<h1 style="font-family:'Archivo Black', Arial, sans-serif;font-size:150px;font-weight:400;line-height:1.0;text-transform:uppercase">[Frase fuerza.]</h1>
<p style="font-size:30px;line-height:1.4;width:1600px">[Lo que la explica, en una o dos frases.]</p>
[pie] [notas]
</section>
```

Variante con definición: suma un bloque con regla izquierda.
`<div style="display:flex;flex-direction:column;gap:8px;border-left:8px solid #B9A2FF;padding:0px 0px 0px 32px"><p style="font-size:26px;line-height:1.4;color:#8F7CC9"><b>[Término]</b> [definición].</p></div>`

## Dos columnas

```html
<div style="display:flex;gap:64px">
<div style="flex:1;display:flex;flex-direction:column;gap:16px;border-top:8px solid #B9A2FF;padding:24px 0px 0px 0px">
<h3 style="font-size:32px;font-weight:700">[Columna A]</h3>
<ul style="font-size:26px;line-height:1.45"><li>[…]</li><li>[…]</li></ul>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;border-top:8px solid #B9A2FF;padding:24px 0px 0px 0px">
<h3 style="font-size:32px;font-weight:700">[Columna B]</h3>
<ul style="font-size:26px;line-height:1.45"><li>[…]</li><li>[…]</li></ul>
</div>
</div>
<p style="font-size:32px;line-height:1.4;font-weight:700;width:1600px">[Conclusión en una frase.]</p>
```

## Tabla

Hasta 8 filas a 24 px si cada celda cabe en una línea; con celdas de dos líneas, hasta 6.

```html
<table style="font-family:'Space Mono', 'Courier New', monospace;font-size:24px;color:#B9A2FF;border:2px solid #B9A2FF">
<tr><th style="width:30%;text-align:left">[Columna 1]</th><th style="width:70%;text-align:left">[Columna 2]</th></tr>
<tr><td><b>[Rótulo]</b></td><td>[Texto]</td></tr>
</table>
```

Para marcar filas con los íconos del deck, usa los caracteres `○ □ △` al inicio del rótulo.

## Grilla de tarjetas (2×4 o 3×2)

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px">
<div style="display:flex;flex-direction:column;gap:8px;border-top:4px solid #B9A2FF;padding:16px 0px 0px 0px"><h3 style="font-size:28px;font-weight:700">01 · [Rótulo]</h3><p style="font-size:24px;line-height:1.35;color:#8F7CC9">[Una frase.]</p></div>
[… repetir]
</div>
```

## Cifras grandes (tres)

```html
<div style="display:flex;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;gap:8px;border-top:8px solid #B9A2FF;padding:20px 0px 0px 0px"><p style="font-family:'Archivo Black', Arial, sans-serif;font-size:88px;line-height:1.0">[19,9 M]</p><p style="font-size:24px;line-height:1.35;color:#8F7CC9">[qué significa la cifra]</p></div>
[… dos más]
</div>
```

Máximo 7 caracteres por cifra (columnas de 520 px a 88 px). La fuente va en el pie o en las notas.

## Tres figuras en fila (íconos con significado)

```html
<div style="display:flex;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<svg aria-label="Círculo: [qué representa]" width="110" height="110" viewBox="0 0 110 110"><circle cx="55" cy="55" r="47" fill="none" stroke="#B9A2FF" stroke-width="8"/></svg>
<h3 style="font-size:30px;font-weight:700">[Rótulo]</h3><p style="font-size:24px;line-height:1.35;color:#8F7CC9">[Frase]</p>
</div>
<!-- cuadrado: <rect x="8" y="8" width="94" height="94" …/> · triángulo: <polygon points="55,8 102,100 8,100" …/> -->
</div>
```

## Punto en cuadrado (lo medido frente a lo que importa)

```html
<div style="display:flex;gap:80px;align-items:center">
<svg aria-label="[Descripción]" width="340" height="340" viewBox="0 0 340 340"><rect x="8" y="8" width="324" height="324" fill="none" stroke="#B9A2FF" stroke-width="8"/><circle cx="252" cy="252" r="22" fill="#B9A2FF"/></svg>
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:8px"><h3 style="font-size:30px;font-weight:700">● [Lo pequeño]</h3><p style="font-size:24px;line-height:1.4;color:#8F7CC9">[…]</p></div>
<div style="display:flex;flex-direction:column;gap:8px"><h3 style="font-size:30px;font-weight:700">□ [Lo grande]</h3><p style="font-size:24px;line-height:1.4;color:#8F7CC9">[…]</p></div>
</div>
</div>
```

## Diapositiva acento

Fondo `#B9A2FF`, texto y reglas `#0E0B14`, pie también en `#0E0B14`. Úsala para abrir la parte central del
argumento. Puede llevar una figura central generada con `--color "#0E0B14" --tenue "#0E0B14"`.

## Figuras centrales (triángulo, cuadrado, círculo, rombo)

Genera el bloque con `scripts/figuras.py` y pégalo después del `<h2>`. Ejemplos ya publicados en el deck
«El diseño conductual ha muerto. Larga vida al diseño conductual.»:

- **Cuadrado:** lámina «Lo que ya hacemos» (cuatro proyectos, cuatro tipos de efecto, «Más que conducta» al
  centro, una frase de cierre centrada en y=800).
- **Círculo de 4 pasos:** lámina «La conducta se mueve» (cambia → se apaga → vuelve → se resiste; «Trayectorias,
  no momentos» al centro).
- **Rombo:** lámina «Seis capas de la conducta» sobre fondo acento («El nuevo diseño conductual» dentro del rombo;
  persona, entorno y sistema en la base, con sus íconos ○ □ △).

Reglas de las figuras centrales:

- El título va en una línea; la figura empieza en y≈240 y nada pasa de y=920.
- Dentro de la figura, una o dos palabras (26-30 px, negrita). Si no caben, la idea no está bien nombrada.
- Cada etiqueta: rótulo corto (36 px Archivo Black o 30 px mono en negrita) + una frase de 24 px en tono tenue.
- Respeta los largos máximos que imprime el script. En el círculo de 5 o 6 pasos, cada frase debe tener 90
  caracteres o menos.
- Una frase de cierre opcional va centrada debajo (y≈800) solo en el cuadrado; en el círculo y el triángulo no hay
  espacio.

## Grilla con habilitador transversal

Cuando una idea no es una más de la lista sino que atraviesa a todas (un habilitador, una condición previa), va
fuera de la grilla: en una franja de ancho completo, debajo, con fondo acento (`#B9A2FF`, texto `#0E0B14`), un rótulo
«Habilitador transversal» y una frase que diga qué habilita. Ejemplo: lámina «Ocho preguntas» (siete describen el
entorno; la octava, «¿Se puede experimentar?», decide el método).

## Referencias (anexo)

Última lámina del deck. Dos columnas de bloques, uno por parte: rótulo de 24 px en negrita y mayúsculas, y debajo las
citas cortas (autor y año) separadas por « · », a 24 px con `line-height:1.2` en tono tenue. Al final, un bloque de
«Fuentes internas». Si no cabe, acorta con «et al.» antes que bajar de 24 px. La lista completa (título, revista,
rigor, enlace) va en un documento aparte junto al deck (en el repo de origen:
`research/_outputs/referencias-<deck>.md`, generado desde el registro de fuentes por ID). Ejemplo en
`ejemplo/slides/referencias.html`.

## Manifiesto (cierre)

```html
<section id="manifiesto" data-transition="fade" style="background:#17121F;color:#B9A2FF;font-family:'Space Mono', 'Courier New', monospace;padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">
<h2 style="…título…">Manifiesto</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
<div style="display:flex;flex-direction:column;gap:8px;border-top:4px solid #B9A2FF;padding:16px 0px 0px 0px"><p style="font-size:24px;color:#8F7CC9">01</p><p style="font-size:28px;line-height:1.3;font-weight:700">[Principio en una frase.]</p></div>
[… hasta 06]
</div>
<div style="display:flex;flex-direction:column;gap:8px;border-left:8px solid #B9A2FF;padding:0px 0px 0px 32px">
<p style="font-size:28px;line-height:1.35"><b>Nuestro propósito:</b> [una o dos frases].</p>
</div>
[pie] [notas]
</section>
```

## Que el texto quepa

- Zona útil: 1664 × 792 px con pie (y de 128 a 920).
- Ancho de carácter: Space Mono ≈ 0,6 × tamaño (24 px → 14,4 px; 28 px → 16,8 px); en negrita, +5 %. Archivo Black
  en mayúsculas ≈ 0,8 × tamaño (80 px → unos 22 caracteres por línea en 1664 px).
- Alto de una línea: tamaño × interlineado (24 px × 1,4 ≈ 34 px). Título de 80 px: 88 px por línea.
- Fila de tabla ≈ 2,1 × tamaño por línea de texto (24 px → unos 50 px por línea; celda de dos líneas ≈ 100 px).
- Suma los altos y los `gap` del `section` antes de publicar. Si pasa de 792 px, acorta el texto o divide la
  lámina: nada se encoge.
