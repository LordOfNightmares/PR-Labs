from queue import Queue
from threading import Thread as T, Lock as L
import time


class mythread(T):
    def __init__(self, myq):
        T.__init__(self)
        self.myq = myq

    def run(self):
        print("***")
        while True:
            with L():
                print("%%%%")
                print(self.myq.get())
                print(self.name)
            self.myq.task_done()


q = Queue()
threadnum = 2
for i in range(threadnum):
    print("Thread creating")
    worker = mythread(q)
    print("Thread created")
    worker.setDaemon(True)
    worker.start()
    print("&&&&")

for x in range(9):
    q.put(x)
    q.join()
print("all done")
