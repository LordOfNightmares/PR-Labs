from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
import time
from threading import Thread as T

url = "https://desolate-ravine-43301.herokuapp.com"
queue = []


class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Threads(T):
    def __init__(self, url, headers):
        T.__init__(self)
        self.url, self.headers = url, headers

    def run(self):
        start = time.time()
        response = requests.get(self.url, headers=self.headers)
        roundup = time.time() - start
        print(BC.BOLD, "\n", self.name, "Status Code -",
              response.status_code, "(", round(roundup, 4), "s )\nUrl:", self.url)

        if response.headers["Content-Type"] == "text/csv":
            appending = parsing(response.headers["Content-Type"], response.text)
            for i in range(len(appending)):
                queue.append(appending[i])
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


def results(url):
    # link = url + key
    response = requests.post(url)
    print("Initial Status Code", response.status_code)
    headers = {"Session": response.headers['Session']}
    urls = path(response.json())
    '''
    Threads-execution
    Tr - list of threads.
    '''
    Tr = [Threads(urls[i], headers) for i in range(len(urls))]
    for i in range(len(urls)):
        Tr[i].start()
    for i in range(len(urls)):
        Tr[i].join()
	#queue processing
    queue.remove(None)
    queue.sort(key=lambda x: (int(x[1]), float(x[2])))
    s = [i for i in range(6)]
    for i in range(len(queue)):
        output(queue[i], s)


def output(block, s):
    device_id, sensor, value = block[0], int(block[1]), block[2]
    if sensor in s:
        if sensor == 0:
            print(BC.OKGREEN, "\nTemperature:")
        if sensor == 1:
            print(BC.HEADER, "\nHumidity:")
        if sensor == 2:
            print(BC.FAIL, "\nAlien Presence:")
        if sensor == 3:
            print(BC.ENDC, "\nDark Matter")
        if sensor == 4:
            print(BC.OKBLUE, "\nGhost Presence:")
        if sensor == 5:
            print(BC.WARNING, "\nDoes this Sensor even exist:")
        s.remove(sensor)
    # ---------------------
    print(" •Device", device_id, "-", value)
    # ---------------------


if __name__ == "__main__":
    results(url)
