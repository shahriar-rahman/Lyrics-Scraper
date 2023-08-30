import os
import sys
import string
import scrapy
import time as t
import codecs
sys.path.append(os.path.abspath('utils'))
import py_utils
import py_scrape
from lyrics_scrape import LyricsScrape as lsc


class RootScraping2(scrapy.Spider):
    # Initialization
    iteration = 0
    name = 'spider_root2'
    gu = py_utils.GenericUtils()
    sc = py_scrape.ScrapeUtils()
    root_link = 'https://www.azlyrics.com/'
    directory = 'C:/Users/pc/PycharmProjects/Lyrics-Scraping/webpages/'
    gu.load_separator()

    # Xpath Codes
    body_xpath = '/html/body'

    # Pagination
    def start_requests(self):
        start_urls = lsc.generate_links(self.root_link)

        for link in start_urls:
            yield scrapy.Request(url=link, callback=self.parse)
            t.sleep(5)

    def parse(self, response, **kwargs):
        # Scrape links
        t.sleep(5)
        self.iteration += 1
        scrape_html = self.sc.xpath_scrape(response, self.body_xpath)
        string_text = ''.join(scrape_html)

        self.sc.save_text(self.directory, str(self.iteration), 'html', string_text)
