import os

from dotenv import load_dotenv


load_dotenv()


AI_PROVIDER = os.getenv("AI_PROVIDER", "groq")
AI_MODEL = os.getenv("AI_MODEL", "")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

SUPPORTED_PROVIDERS = {
    "groq",
    "openai",
    "gemini",
}


if AI_PROVIDER not in SUPPORTED_PROVIDERS:
    raise ValueError(
        f"Unsupported AI provider: {AI_PROVIDER}"
    )