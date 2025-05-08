import os
import openai
from openai import OpenAI
import httpx
from pathlib import Path
from dotenv import load_dotenv

# Try to load API key from .env file in project root
project_root = Path(__file__).parent.parent
env_path = project_root / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# Get API key from environment or use empty string as fallback
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
client = OpenAI(api_key=OPENAI_API_KEY)

def chatgpt(query):
    query_session = [{"role":"user", "content": query}]
    resp = client.chat.completions.create(
        model='gpt-4.1-nano',
        messages=query_session,
        temperature=0.1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    ret = resp.choices[0].message.content
    return ret

if __name__ == '__main__':
    print((chatgpt('怎么用python代码计算第100个质数？')))