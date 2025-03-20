from datasets import load_dataset

from humaneval_uppercase.llm.gemini import GeminiFlashLite2
from humaneval_uppercase.llm.invocation import Prompt

he = load_dataset("openai_humaneval",  split="test")

system_message = Prompt.Message("system", "You are a strong code generation tool that generates Python programs.")
gemini = GeminiFlashLite2(read_from_cache=True, save_to_cache=True)
uppercase_code_dir = "generated_code/uppercase"
normal_code_dir = "generated_code/normal"


def extract_code_from_llm_response(response: str) -> str:
    return '\n'.join(response.split('```')[-2].strip().split('\n')[1:])

for i, d in enumerate(he):
    print(i)
    prompt = d['prompt']
    doc_start = prompt.index('"""')
    code_end = prompt.index('>>>', doc_start + 1)
    sub_prompt = prompt[doc_start:code_end]
    upp_prompt = prompt.replace(sub_prompt, sub_prompt.upper())

    upper_case_code = gemini.get_response(Prompt([system_message, Prompt.Message("user", upp_prompt)])).samples[0].content
    normal_code = gemini.get_response(Prompt([system_message, Prompt.Message("user", prompt)])).samples[0].content

    with open(f"{uppercase_code_dir}/{d['task_id']}.py", "w") as f:
        f.write(extract_code_from_llm_response(upper_case_code))
    with open(f"{normal_code_dir}/{d['task_id']}.py", "w") as f:
        f.write(extract_code_from_llm_response(normal_code))