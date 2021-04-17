import requests
import os
from useragent import *

def get_html_from_oxy(url):
    proxies = {
        'http': 'http://'+os.environ['OXY_USER']+':'+os.environ['OXY_PASS']+'@ngrp.oxylabs.io:60000',
    }
    response = requests.get(url, proxies=proxies)
    return response.text.strip()

def get_html(url):
    response = requests.get(url)
    return response.text.strip()

def write_to_file(name, content):
    f = open(name, "w")
    f.write(content)
    f.close()