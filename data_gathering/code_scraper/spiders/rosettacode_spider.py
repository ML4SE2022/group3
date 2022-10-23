from code_scraper.spiders.abstract_code_spider import AbstractCodeSpider


class RosettacodeSpider(AbstractCodeSpider):
    name = "rosettacode"

    def __init__(self, langs: str = 'Java,Python', rm_drafts: str = 'y', *args, **kwargs):
        super(RosettacodeSpider, self).__init__(langs, *args, **kwargs)

        self.nr_langs_explored = 0
        self.rm_drafts = rm_drafts == 'y'
        self.lang_to_tasks: dict[str, set[str]] = {lang: set() for lang in self.sel_langs}

        self.download_delay = 0.25
        self.start_urls = [
            f'https://rosettacode.org/wiki/Category:{lang}' for lang in self.sel_langs]

    def parse(self, response):
        lang: str = response.css('h1::text').get().removeprefix('Category:')
        tasks: list[str] = response.css(
            '#mw-pages .mw-content-ltr a::attr(href)').getall()
        self.lang_to_tasks[lang].update(tasks)

        next_page: str = response.xpath('//a[contains(.//text(), "next page")]/@href').get()
        if next_page:
            yield response.follow(next_page)
        else:
            self.nr_langs_explored += 1
            if self.nr_langs_explored == len(self.sel_langs):
                final_tasks: set[str] = set.intersection(
                    *(task for task in self.lang_to_tasks.values()))
                yield from response.follow_all(final_tasks, callback=self.parse_task)

    def parse_task(self, response):
        draft: str = response.xpath('//a[contains(.//text(), "Draft Programming Task")]').get()
        if self.rm_drafts and draft:
            return
        task: str = response.css('h1::text').get()
        task = "".join(char if char not in '<>:"/\\|?*' else '_' for char in task)
        for lang in self.sel_langs:
            xpath_exp = f'(//span[@id="{lang}"]//..//following-sibling::div//pre)[1]//text()'
            program = "".join(response.xpath(xpath_exp).getall())
            self.save_file(task, lang, program)
