from code_scraper.spiders.abstract_code_spider import AbstractCodeSpider


class WalkcccSpider(AbstractCodeSpider):
    name = "walkccc"

    def __init__(self, langs: str = 'C++,Java,Python', *args, **kwargs):
        super(WalkcccSpider, self).__init__(langs, *args, **kwargs)

        self.download_delay = 0.25
        self.start_urls = ['https://walkccc.me/LeetCode/']

    def parse(self, response):
        problems: list[str] = response.css('[aria-label="Problems"] a::attr(href)').getall()
        yield from response.follow_all(problems, callback=self.parse_problem)

    def parse_problem(self, response):
        problem: str = response.css('title::text').get()
        problem = problem.removesuffix(' - LeetCode Solutions').replace('.', '')
        try:
            container_elem = response.css('.tabbed-set.tabbed-alternate')[0]
        except IndexError:
            return
        problem_langs: list[str] = container_elem.css('label::text').getall()
        problem_langs = [lang for lang in problem_langs if lang in self.sel_langs]
        if len(problem_langs) != len(self.sel_langs):
            return
        problem_elems = container_elem.css('code')
        for i, lang in enumerate(problem_langs):
            impl = "".join(problem_elems[i].css('::text').getall())
            self.save_file(problem, lang, impl)
