# coding: UTF-8

import urllib.request   # python3じゃないと動かない
from bs4 import BeautifulSoup

# RSSを取得する
rss_url = "https://itunes.apple.com/us/rss/newapplications/limit=100/xml"
response = urllib.request.urlopen(rss_url)
rss = response.read().decode("utf-8")

# RSSからデータを抽出する
soup = BeautifulSoup(rss, "html.parser")
for entry in soup.find_all("entry"):
    # タイトル
    print(entry.find("title").string)
    # リンク先URL
    print(entry.find("id").string)
    # 視聴URL
    links = [link for link in entry.find_all("link") if link["type"] == "audio/x-m4a"]
    if len(links) > 0:
        print(links[0]["href"])
