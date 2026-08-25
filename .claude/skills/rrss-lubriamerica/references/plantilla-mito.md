# Plantilla "mito" — anatomía

Medidas en píxeles sobre el lienzo base de **1080×1350**. Para 1080×1920 se conserva
el ancho y se estira la foto; los tamaños de texto no cambian.

## Rejilla

```
0                                                          1080
├──72──┬────────────────────────────────────────────┬──72──┤   margen lateral 72
│      │                                            │      │
│      │              FOTO (full bleed)             │      │   y: 0 → 860
│      │                                            │      │
│ ░░░░░░░░░░░░░░ scrim: 380 → 880 ░░░░░░░░░░░░░░░░░░░░░░░░ │
│      │                                            │      │
│  ██  │  Titular blanco, 3 líneas máx              │      │   y: 900 → 1120
│  ██  │                                            │      │
│      │                                            │      │
│  (✕) NO │ cuerpo del desmentido                   │      │   y: 1150 → 1245
│      │                                            │      │
│              ⬤ @lubriamericapf                    │      │   y: 1290, centrado
└──────┴────────────────────────────────────────────┴──────┘
```

- **Foto** — `object-fit: cover`, sangrada a los cuatro bordes del área, y=0 a y=860.
  Desaturada al 85% y con `brightness(0.9)` para que el naranja no compita.
- **Scrim** —
  `linear-gradient(180deg, transparent 28%, rgba(39,39,38,.55) 45%, rgba(39,39,38,.92) 58%, #272726 65%)`
  aplicado sobre toda la placa, no solo sobre la foto. El corte nunca es una línea dura.
- **Marca de agua** — engranaje del logo, 720px de ancho, `opacity: .05`, anclado en
  `bottom: -120px; left: 50%`, recortado por el borde inferior. Detrás de todo el texto.
- **Rayado** — franjas blancas de 3px cada 22px a 45°, `opacity: .08`, en la esquina
  superior izquierda (400×400) y una segunda pasada sobre la zona del scrim.

## Zona inferior — slide interior

| Elemento | Tamaño | Peso | Color | Notas |
|---|---|---|---|---|
| Numeral | 230px | 900 | `#ff7400` | Columna izquierda de 150px, `line-height: .8`. Su tope se alinea con el tope de la primera línea del titular. |
| Titular | 66px | 800 | `#f9f7f6` | `line-height: .98`. 3 líneas máx. Corta con `<br>` donde caiga bien, no confíes en el flujo. |
| Badge ✕ | ⌀78px | — | `#e01b1b` | Círculo sólido, aspa blanca de 6px. |
| NO | 76px | 900 | `#f9f7f6` | Pegado al badge, 20px de separación. |
| Regla | 5×86px | — | `#f9f7f6` | Vertical, separa el NO del cuerpo. 24px a cada lado. |
| Eyebrow | 26px | 700 | `#ff7400` | Mayúsculas, `letter-spacing: .06em`. Opcional, va encima del cuerpo. |
| Cuerpo | 27px | 600 | `#f9f7f6` | `line-height: 1.35`, 4 líneas máx. |
| Handle | 34px | 700 | `#f9f7f6` | Centrado, con el glifo de Instagram a 38px. `bottom: 60px`. |

## Zona inferior — portada

La portada rompe la columna: el numeral **se mete dentro del titular** como primera
letra de la frase ("**3** cosas que creías sobre...") en 210px, y debajo va el remate
en itálica de 62px con el badge ✕ al final de la línea.

- El remate va en mayúsculas y siempre cierra la promesa: `Y NO SON CIERTAS`.
- La portada no lleva bloque de cuerpo. Nada de explicación: la explicación es el swipe.

## Errores frecuentes al exportar

- Titular de 4 líneas: el bloque de abajo se come el handle. Recorta el copy, no bajes
  el tamaño del titular.
- Numeral y titular chocando: el numeral usa `line-height: .8` justamente para que su
  caja no empuje. Si chocan, el problema es el ancho de la columna, no el tamaño.
- Scrim corto: si el titular empieza antes del 65% de la altura, sube el punto final
  del degradado, no le pongas fondo sólido a la caja de texto.
