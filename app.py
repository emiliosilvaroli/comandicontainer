from flask import Flask, Response, render_template
import time

app = Flask(__name__)
start_time = time.time()

def event_stream():
    while True:
        elapsed_time = int(time.time() - start_time)
        yield f"data: {elapsed_time}\n\n"
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def sse():
    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)