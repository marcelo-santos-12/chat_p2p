import threading
import time

def escreve_msg():
    while True:
        time.sleep(0.1)
        if control != None:
            print(str(control))
        else:
            continue

def ler_msg():
    global control
    control = None
    while True:
        control = raw_input('O que vc quer mostrar?')

t1 = threading.Thread(target=escreve_msg, args=())
t2 = threading.Thread(target=ler_msg, args=())
t1.start()
t2.start()