import json
import time
from queue import Queue
from threading import Thread as T, Lock as L

import requests
from bs4 import BeautifulSoup

url = "https://desolate-ravine-43301.herokuapp.com"
queue = []
q = Queue()
threads_num = 11


class TextColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Threads(T):
    def __init__(self, myq, h):
        T.__init__(self)
        self.myq = myq
        self.headers = h

    def run(self):
        while True:
            with L():
                response = request(self.myq.get(), self.headers, self.name)
                datasave(response)
            self.myq.task_done()


def request(url, headers, name):
    start = time.time()
    response = requests.get(url, headers=headers)
    roundup = time.time() - start
    print(TextColor.BOLD, "\n", name,
          "Status Code -", response.status_code,
          "(", round(roundup, 4), "s )\nUrl:", url)
    return response


def datasave(response):
    if response.headers["Content-Type"] == "text/csv":
        appending = parsing(response.headers["Content-Type"], response.text)
        for i in range(len(appending)):
            queue.append(appending[i])
    elif response.status_code != 200:
        queue.append(None)
    else:
        queue.append(parsing(response.headers["Content-Type"], response.text))


def parsing(content_type, text):
    if content_type == "Application/xml":
        soup = BeautifulSoup(text, 'html.parser')
        return [soup.device['id'], soup.type.string, soup.value.string]
    elif content_type == "Application/json":
        j_file = json.loads(text)
        return [j_file['device_id'], j_file['sensor_type'], j_file['value']]
    elif content_type == "text/csv":
        text = [s.split(",") for s in text.splitlines()]
        x = [[text[i][0], text[i][1], text[i][2]] for i in range(len(text)) if i != 0]
        return x
    else:
        print(text)


def path(text):
    path = []
    for i in range(len(text)):
        path.append(url + text[i]['path'])
    return path


def output(block, s):
    device_id, sensor, value = block[0], int(block[1]), block[2]
    if sensor in s:
        if sensor == 0:
            print(TextColor.OKGREEN, "\nTemperature:")
        if sensor == 1:
            print(TextColor.HEADER, "\nHumidity:")
        if sensor == 2:
            print(TextColor.FAIL, "\nAlien Presence:")
        if sensor == 3:
            print(TextColor.ENDC, "\nDark Matter")
        if sensor == 4:
            print(TextColor.OKBLUE, "\nGhost Presence:")
        if sensor == 5:
            print(TextColor.WARNING, "\nDoes this Sensor even exist:")
        s.remove(sensor)
    # ---------------------
    print(" •Device", device_id, "-", value)
    # ---------------------


def results(url):
    # link = url + key
    response = requests.post(url)
    print("Initial Status Code", response.status_code)
    headers = {"Session": response.headers['Session']}
    urls = path(response.json())

    # Threads-execution ,Tr - list of threads.
    for i in range(threads_num):
        worker = Threads(q, headers)
        worker.setDaemon(True)
        worker.start()
    for i in range(len(urls)):
        q.put(urls[i])
    q.join()
    print("------------------------------------\n"
          "All done"
          "\n------------------------------------")

    while None in queue:
        queue.remove(None)
    queue.sort(key=lambda x: (int(x[1]), float(x[2])))
    sensor_sort = [i for i in range(6)]
    for i in range(len(queue)):
        output(queue[i], sensor_sort)


if __name__ == "__main__":
    results(url)
