#!/usr/bin/env python3
# coding: utf-8

################################################################################
# Example 03 IoT連携の基本 HTTP GET JSONデータを受信する
################################################################################

import urllib.request                           # HTTP通信ライブラリを組み込む

url_s = 'https://bokunimo.net/test.html'        # アクセス先を変数url_sへ代入

res = urllib.request.urlopen(url_s)             # HTTPアクセスを実行
print(res.read().decode().strip())              # 受信データを表示
res.close()                                     # HTTPアクセスの終了
