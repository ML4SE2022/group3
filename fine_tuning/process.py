from AVATAR.codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from AVATAR.codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import glob, os

pyprocessor = PythonProcessor(root_folder="./out/third_party")
jprocessor = JavaProcessor(root_folder="./out/third_party")

os.chdir("./test_data/test")

for file in glob.glob("*.py"):
    file_name = file[:file.index(".py")]
    (result_python, functions_standalone_python, functions_class_python) = (None, None, None)
    (result_java, functions_standalone_java, functions_class_java) = (None, None, None)


    def process_code(processor, f):
        code = f.read()
        code_tokens = processor.tokenize_code(code)
        fn_standalone, fn_class = processor.extract_functions(code_tokens)
        functions_standalone = [(processor.get_function_name(fn), fn) for fn in fn_standalone]
        functions_class = [(processor.get_function_name(fn), fn) for fn in fn_class]
        result = ' '.join(code_tokens)
        return result, dict(functions_standalone), functions_class

    with open(file_name + ".py", 'r+', encoding='utf8') as f_python:
        (result_python, functions_standalone_python, functions_class_python) = process_code(pyprocessor, f_python)
    with open(file_name + ".java", 'r+', encoding='utf8') as f_java:
        (result_java, functions_standalone_java, functions_class_java) = process_code(jprocessor, f_java)

    if os.path.isfile(file_name + "converted.py"):
        with open(file_name + "converted.py", 'r+', encoding='utf8') as f_python:
            f_python.truncate(0)  # clear file
    if os.path.isfile(file_name + "converted.java"):
        with open(file_name + "converted.java", 'r+', encoding='utf8') as f_java:
            f_java.truncate(0)  # clear file

    if len(functions_standalone_python) == 0:
        with open(file_name + "converted.py", 'w', encoding='utf8') as f_python:
            f_python.write(result_python)
        with open(file_name + "converted.java", 'w', encoding='utf8') as f_java:
            f_java.write(result_java)
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

            with open(file_name + "converted.py", 'a', encoding='utf8') as f_python:
                f_python.write(functions_standalone_python[python_fn])
            with open(file_name + "converted.java", 'a', encoding='utf8') as f_java:
                f_java.write(functions_standalone_java[final])
