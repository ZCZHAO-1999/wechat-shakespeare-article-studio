// docx-js scaffold / Word layout helper: see references/layout-wechat.md for the style map.
// npm i docx, then assemble kids from the content blocks.
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, ImageRun,
        AlignmentType, BorderStyle, ShadingType } = require("docx");
const YA = "Microsoft YaHei";
const R = (t) => new TextRun({ text: t, font: YA, size: 22, color: "333333" });
const B = (t) => new TextRun({ text: t, font: YA, size: 22, color: "111111", bold: true });
const A = (t) => new TextRun({ text: t, font: YA, size: 22, color: "2A6DF4", bold: true }); // 强调色,全文≤4处
const divider = () => new Paragraph({ children: [new TextRun({ text: "\u00B7 \u00B7 \u00B7", font: YA, size: 22, color: "CCCCCC" })], alignment: AlignmentType.CENTER, spacing: { before: 300, after: 300 } });
const body = (runs) => new Paragraph({ children: runs, spacing: { line: 380, after: 260 } });
const secNo = (n) => new Paragraph({ children: [new TextRun({ text: n, font: YA, size: 22, color: "2A6DF4", bold: true })], spacing: { before: 480, after: 80 } });
const secTitle = (t) => new Paragraph({ children: [new TextRun({ text: t, font: YA, size: 28, color: "111111", bold: true })], spacing: { after: 280 } });
const caption = (t) => new Paragraph({ children: [new TextRun({ text: t, font: YA, size: 18, color: "999999" })], alignment: AlignmentType.CENTER, spacing: { before: 100, after: 340 } });
const img = (name, h) => new Paragraph({ children: [new ImageRun({ type: "png", data: fs.readFileSync(name), transformation: { width: 605, height: h } })], alignment: AlignmentType.CENTER, spacing: { before: 120, after: 40 } });
const qOpts = { shading: { type: ShadingType.CLEAR, fill: "F7F7F7" },
  border: { left: { style: BorderStyle.SINGLE, size: 28, color: "D8D8D8", space: 14 } },
  indent: { left: 280, right: 280 } };
const quote = (t, who) => [
  new Paragraph({ ...qOpts, children: [new TextRun({ text: t, font: YA, size: 21, color: "555555" })], spacing: { before: 160, after: 0, line: 340 } }),
  new Paragraph({ ...qOpts, children: [new TextRun({ text: who, font: YA, size: 19, color: "999999" })], spacing: { before: 60, after: 320, line: 300 } })];
// —— 组装示例 ——
// const kids = [];
// kids.push(secNo("01")); kids.push(secTitle("章节标题"));
// kids.push(body([R("正文,"), B("金句加粗。")]));
// kids.push(img("figA.png", 363)); kids.push(caption("品牌 · 图注"));
// kids.push(...quote("\u201C引语\u201D", "—— 署名,头衔"));
// new Document + Packer.toBuffer 写出;图高 = 605 * 原图高/原图宽。
module.exports = { R, B, A, divider, body, secNo, secTitle, caption, img, quote,
  makeDoc: (kids) => new Document({
    styles: { default: { document: { run: { font: YA, size: 22, color: "333333" } } } },
    sections: [{ properties: { page: { margin: { top: 1134, bottom: 1134, left: 1418, right: 1418 } } }, children: kids }]
  }), Packer };
