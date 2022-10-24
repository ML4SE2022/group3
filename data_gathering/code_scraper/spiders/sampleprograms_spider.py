from code_scraper.spiders.abstract_code_spider import AbstractCodeSpider


class SampleprogramsSpider(AbstractCodeSpider):
    name = "sampleprograms"

    def __init__(self, langs: str = 'Java,Python', *args, **kwargs):
        super(SampleprogramsSpider, self).__init__(langs, *args, **kwargs)

        self.download_delay = 0.25
        self.start_urls = ['https://sampleprograms.io/projects/']

    def parse(self, response):
        projects: list[str] = response.css('h2 + p + ul li a::attr(href)').getall()
        yield from response.follow_all(projects, callback=self.parse_project)

    def parse_project(self, response):
        impls_sel = response.css('#articles + ul a')
        impl_langs: list[str] = [
            s.split(' in ')[1] for s in impls_sel.css('::text').getall()]
        impl_hrefs: list[str] = impls_sel.css('::attr(href)').getall()
        lang_to_href = {lang: href for lang, href in zip(impl_langs, impl_hrefs, strict=True)}
        hrefs = [v for (k, v) in lang_to_href.items() if k in self.sel_langs]
        if len(hrefs) == len(self.sel_langs):
            yield from response.follow_all(hrefs, callback=self.parse_impl)

    def parse_impl(self, response):
        proj: str
        lang: str
        proj, lang = response.xpath(
            '//p[contains(.//text(), "Welcome to the")]//a//text()').getall()
        impl = "".join(response.xpath('(//code)[1]//text()').getall())
        self.save_file(proj, lang, impl)
