# sock
ソケット通信サンプル・プログラム集

----------------------------------------------------------------
## Lesson 1 TCP クライアント

### [ex1_tcp_tx.py](learning/ex1_tcp_tx.py)  
TCP でデータを送信します。  

	(Python 対話モード)
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('127.0.0.1', 8080))
	sock.send("Hello!".encode())
	sock.close()
	exit()

----------------------------------------------------------------
## Lesson 2 TCP サーバ

### [ex2_tcp_rx.py](learning/ex2_tcp_rx.py)  
TCP データを受信し、表示します。  

	(Python 対話モード)
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('127.0.0.1', 8080))
	sock.listen(1)
	(client, addr) = sock.accept()

	(Bash コマンドモード)
	cd ~/sock/learning
	python ex1_tcp_tx.py

	(Python 対話モード)
	print(addr[0], addr[1])
	print(client.recv(128).decode())
	client.shutdown(socket.SHUT_WR)
	sock.close()
	exit()

----------------------------------------------------------------
## Lesson 3 HTTP クライアント

### [ex3_http_get.py](learning/ex3_http_get.py)  
HTTP GET で HTML データを受信します。  

	(Bash コマンドモード)
	nslookup bokunimo.net

	(Python 対話モード)
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('210.224.185.41', 80))
	http = 'GET /test.html HTTP/1.1＼n'
	http += 'Host: bokunimo.net＼n＼n'
	print(http)
	sock.send(http.encode())
	res = sock.recv(1024).decode()
	print(res)
	sock.close()
	exit()

----------------------------------------------------------------
## Lesson 4 実験用 HTTP サーバ

### [ex4_http_srv.py](learning/ex4_http_srv.py)  
ブラウザから TCP 接続があると HTML コンテンツを送信します。  

	(Bash コマンドモード)
	cd ~/sock/learning
	python ./ex4_http_srv.py

----------------------------------------------------------------
## Lesson 5 UDP 送信機

### [ex5_udp_tx.py](learning/ex5_udp_tx.py)  
UDP で 文字列 'Ping' を送信します。  

	(Python 対話モード)
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
	sock.sendto("Hello!".encode(), ('255.255.255.255',1024))
	sock.close()
	exit()

----------------------------------------------------------------
## Lesson 6 UDP 受信機

### [ex6_udp_rx.py](learning/ex6_udp_rx.py)  
UDP で受信した文字列を表示します。  

	(Python 対話モード)
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 1024))
	udp = sock.recvfrom(128)
	print(udp[0].decode(), udp[1])
	sock.close()
	exit()

----------------------------------------------------------------
## Lesson 7 リソース使用率送信機

### [ex7_udp_tx_cpu.py](learning/ex7_udp_tx_cpu.py)  
UDPでリソース使用率を送信します。  

	(Bash コマンドモード)
	pip install psutil
	cd ~/sock/learning/
	python ex7_udp_tx_cpu.py

----------------------------------------------------------------
## Lesson 8 センサ用UDP送信機

### [ex8_udp_tx_humi.py](learning/ex8_udp_tx_humi.py)  
UDPで温度値と湿度値を送信します。(外付けセンサ = SHT40)  

	(Bash コマンドモード)
	cd ~/udp/learning
	python ex8_udp_tx_humi.py

### [ex8_udp_tx_temp.py](learning/ex8_udp_tx_temp.py)  
センサ用UDP送信機: UDPで温度値を送信します。(外付けセンサ不要)  

	(Bash コマンドモード)
	cd ~/udp/learning
	python ex8_udp_tx_temp.py

----------------------------------------------------------------
## GitHub Pages (This Document)
* [https://git.bokunimo.com/sock/](https://git.bokunimo.com/sock/)  

----------------------------------------------------------------
# git.bokunimo.com GitHub Pages site
[http://git.bokunimo.com/](http://git.bokunimo.com/)  

----------------------------------------------------------------
