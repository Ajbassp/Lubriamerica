# Assets

| Archivo | Estado |
|---|---|
| `placa.css` | Tokens y escala. Lo comparten todas las plantillas. |
| `plantilla-portada.html` | Portada: numeral dentro del titular + remate. |
| `plantilla-carrusel.html` | Slide interior: numeral en columna + desmentido. |
| `render.sh` | Exporta a PNG. |
| `fonts/Kanit-*.ttf` | Listo. |
| `logo/marca.svg` | **Provisional.** Ver abajo. |

## Falta: el engranaje del logo

`logo/marca.svg` es un engranaje genérico dibujado a mano. Hay que reemplazarlo por el
del logotipo real.

La placa pinta el engranaje **como máscara**, no como imagen:

```css
.marca{ background:var(--blanco); -webkit-mask:var(--marca) center/contain no-repeat; }
```

Lo que implica para el archivo que entregues:

- **Sirve PNG.** También SVG. Lo único que se lee es el canal alfa.
- **El color del archivo da igual** — puede venir negro, naranja o multicolor: siempre
  sale blanco al 3.5% de opacidad.
- **El fondo tiene que ser transparente.** Un PNG con fondo blanco sale como un cuadrado.
- **Mínimo 1400px** de ancho: se dibuja a 700px y hay que cubrir pantallas al doble.
- **Solo el engranaje**, sin la gota ni el texto.

Para cambiarlo basta con dejar el archivo en `logo/` y apuntar `--marca` en `placa.css`.
Guarda también el logotipo completo como `logo/lubriamerica.svg` para las piezas que sí
lo llevan (anuncios, catálogo). En las placas de carrusel no va.

## Tipografía

Kanit en los tres pesos de la marca: Medium 500, Bold 700, Black 900.

Las itálicas (`Kanit-BoldItalic`, `Kanit-BlackItalic`) no venían en la entrega original;
son las oficiales de Google Fonts, misma familia y licencia SIL OFL (`fonts/OFL.txt`).
Se usan solo en el remate de portada. Sin ellas el navegador inventa una itálica falsa
inclinando la redonda, que en un peso Black se nota.

## Fotos

No se versionan aquí. Entran por `<img src="...">` dentro de `.foto`, y hay que quitarle
la clase `vacia` al contenedor.
