from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

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
            print('Porta ocupada')
            return
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

    def disconnect_client(): #ambos os modos
        self.tcp_client.close

def main():

    obj = Server_Cliente()
    
    obj.init_client('192.168.1.6')

    while True:
        if obj.communicate_as_server:
            info = raw_input('Digite sua mensagem:\n')
            
            if info == 'sair':
                print('Finalizando conexao do cliente...')
                obj.conexao.close()
                break

            else:
                obj.conexao.send(info.encode('utf-8'))

            print('\nMensagem do cliente:')
            print(obj.conexao.recv(1024))

        if obj.communicate_as_client:
            print('\nDigite sua mensagem:\n')
            mensagem = raw_input()
            obj.tcp_client.send(str(mensagem).encode())
            if mensagem == 'sair':
	            obj.tcp_client.close()
            
            msg = obj.tcp_client.recv(1024)
            print('\nMensagem do Servidor:\n')
            print(msg.decode('utf-8'))

if __name__ == '__main__':
    
    main()
