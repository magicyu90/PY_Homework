import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        #r.encoding = 'gbk'
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'Get html wrong...'


def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    movies_list = soup.find('ol', class_='grid_view')
    movies = movies_list.find_all('li')

    regex_str= r'(导演:.*?\s\s\s)(主演:.*?\n)'
    for movie in movies:
        name = movie.find('span', class_='title').text
        actors= movie.find('p').text
        print(actors)


if __name__ == '__main__':
    get_content('https://movie.douban.com/top250')
