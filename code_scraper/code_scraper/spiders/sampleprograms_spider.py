from dataclasses import dataclass, field
from pathlib import Path

import re
import time
import scrapy


@dataclass
class LangInfo:
    ext: str
    tasks: set[str] = field(default_factory=set)


class SampleprogramsSpider(scrapy.Spider):
    name = "sampleprograms"

    def __init__(self, langs: str = 'Java,Python', exts: str = 'java,py', res_dir: str = '../data', *args, **kwargs):
        super(SampleprogramsSpider, self).__init__(*args, **kwargs)

        comma_regex: str = r'\s*,\s*'
        lang_list: list[str] = re.split(comma_regex, langs)
        ext_list: list[str] = re.split(comma_regex, exts)

        self.info_lang: dict[str, LangInfo] = {lang: LangInfo(ext) for (lang, ext) in zip(lang_list, ext_list)}
        self.res_dir: Path = Path(res_dir) / f'{self.name}-{int(time.time())}'

        for lang in self.info_lang:
            (self.res_dir / f'{lang}').mkdir(parents=True, exist_ok=True)

        self.download_delay = 0.25
        self.start_urls = ['https://sampleprograms.io/projects/']

    def parse(self, response):
        projects = response.css('h2 + p + ul li a::attr(href)').getall()
        yield from response.follow_all(projects, callback=self.parse_project)

    def parse_project(self, response):
        implementations_sel = response.css('#articles + ul a')
        implementation_langs = implementations_sel.css('::text').getall()
        implementation_langs = [s.split(' in ')[1] for s in implementation_langs]
        implementation_hrefs = implementations_sel.css('::attr(href)').getall()
        lang_to_href = {lang: href for (lang, href) in zip(implementation_langs, implementation_hrefs)}
        hrefs = [v for (k, v) in lang_to_href.items() if k in self.info_lang]
        if (len(hrefs) == len(self.info_lang)):
            yield from response.follow_all(hrefs, callback=self.parse_impl)

    def parse_impl(self, response):
        project, lang = response.xpath('//p[contains(.//text(), "Welcome to the")]//a//text()').getall()
        impl_str: str = "".join(response.xpath('(//code)[1]//text()').getall()).rstrip()
        program_path: Path = self.res_dir / lang / f'{project}.{self.info_lang[lang].ext}'
        program_path.write_text(impl_str, encoding='utf-8', newline='\n')
