---
name: wechat-article-studio
description: Produce one publish-ready WeChat article package from a Chinese or English draft: Word-first layout, phone-readable typography, clear paragraph rhythm, disciplined image placement, commercial-safe visuals, paste-ready HTML, and release notes. / 将中文或英文草稿生产为一套可发布的微信公众号交付包:以 Word 为主交付,严格控制字号、段距、配图、阅读呼吸、HTML 备份和发布说明。 Use this workflow whenever the user mentions 公众号, 推文, 微信文章, WeChat article, 排版, 配图, 作图, 头图, 封面图, 信息图, or pastes/uploads a draft and wants it formatted, illustrated, or made publishable.
---

# WeChat Article Studio / 公众号一次成稿流水线

> English: This workflow turns a draft into a phone-readable WeChat article package, with Word as the main delivery format.
>
> 中文：这套工作流的目标，是把草稿生产成一份能顺畅阅读、能直接粘贴进公众号后台的成稿包。

**主交付只有一个:《文章名》.docx——字号、段距、图文节奏全部预设,图片全部内嵌,打开 → 全选 → 复制 →
粘贴进公众号编辑器 → 发布。** 其余为随附:article.html(等价备选粘贴源)、高清 PNG、
发布说明.txt、zip。docx 缺席 = 任务未完成。

## Quality Bar / 质量基座

本工作流的根本目标是**阅读体验**。优先级如下:

1. 手机阅读通畅:字号、行距、段后距、图文间隔、首屏信息密度必须稳定。
2. 图文协同:每张图承担封面、解释、证据、转场或情绪功能,禁止装饰性堆图。
3. 呼吸感:段落短,但不碎;连续三屏不能只有文字墙,也不能被图片打断逻辑。
4. 内容可信:数字有来源清单,判断有事实支撑,敏感信息不上标题与图。
5. 去 AI 腔:禁止模板化转折、空泛宏大词、机械排比和"不是 A,而是 B"式句法。

## Workflow / 工作流(按序执行)

### 0. 读规范
先读 `references/wechat-layout-patterns.md`(公众号排版范式,通读)、
`references/layout-wechat.md`(排版、字号、呼吸感是本工作流的核心,通读)与
`references/writing-patterns.md`(财经科技写作模式,通读)、
`references/source-quality.md`(背景搜索与顶尖来源规范,涉及搜索时强制)、
`references/editorial.md`(含 AI 腔消毒);规划配图时读 `references/visual-production.md`(多模态/纯代码配图路线)、
`references/design-system.md`(信息图)与
`references/images-sourcing.md`(商用网图)。规范是硬约束。
交付前必须读 `references/release-gate.md` 并逐项通过上线门槛。

### 1. 吃透草稿
通读原稿;抄录**数字与事实清单**;标记敏感表述;确认口吻档位(叙事体/拆解体,
判据见 editorial.md);用户给了参照文则以参照文呼吸感为准。

### 2. 编辑重构
定结构(冷开场 → 编号章节 → 引语/互动句 → 关于栏);写主标题 + 3 备选 + ≤120 字摘要。
**数字纪律**:只用清单内数字,缺则『◻◻』占位并上报;敏感对比只进行文、带缓冲语、
永不进图与标题。
成稿后执行 `editorial.md` 的 AI 腔消毒:删掉模板转折、口号词、连续抽象名词和空泛收束句。

### 3. 图像规划(两类分治)
- **信息图**(论点图):一律原创生成,选型与规范见 design-system.md;
- **实景/氛围图**(头图、人物、场景):优先商用授权网图,按 images-sourcing.md
  三步验证(免费商用源 → 逐图核对授权 → 发布说明登记);下载被网络策略拦截时
  走占位框 + 直链清单回退。用户有自己的 AI 绘画管线时,给占位框 + 现成提示词。
写出图像清单(编号/功能/论点或画面/来源方式/插入位置/前后段落)再动手。

### 4. 产图
```bash
bash scripts/setup_fonts.sh
cp scripts/fig_scaffold.py work/ && cd work
python3 ../scripts/render.py figX.html figX.png   # 信息图,2x
```
网图按 images-sourcing.md 下载核验。**每张图(含网图)必须 view 检查**;
信息图统一 FIG 01/0N 编号,中途增删则全系列重编。

### 5. Word 排版(主交付,不可省)
`npm i docx`,按 layout-wechat.md 第一节的 Word-first 排版规范 + `scripts/docx_scaffold.js`
助手组装:文首大标题(供填入标题栏)→ 头图 → 正文(节奏、金句加粗、强调色、
引语块、分隔符)→ 关于栏。所有图内嵌。
排版完成后按 `layout-wechat.md` 的"手机阅读流 QA"逐屏检查。

### 6. HTML 备份
按 layout-wechat.md 的段落模板出 article_src.html,
`python3 scripts/embed_images.py article_src.html article.html` 生成单文件。

### 7. QA(三道,全部强制)
① 每图 view;② docx → soffice 转 PDF → pdftoppm 页图 → 拼 contact sheet → view 全页
(图未裁切、引语底色连续、页码合理、粗体密度、每屏留白);③ HTML 整页截图切片 view;
④ 通读一遍最终文案,清除 AI 腔和阅读卡顿;⑤ 按 `release-gate.md` 做上线检查。

### 8. 交付
发布说明.txt(标题/摘要/粘贴流程/图片清单**含网图来源与授权**/口径提示)+
全部文件入输出目录 + zip;呈现时 **docx 第一位**。

## Hard Rules / 硬规则
1. 不编数字;清单外数字一律占位上报。
2. 背景搜索只使用顶尖、可信、可追溯来源;禁用随机 SEO、无来源博客、AI 摘要、来路不明数据。
3. 网图必须商用授权可验证:仅限 images-sourcing.md 白名单来源,逐图核对授权页,
   来源与协议写进发布说明;付费库预览图、editorial-only、品牌宣传照一律禁用。
4. 竞品/敏感数字:仅行文 + 缓冲语,不进图、封面、标题、摘要。
5. 多业务默认平行呈现;"主线"字样须作者点头。
6. 三道 QA 不许省。
7. 代拟引语标注"发布前请本人确认";同号跨文不复用引语。
8. 出现"不是 A,而是 B"、"本质上"、"赋能"、"闭环"、"重塑"等模板腔,默认改写或删除。
9. 示例图只是 QA fixture;正式交付图不能是通用节点图,必须包含文章专属机制、证据、场景或产品结构。

## File Map / 文件地图
| 文件 | 用途 |
|---|---|
| `references/wechat-layout-patterns.md` | **核心**:公众号排版范式、手机阅读流、首屏、配图节奏、版式模型 |
| `references/writing-patterns.md` | **核心**:财经科技写作模式、开场、信息阶梯、小标题、段落推进 |
| `references/source-quality.md` | **核心**:背景搜索、顶尖来源、弱来源禁用、搜索记录 |
| `references/layout-wechat.md` | **核心**:docx 排版、字号、段距、粘贴流程、HTML 模板、QA、发布说明模板 |
| `references/visual-production.md` | **核心**:多模态作图、无多模态纯代码作图、视觉质量标准 |
| `references/release-gate.md` | **核心**:最终上线门槛、内容/视觉/排版/交付 QA |
| `references/editorial.md` | 口吻档位、结构库、标题/摘要公式、数字纪律 |
| `references/design-system.md` | 信息图设计系统(token、五种图型、渲染坑) |
| `references/images-sourcing.md` | 商用网图:白名单、验证三步、下载与回退、登记格式 |
| `scripts/` | render.py / setup_fonts.sh / fig_scaffold.py / embed_images.py / docx_scaffold.js |

## Output Contract / 输出契约
docx(主)+ PNG 原图 + article.html + 发布说明 + zip,一个都不能少。
