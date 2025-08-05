import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from easyllm.core.models.model  import LLM
api_key = os.getenv("api_key")
llm = LLM(model_name="qwen-plus", model_provider="aliyun", api_key=api_key)

print(llm("hi"))

t = """
# system
You r a helpful math teacher
# user 
1+1=?
"""

t2 = """
# System
You r a helpful math teacher
# User 
1+1=?
"""

print(llm(t))
print(llm(t2))