import os, json

import humaneval_uppercase.config as conf
from humaneval_uppercase.llm.invocation import Invocation, Prompt


class LLMAdapter:
    def __init__(self, read_from_cache: bool=True, save_to_cache: bool=True):
        self.cache_dir = conf.llm['llm-invocation-cache-dir']
        self.read_from_cache = read_from_cache
        self.save_to_cache = save_to_cache

    def load_cache(self, prompt: Prompt) -> Invocation | None:
        if not self.read_from_cache:
            return None

        prompt_hash = prompt.hash()
        cached_files = [f for f in os.listdir(self.cache_dir) if os.path.isfile(os.path.join(self.cache_dir, f))
                        and prompt_hash in f]

        if len(cached_files) > 0:
            with open(os.path.join(self.cache_dir, cached_files[0]), 'r') as f:
                return Invocation.load_from_json(json.load(f))

        return None

    def save_cache(self, invocation: Invocation):
        if not self.save_to_cache:
            return

        prompt_hash = invocation.prompt.hash()
        cached_files = [f for f in os.listdir(self.cache_dir) if os.path.isfile(os.path.join(self.cache_dir, f))
                        and prompt_hash in f]

        if len(cached_files) > 0 and self.read_from_cache:
            # It is already loaded from cache, no reason to save it again
            return

        cache_file = os.path.join(self.cache_dir, f"{prompt_hash}-{len(cached_files)}.json")
        with open(cache_file, 'w') as f:
            json.dump(invocation, f, default=lambda o: o.__dict__)