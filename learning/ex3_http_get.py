#!/usr/bin/env python3
# coding: utf-8
# Example 07 IoT連携の基本 HTTP GET

import urllib.request                           # HTTP通信ライブラリを組み込む

url_s = 'http://127.0.0.1:8080/'                # アクセス先を変数url_sへ代入

res = urllib.request.urlopen(url_s)             # HTTPアクセスを実行
print(res.read().decode().strip())              # 受信データを変数res_dictへ代入
res.close()                                     # HTTPアクセスの終了

''' ----------------------------------------------------------------------------
HTTPサーバ側：
pi@raspberry:~/udp/learning $ ./ex4_tcp_srv.py
Listening TCP port 8080 ...
127.0.0.1 37874
GET / HTTP/1.1
Accept-Encoding: identity
Host: 127.0.0.1:8080
User-Agent: Python-urllib/3.9
Connection: close
--------------------------------------------------------------------------------
HTTPクラアント側(★本プログラム)：
pi@raspberry:~/udp/learning $ ./ex5_htget.py
<html>Hello!</html>
---------------------------------------------------------------------------- '''
