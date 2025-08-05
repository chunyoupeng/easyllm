from typing import List, Dict
def parse_to_openai_messages(text: str) -> List[Dict]:
    messages = []
    current_role = None
    current_content = []

    roles = ['system', 'user', 'assistant']
    lines = text.splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and stripped[2:].lower() in roles:
            # 如果已有旧内容，保存到消息列表
            if current_role and current_content:
                messages.append({
                    "role": stripped[2:].lower(),
                    "content": "\n".join(current_content).strip()
                })
            # 开始新的块
            current_role = stripped[2:].lower()
            current_content = []
        elif current_role:
            current_content.append(line)

    # 添加最后一块内容
    if current_role and current_content:
        messages.append({
            "role": current_role,
            "content": "\n".join(current_content).strip()
        })

    return messages

if __name__=='__main__':
    text = """
    # System
    你是一个AI助手

    # User
    今天天气怎么样？

    # Assistant
    今天天气晴朗，气温 28 度。
    """

    msgs = parse_to_openai_messages(text)
    from pprint import pprint
    pprint(msgs)
