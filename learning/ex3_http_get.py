#!/usr/bin/env python3
# coding: utf-8

################################################################################
# Example 03 IoT連携の基本 HTTP GET HTMLデータを受信する
################################################################################

################################################################################
# トラブルシューティング
#   sock.connectの応答が無いとき
#   TimeoutError: Connection timed out が表示されるとき
# ------------------------------------------------------------------------------
# http_servのにbokunimo.netのIPv4アドレスを代入してください。
# 調べ方 $ nslookup bokunimo.net
# IPv6の場合は、ソケットのAddress family AF_INETをAF_INET6に変更してください。
################################################################################

import socket                                               # ソケットの組み込み

http_serv = '210.224.185.41'                                # サーバIPアドレス
port = 80                                                   # ポート番号を代入
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP用ソケット作成
sock.connect((http_serv, port))                             # TCP接続

http = 'GET /test.html HTTP/1.1\nHost: bokunimo.net\n\n'    # HTTPリクエスト電文

sock.send(http.encode())                                    # HTTPリクエスト送信
res = sock.recv(1024).decode()                              # HTTPレスポンス受信
sock.close()                                                # ソケット通信の切断

i_body = res.find('\r\n\r\n')                               # HTTP BODY位置検索
body = res[i_body + 4:]                                     # HTTP BODYを収容
if i_body < 0 or len(body) == 0:                            # BODYなし時
    print(res)                                              # 応答文そのまま表示
    exit()                                                  # 終了

print(res[:i_body])                                         # HTTP Header表示
print()                                                     # 改行
print(body)                                                 # HTMLデータを表示
