from flask import Flask, render_template
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_uptime

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html',
                           cpu=get_cpu_usage(),
                           memory=get_memory_usage(),
                           disk=get_disk_usage(),
                           uptime=get_uptime())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
