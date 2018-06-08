import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return 'Get html wrong...'


def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')

    for movie in movies:
        name = movie.find('span', class_='sTit').text
        img_url = 'http:%s' % (movie.find('img')['src'])
        print(img_url)
        try:
            time = movie.find('span', class_='sIntro').text
        except:
            time = "暂无上映时间"
        actors = movie.find('p', class_='pActor')
        actor = ''
        if actors:
            for act in actors.contents:
                actor = actor + act.string + '  '

        print('片名:%s\t%s\t%s' % (name, time, actor))

        if ':' in name:
            name = name[:name.find(':')]
        with open('D:\\imgs\\' + name + '.png', 'wb+') as f:
            f.write(requests.get(img_url).content)


if __name__ == "__main__":
    get_content('http://dianying.2345.com/top/')
