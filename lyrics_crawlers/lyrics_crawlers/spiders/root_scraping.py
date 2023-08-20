import os
import sys
import string
import scrapy
import time as t
sys.path.append(os.path.abspath('utils'))
import py_utils
import py_scrape


class RootScraping(scrapy.Spider):
    # Initialization
    name = 'spider_root'
    artist_links = []
    gu = py_utils.GenericUtils()
    sc = py_scrape.ScrapeUtils()
    root_link = 'https://www.azlyrics.com/'
    gu.load_separator('dash')

    # Xpath Codes
    common_xpath = '/html/body/div[2]/div/'
    column_a_xpath = common_xpath + 'div[2]/a'
    column_b_xpath = common_xpath + 'div[3]/a'

    # Pagination
    def start_requests(self):
        # alphabets = ['q', 'x', 'z']
        alphabets = [letter for letter in string.ascii_lowercase]
        alphabets.append('19')

        start_urls = []
        for letter in alphabets:
            start_urls.append(self.root_link+letter+'.html')

        for link in start_urls:
            yield scrapy.Request(url=link, callback=self.parse)
            t.sleep(50)

    def parse(self, response, **kwargs):
        # Scrape links
        leaf_links_a = self.sc.xpath_scrape(response, self.column_a_xpath+'/@href')
        leaf_links_b = self.sc.xpath_scrape(response, self.column_b_xpath+'/@href')

        # Link Concatenation
        for leaf_link in leaf_links_a:
            self.artist_links.append(self.root_link+leaf_link)

        for leaf_link in leaf_links_b:
            self.artist_links.append(self.root_link+leaf_link)

        # Storage
        artist_dict = {'artist_links': self.artist_links}
        self.gu.display_dict("Display updated data", artist_dict)
        self.gu.save_json('../datasets/artist_links.json', artist_dict)
        t.sleep(5)
