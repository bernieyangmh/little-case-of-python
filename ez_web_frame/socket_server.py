# -*- coding: utf-8 -*-

import socket
import threading
import logging
from parser import ClientRequestParser

_logger = logging.getLogger(__name__)

local = threading.local()

class Socket(object):
    """

    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            while True:
                try:
                    data = client.recv(1024)
                    # 请求什么，再发送回去
                    if data:
                        client.send(data)
                    else:
                        raise ValueError("Client has disconnected")
                except:
                    client.close()

class ThreadSocket(object):
    """

    """
    todo_list = {
        'task_01': 'see someone',
        'task_02': 'read book',
        'task_03': 'play basketball'

    }

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            print("connected")
            #将处理数据交给线程处理
            threading.Thread(target=self.handleClientRequest, args=(
                client, address)).start()

    def handleClientRequest(self, client, address):
        while True:
            try:
                data = client.recv(1024)
                if data:
                    # client.send(data)
                    # python3 需要是二进制文件
                    if b'GET' in data:
                        if len(data.decode().split('/')) == 3:
                            method, task_id, status = data.decode().split('/')
                            result = self.todo_list.get(task_id, 'no key match')
                        else:
                            result = '错误的请求方式'
                    elif b'POST' in data:
                        if len(data.decode().split('/')) == 3:
                            method, command, status = data.decode().split('/')
                            key, value = command.split('=')
                            self.todo_list[key] = value
                            result = '请求成功'
                        else:
                            result = '错误的请求方式'

                    else:
                        response = b'data no found'
                    response = (str(result)+'\r\n').encode()
                    client.send(response)
                else:
                    raise ValueError("Client has disconnected")
            except:
                client.close()


class ParserThreadSocket(object):
    """

    """
    todo_list = {
        'task_01': 'see someone',
        'task_02': 'read book',
        'task_03': 'play basketball'

    }

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            print("connected")
            #将处理数据交给线程处理
            threading.Thread(target=self.handleClientRequest, args=(
                client, address, local)).start()

    # 使用local 使每个客户端拥有自己独立的数据todo_list
    def handleClientRequest(self, client, address, local):
        local.todo_list = {}
        while True:
            #try 会导致没有报错，只用于试验
                data = client.recv(1024)
                if data:
                    response = ClientRequestParser(data=data.decode(), db=local.todo_list).response().encode()
                    client.send(response)
                else:
                    # ValueError只是替代
                    raise ValueError("Client has disconnected")
                client.close()
                # 如果没有break会导致自线程一直循环
                break

if __name__ == '__main__':
    # server = Socket('', 9000)
    server = ParserThreadSocket('', 9000)
    server.listen()

# GET 请求格式：GET/task_01/ok
# POST 请求格式: POST/task_id=value/status