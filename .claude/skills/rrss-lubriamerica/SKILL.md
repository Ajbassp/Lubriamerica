---
name: rrss-lubriamerica
description: Sistema de diseño para las piezas de redes sociales de Distribuidora Lubriamérica (@lubriamericapf) - carruseles educativos, placas de feed y stories sobre lubricantes y mantenimiento automotriz. Usar al crear, adaptar o revisar cualquier arte para Instagram u otra red de la marca.
---

# RRSS Lubriamérica

Distribuidora Lubriamérica vende lubricantes y le habla a dueños de carro y mecánicos.
El contenido que funciona es **didáctico y correctivo**: desarma creencias equivocadas
sobre el motor y da el dato técnico correcto. La marca suena a taller que sabe, no a
agencia que vende.

Antes de diseñar, lee `references/plantilla-mito.md` para la anatomía exacta de la
plantilla base. El código arranca de `assets/plantilla-portada.html` o
`assets/plantilla-carrusel.html` según la placa; `assets/README.md` lista lo que
todavía falta montar.

## Tokens

```
--naranja        #ff7400   Acento. Numerales, eyebrows, detalles.
--naranja-oscuro #c96410   Sombras, degradados, estados. Nunca texto chico.
--gris           #272726   Fondo base y scrim sobre foto.
--blanco         #f9f7f6   Texto principal.
--rojo           #e01b1b   Solo el badge de mito falso. No es color de marca.
```

Contrastes reales, ya medidos — respétalos, no los recalcules:

| Combinación | Ratio | Uso permitido |
|---|---|---|
| `#f9f7f6` sobre `#272726` | 14.3:1 | Todo. Es la combinación por defecto del texto. |
| `#ff7400` sobre `#272726` | 5.5:1 | Todo, incluido texto chico. |
| `#c96410` sobre `#272726` | 3.8:1 | Solo 48px o más, o elementos no textuales. |
| `#ff7400` sobre `#f9f7f6` | 2.6:1 | **Prohibido para texto.** |

El naranja sobre claro solo existe con contorno gris `#272726`, como en el logotipo.
Fuera de ese caso, el naranja vive sobre gris o sobre foto oscurecida.

## Tipografía

Display y cuerpo salen de la misma familia; la jerarquía la cargan el peso y el tamaño,
no un segundo tipo. `Montserrat` (variable, incluida en `assets/fonts/`) es la referencia:

- **Titular** — 800, `line-height: 0.98`, `letter-spacing: -0.01em`. Máximo 3 líneas.
- **Numeral** — 900, tamaño desproporcionado (unas 4 veces el titular). Es figura, no texto.
- **Remate** — 800 itálica, mayúsculas. Solo en portada.
- **Eyebrow** — 700 mayúsculas, `letter-spacing: 0.06em`, naranja.
- **Cuerpo** — 600, `line-height: 1.35`. Máximo 4 líneas.
- **Handle** — 700, centrado en el pie.

Nunca centres un titular. Todo el texto de la zona inferior se alinea a la izquierda
del margen; lo único centrado en la placa es el handle del pie.

## Formatos

| Pieza | Medida | Notas |
|---|---|---|
| Carrusel / feed | 1080×1350 | Formato base. Todo se diseña aquí primero. |
| Story / portada de reel | 1080×1920 | Zona segura: 250px arriba, 320px abajo. |
| Cuadrado | 1080×1080 | Solo si la red lo exige. |

## La estructura de la placa

Cada placa es **foto arriba, palabra abajo**, unidas por un scrim que baja de
transparente a `#272726` sólido. La foto muestra la situación real (la mano con la
llave, el aceite cayendo, el carro parado); el texto ocurre sobre gris limpio, nunca
encima de la imagen viva.

Sobre esa base van tres marcas de la casa, y solo esas tres:

1. **El numeral naranja**, gigante, a la izquierda.
2. **El engranaje del logo** como marca de agua al 5% de opacidad, recortado por el borde.
3. **Rayado diagonal** blanco al 8%, en la esquina superior y sobre el scrim.

No agregues una cuarta. Si una placa necesita más energía, súbele el tamaño al numeral
antes que sumarle un elemento.

## Cuándo numerar

Los marcadores 01 / 02 / 03 son decoración en casi cualquier otra marca. Aquí no: el
carrusel de mitos **es** una secuencia — el lector llega por "3 cosas" y el numeral le
dice cuánto falta. Numera cuando el conteo esté prometido en la portada. Si la pieza es
un solo dato, un producto o un anuncio, el numeral no aplica y no se fuerza.

## Reglas duras

- El logo completo no va en las placas del carrusel. Va el engranaje de marca de agua
  y el handle en el pie.
- Nada de texto directamente sobre la foto sin scrim de por medio.
- Un solo acento fuerte por placa: o manda el numeral, o manda el badge. No compiten.
- Sin degradados naranja sobre naranja de relleno.
- Sin sombras suaves ni bordes redondeados generosos: la marca es de contorno duro.
  El único radio grande de la pieza es el círculo del badge.
- El rojo del badge no se usa para nada más. No es color de marca.

## Copy

Tuteo, español panameño natural. **Carro**, no coche. **Aceite** cuando le hablas al
dueño; **lubricante** cuando hablas de catálogo.

El titular es el mito dicho tal como la gente lo dice, en su propia voz: "Mientras más
espeso el aceite, mejor es la lubricación del motor". No lo corrijas en el titular —
esa es la función del bloque de abajo.

La respuesta es un **NO** seco y después el porqué en una frase, con el mecanismo
concreto: qué pasa físicamente y qué se daña. "Al estar en frío no circula como debe y
ahí es cuando el motor se desgasta más rápido" funciona porque nombra la causa.

Cuando el dato tenga matiz, se dice el matiz — inyección electrónica contra carburado,
kilometraje contra tiempo. Simplificar de más le quita a la marca lo único que la hace
creíble. Si el matiz cambia la respuesta, va con eyebrow naranja ("PERO OJO CON UN DATO").

Prohibido: "¡Descubre!", "¡No te lo pierdas!", "En el mundo de hoy...", cadenas de signos
de admiración, y prometer lo que el carrusel no entrega.

## Producción

Las placas se arman en HTML y se exportan a PNG con Chromium:

```bash
cd .claude/skills/rrss-lubriamerica/assets
./render.sh mi-pieza.html ../../../salida/slide-1.png
```

`render.sh` usa `headless_shell` a propósito: el binario completo de Chromium descuenta
unos 88px de altura de ventana y recorta el handle del pie sin avisar.

Revisa el PNG antes de darlo por bueno. Los errores que aparecen al exportar y no en el
navegador son casi siempre titulares que pasaron de 3 líneas o el numeral chocando con
la primera línea del texto.
