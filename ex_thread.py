import threading
import time
 
def worker(message):
    for i in range(5):
        print message
        time.sleep(1)
 
 
t = threading.Thread(target=worker,args=("thread sendo executada",))
t.start()
while t.isAlive():
    print "Aguardando thread"
    time.sleep(5)
 
print "Thread morreu"
print "Finalizando programa"