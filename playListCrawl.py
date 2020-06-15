from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
## webdriver headless opiton


class Crawler:
    ## Set Webdriver(Used Chrome Driver)
    def __init__(self):
        print(self.len)
    # def crawlRawData(self):

driver = webdriver.Chrome('/Users/bakseo3060/Documents/chromedriver')
## Create webdriver object from corona tab of Someone's Apple Music  playlist
# url = 'https://music.apple.com/kr/playlist/%EC%86%8C%ED%94%84%ED%8A%B8%ED%8C%9D/pl.u-mJy81j7TleRRyR'
# url2 = 'https://music.apple.com/kr/playlist/pl.u-mJy81K0IleRRyR'

print("Please Input URL")
url = input()
driver.get(url)

# 클릭한 페이지에서 html 가져오기
html = driver.page_source


songContainerId = 'ember14'
songContainer = driver.find_element_by_id(songContainerId)
stopFlag = True
while stopFlag:
    try:

        print(songContainer.find_element_by_class_name("bottom-metadata"))
        print("Completed Scrool to END PAGE!")
        time.sleep(2)
        stopFlag = False
    except:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)
        print("Can not find yet END PAGE")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
songNameDiv = 'div.song-name.typography-label'
artistNameDiv = 'div.by-line.typography-caption'

songList = soup.select(songNameDiv)
songListSize = len(songList)

artistList = soup.select(artistNameDiv)
songListSize = len(artistList)

print("노래 : {}".format(len(songList)))
print("아티스트 : {}".format(len(artistList)))


#노래 수 만큼 노래 제목, 가수 크롤
for i in range(songListSize):
    print("Title : {0}, Artist : {1}".format(songList[i].get_text().lstrip('\n'), artistList[i].get_text().lstrip('\n')))
print()
print("Thx for your playlist!!")
print()