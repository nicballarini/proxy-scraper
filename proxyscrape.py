import urllib3
from requests import get
from lxml import html

def proxy_list():
    url = 'https://www.us-proxy.org/'
    urllib3.disable_warnings()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 Safari/537.36'}
    response = get(url, headers=headers, verify=False, timeout=60)
    tree = html.fromstring(response.content)
    print('Aquiring list of proxies...')
    # ---------------MY STUFF---------------
    # abs xpath ip: /html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]

    # store cell data to ip & port
    ip = tree.xpath ('//table[@id="proxylisttable"]/tbody/tr/td[1]/text()')
    port = tree.xpath('//table[@id="proxylisttable"]/tbody/tr/td[2]/text()')

    print('Storing proxy list')

    proxy_list = []

    # this combines lists(ip, port) together
    for a,b in zip(ip, port):
        proxy_list.append( a + ":" + b)
        
    print('Here\'s your list of proxies')
    print(proxy_list)

    return proxy_list

def main():
    proxy_list()


main()
