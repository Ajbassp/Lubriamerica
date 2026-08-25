#!/usr/bin/env bash
# Exporta una placa HTML a PNG con Chromium headless.
#   render.sh pieza.html salida.png [ancho] [alto]
#
# Usa headless_shell cuando está disponible: el binario completo de Chromium
# descuenta ~88px de altura de ventana y recorta el pie de la placa.
set -euo pipefail

IN="${1:?uso: render.sh entrada.html salida.png [ancho] [alto]}"
OUT="${2:?uso: render.sh entrada.html salida.png [ancho] [alto]}"
W="${3:-1080}"
H="${4:-1350}"

BIN=""
for c in /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell \
         "$(command -v headless_shell || true)"; do
  [ -x "$c" ] && BIN="$c" && break
done
if [ -z "$BIN" ]; then
  BIN="$(command -v chromium || command -v chromium-browser || command -v google-chrome || true)"
  [ -x /opt/pw-browsers/chromium ] && BIN=/opt/pw-browsers/chromium
  echo "aviso: sin headless_shell; verifica que el pie no salga recortado." >&2
fi
[ -z "$BIN" ] && { echo "No encuentro Chromium." >&2; exit 1; }

# --allow-file-access-from-files: sin esto Chromium bloquea el SVG de la marca de
# agua como recurso cross-origin y la placa sale sin engranaje, sin dar ningún error.
"$BIN" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --allow-file-access-from-files \
  --force-device-scale-factor=1 --window-size="${W},${H}" \
  --screenshot="$OUT" "file://$(realpath "$IN")" 2>/dev/null

echo "$OUT  ${W}x${H}"
