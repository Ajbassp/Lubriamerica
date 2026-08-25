# Assets

| Archivo | Estado |
|---|---|
| `plantilla-carrusel.html` | Listo. Slide interior (numeral + desmentido). |
| `plantilla-portada.html` | Listo. Portada (numeral dentro del titular + remate). |
| `render.sh` | Listo. Exporta a PNG. |
| `fonts/Montserrat*.ttf` | Provisional. Ver abajo. |
| `logo/marca.svg` | **Falta.** Ver abajo. |

## Falta: el engranaje del logo

Las plantillas dibujan un engranaje genérico en SVG como marca de agua. Hay que
reemplazarlo por el del logotipo real:

1. Guardar el engranaje solo (sin gota ni texto) como `logo/marca.svg`, en blanco plano.
2. En las plantillas, cambiar el bloque `<div class="marca">…</div>` por
   `<div class="marca"><img src="logo/marca.svg" alt=""></div>`.

Guardar también el logotipo completo como `logo/lubriamerica.svg` para las piezas que
sí lo llevan (anuncios, portadas de catálogo). En las placas de carrusel no va.

## Provisional: la tipografía

`Montserrat` (SIL OFL, incluida) es un sustituto cercano de la fuente de las piezas
originales, no la fuente real. Si la marca tiene una licenciada, poner el archivo en
`fonts/` y cambiar el `@font-face` de las plantillas. Las medidas del sistema están
calibradas para el peso 800 de Montserrat; con otra fuente hay que revisar que el
titular siga cerrando en 3 líneas.

## Fotos

No se versionan aquí. La foto de cada placa entra por `<img src="...">` dentro de
`.foto` y hay que borrarle la clase `vacia` al contenedor.
