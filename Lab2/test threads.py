from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
import time
from threading import Thread as T, Lock as L

url = "https://desolate-ravine-43301.herokuapp.com"


class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Threads(T):
    def __init__(self, url, headers):
        T.__init__(self)
        self.url, self.headers = url, headers

    def run(self):
        def output(device_id, sensor, value):
            device_id, sensor, value = device_id, int(sensor), float(value)
            if sensor == 0:
                print(BC.OKGREEN, "Temperature:")
            if sensor == 1:
                print(BC.OKGREEN, "Humidity:")
            if sensor == 2:
                print(BC.OKGREEN, "Alien Presence:")
            if sensor == 3:
                print(BC.OKGREEN, "Dark Matter")
            if sensor == 4:
                print(BC.OKGREEN, "Ghost Presence:")
            if sensor >= 5:
                print(BC.OKBLUE, "Does this Sensor even exist:")
            # ---------------------
            print("Device", device_id, "-", value, sep=' ', end='', flush=True)
            # ---------------------
            if value > 0 and sensor == 3:
                print(BC.WARNING, "(Is 'CERN' particle accelerator turned off?)")
            if value == 0 and sensor == 2:
                print("(No aliens detected)")
            if value > 0 and sensor == 2:
                print(BC.FAIL, "(RUN - ALIEN LIFE DETECTED)")
            if value > 0 and sensor == 4:
                print(BC.FAIL, "(RIP - GHOSTS DETECTED)")
            print()

        def parsing(content_type, text):
            if content_type == "Application/xml":
                soup = BeautifulSoup(text, 'html.parser')
                output(soup.device['id'], soup.type.string, soup.value.string)
            elif content_type == "Application/json":
                j_file = json.loads(text)
                output(j_file['device_id'], j_file['sensor_type'], j_file['value'])

            elif content_type == "text/csv":
                text = [s.split(",") for s in text.splitlines()]
                for i in range(len(text)):
                    if i != 0:
                        output(text[i][0], text[i][1], text[i][2])
            else:
                print(text)

        with L():
            start = time.time()
            response = requests.get(self.url, headers=self.headers)
            roundtrip = time.time() - start
            print(BC.HEADER, "\n", self.name, "Statuscode",
                  response.status_code, round(roundtrip, 4), "s\nUrl:", self.url)
            parsing(response.headers["Content-Type"], response.text)


def reading(url):
    # link = url + key
    response = requests.post(url)
    print("Status code", response.status_code)
    headers = {"Session": response.headers['Session']}
    urls = path(response.json())
    Tr = []

    for i in range(len(urls)):
        Tr.append(Threads(urls[i], headers))
    for i in range(len(urls)):
        Tr[i].start()
    return


def path(text):
    path = []
    for i in range(len(text)):
        path.append(url + text[i]['path'])
    return path


reading(url)
