import os
from time import sleep
from datasets import load_dataset
import ast
import json
import subprocess as sb

from humaneval_uppercase.llm.gemini import GeminiFlashLite2
from humaneval_uppercase.llm.invocation import Prompt

he = load_dataset("openai_humaneval",  split="test")

system_message = Prompt.Message("system", "You are a strong code generation tool that generates Python programs.")
gemini = GeminiFlashLite2(read_from_cache=True, save_to_cache=True)
uppercase_code_dir = "generated_code/uppercase"
normal_code_dir = "generated_code/normal"


def extract_code_from_llm_response(response: str) -> str:
    return '\n'.join(response.split('```')[-2].strip().split('\n')[1:])

def generated_code_versions():
    for i, d in enumerate(he):
        print(i)
        prompt = d['prompt']
        prompt = prompt.replace('""""', '"""')
        while True:
            try:
                upp_prompt = prompt

                scan_index = 0
                while True:
                    if '"""' not in upp_prompt[scan_index:]:
                        break
                    doc_start = upp_prompt.index('"""', scan_index)

                    if '>>>' in upp_prompt[doc_start:]:
                        doc_end = upp_prompt.index('>>>', doc_start + 1)
                    else:
                        doc_end = upp_prompt.index('"""', doc_start + 1)

                    sub_prompt = upp_prompt[doc_start:doc_end]
                    upp_prompt = upp_prompt.replace(sub_prompt, sub_prompt.upper())
                    scan_index = upp_prompt.index('"""', doc_start + 1) + 1

                upper_case_code = gemini.get_response(Prompt([system_message, Prompt.Message("user", upp_prompt)])).samples[0].content
                normal_code = gemini.get_response(Prompt([system_message, Prompt.Message("user", prompt)])).samples[0].content

                with open(f"{uppercase_code_dir}/{d['task_id']}.py", "w") as f:
                    f.write(extract_code_from_llm_response(upper_case_code))
                with open(f"{normal_code_dir}/{d['task_id']}.py", "w") as f:
                    f.write(extract_code_from_llm_response(normal_code))

            except ValueError as e:
                print(e)
                break
            except Exception as e:
                print("General exception {}", e)
                sleep(20)
                continue

            break

def correct_program_names():
    import os

    for i in range(164):
        os.rename('generated_code/uppercase/HumanEval/' + str(i) + '.py', 'generated_code/uppercase/HumanEval/p' + str(i) + '.py')
        os.rename('generated_code/normal/HumanEval/' + str(i) + '.py',
                  'generated_code/normal/HumanEval/p' + str(i) + '.py')

def save_renamed_function(file):
    with open(file, 'r') as f:
        code = f.read()
        root_node = ast.parse(code)
        for child in ast.walk(root_node):
            if isinstance(child, ast.FunctionDef):
                child.name = 'candidate'
                break
        with open('tmp.py', 'w') as f:
            f.write(ast.unparse(root_node))
            return True
    return False

def get_test_result(src_path, test):
    save_renamed_function(src_path)
    test = 'from tmp import candidate\n' + test + '\ncheck(candidate)'
    with open('tmp_test.py', 'w') as test_file:
        test_file.write(test)

    # run test and save output
    output = sb.getoutput('python tmp_test.py')
    # check if test passed
    if 'Traceback' in output:
        return False
    else:
        return True

def run_tests():
    test_results = {'uppercase': {}, 'normal': {}}

    for i, d in enumerate(he):
        test_result = get_test_result('generated_code/uppercase/HumanEval/p' + str(i) + '.py', d['test'])
        test_results['uppercase'][d['task_id']] = test_result
        test_result = get_test_result('generated_code/normal/HumanEval/p' + str(i) + '.py', d['test'])
        test_results['normal'][d['task_id']] = test_result

    json.dump(test_results, open('test_results.json', 'w'))

if __name__ == "__main__":
    run_tests()