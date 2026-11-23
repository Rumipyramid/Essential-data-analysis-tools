# Fuentes y verificación de los tres gráficos

Verificación hecha el 23 de noviembre de 2026. Se volvieron a descargar las fuentes y se comparó cada cifra del gráfico con la fuente: 157 cifras revisadas, 0 diferencias.

## 1. Informalidad y penetración de seguros (`cuadrantes.svg` / `.png`)

| Dato | Fuente | Año del dato |
|---|---|---|
| Formalidad (eje X) = 100 − tasa de empleo informal | OIT, ILOSTAT, indicador EMP_NIFL_SEX_RT (ambos sexos), consultado en rplumber.ilo.org | 2025 |
| Penetración sin primas de la seguridad social (eje Y) | MAPFRE Economics (2025), *El mercado asegurador latinoamericano en 2024*, cuadro de penetración ajustada | 2024 |
| Gasto en seguros por habitante (tamaño) | MAPFRE Economics (2025), mismo informe, cuadro de densidad | 2024 |
| Promedio de América Latina, 2,7% del PBI | MAPFRE Economics (2025), mismo informe | 2024 |

Cifras: Perú 70,5% informal / 1,7% / US$ 173; Bolivia 85,6 / 1,6 / 63; Ecuador 68,5 / 1,8 / 124; Paraguay 64,5 / 1,2 / 78; Colombia 56,0 / 2,2 / 261; México 56,9 / 2,6 / 383; Argentina 52,8 / 2,3 / 418; Brasil 35,6 / 3,3 / 338; Uruguay 32,7 / 1,5 / 853; Chile 26,4 / 2,8 / 762.

Ojo: las cifras de informalidad de ILOSTAT difieren de las del *Panorama Laboral* de la OIT que cita la prensa (por ejemplo, Uruguay 32,7% frente a 22,2%), porque se calculan sobre bases distintas. En el gráfico se usa ILOSTAT, porque da la serie de todos los países desde una misma base de datos.

## 2. Conductas de digitalización (`digitalizacion.svg` / `.png`)

| Dato | Fuente | Año del dato |
|---|---|---|
| Tiene una cuenta | Banco Mundial (2025), Global Findex Database 2025, FX.OWN.TOTL.ZS (igual a account.t.d) | 2024 |
| Hizo o recibió un pago digital | Banco Mundial (2025), Global Findex Database 2025, g20.any | 2024; Chile y Uruguay, 2021 (último disponible) |

Consultado en api.worldbank.org.

## 3. Parámetros de conducta financiera (`matriz-conducta.svg` / `.png`)

Fuente: Banco Mundial (2025), Global Findex Database 2025, datos de 2024, api.worldbank.org.

| Fila del gráfico | Código |
|---|---|
| Ahorró dinero en el último año | save.any.t.d |
| Ahorró en un banco, financiera o billetera | fin17a.17a1.d |
| Pidió prestado a familiares o amigos | fin22b |
| Pidió prestado para gastos de salud | fin22d |
| En una emergencia, recurriría a la familia | fin24fam |
| En una emergencia, usaría sus ahorros | fin24sav |
| Lo que más le preocupa: gastos médicos graves | fin45c |
| Lo que más le preocupa: dinero para la vejez | fin45a |
| Paga con regularidad a una aseguradora | fin19 |

Las 90 celdas del gráfico coinciden con la fuente. La distancia es un cálculo propio: cada indicador se estandariza con los 20 países que tienen los nueve datos, y la distancia es la raíz del promedio de las nueve diferencias al cuadrado respecto de Perú.

Los datos descargados están en `research_notes/Valor digital aseguradoras Sudamérica Perú/datos_findex_ilostat/`.
