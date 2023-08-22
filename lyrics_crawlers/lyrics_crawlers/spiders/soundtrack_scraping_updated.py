import os
import sys
import scrapy
import time as t
from ..items import LyricsCrawlersItem
sys.path.append(os.path.abspath('utils'))
import py_utils
import py_scrape


class SoundtrackScraping(scrapy.Spider):
    # Initialization
    name = 'spider_track_updated'
    gu = py_utils.GenericUtils()
    sc = py_scrape.ScrapeUtils()

    gu.load_separator('dash')
    data = gu.load_json('../datasets/track_links.json')
    start_urls = data['artist_links']
    # start_urls = ['https://www.azlyrics.com/lyrics/doors/ridersonthestorm.html']

    # Xpath Codes
    common_xpath = '/html/body/div[2]/div[2]/div[2]'
    title_xpath = common_xpath + '/b'
    artist_xpath = common_xpath + '/ol/li[3]/a/span'
    album_xpath = common_xpath + '/div/div[1]/b'
    year_xpath = common_xpath + '/div/div[1]'
    writer_xpath = common_xpath + '/div/small'
    lyrics_xpath = common_xpath + '/div[5]'

    # Built-in Storage
    title_list = []
    artist_list = []
    album_list = []
    year_list = []
    writer_list = []
    lyrics_list = []

    def parse(self, response, **kwargs):
        items = LyricsCrawlersItem()

        # Extract Soundtrack Title
        items['title'] = self.gu.str_convert(self.sc.xpath_scrape(response, self.title_xpath+'/text()'))\
            .replace('"', '')
        self.title_list.append(items['title'])

        # Extract Soundtrack Artist
        items['artist'] = self.gu.str_convert(self.sc.xpath_scrape(response, self.artist_xpath+'/text()'))\
            .split(' ')[0: -1]
        items['artist'] = ' '.join(items['artist'])
        self.artist_list.append(items['artist'])

        # Extract Soundtrack Album
        items['album'] = self.gu.str_convert(self.sc.xpath_scrape(response, self.album_xpath+'/text()'))\
            .replace('"', '')
        self.album_list.append(items['album'])

        # Extract Soundtrack Year
        items['year'] = self.gu.str_convert(self.sc.xpath_scrape(response, self.year_xpath+'/text()[2]'))\
            .replace('(', '').replace(')', '').lstrip()
        self.year_list.append(items['year'])

        # Extract Soundtrack Writer(s)
        items['writer'] = self.sc.xpath_scrape(response, self.writer_xpath+'/text()')
        if items['writer'] is not None:
            temp_writer = self.gu.str_convert(items['writer']).split(' ')[1:]
            items['writer'] = ' '.join(temp_writer)
        self.writer_list.append(items['writer'])

        # Extract Soundtrack Lyrics
        items['lyrics'] = self.gu.str_convert(self.sc.xpath_scrape(response, self.lyrics_xpath+'/text()'))\
            .replace('\n', ' ').replace('\r', '')
        self.lyrics_list.append(items['lyrics'])

        # Data storage
        data_dict = {'title': self.title_list, 'artist': self.artist_list, 'album': self.album_list,
                     'year': self.year_list, 'writer': self.writer_list, 'lyrics': self.lyrics_list}
        self.gu.display_dict("Display updated data", data_dict)
        self.gu.save_json('../datasets/soundtrack_data.json', data_dict)
        self.gu.load_separator('dash')
        t.sleep(50)
        yield items
