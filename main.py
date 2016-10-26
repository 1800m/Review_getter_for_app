#!/usr/bin/env python
# coding: UTF-8

import urllib2 # python2版
from bs4 import BeautifulSoup
import numpy
#import sys

#rss_uri.datを読み込む
f = open('./input/rss_url.dat', 'r')
lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

#改行コードの削除処理
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('\n', '')   #改行コードの削除

rss_list = []   #RSSリストの初期化
#RSSリストへの追加
for line in lines:
    #偶数番：ジャンルの文字列
    #奇数番・URLの文字列
    rss_list.append(line)

#ジャンル数を取得する
rss_size = (len(rss_list)-2)/2

#ジャンルの数だけ繰り返す
for i in range(0, rss_size):
    name_output = "output_TopFreeApp100_" + rss_list[i*2]

    #出力結果を書き込む
    f = open('./output/'+name_output+'.dat', 'w')
    f.close()



# RSSを取得する
# rss_url = "https://itunes.apple.com/jp/rss/topfreeapplications/limit=100/genre=6014/xml"
# rss_request = urllib2.Request(rss_url)
# response = urllib2.urlopen(rss_request)
# rss = response.read().decode("utf-8")
#
# # RSSからデータを抽出する
# soup = BeautifulSoup(rss, "html.parser")
# for entry in soup.find_all("entry"):
#     # タイトル
#     print(entry.find("title").string.encode('utf-8'))
#     # リンク先URL
#     print(entry.find("id").string.encode('utf-8'))
#     # 視聴URL
#     links = [link for link in entry.find_all("link") if link["type"] == "audio/x-m4a"]
#     if len(links) > 0:
#         print(links[0]["href"])
