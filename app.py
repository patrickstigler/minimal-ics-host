from flask import Flask
import os
import signal
import sys

app = Flask(__name__)
app_host = os.getenv("APP_HOST") or "0.0.0.0"
app_port = os.getenv("APP_PORT") or "5000"

global fileInCache
fileInCache = ""

def loadiCal():
    global fileInCache
    try:
        if fileInCache is "":
            f = open("data/file.ics", "r")
            fileInCache = f.read()
            return fileInCache
        else:
            return fileInCache
    except IOError as e:
        print(e)


@app.route('/')
def index():
    return loadiCal()

def signal_handler(sig, frame):
    print('Shutting down.')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    app.run(host=app_host, port=app_port)
