from openai import OpenAI
from .invocation import *
from .llm_adapter import LLMAdapter


class GeminiFlashLite2(LLMAdapter):
    def __init__(self, read_from_cache: bool=True, save_to_cache: bool=True):
        super().__init__(read_from_cache=read_from_cache, save_to_cache=save_to_cache)
        self.client = OpenAI(
            base_url=llm['api-url'],
            api_key=llm['openrouter-api-key'],
        )

    def get_response(self, prompt: Prompt) -> Response:
        cached_invocation = self.load_cache(prompt)
        if cached_invocation:
            return cached_invocation.response

        completion = self.client.chat.completions.create(
            model="google/gemini-2.0-flash-lite-preview-02-05:free",
            messages=[m.__dict__ for m in prompt.messages]
        )
        response = Response([Response.Sample(c.message.content)
                             for c in completion.choices])

        self.save_cache(Invocation(prompt, response))
        return response