from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

async def get_news_direct_link(url):
    header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    open_link = Request(url, headers=header)
    html_code = urlopen(open_link,timeout=10).read().decode('utf-8')
    soup = BeautifulSoup(html_code, 'lxml')

    date = soup.find(class_='ninja_column_0 ninja_clmn_nm_date footable-first-visible').text
    link = soup.find(class_='ninja_column_1 ninja_clmn_nm_download footable-last-visible').a['href']

    return date, link