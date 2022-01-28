from flask import Flask
import os

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
            print("read file")
            return fileInCache
        else:
            print("cached file")
            return fileInCache
    except IOError, e:
        print e


@app.route('/')
def index():
    return loadiCal()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
