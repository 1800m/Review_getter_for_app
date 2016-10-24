# coding: UTF-8

# python2版
import urllib2
from bs4 import BeautifulSoup

# RSSを取得する
rss_url = "https://itunes.apple.com/us/rss/newapplications/limit=100/xml"
rss_request = urllib2.Request(rss_url)
response = urllib2.urlopen(rss_request)
rss = response.read().decode("utf-8")

# RSSからデータを抽出する
soup = BeautifulSoup(rss, "html.parser")
for entry in soup.find_all("entry"):
    # タイトル
    print(entry.find("title").string.encode('utf-8'))
    # リンク先URL
    print(entry.find("id").string.encode('utf-8'))
    # 視聴URL
    links = [link for link in entry.find_all("link") if link["type"] == "audio/x-m4a"]
    if len(links) > 0:
        print(links[0]["href"])
