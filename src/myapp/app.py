import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def hello_test():
    return "This is a test"

@app.route("/hello/<name>")
def hello_name(name):
    return f"<p>Hello, {name}!</p>"

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", 3000)
    app.run(host,port)
