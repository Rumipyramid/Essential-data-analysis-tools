# Monolito: presentaciones brutalistas que argumentan

Skill para Claude que construye decks de manifiesto o propuesta: fondo casi negro, texto violeta, Archivo Black y
Space Mono, un hilo narrativo que empieza por el problema, redacción de experto, evidencia citada y láminas con una
figura central (triángulo, cuadrado, círculo o rombo).

## Cómo instalarla

- **Claude Code:** descomprime el archivo dentro de `~/.claude/skills/` (para todos tus proyectos) o de
  `.claude/skills/` (solo para un proyecto). Debe quedar `monolito/SKILL.md`. Después pide «una presentación
  brutalista» o escribe `/monolito`.
- **claude.ai:** súbela como skill personalizada desde la sección de skills de la configuración. Necesita la
  ejecución de código activada.
- **Desde el repositorio de origen:** `/plugin marketplace add Rumipyramid/Machine_Learning` y luego
  `/plugin install rumipyramid-skills@rumipyramid-machine-learning`.

## Qué necesita

- Python 3 para `scripts/figuras.py`, que dibuja las figuras centrales (solo biblioteca estándar).
- Para publicar el deck en línea, la herramienta de Artifacts con el tipo «Slides». Sin ella, la skill entrega un
  archivo HTML con una lámina de 1920×1080 por sección.

## Qué trae

| Archivo | Qué contiene |
|---|---|
| `SKILL.md` | El manual: proceso, sistema visual, formatos, figuras, publicación y revisión crítica |
| `references/layouts.md` | Plantillas HTML de cada formato y fórmulas para que el texto quepa |
| `references/narrativa.md` | Arco narrativo, frases puente, manifiesto y cómo rotular la evidencia |
| `references/redaccion.md` | Reglas para que cada lámina se entienda sola |
| `references/ejemplo/` | Ocho láminas reales del deck «El diseño conductual ha muerto. Larga vida al diseño conductual.» |
| `scripts/figuras.py` | Genera las figuras centrales con sus etiquetas ya posicionadas |
