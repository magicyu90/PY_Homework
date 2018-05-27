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
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')  # 格式化内容
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    comments = []
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['author'] = li.find(
                'a', attrs={'class': 'frs-author-name j_user_card '}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num', 'title': '回复'}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()

            comments.append(comment)
        except expression as identifier:
            print('error')

    return comments


def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open('TTBT.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['author'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'

if __name__ == '__main__':
    comments = get_content('%s&pn=50' % base_url)
    Out2File(comments)
    print('所有的信息都已经保存完毕！')