#!/usr/bin/env bash
# 拉取 Archivo + JetBrains Mono 到用户字体目录;CJK 依赖系统 Noto Sans CJK。
set -e
D="$HOME/.fonts"; mkdir -p "$D"
fetch(){ [ -f "$D/$2" ] || (pip download "$1" -d /tmp/f --no-deps -q 2>/dev/null || true); }
python3 - <<'PY'
import pathlib, urllib.request, os
d = pathlib.Path.home()/".fonts"; d.mkdir(exist_ok=True)
srcs = {
 "Archivo.ttf":"https://github.com/google/fonts/raw/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf",
 "JetBrainsMono.ttf":"https://github.com/JetBrains/JetBrainsMono/raw/master/fonts/variable/JetBrainsMono%5Bwght%5D.ttf",
}
for name, url in srcs.items():
    p = d/name
    if not p.exists():
        try:
            urllib.request.urlretrieve(url, p); print("fetched", name)
        except Exception as e:
            print("skip", name, e)
PY
fc-cache -f >/dev/null 2>&1 || true
echo "fonts ready"
