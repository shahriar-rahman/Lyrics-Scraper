import scrapy


class SpiderLyrics(scrapy.Spider):
    # Spider Initialization
    name = 'xp01'
    start_urls = ['https://www.azlyrics.com/lyrics/linkinpark/castleofglass.html']

    @staticmethod
    def string_convert(str_arg):
        return ''.join(str_arg)

    def parse(self, response, **kwargs):
        print("•Scrapy Activated")

        title = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/h1/text()').extract()
        print("• Title: ", self.string_convert(title).replace('"', ''))

        lyrics = response.xpath('/html/body/div[2]/div[2]/div[2]/div[5]/text()').extract()
        print("• Lyrics: \n", self.string_convert(lyrics).replace('\n', ' ').replace('\r', ''))

