import time
from humaneval_uppercase.config import llm
from typing import List
import json
import hashlib

class Prompt:
    class Message:
        def __init__(self, role: str, content: str):
            self.role = role
            self.content = content

        @staticmethod
        def load_from_json(j):
            return Prompt.Message(j['role'], j['content'])

    def __init__(self, messages: List[Message], temp: float = llm['default-temp'],
                 sample_size: int = llm['default-sample-size'], model: str = llm['default-model']):
        self.messages = messages
        self.temp = temp
        self.sample_size = sample_size
        self.model = model

    def hash(self):
        return hashlib.md5(str(json.dumps(self, default=lambda o: o.__dict__)).encode('utf-8')).hexdigest()

    @staticmethod
    def load_from_json(j):
        return Prompt([Prompt.Message.load_from_json(m) for m in j['messages']],
                      j['temp'],
                      j['sample_size'])

class Response:
    class Sample:
        def __init__(self, content: str):
            self.content = content

        @staticmethod
        def load_from_json(j):
            return Response.Sample(j['content'])

    def __init__(self, samples: List[Sample]):
        self.samples = samples

    @staticmethod
    def load_from_json(j):
        return Response([Response.Sample.load_from_json(s) for s in j['samples']])

class Invocation:
    def __init__(self, prompt: Prompt, response: Response, current_time: float = time.time()):
        self.prompt = prompt
        self.response = response
        self.invocation_time = current_time

    @staticmethod
    def load_from_json(j):
        return Invocation(prompt=Prompt.load_from_json(j['prompt']),
                          response=Response.load_from_json(j['response']),
                          current_time=j['invocation_time'])