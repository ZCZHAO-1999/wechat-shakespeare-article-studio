# Commercial Image Sourcing / 商用网图规范(白名单、验证、回退、登记)

This guide covers commercial-safe scene and atmosphere images only; all charts and infographics remain original.

信息图/论点图一律原创;本规范只管**实景与氛围图**(头图、人物、场景、质感底图)。

## 一、来源白名单与授权要点
| 来源 | 授权 | 商用 | 署名 | 备注 |
|---|---|---|---|---|
| unsplash.com | Unsplash License | ✅ | 不强制(建议) | 禁止把图原样转售/做竞品图库 |
| pexels.com | Pexels License | ✅ | 不强制 | 禁止出售未改动原图 |
| pixabay.com | Content License | ✅ | 不强制 | 部分 AI 生成图有额外标注,照标注执行 |
| commons.wikimedia.org | 逐图而定 | 视协议 | 视协议 | 只用 CC0 / CC BY / CC BY-SA;**CC *-NC 禁商用**;BY 系必须按页面要求署名 |
| 客户自有图库 / 自有 AI 绘画管线 | 客户自证 | ✅ | — | 首选,零风险 |

## 二、绝对禁用
付费图库预览图(视觉中国、Getty、摄图网、包图网、Shutterstock 水印/无水印预览);
标注 **Editorial use only** 的新闻图;任何品牌/竞品的产品宣传照与 UI 截图;
名人与公众人物肖像;授权不明的可识别人脸用于商业推广;来路不明的"百度图片"结果。

## 三、验证三步(每张网图逐一执行)
1. **找**:用 image_search / web_search 检索候选(英文关键词命中率更高,如
   "home robot interior unsplash");
2. **核**:web_fetch 打开该图在白名单站点的**详情页**,确认站点与授权标识,
   记录页面 URL;不是白名单站点直出的图(如被第三方转载)一律弃用;
3. **登**:发布说明「图片来源与授权」表登记:文件名 / 详情页 URL / 协议名 /
   是否需署名;需署名的在文中图注写"图:作者名 / 平台"。

## 四、下载与回退
```bash
curl -L -o photo1.jpg "https://images.unsplash.com/photo-...&w=1600"
```
- 下载成功 → 压到宽 ≤1600px、JPEG q85(照片可用 JPEG;信息图仍 PNG)→ 内嵌进 docx/HTML;
- **域名被环境网络策略拦截**(常见)→ 正文该位置放虚线占位框(写明画面主题与建议尺寸),
  发布说明给出图片直链 + 详情页链接,编辑在 Word 里 30 秒替换;
- 无合适商用图 → 降级为原创生成的氛围图,或给用户 AI 绘画提示词。

## 五、尺寸与质感
头图/封面 ≥1200px 宽(封面 2.35:1 裁切);正文横图 ≥1000px;避免竖图与强水印感构图;
同篇网图色调统一(冷/暖二选一),必要时统一加 5–8% 暗角压色以贴合信息图族。
