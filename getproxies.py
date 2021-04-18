import requests
import sys
import json
from useragent import *
from bs4 import BeautifulSoup

def write_proxies(html):
    f = open("proxies.txt", "w")
    soup = BeautifulSoup(html, "html5lib")
    table = soup.find("table", {'id':'proxylisttable'})
    rows = table.find('tbody').find_all('tr')
    for r in rows:
        tds = r.find_all('td')
        f.write(tds[0].get_text()+":"+tds[1].get_text()+"\n")
    f.close()

providers = {
    'ANONYMOUS':"https://free-proxy-list.net/anonymous-proxy.html",
    'US':"https://www.us-proxy.org/",
    'UK':"https://free-proxy-list.net/uk-proxy.html",
    'SSL': "https://sslproxies.org/"
}

if len(sys.argv) == 2:
    location = providers[sys.argv[1]]
else:
    location = providers['ANONYMOUS']

headers = {'User-Agent':get_useragent()}
r = requests.get(location, headers=headers)
if r.status_code == 200:
    write_proxies(r.text)
else:
    print(r.raise_for_status())
