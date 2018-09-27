#!/usr/bin/env python3
import json
import requests 
import requests_cache
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36'}
requests_cache.install_cache('demo_cache')


for i in range(1000):
    r=requests.get('https://www.reddit.com/r/pokemon/top.json', headers=headers)
    data = r.json()
    for x in data["data"]["children"]:
       print(x["data"]["title"])
