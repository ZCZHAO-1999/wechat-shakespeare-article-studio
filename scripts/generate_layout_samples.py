# -*- coding: utf-8 -*-
"""Generate sample WeChat article layouts for QA.

Usage:
  python3 scripts/generate_layout_samples.py
"""
from pathlib import Path
from html import escape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "examples" / "layout-samples"


VISUAL_CSS = """
*{box-sizing:border-box}body{margin:0;background:#000}
#visual{position:relative;overflow:hidden;background:#071014;color:#f6f2e8;
font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif}
#visual:before{content:"";position:absolute;inset:-20%;background:
radial-gradient(620px 360px at 78% 18%,rgba(129,204,210,.30),transparent 62%),
radial-gradient(420px 300px at 8% 84%,rgba(207,199,154,.18),transparent 60%),
linear-gradient(135deg,#081117 0%,#111a1f 48%,#080b0d 100%)}
#visual:after{content:"";position:absolute;inset:0;opacity:.17;background-image:
linear-gradient(110deg,rgba(255,255,255,.055) 1px,transparent 1px),
linear-gradient(0deg,rgba(255,255,255,.035) 1px,transparent 1px);
background-size:48px 48px,48px 48px;mask-image:radial-gradient(circle at 50% 45%,#000 20%,transparent 82%)}
.grain{position:absolute;inset:0;opacity:.18;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.35'/%3E%3C/svg%3E");mix-blend-mode:soft-light}
.wrap{position:absolute;inset:0;padding:48px 58px;z-index:2}
.kicker{font-size:14px;letter-spacing:.28em;text-transform:uppercase;color:#88d5dc;font-weight:700}
.title{font-size:48px;line-height:1.16;font-weight:800;letter-spacing:0;margin-top:18px;max-width:610px}
.sub{position:absolute;left:58px;bottom:48px;font-size:20px;color:#c9d1d0;letter-spacing:.04em}
.plate{position:absolute;right:58px;bottom:42px;padding:12px 16px;border:1px solid rgba(136,213,220,.36);color:#88d5dc;font-size:13px;letter-spacing:.22em;text-transform:uppercase}
.diagram{position:absolute;right:54px;top:50px;width:500px;height:395px;z-index:1}
.node{position:absolute;border:1px solid rgba(142,218,222,.48);background:rgba(7,16,20,.72);border-radius:8px;padding:13px 15px;box-shadow:0 18px 40px rgba(0,0,0,.28)}
.node b{display:block;font-size:24px;letter-spacing:.02em}.node span{display:block;margin-top:7px;color:#aeb9b8;font-size:16px;line-height:1.5}
.n1{left:0;top:44px}.n2{right:4px;top:24px}.n3{right:42px;bottom:38px}.n4{left:38px;bottom:18px}
.pulse{position:absolute;left:184px;top:142px;width:150px;height:150px;border-radius:50%;background:radial-gradient(circle,rgba(136,213,220,.34),rgba(136,213,220,.05) 54%,transparent 72%);border:1px solid rgba(136,213,220,.24)}
.line{position:absolute;height:2px;background:linear-gradient(90deg,transparent,#88d5dc,transparent);transform-origin:left center;opacity:.8}
.l1{left:148px;top:95px;width:215px;transform:rotate(-5deg)}.l2{left:306px;top:126px;width:165px;transform:rotate(72deg)}.l3{left:174px;top:316px;width:220px;transform:rotate(-8deg)}.l4{left:78px;top:250px;width:160px;transform:rotate(-70deg)}
.fig-title{font-size:42px;line-height:1.18;font-weight:800}.fig-sub{margin-top:10px;color:#9fa9a8;font-size:18px}
.canvas{position:absolute;left:50px;right:50px;top:128px;bottom:70px;border:1px solid rgba(255,255,255,.10);background:rgba(255,255,255,.035);border-radius:14px}
.step{position:absolute;width:250px;min-height:128px;border:1px solid rgba(136,213,220,.44);background:rgba(11,22,27,.82);border-radius:12px;padding:21px}
.step .num{font-size:14px;letter-spacing:.22em;color:#88d5dc;font-weight:800}.step b{display:block;margin-top:10px;font-size:28px}.step span{display:block;margin-top:10px;color:#aeb9b8;font-size:17px;line-height:1.5}
.s1{left:38px;top:42px}.s2{left:334px;top:42px}.s3{right:38px;top:42px}.s4{left:334px;bottom:32px;border-color:rgba(223,209,145,.58)}
.arrow{position:absolute;height:3px;background:#88d5dc;opacity:.75}.a1{left:298px;top:105px;width:30px}.a2{left:594px;top:105px;width:30px}.a3{right:260px;top:210px;width:120px;transform:rotate(132deg)}
.note{position:absolute;left:58px;right:58px;bottom:34px;border-top:1px solid rgba(255,255,255,.12);padding-top:15px;color:#c9d1d0;font-size:19px}
.lane{position:absolute;left:58px;right:58px;top:230px;height:2px;background:rgba(155,59,47,.28)}
.milestone{position:absolute;top:170px;width:250px;padding:22px 22px 20px;border-radius:4px;background:rgba(255,255,255,.74);border-top:4px solid #9b3b2f;box-shadow:0 16px 34px rgba(46,37,24,.10)}
.milestone .num{font-size:13px;letter-spacing:.22em;color:#9b3b2f;font-weight:800}.milestone b{display:block;margin-top:12px;font-size:30px}.milestone span{display:block;margin-top:10px;color:#5f5a52;font-size:17px;line-height:1.5}
.m1{left:78px}.m2{left:346px}.m3{left:614px}.m4{left:882px}
.interface{position:absolute;left:54px;right:54px;top:138px;bottom:70px;border-radius:18px;background:rgba(255,255,255,.72);border:1px solid rgba(23,108,130,.14);box-shadow:0 18px 42px rgba(36,71,82,.12);overflow:hidden}
.sidebar{position:absolute;left:0;top:0;bottom:0;width:230px;background:rgba(227,240,244,.72);border-right:1px solid rgba(23,108,130,.12);padding:28px 24px}
.sideitem{height:38px;margin-bottom:13px;border-radius:8px;background:rgba(255,255,255,.8);border:1px solid rgba(23,108,130,.12)}
.workspace{position:absolute;left:260px;right:30px;top:28px;bottom:28px}
.ticket{position:absolute;width:250px;min-height:110px;border:1px solid rgba(23,108,130,.20);background:#fff;border-radius:14px;padding:19px 20px;box-shadow:0 14px 28px rgba(36,71,82,.10)}
.ticket b{display:block;font-size:25px;color:#142026}.ticket span{display:block;margin-top:8px;font-size:16px;color:#5b6b72;line-height:1.5}.ticket em{font-style:normal;font-size:13px;letter-spacing:.18em;color:#176c82;font-weight:800}
.t1{left:0;top:0}.t2{left:288px;top:0}.t3{left:576px;top:0}.t4{left:288px;bottom:0;border-color:rgba(23,108,130,.35)}

#visual.analysis{background:#f6f3ec;color:#171717}
#visual.analysis:before{background:
linear-gradient(90deg,rgba(22,22,22,.06) 1px,transparent 1px),
linear-gradient(0deg,rgba(22,22,22,.05) 1px,transparent 1px),
linear-gradient(135deg,#faf8f2 0%,#ede7da 100%);background-size:54px 54px,54px 54px,auto}
#visual.analysis:after{opacity:.38;background-image:radial-gradient(circle at 78% 20%,rgba(156,56,42,.16),transparent 28%),radial-gradient(circle at 15% 82%,rgba(34,83,91,.14),transparent 30%);mask-image:none}
.analysis .kicker,.analysis .plate,.analysis .step .num{color:#9b3b2f}.analysis .title,.analysis .fig-title,.analysis .step b,.analysis .node b{color:#151515}
.analysis .sub,.analysis .fig-sub,.analysis .node span,.analysis .step span,.analysis .note{color:#5f5a52}
.analysis .plate{border-color:rgba(155,59,47,.34)}.analysis .node,.analysis .step{background:rgba(255,255,255,.78);border-color:rgba(30,30,30,.14);box-shadow:0 16px 34px rgba(46,37,24,.12)}
.analysis .canvas{background:rgba(255,255,255,.55);border-color:rgba(30,30,30,.12)}.analysis .line,.analysis .arrow{background:#9b3b2f}.analysis .pulse{background:radial-gradient(circle,rgba(155,59,47,.16),rgba(155,59,47,.05) 55%,transparent 72%);border-color:rgba(155,59,47,.2)}
.analysis .grain{opacity:.08;mix-blend-mode:multiply}

#visual.product{background:#eef4f7;color:#152026}
#visual.product:before{background:
radial-gradient(460px 300px at 82% 22%,rgba(67,139,162,.24),transparent 58%),
linear-gradient(180deg,#f8fbfc 0%,#e8f1f3 100%)}
#visual.product:after{opacity:.55;background-image:
linear-gradient(90deg,rgba(28,56,67,.065) 1px,transparent 1px),
linear-gradient(0deg,rgba(28,56,67,.055) 1px,transparent 1px);background-size:42px 42px;mask-image:none}
.product .kicker,.product .plate,.product .step .num{color:#176c82}.product .title,.product .fig-title,.product .step b,.product .node b{color:#142026}
.product .sub,.product .fig-sub,.product .node span,.product .step span,.product .note{color:#5b6b72}
.product .plate{border-color:rgba(23,108,130,.32);background:rgba(255,255,255,.55)}.product .node,.product .step{background:rgba(255,255,255,.86);border-color:rgba(23,108,130,.20);box-shadow:0 18px 38px rgba(36,71,82,.14)}
.product .canvas{background:rgba(255,255,255,.62);border-color:rgba(23,108,130,.15)}.product .line,.product .arrow{background:#176c82}.product .pulse{background:radial-gradient(circle,rgba(23,108,130,.18),rgba(23,108,130,.05) 55%,transparent 72%);border-color:rgba(23,108,130,.18)}
.product .grain{opacity:.06;mix-blend-mode:multiply}
"""


def visual_page(width, height, inner, kind):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{VISUAL_CSS}</style></head>
<body><div id="visual" class="{kind}" style="width:{width}px;height:{height}px">{inner}<div class="grain"></div></div></body></html>"""


def render_visual(browser, folder, name, width, height, inner, kind):
    html_path = folder / f"{name}.html"
    png_path = folder / f"{name}.png"
    html_path.write_text(visual_page(width, height, inner, kind), encoding="utf-8")
    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
    page.goto(html_path.resolve().as_uri())
    page.locator("#visual").screenshot(path=str(png_path))
    page.close()
    return png_path


def make_cover(browser, folder, title, subtitle, kind):
    nodes = {
        "report": [("订单", "需求先变"), ("现场", "样本回来"), ("岗位", "补上算法"), ("交付", "结果复购")],
        "analysis": [("搜索", "找到答案"), ("判断", "比较追问"), ("动作", "写回流程"), ("留存", "反复打开")],
        "product": [("风险", "先看卡点"), ("关系人", "找到下一步"), ("证据", "回到来源"), ("动作", "减少切换")],
    }[kind]
    node_html = "".join(
        f'<div class="node n{i+1}"><b>{escape(a)}</b><span>{escape(b)}</span></div>'
        for i, (a, b) in enumerate(nodes)
    )
    inner = f"""<div class="wrap"><div class="kicker">{escape(kind)} · WECHAT ARTICLE</div>
<div class="title">{escape(title)}</div><div class="sub">{escape(subtitle)}</div>
<div class="plate">SAFE CROP 2.35:1</div></div>
<div class="diagram"><div class="pulse"></div><div class="line l1"></div><div class="line l2"></div><div class="line l3"></div><div class="line l4"></div>{node_html}</div>"""
    render_visual(browser, folder, "cover", 1200, 511, inner, kind)


def make_figure(browser, folder, title, subtitle, kind):
    steps = {
        "report": [("01", "设备交付", "硬件进入现场"), ("02", "现场反馈", "异常样本回来"), ("03", "样本整理", "问题变成标签"), ("04", "下次交付", "系统变得更稳")],
        "analysis": [("01", "搜索", "找到候选答案"), ("02", "判断", "比较风险与证据"), ("03", "动作", "写入表格或项目"), ("04", "复用", "下次继续打开")],
        "product": [("01", "风险", "先看卡在哪里"), ("02", "关系人", "找到该问谁"), ("03", "证据", "回到原始来源"), ("04", "动作", "减少内部同步")],
    }[kind]
    if kind == "analysis":
        step_html = "".join(
            f'<div class="milestone m{i+1}"><div class="num">{n}</div><b>{escape(t)}</b><span>{escape(d)}</span></div>'
            for i, (n, t, d) in enumerate(steps)
        )
        inner = f"""<div class="wrap"><div class="kicker">FIG.01 · {escape(kind)}</div>
<div class="fig-title">{escape(title)}</div><div class="fig-sub">{escape(subtitle)}</div></div>
<div class="lane"></div>{step_html}<div class="note">横向链路用来判断:答案之后,动作在哪里发生。</div>"""
    elif kind == "product":
        tickets = "".join(
            f'<div class="ticket t{i+1}"><em>{n}</em><b>{escape(t)}</b><span>{escape(d)}</span></div>'
            for i, (n, t, d) in enumerate(steps)
        )
        inner = f"""<div class="wrap"><div class="kicker">FIG.01 · {escape(kind)}</div>
<div class="fig-title">{escape(title)}</div><div class="fig-sub">{escape(subtitle)}</div></div>
<div class="interface"><div class="sidebar"><div class="sideitem"></div><div class="sideitem"></div><div class="sideitem"></div><div class="sideitem"></div></div>
<div class="workspace">{tickets}</div></div><div class="note">客户页不是字段堆叠,而是下一步动作的排序。</div>"""
    else:
        step_html = "".join(
            f'<div class="step s{i+1}"><div class="num">{n}</div><b>{escape(t)}</b><span>{escape(d)}</span></div>'
            for i, (n, t, d) in enumerate(steps)
        )
        inner = f"""<div class="wrap"><div class="kicker">FIG.01 · {escape(kind)}</div>
<div class="fig-title">{escape(title)}</div><div class="fig-sub">{escape(subtitle)}</div></div>
<div class="canvas"><div class="arrow a1"></div><div class="arrow a2"></div><div class="arrow a3"></div>{step_html}</div>
<div class="note">图前负责铺垫,图中负责解释,图后负责收束。</div>"""
    render_visual(browser, folder, "fig01", 1200, 620, inner, kind)


P = {
    "p": "font-size:16px;line-height:2.05;letter-spacing:.4px;margin:0 0 24px;color:#333;",
    "hno": "font-size:16px;font-weight:700;color:#2A6DF4;margin:46px 0 4px;",
    "h": "font-size:21px;font-weight:700;color:#111;line-height:1.5;margin:0 0 24px;",
    "cap": "font-size:12px;color:#999;text-align:center;margin:10px 0 30px;letter-spacing:.4px;",
}


def para(text):
    return f'<p style="{P["p"]}">{text}</p>'


def section(no, title):
    return f'<p style="{P["hno"]}">{no}</p><p style="{P["h"]}">{title}</p>'


def image(name, cap):
    return (
        f'<img src="{name}" style="width:100%;display:block;border-radius:4px;margin:8px 0 0;">'
        f'<p style="{P["cap"]}">{cap}</p>'
    )


def quote(text, who):
    return (
        '<div style="background:#F7F7F7;border-left:3px solid #D8D8D8;'
        'padding:20px 22px;margin:8px 0 28px;">'
        f'<p style="font-size:15px;line-height:1.95;color:#555;margin:0;">{text}</p>'
        f'<p style="font-size:13px;color:#999;margin:12px 0 0;">{who}</p></div>'
    )


def page(title, subtitle, body):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
body {{ margin:0; background:#f4f4f2; font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif; }}
.phone {{ width:min(390px, 100vw); margin:0 auto; background:#fff; min-height:100vh; }}
.article {{ padding:24px 20px 34px; }}
h1 {{ font-size:24px; line-height:1.35; letter-spacing:0; margin:0 0 18px; color:#111; }}
.subtitle {{ font-size:14px; line-height:1.8; color:#777; margin:0 0 22px; }}
strong {{ color:#111; font-weight:700; }}
.about {{ border-top:1px solid #eee; padding-top:20px; margin-top:40px; }}
.about p {{ font-size:13.5px; line-height:1.9; color:#888; margin:0; }}
</style>
</head>
<body>
<main class="phone"><article class="article">
<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
{body}
</article></main>
</body>
</html>"""


def write_sample(slug, title, subtitle, kind, blocks):
    folder = OUT / slug
    folder.mkdir(parents=True, exist_ok=True)
    html = page(title, subtitle, "\n".join(blocks))
    (folder / "article.html").write_text(html, encoding="utf-8")
    return folder, title, subtitle, kind


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    samples = []
    samples.append(write_sample(
        "report",
        "一家县城工厂,为什么突然开始招聘算法工程师",
        "报道型样文 · 首屏三件套 + 事实冲突 + 人物引语",
        "report",
        [
            image("cover.png", "样文 · 县城工厂的技术岗位"),
            para("六月的最后一周,这家做传感器的小工厂多挂了三个岗位:算法工程师、数据标注主管、现场应用工程师。"),
            para("它没有宣布转型,也没有开发布会。变化先出现在招聘页上。"),
            section("01", "订单变了,岗位先变"),
            para("过去,客户只问交期和价格。现在,客户会把一段产线视频发来,问系统能不能提前识别异常。"),
            para("这类需求让工厂的报价方式发生变化。<strong>硬件仍然是入口,服务开始决定复购。</strong>"),
            image("fig01.png", "FIG 01 · 从硬件交付到现场反馈"),
            para("图里的变化不复杂:设备卖出去之后,数据还会继续回来。真正拉开差距的,是团队能不能把这些反馈变成下一次交付的改进。"),
            section("02", "小团队的优势在现场"),
            para("大公司有平台,小团队有现场。工程师白天在产线调参数,晚上把误报样本整理成下一轮训练集。"),
            quote("“客户不关心模型名字,只关心凌晨两点会不会误停线。”", "—— 样文代拟引语,发布前需确认"),
            para("这也是县城工厂招聘算法工程师的原因。现场问题要被带回系统里,下一次交付才会变得更稳。"),
            '<div class="about"><p>关于样文:本文为排版测试内容,用于验证报道型公众号文章的字号、段距、配图和手机阅读节奏。</p></div>',
        ],
    ))
    samples.append(write_sample(
        "analysis",
        "AI 搜索真正难的,是答案之后的动作",
        "拆解型样文 · 机制解释 + 信息图 + 要点收束",
        "analysis",
        [
            image("cover.png", "样文 · AI 搜索的动作链路"),
            para("过去一年,AI 搜索把“找到答案”变得更快。新的问题也随之出现:答案出来以后,用户下一步做什么?"),
            para("如果系统只停在总结页面,它解决的是检索效率。用户真正花时间的地方,往往在比较、追问、记录和执行。"),
            section("01", "搜索结束后,工作才开始"),
            para("一个采购经理查完供应商名单,还要筛掉交付不稳定的公司,整理邮件,约时间,再把内部评审材料补齐。"),
            para("<strong>答案只是链路的中点。动作能不能接上,决定产品会不会被反复打开。</strong>"),
            image("fig01.png", "FIG 01 · 搜索、判断、动作的三段链路"),
            para("这也是很多 AI 搜索产品开始接入表格、邮件、CRM 和知识库的原因。核心竞争会延伸到查询后的工作流。"),
            section("02", "好入口要减少切换"),
            para("用户每多复制一次内容,每多切一个窗口,系统就多一次被放弃的机会。真正有效的入口,会把下一步动作放在答案旁边。"),
            para("例如,把候选公司直接加入对比表,把风险点生成追问清单,把会议纪要写回项目页。"),
            section("03", "三个判断"),
            para("第一,AI 搜索会从答案页走向工作台。第二,数据连接比模型口号更能留住用户。第三,真正的壁垒来自高频场景里的重复使用。"),
            '<div class="about"><p>关于样文:本文为排版测试内容,用于验证拆解型公众号文章的信息图位置和段落呼吸。</p></div>',
        ],
    ))
    samples.append(write_sample(
        "product",
        "一张客户页,能不能替销售少开三次会",
        "产品技术型样文 · 痛点场景 + 机制解释 + 使用案例",
        "product",
        [
            image("cover.png", "样文 · 销售工作台的客户页"),
            para("销售开会前最耗时间的环节,常常是重新拼一遍客户背景。"),
            para("合同在哪一步、上次谁反对、技术问题有没有解决、预算窗口什么时候关闭,这些信息散在聊天、邮件和表格里。"),
            section("01", "客户页要先回答三个问题"),
            para("第一,这单现在卡在哪里。第二,下一步该找谁。第三,有哪些风险不能再拖。"),
            para("如果客户页只展示字段,销售还是要自己判断。<strong>好的客户页应该把信息整理成行动顺序。</strong>"),
            image("fig01.png", "FIG 01 · 从散点信息到行动顺序"),
            para("图里的重点是顺序:先看风险,再看关系人,最后看下一步动作。这样销售不用从十几个字段里重新推理。"),
            section("02", "技术细节要落到场景"),
            para("系统会读取会议纪要、邮件和 CRM 记录,把重复出现的异议归在一起。预算、竞品、法务、集成问题分别进入不同标签。"),
            para("当销售打开客户页时,页面先给出三条可追问线索,再列出原始证据。这样既能快,也能回到来源。"),
            quote("“销售少问三个人,这个页面才有价值。”", "—— 样文代拟引语,发布前需确认"),
            para("产品价值最终落在节省切换上。少开一次内部同步会,比多一个漂亮看板更容易被记住。"),
            '<div class="about"><p>关于样文:本文为排版测试内容,用于验证产品技术型文章的机制解释和图文衔接。</p></div>',
        ],
    ))
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for folder, title, subtitle, kind in samples:
            make_cover(browser, folder, title, subtitle, kind)
            make_figure(browser, folder, "三个环节决定交付速度", subtitle, kind)
        browser.close()
    print(f"generated samples -> {OUT}")


if __name__ == "__main__":
    main()
