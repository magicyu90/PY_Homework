import requests
from bs4 import BeautifulSoup
import re
import time


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # r.encoding = 'gbk'
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'Get html wrong...'


def get_content(url, startIndex):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    movies_list = soup.find('ol', class_='grid_view')
    movies = movies_list.find_all('li')

    regex_str = r'(\n\s+导演:.*?\s\s\s)(主演:.*?\n)'
    pattern = re.compile(regex_str)
    index = (startIndex-1)*25+1

    for movie in movies:
        name = movie.find('span', class_='title').text.strip()
        info = movie.find('p').text
        rating = movie.find('span', class_='rating_num').text
        match = pattern.match(info)
        if match:
            director = match.group(1).strip()
            actor = match.group(2).strip()
            print('序号:%d\t片名:%s\t%s\t%s\t评分:%s' %
                  (index, name, director, actor, rating))
        else:
            print('序号:%d\t片名:%s\t评分:%s' % (index, name, rating))
        index += 1


if __name__ == '__main__':

    for i in range(1, 11):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % str((i-1)*25)
        get_content(url, i)
        time.sleep(0.5)
