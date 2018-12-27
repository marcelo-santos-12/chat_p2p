from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

class Server_Cliente():
    
    def __init__(self, host_client):
        
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.host_server = ''
        self.port_server = 5000
        self.host_client = host_client
        self.port_client = self.port_server
        self.list_users  = []
        self.t1 = threading.Thread(target = self.init_server, args=())
        self.t1.start()

    def init_server(self):
        self.origem = (self.host_server, self.port_server)
        self.tcp_server.bind(self.origem)
        self.tcp_server.listen(1)
        while True:
            print('\nAguardando conexao...')
            self.conexao, self.cliente = self.tcp_server.accept()
            user = (self.conexao, self.cliente)
            print('Cliente {} conectado ao server {} com sucesso...'.format(self.cliente, self.host_server))
            self.list_users.append(user)

    def init_client(self):
        self.destino = (self.host_client, self.port_client)
        
        while True:
            print('Tentando se conectar ao host {}:{}'.format(self.host_client, self.port_client))
            try:
                self.tcp_client.connect(self.destino)
                print('\nConectado com sucesso...')
                break

            except:
                print('\nNo conection!')
                time.sleep(1)
                continue
    
    def communicate_as_server():
        pass

    def communicate_as_client():
        pass
    
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

    obj = Server_Cliente('192.168.1.7')
    time.sleep(5)
    obj.init_client()

if __name__ == main():
    
    main()
