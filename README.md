# WeChat Shakespeare Article Studio

Top-tier WeChat article workflow for Claude Code, Claude CLI, Codex CLI, and other local writing agents.

一套面向微信公众号深度稿、财经科技稿、产品分析稿的 agent-ready 写作与排版工作流。目标是把一个主题或草稿推进到可发布的完整成稿包：正文、标题、封面、信息图、HTML 预览、发布说明和质量检查。

## Why This Exists

Most AI writing workflows stop too early.

They can produce paragraphs, but they often fail at the parts that decide whether an article can actually be published:

- opening tension
- evidence discipline
- paragraph rhythm
- mobile reading flow
- typography hierarchy
- cover and infographic quality
- source notes and publishing cautions
- removing AI-like sentence patterns

This repository turns those requirements into a repeatable workflow.

## What It Produces

Core package:

- `final.md`: edited article, source notes, and image placement.
- `wechat-ready.html`: mobile-readable WeChat-style preview.
- `assets/cover.svg`: article-specific cover visual.
- `assets/*.svg`: timelines, mechanism diagrams, data cards, or explainers.
- optional `.docx`: Word-first publishing package when the agent runtime supports document assembly.
- optional `publishing-note.txt`: title set, summary, source cautions, image list, and paste steps.

Example now included:

- [Fable 5 被封禁，智谱冲万亿：模型采购进入双供应商时代](examples/fable-zhipu/final.md)
- [WeChat HTML preview](examples/fable-zhipu/wechat-ready.html)

## Editorial Standard

The standard is reading experience, not length.

A publishable article should have:

- a first screen that makes the reader understand why the topic matters now
- a clear information ladder, not a list of loosely connected opinions
- short but not choppy paragraphs
- numbers that come from traceable sources
- titles and covers that do not overclaim sensitive facts
- visuals that explain the article, not decorate it
- enough white space for phone reading
- no obvious AI scaffolding such as “not only A, but also B”

## Visual Standard

Visuals must be article-specific.

Good visuals in this workflow can be:

- cover cards with the article’s actual mechanism or tension
- event timelines
- causal loops
- market maps
- comparison tables
- source-backed data charts
- quote/data cards

Bad visuals are rejected:

- generic dark node diagrams
- decorative abstract backgrounds
- charts without a real data question
- stock images without verified commercial rights
- repeated visual templates across unrelated articles

## Source Standard

Background research must use top-tier sources only.

Allowed sources include:

- company official announcements and documentation
- regulators, courts, government agencies, and standards bodies
- primary research institutions and datasets
- audited public filings
- reputable business, technology, or financial media with named reporting

Rejected sources include:

- random SEO articles
- unsourced blog posts
- AI-summary pages
- repost farms
- screenshots with no original source
- vague “industry data says” claims

See [references/source-quality.md](references/source-quality.md).

## How To Use

Start here:

- [SKILL.md](SKILL.md)

Recommended agent flow:

1. Read [references/source-quality.md](references/source-quality.md) before any search.
2. Read [references/writing-patterns.md](references/writing-patterns.md) to choose the article structure.
3. Read [references/wechat-layout-patterns.md](references/wechat-layout-patterns.md) before layout.
4. Read [references/visual-production.md](references/visual-production.md) before creating images.
5. Read [references/release-gate.md](references/release-gate.md) before delivery.

Compatible with:

- Claude Code
- Claude CLI
- Codex CLI
- local agent runners that can read files, search, edit Markdown/HTML, create images, and run scripts

Search keywords:

- WeChat article workflow
- WeChat article layout
- Claude Code writing skill
- Claude CLI article workflow
- Codex CLI writing workflow
- AI agent WeChat writing
- Chinese finance technology article layout

## Repository Structure

- [SKILL.md](SKILL.md): execution protocol for agents.
- [references/source-quality.md](references/source-quality.md): source rules for background research.
- [references/writing-patterns.md](references/writing-patterns.md): finance, technology, venture, and product writing patterns.
- [references/wechat-layout-patterns.md](references/wechat-layout-patterns.md): mobile reading rhythm and WeChat layout archetypes.
- [references/visual-production.md](references/visual-production.md): multimodal and code-native visual production rules.
- [references/release-gate.md](references/release-gate.md): final go-live quality gate.
- [examples/fable-zhipu](examples/fable-zhipu): complete article example with HTML preview and SVG visuals.
- [scripts](scripts): helpers for rendering figures and layout samples.

## Quality Gate

Before release, the output must pass:

- no unsupported numbers
- no weak or random background sources
- no title/cover overclaiming
- no generic final visuals
- no long wall of text across multiple phone screens
- no abrupt image insertion
- no obvious AI-prose patterns
- no missing source list
- no broken image path in HTML preview

## Goal

Draft in. Publishable WeChat package out.

草稿进入流程，交付出来的是一份能读、能看、能复制、能发布的公众号成稿。
