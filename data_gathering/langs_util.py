from pathlib import Path

from tree_sitter import Language, Parser

LANG_EXTS = {'Java': 'java', 'Python': 'py', 'C++': 'cpp'}


class CodeChecker:

    def __init__(self):
        resources_path = Path(__file__).parent / 'resources'
        lib = (resources_path / 'tree-sitter_build' / 'langs.so').as_posix()
        Language.build_library(
            lib,
            [
                (resources_path / f'tree-sitter-{self.__norm_lang_name(lang)}').as_posix()
                for lang in LANG_EXTS
            ]
        )
        self.__lang_map: dict[str, Language] = {
            lang: Language(lib, self.__norm_lang_name(lang))
            for lang in LANG_EXTS
        }
        self.__parser = Parser()

    def is_invalid(self, code: str, lang: str) -> bool:
        self.__parser.set_language(self.__lang_map[lang])
        tree = self.__parser.parse(bytes(code, 'utf-8'))
        return tree.root_node.has_error

    @staticmethod
    def __norm_lang_name(lang: str) -> str:
        return lang.casefold().replace('+', 'p').replace('#', '-sharp')
