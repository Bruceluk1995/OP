# 图像 API fallback

只在运行时没有原生图像生成/编辑工具时使用。优先兼容 OpenAI Images API；代理端点可能忽略尺寸参数，最终仍要按平台比例裁切验收。

## 环境变量

| 变量 | 必填 | 默认 |
|---|---|---|
| `GPT_IMAGE_API_KEY` | 是 | — |
| `GPT_IMAGE_BASE_URL` | 否 | `https://api.openai.com/v1` |
| `GPT_IMAGE_MODEL` | 否 | `gpt-image-2` |
| `GPT_IMAGE_SIZE` | 否 | 按平台规格 |
| `REF_IMAGE` | 否 | 提供时走图生图 |

## 调用守卫

- 文生图使用 `/v1/images/generations`；参考图编辑使用 `/v1/images/edits` multipart。
- 用 JSON 库构造请求体，不手拼包含中文、引号和换行的 JSON 字符串。
- 检查 HTTP 状态、`.error`、输出字段和文件非空，再写最终文件。
- 不把错误 JSON 解码成 PNG；不覆盖旧文件；提示词与参考图来源一并保存。
- 代理返回比例不符时等比缩放后裁切，不拉伸。
- API 不可用时降级为 prompt-only，不循环付费重试。

## 文字策略

API 生成图中的中文/日文必须逐字核对。标题较长或第一次生成有错字时，停止让模型反复赌文字，改为无字底图 + `scripts/overlay_cover_text.py`。
