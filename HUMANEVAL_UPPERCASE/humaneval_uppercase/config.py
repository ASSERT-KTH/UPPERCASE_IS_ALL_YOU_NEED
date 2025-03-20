import os
from enum import Enum

class PromptType(Enum):
    SIMPLE = 'SIMPLE'

    def __str__(self):
        return self.value

llm = {
    'llm-invocation-cache-dir': 'cache/llm_invocations',
    'api-url': 'https://openrouter.ai/api/v1',
    'openrouter-api-key': os.environ['OPENROUTER_API_KEY'],
    'default-temp': 0,
    'default-sample-size': 1,
    'default-improvement-iterations': 0,
    'valid-models': ['google/gemini-2.0-flash-lite-preview-02-05:free'],
    'default-model': 'google/gemini-2.0-flash-lite-preview-02-05:free',
    'max-iterations': 10,
    'prompt-template-dir': 'prompt_templates',
}