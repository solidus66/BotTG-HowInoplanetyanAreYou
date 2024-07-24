import os
import time
from flask import Flask
from threading import Thread
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive"


def run():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


def keep_alive():
    url = "https://bottg-howinoplanetyanareyou.onrender.com"
    while True:
        try:
            requests.get(url)
            print(f"Sent keep-alive request to {url}")
        except Exception as e:
            print(f"Error keeping alive: {e}")
        time.sleep(300)


if __name__ == '__main__':
    server_thread = Thread(target=run)
    server_thread.start()

    keep_alive_thread = Thread(target=keep_alive)
    keep_alive_thread.start()
