#!/usr/bin/env python3
# coding: utf-8

# HTTPサーバで受信と送信を行う
# Copyright (c) 2022-2025 Wataru KUNINO

from wsgiref.simple_server import make_server               # HTTPサーバ組み込み
from time import sleep                                      # スリープの組み込み
import threading                                            # スレッドを組み込む

def wsgi_app(environ, start_response):                      # (関数)HTTP受信処理
    global html                                             # HTMLデータ読み込み
    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    return [html.encode()]                                  # 応答メッセージ返却

def httpd():                                                # (関数)HTTPサーバ
    port = 8080                                             # ポート番号を代入
    htserv = make_server('', port, wsgi_app)                # サーバ実体化
    try:                                                    # 例外処理の監視
        htserv.serve_forever()                              # HTTPサーバを起動
    except KeyboardInterrupt as e:                          # キー割り込み発生時
        raise e                                             # 例外を発生

html = '<html>Hello!</html>\r\n'                            # HTMLデータ
thread = threading.Thread(target=httpd, daemon=True)        # httpdの実体化
thread.start()                                              # httpdの起動

i = 10
while True:                                                 # 繰り返し構文
    sleep(10)                                               # 待ち時間処理
    i += 10                                                 # iに10を加算
    html = '<html>Hello! (Time='+str(i)+'sec.)</html>\r\n'  # HTMLデータの更新
