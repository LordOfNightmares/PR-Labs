import requests
from bs4 import BeautifulSoup
import requests
from contextlib import closing
import csv
import codecs
import json
from pprint import pprint
import time
from threading import Thread as T, Lock as L
import _thread
from pprint import pprint

link = "https://evil-legacy-service.herokuapp.com/api/v101"
url = [link + "/categories/", link + "/orders/"]
headers = {"Accept": "text/csv",
           "X-API-KEY": "55193451-1409-4729-9cd4-7c65d63b8e76"}


class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


'''
class CountdownThread(T):
    def __init__(self, count):
        T.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            current_thread = self.name[len("Thread-")::]
            with L():
                if current_thread == '1':
                    print(BC.OKBLUE, "1-Countdown", self.count, self.count)
                if current_thread == '2':
                    print(BC.WARNING, "2-Countdown", self.count, self.count)
                self.count -= 1

                # time.sleep(.1)
        return
'''


#

def reading(url, headers):
    # link = url + key
    response = requests.get(url, headers=headers)
    print("Status code", response.status_code)
    with closing(requests.get(url, headers=headers)) as r:
        rcsv = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
        next(rcsv, None)
        for row in rcsv:
            print(str(rcsv.line_num) + ' ' + str(row))
            # jfile = json.dumps([{key, val} for key in rcsv[0] for val in rcsv[1::]])
    # pprint(rcsv)
    return


def print_time(threadName, delay=.30):
        time.sleep(delay)
        if int(threadName[len("Thread-")::]) == 1:
            with L():
                print(BC.OKBLUE, "%s: %s" % (threadName, time.ctime(time.time())))
                reading(url[0], headers)
        if int(threadName[len("Thread-")::]) == 2:
            with L():
                print(BC.WARNING, "%s: %s" % (threadName, time.ctime(time.time())))
                reading(url[1], headers)


# Create two threads as follows
try:
    _thread.start_new_thread(print_time, ("Thread-1",))
    _thread.start_new_thread(print_time, ("Thread-2",))
except:
    print("Error: unable to start thread")

while 1:
    pass
