from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
## webdriver headless opiton


class Crawler:
    ## Set Webdriver(Used Chrome Driver)
    driver = webdriver.Chrome('/Users/bakseo3060/Documents/chromedriver')
    # def __init__(self):
    #

class AppleMusic(Crawler):

    def __init__(self, url):
        Crawler.driver.get(url)

    def get_play_list(self):
        stop_flag = True
        while stop_flag:
            try:
                Crawler.driver.find_element_by_class_name("bottom-metadata")
                print("Completed Scrool to END PAGE!")
                stop_flag = False
                time.sleep(2)
            except:
                Crawler.driver.find_element_by_tag_name('body').send_keys(Keys.END)
                time.sleep(2)
                print("END PAGE LOADING...")

        html = Crawler.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        song_name_div = 'div.song-name.typography-label'
        artist_name_div = 'div.by-line.typography-caption'

        song_list = soup.select(song_name_div)
        song_list_size = len(song_list)

        artist_list = soup.select(artist_name_div)
        artist_list_size = len(artist_list)

        print("노래 : {}".format(song_list_size))
        print("아티스트 : {}".format(artist_list_size))

        # 노래 수 만큼 노래 제목, 가수 크롤
        for i in range(song_list_size):
            print("Title : {0}, Artist : {1}".format(song_list[i].get_text().lstrip('\n'),
                                                     artist_list[i].get_text().lstrip('\n')))
        print("Thx for your playlist!!")
        print()
## Create webdriver object from corona tab of Someone's Apple Music  playlist
# url = 'https://music.apple.com/kr/playlist/%EC%86%8C%ED%94%84%ED%8A%B8%ED%8C%9D/pl.u-mJy81j7TleRRyR'
# url2 = 'https://music.apple.com/kr/playlist/pl.u-mJy81K0IleRRyR'

# class MelonMusic(Crawler):




