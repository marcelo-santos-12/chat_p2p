import threading
import time
import socket

def printa_intervalo():
    
    while True:
        time.sleep(0.5)
        print('Marcelo')

def para_print():
    time.sleep(3)
    print('Aqui...')
    t1.exit()
    
def main():
    global t1, t2

    t1 = threading.Thread(name = 'printa_intervalo',target = printa_intervalo, args=())
    t1.start()

    t2 = threading.Thread(name = 'para_print', target = para_print, args=())
    t2.start()

if __name__ == "__main__":

    main()
