
# EasyLLM
[中文文档 🇨🇳](./README.zh.md)  
[![PyPI](https://img.shields.io/pypi/v/python-easy-llm?label=PyPI)](https://pypi.org/project/python-easy-llm/0.1.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/chunyoupeng/python-easy-llm?style=social)](https://github.com/chunyoupeng/python-easy-llm)

**EasyLLM** is a lightweight LLM wrapper library that helps you interact with large language models in the most intuitive and natural way.  
Whether it's prompt engineering, structured output, or multi-vendor model access, EasyLLM is designed to make development simpler and more enjoyable.

---

## 🚀 Features

- 🔁 **Unified Interface**: Supports multiple model providers (OpenAI, DeepSeek, Moonshot, Kimi, Claude, etc.) with consistent API usage.
- 🧠 **Prompt-as-Content**: Write prompts in Markdown + Jinja2 instead of verbose `messages` dictionaries.
- 🧩 **Structured Output Support**: Enable JSON-mode to receive structured responses from models — great for product integration.
- 🛠️ **Easy Integration**: Minimal dependencies, easily embedded into any Python project with no learning curve.

---

## 📦 Installation

```bash
pip install python-easy-llm==0.1.2
````

---

## ✨ Quick Example: Calling an LLM

```python
from easyllm import LLM
import os

llm = LLM(
    model_name="deepseek-chat",
    model_provider="deepseek",
    api_key=os.environ["DEEPSEEK_API_KEY"]
)

response = llm("What is 1 + 1?")
print(response)
```

---

## 📄 Example: Structured Output + Jinja2 Prompt Template

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
You are a {{ domain }} assistant. Based on the user's interests and skills, recommend a suitable career path. Please respond in JSON format:
{
  "recommended_job": string,
  "reason": string
}

# User
I'm interested in tech, enjoy programming, and I'm introverted with average communication skills. What job is a good fit for me?
""")

prompt = prompt_t.render(domain="career recommendation")
response = llm(prompt, json_mode=True)
print(response)
```

Sample output:

```json
{
  "recommended_job": "Backend Developer",
  "reason": "You enjoy programming, have strong technical interests, and prefer limited interpersonal interaction. Backend development is a great fit for focusing on system logic and architecture."
}
```

---

## 🔄 Prompt Style Comparison

| Framework   | Prompt Structure     | Complexity | Readability |
| ----------- | -------------------- | ---------- | ----------- |
| OpenAI SDK  | `messages=[...]`     | ⭐⭐         | ❌           |
| LangChain   | `ChatPromptTemplate` | ⭐⭐⭐⭐       | ⭐⭐          |
| **EasyLLM** | Markdown + Jinja2    | ⭐          | ✅✅✅         |

### ✅ Recommended EasyLLM Style

```python
from jinja2 import Template

prompt_t = Template("""
# System
You are a {{ domain }} assistant who helps users solve their problems.
# User
What is 1 + 1?
""")

response = llm(prompt_t.render(domain="math"))
print(response)
```

---

## 🔧 Roadmap / TODO

* [ ] Built-in prompt versioning and template storage
* [ ] Visual Prompt Editor (Prompt Studio)
* [ ] Additional providers (e.g., Tongyi, Zhipu AI, Baichuan)

---

## ❤️ Contributing

We welcome contributions from the community! You can:

* Open issues or submit PRs
* Suggest new prompt templates
* Help improve the documentation or examples

👉 Don’t forget to ⭐️ the repo to support its growth!

---

## 📄 License

MIT License © 2025 \[Chunyou Peng]

---

## 📬 Contact

<!-- * WeChat / Discord Community (Coming soon) -->

* Email: [chunyoupeng@gmail.com](mailto:chunyoupeng@gmail.com)

---

## ⭐️ Project Vision

> "We aim to make EasyLLM the most intuitive tool for building Chinese LLM applications — writing prompts should feel as natural as writing Markdown."