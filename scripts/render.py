# -*- coding: utf-8 -*-
"""HTML -> PNG @2x. 用法: python3 render.py in.html out.png"""
import sys, pathlib
from playwright.sync_api import sync_playwright

src, dst = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2)
    pg.goto(pathlib.Path(src).resolve().as_uri())
    pg.wait_for_timeout(400)
    dims = pg.evaluate("window.__POSTER__ || null") or {}
    W = dims.get("W") or pg.evaluate("document.getElementById('poster').offsetWidth")
    H = dims.get("H") or pg.evaluate("document.getElementById('poster').offsetHeight")
    pg.set_viewport_size({"width": int(W), "height": int(H)})
    pg.wait_for_timeout(250)
    pg.locator("#poster").screenshot(path=dst)
    b.close()
from PIL import Image
print("rendered", dst, "->", Image.open(dst).size)
