from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

async def get_news_direct_link(url):
    date = []
    obt_link = []
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

    data_1 = soup.find('tr', class_='ninja_table_row_0 nt_row_id_0')
    content = data_1.findAll('td')
    date.append(content[0].text)
    obt_link.append(content[1].text)

    data_2 = soup.find('tr', class_='ninja_table_row_1 nt_row_id_1')
    content = data_2.findAll('td')
    date.append(content[0].text)
    obt_link.append(content[1].text)


    return date, obt_link