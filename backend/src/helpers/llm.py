import os
from dotenv import load_dotenv
from langchain.chat_models import BaseChatModel
from src.config.app_config import app_settings
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

load_dotenv()
llm: BaseChatModel

if os.getenv('dev'):
    llm = ChatOpenAI(
        base_url=os.getenv('openai_base_url') or "",
        api_key=os.getenv('openai_api_key') or "", #type:ignore
        model=os.getenv('openai_model') or "",
        temperature=0,
        timeout=None,
        max_retries=2,
    )
else:
    llm = ChatGroq(
        model=app_settings.GROQ_MODEL,
        api_key=app_settings.GROQ_API_KEY , #type:ignore
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
    )
