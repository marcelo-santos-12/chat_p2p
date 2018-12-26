import socket
import threading
import time
import random

class Server_Cliente():
    
    def __init__(self, host_server, port_server, host_client, port_client):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_server = host_server
        self.port_server = port_server
        self.host_client = host_client
        self.port_client = port_client
        self.list_users  = []
    
    def init_server(self):
        self.origem = (self.host_server, self.port_server)
        self.tcp.bind(self.origem)
        self.tcp.listen(1)
        print('\nAguardando conexao...')
        self.conexao, self.cliente = self.tcp.accept()
        print('Cliente {} conectado ao server {} com sucesso...'.format(self.cliente, self.host_server))

    def init_cliente(self):
        
        self.destino = (self.host_client, self.port_client)
        
        while True:
            print('Tentando se conectar ao host {}:{}'.format(self.host_client, self.port_client))
            try:
                self.tcp.connect(self.destino)
                controle = True
                print('\nConectado com sucesso...')
                break

            except:
                print('\nNo conection!')
                time.sleep(1)
                continue
   
    def recebe_msg(self):#servidor
        msg = self.conexao.recv(4096)
        self.msg = msg.decode()
        
    def envia_msg(self, write_msg): #cliente
        self.tcp.send(str(write_msg).encode())

    def disconnect_server():
        self.conexao.close

    def disconnect(): #ambos os modos
        self.tcp.close

def main():
    global controle
    controle = False
    porta1 = int(raw_input('Porta usada: '))
    a = raw_input('\nC para cliente...\nS para Servidor...\nResposta: ')

    obj = Server_Cliente('', porta1, '192.168.1.4', porta1)

    if a == 'c' or a == 'C':
        t1 = threading.Thread(target=obj.init_cliente)
        t1.start()

    elif a == 's' or a == 'S':
        t2 = threading.Thread(target=obj.init_server)
        t2.start()

    else:
    
        print('Erro...')
    
    '''while True:
        a = random.randint(0,1)    
        if a:
            t2.start()
        else:
            t1.start()'''

if __name__ == main():
    
    main()
