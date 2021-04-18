import requests
import os
import random
from useragent import *

working_proxy = None
headers = {'User-Agent':get_useragent()}

def get_proxy():
    f = open("proxies.txt", "r")
    lines = f.readlines()
    for line in lines:
        if len(line) > 0:
            proxy = { 'http': line.strip() }
            response = requests.get("https://api.myip.com", headers=headers, proxies=proxy)
            if response.status_code == 200:
                working_proxy = proxy
                print(proxy)
                break

def get_html_from_oxy(url):
    proxies = {
        'http': 'http://'+os.environ['OXY_USER']+':'+os.environ['OXY_PASS']+'@ngrp.oxylabs.io:60000',
    }
    response = requests.get(url, proxies=proxies)
    return response.text.strip()

def get_html(url):
    if working_proxy:
        response = requests.get(url, headers=headers, proxies=working_proxy)
        if response.status_code == 200:
            return response.text
    else:
        response = requests.get(url, headers=headers)
        return response.text

def write_to_file(name, content):
    f = open(name, "w")
    f.write(content)
    f.close()