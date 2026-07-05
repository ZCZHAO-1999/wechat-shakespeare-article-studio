# -*- coding: utf-8 -*-
"""公众号信息图脚手架:token + page/header + 组件构造器。
用法:在工作目录写 build.py -> `from fig_scaffold import *`,组装 body 后 page(...)
再用 render.py 渲染。规范见 references/design-system.md。"""
import pathlib

ACCENT = "#8FC6E8"          # 品牌强调色,可整体替换
ACCENT_BRIGHT = "#D4EBF9"
GLOW = "rgba(143,198,232,.36)"

BASE_CSS = f"""
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
:root{{
  --bg:#08090D; --panel:#0E1118; --panel2:#10141C;
  --ink:#F2EFE7; --dim:#A9AEB9; --faint:#61687A;
  --hair:rgba(242,239,231,.10); --hair2:rgba(242,239,231,.16);
  --ice:{ACCENT}; --ice-bright:{ACCENT_BRIGHT}; --glow:{GLOW};
}}
body{{background:#000;}}
#poster{{position:relative;overflow:hidden;background:
  radial-gradient(120% 90% at 72% 0%, #0D1220 0%, var(--bg) 55%);
  font-family:'Archivo','Noto Sans CJK SC','Noto Sans SC','PingFang SC',sans-serif;
  color:var(--ink);}}
.grain{{position:absolute;inset:0;opacity:.045;pointer-events:none;mix-blend-mode:overlay;}}
.vign{{position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(140% 110% at 50% 42%, transparent 55%, rgba(0,0,0,.42) 100%);}}
.wrap{{position:absolute;inset:0;padding:44px 52px 40px;display:flex;flex-direction:column;}}
.hd{{display:flex;justify-content:space-between;align-items:flex-start;}}
.hd .t-cn{{font-family:'Noto Sans CJK SC','Noto Sans SC',sans-serif;font-weight:700;font-size:27px;letter-spacing:.06em;color:var(--ink);}}
.hd .t-en{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.34em;color:var(--faint);margin-top:9px;text-transform:uppercase;}}
.hd .figno{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.3em;color:var(--faint);text-align:right;line-height:1.9;}}
.hd .figno b{{display:block;color:var(--dim);font-weight:500;}}
.ft{{margin-top:auto;padding-top:16px;border-top:1px solid var(--hair);
  display:flex;justify-content:space-between;align-items:baseline;}}
.ft .note{{font-family:'Noto Sans CJK SC',sans-serif;font-size:12.5px;letter-spacing:.05em;color:var(--dim);}}
.ft .note b{{color:var(--ink);}}
.ft .src{{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.24em;color:var(--faint);text-transform:uppercase;white-space:nowrap;margin-left:28px;}}
.mono{{font-family:'JetBrains Mono',monospace;}}
.cn{{font-family:'Noto Sans CJK SC','Noto Sans SC',sans-serif;}}
/* —— 组件 —— */
.cols{{display:flex;gap:20px;margin-top:30px;flex:1;}}
.col{{flex:1;background:var(--panel);border:1px solid var(--hair);border-radius:10px;padding:24px 24px 20px;position:relative;}}
.col.hero{{background:linear-gradient(180deg,#101826 0%, #0D1320 100%);border:1px solid rgba(143,198,232,.45);
  box-shadow:0 0 60px -12px var(--glow), inset 0 0 40px -20px rgba(143,198,232,.25);}}
.chip{{position:absolute;top:-11px;right:16px;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.22em;
  color:#0A0E14;background:var(--ice);border-radius:3px;padding:4px 9px;font-weight:700;}}
.chip.ghost{{color:var(--ice-bright);background:#0A0E14;border:1px solid rgba(143,198,232,.6);}}
.brand{{font-weight:800;font-size:21px;letter-spacing:.02em;color:var(--ink);}}
.route{{font-size:12.5px;letter-spacing:.14em;color:var(--faint);margin-top:6px;}}
.col.hero .route{{color:var(--ice-bright);}}
.row{{margin-top:19px;}}
.lab{{font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.26em;color:var(--faint);text-transform:uppercase;}}
.val{{font-size:14px;line-height:1.65;letter-spacing:.03em;color:var(--dim);margin-top:6px;}}
.col.hero .val{{color:#D9DDE4;}}
.val b{{color:var(--ink);font-weight:700;}}
.col.hero .val b{{color:var(--ice-bright);}}
.dist{{display:flex;align-items:center;gap:8px;margin-top:7px;}}
.dist .d{{width:7px;height:7px;border-radius:50%;border:1px solid var(--faint);}}
.dist .d.on{{background:var(--ice);border-color:var(--ice);box-shadow:0 0 10px var(--glow);}}
.dist span{{font-size:13.5px;color:var(--dim);letter-spacing:.04em;}}
.col.hero .dist span{{color:var(--ice-bright);font-weight:600;}}
.heroP{{background:linear-gradient(180deg,#101826 0%, #0D1320 100%);border:1px solid rgba(143,198,232,.45);
  border-radius:12px;padding:26px 28px;position:relative;display:flex;flex-direction:column;
  box-shadow:0 0 70px -14px var(--glow), inset 0 0 46px -22px rgba(143,198,232,.25);}}
.big{{font-family:'Archivo',sans-serif;font-weight:800;font-size:74px;letter-spacing:-.015em;color:var(--ink);
  margin-top:12px;text-shadow:0 0 44px rgba(143,198,232,.35);}}
.cellgrid{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;flex:1;}}
.cell{{background:var(--panel);border:1px solid var(--hair);border-radius:10px;padding:17px 18px;display:flex;flex-direction:column;}}
.cell .k{{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.26em;color:var(--faint);text-transform:uppercase;}}
.cell .n{{font-weight:800;font-size:23px;color:var(--ink);margin-top:8px;}}
.cell .n i{{font-style:normal;font-size:13px;color:var(--ice);margin-left:2px;}}
.cell .d{{font-size:11.5px;color:var(--dim);margin-top:auto;letter-spacing:.04em;line-height:1.55;}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px;flex:1;}}
.gcard{{background:var(--panel);border:1px solid var(--hair);border-radius:10px;padding:15px 17px 13px;
  position:relative;display:flex;flex-direction:column;}}
.gcard .k{{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.2em;color:var(--faint);text-transform:uppercase;}}
.gcard .t{{font-weight:700;font-size:16px;color:var(--ink);margin-top:7px;letter-spacing:.05em;}}
.gcard .d{{font-size:11.5px;color:var(--dim);margin-top:auto;padding-top:9px;letter-spacing:.04em;line-height:1.6;}}
.strip{{margin-top:15px;background:var(--panel);border:1px solid var(--hair);border-radius:8px;
  padding:12px 20px;display:flex;align-items:center;gap:14px;}}
.strip .k{{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.26em;color:var(--ice);white-space:nowrap;}}
.strip .v{{font-size:13.5px;color:var(--dim);letter-spacing:.05em;}}
.strip .v b{{color:var(--ink);}}
</style>
"""
GRAIN = ('<svg class="grain" width="100%" height="100%"><filter id="n">'
         '<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/></filter>'
         '<rect width="100%" height="100%" filter="url(#n)"/></svg>')

def page(name, W, H, body, extra_css=""):
    """写出一张图的 html;body 顶层用 <div class="wrap">…</div>。"""
    html = f"""<!doctype html><html><head><meta charset="utf-8">{BASE_CSS}<style>{extra_css}</style></head>
<body><div id="poster" style="width:{W}px;height:{H}px">{GRAIN}<div class="vign"></div>{body}</div>
<script>window.__POSTER__={{W:{W},H:{H}}};window.__art_done=true;</script></body></html>"""
    pathlib.Path(name).write_text(html, encoding="utf-8")
    print("wrote", name)

def header(cn, en, fig_no, brand="STUDIO"):
    return (f'<div class="hd"><div><div class="t-cn">{cn}</div><div class="t-en">{en}</div></div>'
            f'<div class="figno"><b>FIG. {fig_no}</b>{brand}</div></div>')

def footer(note_html, fig_no, total):
    return (f'<div class="ft"><div class="note">{note_html}</div>'
            f'<div class="src">FIG {fig_no} / {total}</div></div>')

# —— 组件构造器 ——
def bizcol(brand, route, rows, dots, dist_txt, hero=False, chip=""):
    """双栏对照的一列。rows=[(LABEL, html值),…] dots∈1..3"""
    d = "".join(f'<i class="d {"on" if i < dots else ""}"></i>' for i in range(3))
    rs = "".join(f'<div class="row"><div class="lab">{l}</div><div class="val cn">{v}</div></div>' for l, v in rows)
    c = f'<div class="chip">{chip}</div>' if chip else ''
    return (f'<div class="col {"hero" if hero else ""}">{c}'
            f'<div class="brand cn">{brand}</div><div class="route cn">{route}</div>{rs}'
            f'<div class="row"><div class="lab">Distance · 离最终结果</div>'
            f'<div class="dist">{d}<span class="cn">{dist_txt}</span></div></div></div>')

def hero_metric(k, big, sub_html, cells):
    """英雄数字面板 + 2×2 chips。cells=[(K,数值html,说明),…]×4"""
    cs = "".join(f'<div class="cell"><span class="k">{a}</span><div class="n">{b}</div>'
                 f'<div class="d cn">{c}</div></div>' for a, b, c in cells)
    return (f'<div style="display:flex;gap:20px;margin-top:28px;flex:1;">'
            f'<div class="heroP" style="flex:1.15;"><span class="lab" style="color:var(--ice);">{k}</span>'
            f'<div class="big">{big}</div><div class="cn" style="margin-top:auto;font-size:13px;color:var(--dim);">{sub_html}</div></div>'
            f'<div class="cellgrid">{cs}</div></div>')

def grid_cards(cards):
    """平行网格。cards=[(EN_K, 标题, 说明, chip或'')…],3 列自动换行。"""
    out = []
    for k, t, d, chip in cards:
        c = f'<div class="chip ghost">{chip}</div>' if chip else ''
        out.append(f'<div class="gcard">{c}<span class="k">{k}</span>'
                   f'<div class="t cn">{t}</div><div class="d cn">{d}</div></div>')
    return f'<div class="grid3">{"".join(out)}</div>'

def strip(k, v_html):
    return f'<div class="strip"><span class="k">{k}</span><span class="v cn">{v_html}</span></div>'

# 反馈回路(SVG)与问题—方案对比无法完全参数化,写法范式见 design-system.md 第三节;
# 要点:站点矩形置四角 + marker 箭头 + 亮色回流边 + 中心 radial 光。

if __name__ == "__main__":
    # 冒烟测试:一张双栏对照 demo
    body = f"""<div class="wrap">
{header("两种生意:卖组件,还是卖结果", "DEMO · TWO WAYS", "01", "DEMO")}
<div class="cols">
{bizcol("路线甲", "MIDDLEWARE", [("What · 卖什么", "通用组件,按调用计费")], 1, "隔两层")}
{bizcol("路线乙", "ENGINE", [("What · 卖什么", "一台<b>会自己变强的引擎</b>")], 3, "零距离", hero=True, chip="主角")}
</div>
{footer("没有人为「记住了」买单,人们只为「<b>做对了</b>」买单。", "01", "01")}
</div>"""
    page("demo_fig.html", 1000, 520, body)
