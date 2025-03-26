from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def counter():
    seconds = int(time.time() - start_time)
    return f"<h1>Contatore: {seconds} secondi</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
