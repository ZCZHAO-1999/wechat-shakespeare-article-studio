# -*- coding: utf-8 -*-
"""把 HTML 中 src="X.png" 全部 base64 内嵌。用法: python3 embed_images.py in.html out.html [宽度=1354]"""
import sys, re, io, base64, pathlib
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
tw = int(sys.argv[3]) if len(sys.argv) > 3 else 1354
html = pathlib.Path(src).read_text(encoding="utf-8")

def uri(name):
    im = Image.open(name)
    if im.width > tw:
        im = im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

for name in sorted(set(re.findall(r'src="([^"]+\.png)"', html))):
    if pathlib.Path(name).exists():
        html = html.replace(f'src="{name}"', f'src="{uri(name)}"')
    else:
        print("WARN missing:", name)
pathlib.Path(dst).write_text(html, encoding="utf-8")
print("embedded ->", dst, round(len(html)/1e6, 1), "MB")
