import time
from threading import Thread as T, Lock as L
from pprint import pprint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CountdownThread(T):
    def __init__(self, count):
        T.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            with L():
                current_thread = self.name[len("Thread-")::]
                if current_thread == '1':
                    print(bcolors.OKBLUE,"Countdown", self.count,self.count)
                if current_thread == '2':
                    print(bcolors.WARNING,"Countdown", self.count,self.count)
                self.count -= 1
            time.sleep(.1)
        return


t1 = CountdownThread(10)
t1.start()
t2 = CountdownThread(20)
t2.start()

