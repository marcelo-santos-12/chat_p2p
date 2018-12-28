from socket import socket, AF_INET, SOCK_STREAM
import threading
import time
import os

class Server_Cliente():
    
    def __init__(self):
        
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.host_server = ''
        self.port_server = 5000
        self.port_client = self.port_server
        self.list_users  = []
        self.t1 = threading.Thread(target = self.init_server, args=())
        self.t1.start()
        self.communicate_as_client = False
        self.communicate_as_server = False

    def init_server(self):
        
        self.origem = (self.host_server, self.port_server)
        
        try:
            self.tcp_server.bind(self.origem)
        
        except:
            print('_______Porta ocupada_____________')
            os.system('fuser -k 5000/tcp')
            self.tcp_server.bind(self.origem)
            print('\n__________Porta Aberta____________')

        self.tcp_server.listen(1)
        
        while True:
            print('\nAguardando conexao...')
            #self.communicate_as_server = False
            self.conexao, self.cliente = self.tcp_server.accept()
            self.communicate_as_server = True
            user = (self.conexao, self.cliente)
            print('Cliente {} conectado ao server {} com sucesso...'.format(self.cliente, self.host_server))
            self.list_users.append(user)

    def init_client(self, host_client):
        self.host_client = host_client
        self.destino = (self.host_client, self.port_client)
        
        while True:
            print('Tentando se conectar ao host {}:{}'.format(self.host_client, self.port_client))
            try:
                self.tcp_client.connect(self.destino)
                self.communicate_as_client = True
                print('\nConectado com sucesso...')
                break

            except:
                print('\nNo conection!')
                time.sleep(1)
                continue
    
    def recebe_msg(self, is_server):
        if is_server:
            return self.conexao.recv(1024)
        else:
            return self.tcp_client.recv(1024).decode('utf-8')
            
    def envia_msg(self, mensagem, is_server):
        if is_server:
            if mensagem == 'sair':
                self.conexao.close()
                print('Finalizando conexao do cliente...')
            else:
                self.conexao.send(mensagem.encode('utf-8'))

        else:
            if mensagem == 'sair':
	            self.tcp_client.close()
            else:
                self.tcp_client.send(str(mensagem).encode())

def print_msg_return(is_server, obj):
    while True:
        print('\n Mensagem recebida: ')
        print(obj.recebe_msg(is_server))

def envia_msg(is_server, obj):
    while True:
        msg = input('Digite sua mensagem: ')
        obj.envia_msg(msg, is_server)

def main():

    obj = Server_Cliente()
    
    #obj.init_client('192.168.1.6')

    while True:
        if obj.communicate_as_server:
            t1 = threading.Thread(target=print_msg_return, args=(True, obj))
            t2 = threading.Thread(target=envia_msg, args=(True, obj))
            break

        if obj.communicate_as_client:
            t1 = threading.Thread(target=print_msg_return, args=(False, obj))
            t2 = threading.Thread(target=envia_msg, args=(False, obj))
            break

    t1.start()
    t2.start()

if __name__ == '__main__':
    
    main()
