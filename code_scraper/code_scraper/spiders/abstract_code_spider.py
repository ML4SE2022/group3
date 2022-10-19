import re
import time
from pathlib import Path

import scrapy


class AbstractCodeSpider(scrapy.Spider):

    LANG_EXTS = {'Java': 'java', 'Python': 'py', 'C++': 'cpp'}

    def __init__(self, langs: str, res_dir: str = '../data'):
        comma_regex = r'\s*,\s*'
        self.sel_langs: list[str] = [
            lang for lang in re.split(comma_regex, langs) if lang in self.LANG_EXTS]
        self.res_dir = Path(res_dir) / f'{self.name}-{int(time.time())}'

        for lang in self.sel_langs:
            (self.res_dir / f'{lang}').mkdir(parents=True, exist_ok=True)

    def save_file(self, name: str, lang: str, content: str) -> None:
        name_preproc = "".join(c if c not in '<>:"/\\|?*' else '_' for c in name)
        content_preproc = content.rstrip()
        file_path = self.res_dir / lang / f'{name_preproc}.{self.LANG_EXTS[lang]}'
        file_path.write_text(content_preproc, encoding='utf-8', newline='\n')
