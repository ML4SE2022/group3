from AVATAR.codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from AVATAR.codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import glob, os
from pathlib import Path

pyprocessor = PythonProcessor(root_folder="./out/third_party")
jprocessor = JavaProcessor(root_folder="./out/third_party")

os.chdir("../data")


def process_code(processor, f):
    code = f.read()
    for line in code.splitlines():
        if line.startswith(">"):
            raise Exception("Cannot parse")
    code_tokens = processor.tokenize_code(code)
    fn_standalone, fn_class = processor.extract_functions(code_tokens)
    functions_standalone = [(processor.get_function_name(fn), fn) for fn in fn_standalone]
    for function in fn_standalone:
        if "\"\"\"" in function:
            raise Exception("Cannot parse")
    functions_class = [(processor.get_function_name(fn), fn) for fn in fn_class]
    result = ' '.join(code_tokens)
    if "\"\"\"" in result:
        raise Exception("Cannot parse")
    return result, dict(functions_standalone), functions_class

for file in Path("../data").rglob('*.py'):
    file_name = file.name[:file.name.index(".py")]
    (result_python, functions_standalone_python, functions_class_python) = (None, None, None)
    (result_java, functions_standalone_java, functions_class_java) = (None, None, None)

    try:
        with open(file.parent.as_posix() + "/" + file_name + ".py", 'r+', encoding='utf8') as f_python:
            (result_python, functions_standalone_python, functions_class_python) = process_code(pyprocessor, f_python)
        with open(file.parent.as_posix() + "/" + file_name + ".java", 'r+', encoding='utf8') as f_java:
            (result_java, functions_standalone_java, functions_class_java) = process_code(jprocessor, f_java)
    except Exception as e:
        print(file_name)
        continue

    if len(functions_standalone_python) == 0:
        with open("../converted.py", 'a', encoding='utf8') as f_python:
            f_python.write(result_python)
            f_python.write("\n")
        with open("../converted.java", 'a', encoding='utf8') as f_java:
            f_java.write(result_java)
            f_java.write("\n")
    else:
        for python_fn in functions_standalone_python:
            camel_case = python_fn.title().replace("_", "")
            camel_case_sorta = camel_case[:1].lower() + camel_case[1:]
            final = None
            if camel_case in functions_standalone_java:
                final = camel_case
            elif camel_case_sorta in functions_standalone_java:
                final = camel_case_sorta
            else:
                continue

            with open("../converted.py", 'a', encoding='utf8') as f_python:
                f_python.write(functions_standalone_python[python_fn])
                f_python.write("\n")
            with open("../converted.java", 'a', encoding='utf8') as f_java:
                f_java.write(functions_standalone_java[final])
                f_java.write("\n")