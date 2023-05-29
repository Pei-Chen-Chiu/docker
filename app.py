from flask import Flask, render_template
from redis import Redis
from datetime import datetime

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')  # Increment the value of 'hits' key in Redis
    hits = int(redis.get('hits').decode('utf-8'))
    return 'Hello World! I have been hit %d times.' % hits

@app.route('/index')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
