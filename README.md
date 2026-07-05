# WeChat Article Studio

一套用于生产微信公众号成稿的 Codex skill。核心交付是一份排好版、嵌好图、可直接复制进公众号后台的 Word 文档。

A Codex skill for producing WeChat article packages from Chinese or English drafts. The main deliverable is a Word document with controlled typography, embedded visuals, and a paste-ready publishing flow.

## 核心标准 / Core Standard

好文章最终落在阅读体验上:

- 排版有范式:先判断报道型、拆解型、访谈/人物型或产品/技术型,再套对应阅读节奏。
- 字号稳定:正文、章节、小标题、图注和引语各有固定层级。
- 呼吸稳定:段落长度、段后距、图前图后留白都要能在手机上顺着读。
- 配图有职责:封面负责第一眼,信息图负责解释,场景图负责转场或补充现场感。
- 内容去 AI 腔:清理模板化转折、空泛宏大词、机械排比和万能收束句。
- 交付能直接用:Word、HTML、图片原图、发布说明和 zip 一起交付。

The standard is not measured by length or ornament. It is measured by whether a reader can keep moving through the article without friction, and whether an editor can publish the package without rebuilding it.

## 参考对象 / Reference Set

This workflow studies the shared production habits of strong Chinese finance and technology publishers: sharp entry points, concrete information, source discipline, clean section logic, and image-supported reading.

这套工作流参考财经、科技、创投内容里的成熟做法:题眼清楚,信息具体,判断克制,结构顺滑,图文关系明确。它不复刻某一家媒体的腔调,只吸收可迁移的生产标准。

## 产出 / Deliverables

- `文章名.docx`: main deliverable, built for copy-paste publishing in the WeChat editor.
- `article.html`: paste-ready HTML backup with images embedded.
- `cover + figX.png`: cover and infographic originals.
- `发布说明.txt`: title, summary, image list, licensing notes, wording cautions, and publishing steps.
- `zip`: packaged final delivery.

## 工作流 / Workflow

1. Read the draft, extract facts, figures, names, claims, and sensitive details.
2. Set the article rhythm: opening, sections, quotes, images, summary, and closing note.
3. Remove AI-like prose patterns and replace vague language with concrete facts or scenes.
4. Plan image placement before rendering: each visual needs a role and a position.
5. Assemble the Word document with fixed type hierarchy, spacing, captions, and embedded images.
6. Export the HTML backup and run QA on images, Word pages, and mobile-width reading flow.
7. Package everything with release notes.

## 质量检查 / Quality Checks

- No unverified numbers.
- No sensitive claims in titles, summaries, covers, or infographics.
- No decorative images without a reading function.
- No long text wall across more than six consecutive paragraphs.
- No abrupt image insertion without a setup paragraph and a follow-up sentence.
- No common AI tics such as binary reversal formulas, empty business jargon, or repetitive sentence scaffolds.

## 仓库结构 / Repository Structure

- [SKILL.md](SKILL.md): core execution protocol.
- [references/wechat-layout-patterns.md](references/wechat-layout-patterns.md): WeChat layout patterns, mobile reading rhythm, and article archetypes.
- [references/editorial.md](references/editorial.md): voice, structure, title, summary, and AI-prose cleanup.
- [references/layout-wechat.md](references/layout-wechat.md): Word layout, typography, spacing, HTML backup, and QA.
- [references/design-system.md](references/design-system.md): visual system and image responsibilities.
- [references/images-sourcing.md](references/images-sourcing.md): commercial image sourcing and license verification.
- [scripts/](scripts): helpers for rendering, image embedding, font setup, and Word assembly.

## 最终目标 / Goal

Draft in. Publishable WeChat package out.

草稿进入流程,交付出来的是一份能读、能看、能复制、能发布的公众号成稿包。
