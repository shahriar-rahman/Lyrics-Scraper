import os
import sys
import scrapy
import time as t
sys.path.append(os.path.abspath('utils'))
import py_utils
import py_scrape
artists = ['the beatles']


class ArtistScraping(scrapy.Spider):
    # Initialization
    name = 'spider_artist_updated'
    artist_url = []
    track_links = []
    gu = py_utils.GenericUtils()
    sc = py_scrape.ScrapeUtils()
    gu.load_separator('dash')
    root_link = 'https://www.azlyrics.com'

    for artist in artists:
        if 'the' in artist.split(' ')[0]:
            artist = artist.replace('the ', '')
        artist.strip()
        artist_link = root_link + '/' + artist[0] + '/' + artist + '.html'
        artist_url.append(artist_link)
        print(artist_url)
    gu.load_separator('dash')
    start_urls = artist_url
    # data = gu.load_json('../datasets/artist_links.json')
    # start_urls = data['artist_links']

    # Xpath Codes
    common_xpath = '//*[@id="listAlbum"]/'
    tracks_xpath = common_xpath + 'div/a'

    def parse(self, response, **kwargs):
        # Scrape Links
        leaf_links = self.sc.xpath_scrape(response, self.tracks_xpath+'/@href')

        # Link Concatenation
        for leaf_link in leaf_links:
            self.track_links.append(self.root_link+leaf_link)

        track_dict = {'artist_links': self.track_links}
        self.gu.display_dict("Display updated data", track_dict)
        self.gu.save_json('../datasets/track_links.json', track_dict)
        t.sleep(50)

