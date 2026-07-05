# -*- coding: utf-8 -*-
"""Capture mobile-width screenshots for generated layout samples.

Usage:
  python3 scripts/capture_layout_samples.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "examples" / "layout-samples"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for article in sorted(SAMPLES.glob("*/article.html")):
            page = browser.new_page(viewport={"width": 390, "height": 1200}, device_scale_factor=2)
            page.goto(article.resolve().as_uri())
            page.screenshot(path=str(article.parent / "mobile-preview.png"), full_page=True)
            page.close()
            print("captured", article.parent / "mobile-preview.png")
        browser.close()


if __name__ == "__main__":
    main()
