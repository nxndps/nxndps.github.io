#!/usr/bin/python3
from http.server import HTTPServer, ThreadingHTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from threading import Thread
import ssl
import os
import sys

address = "127.0.0.1" # localhost and add local.test.dom to hosts
httpport = 9080
sslport = 9443

httpsd = ThreadingHTTPServer((address, sslport), SimpleHTTPRequestHandler)

httpsd.socket = ssl.wrap_socket (httpsd.socket, 
        keyfile="./simplekey.pem", 
        certfile='./simplecert.pem', server_side=True)

print(f"serving on {address} at {sslport}")
httpst = Thread(target=httpsd.serve_forever,name="HTTPS")
httpst.start()

httpd = ThreadingHTTPServer((address, httpport), SimpleHTTPRequestHandler)
print(f"serving on {address} at {httpport}")
httpt = Thread(target=httpd.serve_forever,name="HTTP")
httpt.start()

i=""  
while i.lower() != 'q':
        i = input("q to quit")

os._exit(0)
