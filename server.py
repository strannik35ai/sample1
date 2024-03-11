import os

from flask import Flask

app = Flask(__name__)

i = 0
@app.route("/")
def index():
    global i
    i += 1
    return "Привет от приложения Flask " + str(i)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)