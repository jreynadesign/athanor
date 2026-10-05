#!/bin/sh
# renders tools/og.html to /og.jpg (1200×630) with headless chrome. run from the repo root.
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1200,630 --virtual-time-budget=5000 --screenshot=/tmp/og.png "file://$PWD/tools/og.html" 2>/dev/null
sips -s format jpeg -s formatOptions 88 /tmp/og.png --out og.jpg >/dev/null
echo "og.jpg: $(sips -g pixelWidth -g pixelHeight og.jpg | tail -2 | awk '{print $2}' | paste -sd× -)"
