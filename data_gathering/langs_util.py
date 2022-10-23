from tree_sitter import Language, Parser

LANG_EXTS = {'Java': 'java', 'Python': 'py', 'C++': 'cpp'}


class CodeChecker:

    def __init__(self):
        lib = 'resources/tree-sitter_build/langs.so'
        Language.build_library(
            lib,
            [
                f'resources/tree-sitter-{self.__norm_lang_name(lang)}'
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
