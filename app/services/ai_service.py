import litellm

from app.config import AI_MODEL, AI_PROVIDER


class AIService:
    """
    All AI interactions go through this class.
    Nothing outside this class touches LiteLLM directly.
    """
    def __init__(self):
        self.provider = AI_PROVIDER
        self.model = AI_MODEL

    def chat(self, message: str) -> str:
        try:
            response = litellm.completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
            )

            return response.choices[0].message.content

        except litellm.RateLimitError:
            raise RuntimeError(
                "The AI provider is currently rate limited."
            )

        except litellm.AuthenticationError:
            raise RuntimeError(
                "AI provider authentication failed."
            )

        except litellm.NotFoundError:
            raise RuntimeError(
                "The configured AI model was not found."
            )

        except litellm.APIError:
            raise RuntimeError(
                "The AI provider returned an API error."
            )