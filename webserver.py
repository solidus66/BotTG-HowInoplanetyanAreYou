from flask import Flask
from threading import Thread
import requests
import time

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=80)

# def ping_server():
#     while True:
#         try:
#             requests.get('http://')
#         except requests.exceptions.RequestException:
#             pass
#         time.sleep(300)  # Отправлять запрос каждые 5 минут (300 секунд)

def keep_alive():
    t = Thread(target=run)
    t.start()
    # ping_thread = Thread(target=ping_server)
    # ping_thread.start()