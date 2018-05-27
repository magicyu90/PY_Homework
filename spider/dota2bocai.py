import requests
from bs4 import BeautifulSoup


def get_html(url):
    '''
    获取网页内容
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'error'


def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')  # 格式化内容

        match = soup.find_all('div', attrs={'class': 'matchmain'})[0]
        teams = []
        for team in match.find_all('div', {'class': 'teamtext'}):
            teams.append(team.find('b').text.strip())
    except Exception as ex:
        print('error happend:%s' % str(ex))


if __name__ == '__main__':
    baseUrl = 'https://dota2lounge.com/'
    get_content(baseUrl)
