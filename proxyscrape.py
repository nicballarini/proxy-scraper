import urllib3
from requests import get
from lxml import html
from lxml import etree


def capture_https_proxy_list():
    url = 'https://www.us-proxy.org/'
    urllib3.disable_warnings()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 Safari/537.36'}
    response = get(url, headers=headers, verify=False, timeout=60)
    tree = html.fromstring(response.content)
        # print('Aquiring list of proxies...')
        # ---------------MY STUFF---------------
        # abs xpath ip: /html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]
        # httpsValue = tree.xpath('//table[@id="proxylisttable"]/tbody/tr/td[position()=7 and contains(text(), "yes")]/text()')

    ip = tree.xpath('//table[@id="proxylisttable"]/tbody/tr/td[1]/text()')
    port = tree.xpath('//table[@id="proxylisttable"]/tbody/tr/td[2]/text()')
    https_value = tree.xpath('//table[@id="proxylisttable"]/tbody/tr/td[7]/text()')

    proxy_list = []
)
    for a, b in zip(ip, port):
        proxy_list.append(a + ":" + b)

    grab_only_https = [i for i in list(zip(proxy_list, https_value)) if i[1] == "yes"]
    formated_https_proxy_list = [x[0] for x in grab_only_https]

    return formated_https_proxy_list


def outputproxiestofile(proxies):

    try:
        open("./proxies.txt", 'w').close()
    except:
        open("./proxies.txt", "x")

    proxyoutputfile = open("./proxies.txt", "w")

    for proxy in proxies:
        proxyoutputfile.writelines(proxy)
        proxyoutputfile.write('\n')
    proxyoutputfile.close()


def main():
    outputproxiestofile(capture_https_proxy_list())


main()
