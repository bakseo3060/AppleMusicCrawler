from playListCrawl import *

if __name__ == '__main__':
    url = 'https://music.apple.com/kr/playlist/%EC%86%8C%ED%94%84%ED%8A%B8%ED%8C%9D/pl.u-mJy81j7TleRRyR'

    apple = AppleMusic(url)
    apple.get_play_list()