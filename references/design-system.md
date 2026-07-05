# Infographic Design System / 图表设计系统

This guide defines the shared visual language for deterministic infographics, covers, and supporting visuals. Read `visual-production.md` first to choose between multimodal image generation and deterministic HTML/SVG production.

目标:同一篇文章的所有图像出自同一套视觉语言,单张可截图传播,整组像一个系列。视觉语言必须按项目微调,不要所有文章都使用暗底科技风。
脚手架 `scripts/fig_scaffold.py` 已实现本规范的 token 与组件,直接 import 使用。无多模态图像能力时,默认使用 HTML/SVG/Playwright 生成图,禁止交付占位式暗色标题框。

## 一、Token
| 名称 | 值 | 用途 |
|---|---|---|
| --bg | #08090D | 画布底,叠 radial 顶部微光 |
| --panel / --panel2 | #0E1118 / #10141C | 卡片底 |
| --ink | #F2EFE7 | 主文字(暖白) |
| --dim / --faint | #A9AEB9 / #61687A | 次级/最弱文字 |
| --hair | rgba(242,239,231,.10) | 发丝边框 |
| --ice / --ice-bright | #8FC6E8 / #D4EBF9 | 品牌强调(可整体替换为客户品牌色) |
| --glow | rgba(143,198,232,.36) | 英雄卡外发光 |
字体:标题 CJK = Noto Sans CJK SC 700;英文/数字 = Archivo(大数字 800);
标签/编号 = JetBrains Mono(letter-spacing .2–.34em,uppercase)。
质感:全画布叠 4.5% fractalNoise grain + 边缘 vignette(脚手架自带)。

## 二、画布
- 逻辑宽 1000px,高按密度 460–720px;render.py 以 2x 输出(2000px 宽)。
- 内边距 wrap:44px 52px 40px;上下结构 = 头部 hd + 内容 + 底部 ft。
- 头部:左侧 CJK 标题 27px/700 + 英文眉 mono 11px;右侧 `FIG. 0X / RIGHTWAY式品牌名`。
- 底部:左侧一句话 note(可含加粗),右侧 mono `FIG 0X / 0N`。
- 封面:2.35:1(如 2400×1022),左对齐文字块 ≤60% 宽 + 右侧主视觉 + 底部 plate 行。

## 三、五种图型(一图一论点)
| 图型 | 适用论点 | 组件 |
|---|---|---|
| 双栏对照 | 两条路线/两种生意,主角在右 | `bizcol()`:普通列 + hero 列(冰蓝描边+外发光+角标 chip),行结构 LABEL/值,底部"距离圆点"1–3 档 |
| 反馈回路 | 系统怎么运转/自增强 | SVG:四站点矩形置四角,顺时针细箭头;**回流边**用亮色加粗并标注论点句;中心 radial 光 + 引擎名;可加底部 strip 金句条 |
| 英雄数字 | 一个碾压性指标 | hero 面板(74px Archivo 800 数字 + 发光)+ 右侧 2×2 chips(mono 标签 + 23px 数字 + 说明) |
| 平行网格 | 多场景/多业务等权 | 顶部引擎横条(居中,机制一句话)+ 3×N 等卡(mono 眉 + 16px 题 + 11.5px 注);状态卡只加小 chip(如"联合研发中"),不给视觉特权 |
| 问题—方案对比 | 朴素做法 vs 我们的做法 | 左 panel 拥挤碎片(轻微旋转、允许溢出裁切表达"挤压")+ 右 hero panel 内嵌 SVG 树(根节点 + 分支卡,亮色新分支) |

## 四、构图守则
1. 每图一个论点;论点写进头部标题或底部 note,二选一强化,不重复。
2. hero 元素全图唯一;平行语义时**任何卡都不做 hero**。
3. 敏感/竞品数字不进图(editorial.md 硬规则)。
4. 图内文案 ≤ 正文对应段的 1/3;能用结构表达就不用文字。
5. 中英混排:CJK 主信息,EN mono 做眉/标注;英文全大写 + 宽字距。
6. 系列一致:同 token、同头尾、连续 FIG 编号、同一图注格式。

## 五、配图职责

每张图生成前先写清它在文章里的职责。职责不清,不产图。

| 职责 | 放置位置 | 判断标准 |
|---|---|---|
| 封面/头图 | 标题后 | 一眼给出行业、主角或情绪,适合微信列表裁切 |
| 解释图 | 机制段后 | 读者看完能更快理解系统如何运转 |
| 证据图 | 数据/案例段后 | 承载公开数据或非敏感指标,减少正文解释负担 |
| 转场图 | 长节之间 | 缓冲阅读疲劳,但不能替代论证 |
| 收束图 | 结尾前 | 强化最终判断或业务全景 |

图的作用是降低理解成本,并让读者更愿意继续往下滑。

## 六、常见渲染坑
- CJK + letter-spacing 会撑宽:标题 .06em 内,正文标签 ≤.05em。
- 溢出裁切只允许在"表达拥挤"的问题面板;其余 panel 文案先量宽。
- SVG text 需显式 font-family(继承常失效);箭头用 marker,勿手画三角。
- 深色渐变导出 JPEG 会 banding:一律 PNG。
- 中途增删图:全系列 FIG 0X/0N 重编 + 重渲染,勿只改单张。

## 七、品牌化
换客户品牌:改 :root 的 --ice/--ice-bright/--glow(建议取品牌色的 65% 亮度冷调变体),
其余 token 不动;封面 kicker/plate 换品牌名与系列名。整套即迁移完成。
