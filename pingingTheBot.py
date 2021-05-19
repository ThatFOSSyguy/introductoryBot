from flask import Flask
from threading import Thread

app = Flask('')

@app.route("/")
def home():
  return "Hello there!"

def run():
  app.run(host='',port='')# Enter the host and port there.

def keeping_alive():
  t = Thread(target=run)
  t.start()
  
