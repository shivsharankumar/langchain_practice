"""
Central LLM provider for LangChain (Bedrock + OpenAI)
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from langchain_aws import BedrockLLM

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# ---- Models ----
def get_llm(provider: str = "claude"):
    if provider == "claude":
        return ChatBedrock(
            model_id="us.anthropic.claude-3-sonnet-20240229-v1:0",
            region_name=AWS_REGION,
            model_kwargs={
                "temperature": 0.7,
                "max_tokens": 1000
            }
        )

    elif provider == "openai":
        return BedrockLLM(
            model_id="openai.gpt-oss-20b-1:0",
            region_name=AWS_REGION,
            model_kwargs={
                "temperature": 0.7,
                "max_tokens": 1000
            }
        )
    elif provider == "llama":
        return BedrockLLM(
            model_id="us.meta.llama3-3-70b-instruct-v1:0",
            region_name=AWS_REGION,
            model_kwargs={
                "temperature": 0.7,
                "max_tokens": 1000
            }
        )

    else:
        raise ValueError("Unknown provider")