from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

working_links = []

async def check_list():
    header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    fresherwave_link = Request("https://www.fresherwave.com/newspaper/", headers=header)

    html_code = urlopen(fresherwave_link,timeout=10).read().decode('utf-8')

    soup = BeautifulSoup(html_code, 'lxml')

    buttons = soup.findAll(class_='wptb-button-wrapper wptb-size-s')

    for i in buttons:
        link = i.find('a').get('href')
        working_links.append(link)

    return working_links