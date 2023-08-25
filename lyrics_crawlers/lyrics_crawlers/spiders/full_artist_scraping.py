import os
import sys
import pandas as pd
import scrapy
import time as t
sys.path.append(os.path.abspath('utils'))
import py_utils
import py_scrape
artists = ['the beatles']


class FullArtist(scrapy.Spider):
    name = 'spider_full_artist'
    start_urls = []
    artist_page_scrape = []
    gu = py_utils.GenericUtils()
    sc = py_scrape.ScrapeUtils()
    gu.load_separator('dash')
    root_link = 'https://www.azlyrics.com'

    for artist in artists:
        if 'the' in artist.split(' ')[0]:
            artist = artist.replace('the ', '')
        artist.strip()
        start_urls.append(root_link + '/' + artist[0] + '/' + artist + '.html')

    print(start_urls)
    full_xpath = '/html/body'

    def parse(self, response, **kwargs):
        leaf_links = self.sc.xpath_scrape(response, self.full_xpath)
        print(leaf_links)
        self.artist_page_scrape.append(leaf_links)

        custom_dict = {'beatles': self.artist_page_scrape}
        df = pd.DataFrame(custom_dict, columns=['beatles'])
        # df.to_csv('../datasets/artist_page_scrape.csv')
        self.gu.save_df(df, '../datasets/artist_page_scrape.csv', 'csv')
        self.gu.save_json('../datasets/artist_page_scrape.json', custom_dict)
