# EasyLLM

[![PyPI](https://img.shields.io/pypi/v/python-easy-llm?label=PyPI)](https://pypi.org/project/python-easy-llm/0.1.0/)

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[![Stars](https://img.shields.io/github/stars/chunyoupeng/python-easy-llm?style=social)](https://github.com/chunyoupeng/python-easy-llm)

**EasyLLM** 是一个轻量级的 LLM 封装库，帮助你用最直观、最自然的方式调用大语言模型。  
无论是提示词编排、结构化输出，还是跨厂商模型调用，EasyLLM 都旨在让开发更高效、更愉悦。

---

## 🚀 特性亮点

- 🔁 **统一接口**：支持多个模型厂商（OpenAI、DeepSeek、Moonshot、Kimi、Claude 等），API 风格统一。
- 🧠 **提示词即内容**：使用 Markdown 和 Jinja2 写提示词，不再被 `messages` 字典困扰。
- 🧩 **结构化输出支持**：支持 JSON 模式，增强模型可控性，适配各类产品需求。
- 🛠️ **易集成**：依赖极少，可嵌入任意 Python 项目，无需重学习曲线。

---

## 📦 安装

```bash
pip install python-easy-llm==0.1.2
````

---

## ✨ 快速示例：调用大模型

```python
from easyllm import LLM
import os

llm = LLM(
    model_name="deepseek-chat",
    model_provider="deepseek",
    api_key=os.environ["DEEPSEEK_API_KEY"]
)

response = llm("1 + 1 是多少？")
print(response)
```

---

## 📄 示例：结构化输出 + Jinja2 模板

```python
from jinja2 import Template
from easyllm import LLM
import os

llm = LLM(
    model_name="deepseek-chat",
    model_provider="deepseek",
    api_key=os.environ["DEEPSEEK_API_KEY"]
)

prompt_t = Template("""
# System
你是一个{{ domain }}助手，根据用户的兴趣和技能推荐合适的职业方向。请以 JSON 格式返回：
{
  "recommended_job": string,
  "reason": string
}

# User
我对技术感兴趣，喜欢编程，沟通能力一般，有点社恐，适合什么职业？
""")

prompt = prompt_t.render(domain="职业推荐")
response = llm(prompt, json_mode=True)
print(response)
```

输出示例：

```json
{
  "recommended_job": "后端开发工程师",
  "reason": "你喜欢编程、擅长技术，且对沟通要求较低，后端开发更适合你专注于逻辑和架构设计。"
}
```

---

## 🔄 提示词编写风格对比

| 框架          | 调用方式                 | 复杂度  | 可读性 |
| ----------- | -------------------- | ---- | --- |
| OpenAI SDK  | `messages=[...]`     | ⭐⭐   | ❌   |
| LangChain   | `ChatPromptTemplate` | ⭐⭐⭐⭐ | ⭐⭐  |
| **EasyLLM** | Markdown + Jinja2    | ⭐    | ✅✅✅ |

### ✅ EasyLLM 推荐风格

```python
from jinja2 import Template

prompt_t = Template("""
# System
你是一个{{ domain }}助手，帮助用户解决他提出的问题
# User
1+1 = ?
""")

response = llm(prompt_t.render(domain="数学"))
print(response)
```

---

## 🔧 待开发功能（TODO）

* [ ] 内置提示词版本管理和存储机制
* [ ] 视觉提示词编辑器（Prompt Studio）
* [ ] 更多厂商支持（阿里通义、智谱清言、百川等）

---

## ❤️ 贡献指南

我们欢迎所有的贡献者！你可以通过以下方式参与：

* 提交 Issue 或 PR
* 推荐新的 Prompt 模板
* 帮助我们完善文档或样例

👉 Star 一下支持项目成长！

---

## 📄 License

MIT License © 2025 \[Chunyou Peng]

---

## 📬 联系我们 / 加群讨论

<!-- * 微信交流群/Discord（待补充） -->
* 邮箱：[chunyoupeng@gmail.com](mailto:chunyoupeng@gmail.com)

---

## ⭐️ 项目愿景

> “我们希望 EasyLLM 成为中文 LLM 应用开发最顺手的工具之一，就像你写 Markdown 一样自然地写提示词。”
