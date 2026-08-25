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
| Numeral | 290px | 900 | `#ff7400` + trazo `#f9f7f6` 8px | `paint-order: stroke fill`, para que el trazo quede por fuera y el naranja conserve su grosor. Centrado contra el bloque del titular, con `top: -8px` de corrección óptica. |
| Titular | 72px | 700 | `#f9f7f6` | `line-height: 1.02`. 3 líneas máx. Arranca en `--texto`. |
| Badge | ⌀62px | — | `#e01b1b` | Círculo sólido, aspa blanca. |
| NO | 60px | 900 | `#f9f7f6` | Dentro del canal izquierdo, junto al badge. |
| Regla | 5×78px | — | `#f9f7f6` | `margin-left: auto`: cae exactamente sobre el margen del texto y lo marca. |
| Eyebrow | 26px | 700 | `#ff7400` | Mayúsculas, `letter-spacing: .06em`. Opcional. |
| Cuerpo | 28px | 500 | `#f9f7f6` | `line-height: 1.35`, `text-wrap: balance`, 4 líneas máx. Arranca en `--texto`. |
| Handle | 34px | 700 | `#f9f7f6` | Centrado, `bottom: 60px`. |

### El canal izquierdo

```
72        252                                          1008
├────canal────┤├──────────── texto corrido ─────────────┤
│  numeral    ││  titular                               │
│  badge+NO│  ││  cuerpo                                │
      regla ──┘   (la regla marca el margen)
```

El canal mide `--texto - --margen - --canal`. Numeral y veredicto lo ocupan por
completo; nada de texto corrido entra ahí.

Medidas verificadas sobre el render: titular y cuerpo arrancan los dos en x=254, y
el numeral cubre el bloque de titular con menos de 8px de desfase arriba y abajo.
El canal es de 12px, así que el numeral queda pegado al texto; con un "1" el aire
crece porque el dígito es más estrecho, y eso es correcto.
Si tocas el tamaño del titular, vuelve a medir el PNG en vez de estimar a ojo.

## Zona inferior — portada

La portada rompe la columna: el numeral **se mete dentro del titular** como primera
letra de la frase ("**3** cosas que creías sobre...") en 232px, y debajo va el remate
en itálica Black de 90px con el badge ✕ al final de la línea.

- El remate va en mayúsculas y siempre cierra la promesa: `Y NO SON CIERTAS`.
- El badge de la portada (⌀86px, mayor que el de los slides) se ancla al margen
  derecho con `justify-content: space-between`, no pegado al texto.
- La portada no lleva bloque de cuerpo. Nada de explicación: la explicación es el swipe.

## Errores frecuentes al exportar

- Titular de 4 líneas: el bloque de abajo se come el handle. Recorta el copy, no bajes
  el tamaño del titular.
- Numeral y titular chocando: el numeral usa `line-height: .8` justamente para que su
  caja no empuje. Si chocan, el problema es el ancho de la columna, no el tamaño.
- Scrim corto: si el titular empieza antes del 65% de la altura, sube el punto final
  del degradado, no le pongas fondo sólido a la caja de texto.
