from flask import Flask

app = Flask(__name__)
global fileInCache
fileInCache = ""

def loadiCal():
    try:
        if fileInCache is "":
            f = open("data/file.ics", "r")
            global fileInCache
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
