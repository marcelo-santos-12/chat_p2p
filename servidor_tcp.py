# -*- coding: utf-8 -*-
import threading
import socket
import time

def aguardar_conexao():
    HOST = "localhost" # Endereço IP do Servidor
    PORT = 4000        # Porta que o Servidor esta
    global tcp
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    origem = (HOST, PORT)
    tcp.bind(origem)
    tcp.listen(1)
    print('\nServidor TCP iniciado no IP {} na porta {}'.format(HOST, PORT))
    
    global list_users
    list_users = []

    while True:
        conexao, cliente = tcp.accept()
        print('\nConexao realizada por {}!\n'.format(cliente))
        user = (conexao, cliente)
        list_users.append(user)

def enviar_msg():
    while True:
        if list_users == []:
            continue
        
        else:
            print('Digite uma mensagem:\n')
            info = raw_input()
            
            if info == 'sair':
                print('Finalizando conexao do cliente {}'.format(list_users[0][1]))
                #list_users = []
                tcp.close()
                list_users[0][0].close()
                break

            else:
                list_users[0][0].send(info.encode('utf-8'))
        
def receber_msg():

    while True:

        if list_users == []:
            continue
        
        else:
            mensagem = list_users[0][0].recv(4096)
            
            if not mensagem:
                break

            print('\nCliente:{} \n Mensagem:{}'.format(list_users[0][1], mensagem.decode()))

t1 = threading.Thread(target=aguardar_conexao, args = ())
t2 = threading.Thread(target=receber_msg, args = ())
t3 = threading.Thread(target=enviar_msg, args = ())

t1.start()
time.sleep(0.5)
t2.start()
t3.start()
