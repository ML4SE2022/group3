import re
import time
from abc import ABC
from pathlib import Path

import scrapy
from langs_util import LANG_EXTS


class AbstractCodeSpider(scrapy.Spider, ABC):

    def __init__(self, langs: str, res_dir: str = '../data', **kwargs):
        super().__init__(**kwargs)
        comma_regex = r'\s*,\s*'
        self.sel_langs: list[str] = [
            lang for lang in re.split(comma_regex, langs) if lang in LANG_EXTS]
        self.res_dir = Path(res_dir) / f'{self.name}_{int(time.time())}'

        for lang in self.sel_langs:
            (self.res_dir / lang).mkdir(parents=True, exist_ok=True)

    def save_file(self, name: str, lang: str, content: str) -> None:
        name_preproc = "".join(c if c not in '<>:"/\\|?*–' else '_' for c in name)
        content_preproc = content.rstrip()
        file_path = self.res_dir / lang / f'{name_preproc}.{LANG_EXTS[lang]}'
        file_path.write_text(content_preproc, encoding='utf-8', newline='\n')
