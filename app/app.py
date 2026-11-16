import os
import socket
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "db"), port=6379,
                socket_connect_timeout=2)

@app.route("/")
def index(): # звернення до БД
    count = r.incr("visits")           
    return f"Hello from {socket.gethostname()}! Visits: {count}\n"

@app.route("/health")
def health(): # перевірка стану БД
    r.ping()
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)