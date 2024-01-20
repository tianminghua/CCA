from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    try:
        # Start the CPU stress script in a non-blocking manner
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'CPU stress process started.', 200
    except Exception as e:
        return str(e), 500

@app.route('/', methods=['GET'])
def get_private_ip():
    try:
        hostname = socket.gethostname()
        private_ip = socket.gethostbyname(hostname)
        return private_ip, 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
