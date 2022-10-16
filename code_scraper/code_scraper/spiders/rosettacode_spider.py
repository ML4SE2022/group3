from dataclasses import dataclass, field
from pathlib import Path

import re
import time
import scrapy


@dataclass
class LangInfo:
    ext: str
    tasks: set[str] = field(default_factory=set)


class RosettacodeSpider(scrapy.Spider):
    name = "rosettacode"

    def __init__(self, langs: str = 'Java,Python', exts: str = 'java,py', res_dir: str = '../data', *args, **kwargs):
        super(RosettacodeSpider, self).__init__(*args, **kwargs)

        comma_regex: str = r'\s*,\s*'
        lang_list: list[str] = re.split(comma_regex, langs)
        ext_list: list[str] = re.split(comma_regex, exts)

        self.nr_langs_explored: int = 0
        self.info_lang: dict[str, LangInfo] = {lang: LangInfo(ext) for (lang, ext) in zip(lang_list, ext_list)}
        self.res_dir: Path = Path(res_dir) / f'{self.name}-{int(time.time())}'

        for lang in self.info_lang:
            (self.res_dir / f'{lang}').mkdir(parents=True, exist_ok=True)

        self.download_delay = 0.25
        self.start_urls = [f'https://rosettacode.org/wiki/Category:{lang}' for lang in self.info_lang]

    def parse(self, response):
        lang = response.css('h1::text').get().removeprefix('Category:')
        tasks_on_page = response.css('#mw-pages .mw-content-ltr a::attr(href)').getall()
        self.info_lang[lang].tasks.update(tasks_on_page)

        next_page = response.xpath("//a[contains(.//text(), 'next page')]/@href").get()
        if next_page:
            yield response.follow(next_page)
        else:
            self.nr_langs_explored += 1
            if self.nr_langs_explored == len(self.info_lang):
                final_tasks: set[str] = set.intersection(*(x.tasks for x in self.info_lang.values()))
                yield from response.follow_all(final_tasks, callback=self.parse_task)

    def parse_task(self, response):
        task: str = response.css('h1::text').get()
        task = "".join(char if char not in '<>:"/\\|?*' else '_' for char in task)
        for lang, lang_info in self.info_lang.items():
            xpath_sel: str = f'(//span[@id="{lang}"]//..//following-sibling::div//pre)[1]//text()'
            program_str: str = "".join(response.xpath(xpath_sel).getall()).rstrip()
            program_path: Path = self.res_dir / lang / f'{task}.{lang_info.ext}'
            program_path.write_text(program_str, encoding='utf-8', newline='\n')
