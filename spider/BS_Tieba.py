import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r= requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except :
        return 'error'

def get_content()




if __name__=='__main__':