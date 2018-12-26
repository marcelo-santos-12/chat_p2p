#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading

def recebe_msg(tcp):
   while True:
      msg = tcp.recv(4096)
      print('\nMensagem do Servidor:\n')
      print(msg.decode('utf-8'))

def envia_msg(tcp):
   while True:
      print('\nDigite sua mensagem:\n')
      mensagem = raw_input()
      tcp.send(str(mensagem).encode())
      if mensagem == 'sair':
	      tcp.close

HOST = 'localhost'     # Endereço IP do Servidor
#HOST = socket.gethostname()
PORT = 4000            # Porta que o Servidor está

destino = (HOST, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(destino)

t1 = threading.Thread(target=recebe_msg,args=(tcp,))
t2 = threading.Thread(target=envia_msg,args=(tcp,))

t1.start()
t2.start()
