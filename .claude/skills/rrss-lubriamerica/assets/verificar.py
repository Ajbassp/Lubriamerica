#!/usr/bin/env python3
"""Verifica que una placa exportada respete el sistema de márgenes.

    python3 verificar.py salida.png

Parte la placa en bandas horizontales de contenido, y dentro de cada banda separa
los bloques que están sueltos horizontalmente. Cada bloque debe arrancar en una de
las dos verticales del sistema (el margen exterior o el margen de texto), salvo el
handle del pie, que va centrado. Nada puede cruzar el margen derecho.

Comprueba además que el numeral naranja cubra exactamente el alto del bloque de
titular: es el desajuste que menos se nota mirando y más se nota en el feed.

Sale con código 1 si algo queda fuera, para poder encadenarlo tras render.sh.

Límite conocido: en el slide interior la regla vertical toca el margen de texto por
diseño, así que el veredicto y el cuerpo se leen como un solo bloque que arranca en
el margen exterior. Ese caso hay que mirarlo a ojo.
"""
import sys
from PIL import Image

MARGEN, TEXTO, ANCHO, ALTO = 72, 252, 1080, 1350
TOLERANCIA = 6     # px: lateral tipográfico y antialiasing
HUECO = 30         # px de aire que separan dos bloques dentro de una banda

def contenido(c):
    """Naranja, blanco y el rojo del badge cuentan; el gris, el rayado y la
    marca de agua no."""
    return max(c) > 150

def bandas(px, w, h):
    filas = [[x for x in range(w) if contenido(px[x, y])] for y in range(h)]
    out, act = [], None
    for y, xs in enumerate(filas):
        if len(xs) > 3:
            act = [y, y, set(xs)] if act is None else [act[0], y, act[2] | set(xs)]
        elif act is not None and y - act[1] > 12:
            out.append(act); act = None
    if act: out.append(act)
    return out

def bloques(xs):
    xs = sorted(xs); grupos, ini, prev = [], xs[0], xs[0]
    for x in xs[1:]:
        if x - prev > HUECO:
            grupos.append((ini, prev)); ini = x
        prev = x
    grupos.append((ini, prev))
    return grupos

def numeral_vs_titular(px, w, h):
    """El numeral debe cubrir el alto del bloque de titular, ni más ni menos.
    Compara el relleno naranja con el texto claro que tiene a su derecha."""
    naranja = lambda c: abs(c[0]-255) < 25 and abs(c[1]-116) < 45 and c[2] < 70
    ys_n = [y for y in range(h) for x in range(MARGEN, TEXTO, 2) if naranja(px[x, y])]
    if not ys_n:
        return None
    n0, n1 = min(ys_n), max(ys_n)
    ys_t = [y for y in range(max(0, n0-60), min(h, n1+60))
            for x in range(TEXTO, ANCHO - MARGEN, 3) if contenido(px[x, y])]
    if not ys_t:
        return None
    t0, t1 = min(ys_t), max(ys_t)
    return (n0, n1, t0, t1)

def main(ruta):
    im = Image.open(ruta).convert("RGB"); w, h = im.size
    if (w, h) != (ANCHO, ALTO):
        print(f"aviso: la placa mide {w}x{h}, no {ANCHO}x{ALTO}")
    px = im.load(); fallos = 0
    print(f"{'banda':>13}  {'bloque':>13}   estado")
    for y0, y1, xs in bandas(px, w, h):
        for x0, x1 in bloques(xs):
            centrado = abs(x0 - (w - x1)) <= TOLERANCIA
            derecha  = abs(x1 - (ANCHO - MARGEN)) <= TOLERANCIA
            if abs(x0 - MARGEN) <= TOLERANCIA:   est = "margen exterior"
            elif abs(x0 - TEXTO) <= TOLERANCIA:  est = "margen de texto"
            elif centrado:                       est = "centrado"
            elif derecha:                        est = "pegado al margen derecho"
            else:
                est = f"FUERA: arranca en {x0}"; fallos += 1
            if x1 > ANCHO - MARGEN + TOLERANCIA:
                est += f" | FUERA: cruza el margen derecho ({x1})"; fallos += 1
            print(f"{y0:>5}-{y1:<7}  {x0:>5}-{x1:<7}   {est}")
    cmp = numeral_vs_titular(px, w, h)
    if cmp:
        n0, n1, t0, t1 = cmp
        arriba, abajo = n0 - t0, n1 - t1
        print()
        print(f"numeral y:{n0}-{n1} (alto {n1-n0})   titular y:{t0}-{t1} (alto {t1-t0})")
        if abs(arriba) > 8 or abs(abajo) > 8:
            print(f"  FUERA: el numeral no cubre el alto del titular "
                  f"(desfase arriba {arriba:+d}, abajo {abajo:+d})")
            fallos += 1
        else:
            print(f"  el numeral cubre el titular (desfase {arriba:+d} / {abajo:+d})")

    print()
    if fallos:
        print(f"{fallos} problema(s) de margen."); return 1
    print("Todo cae en el sistema de márgenes."); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "salida.png"))
