from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)
port_number = 20021

@app.route('/latency', methods=['POST'])
def get_latency():
    client_ip = request.form['client_ip']
    server_ip = socket.gethostbyname(socket.gethostname())

    result = subprocess.run(
        ["scamper", "-c", f"ping -c 1 -s {client_ip}", "-i", server_ip],
        stdout=subprocess.PIPE,
        text=True
    )

    lines = result.stdout.splitlines()
    for line in lines:
        if line.startswith("icmp_seq=0"):
            latency = float(line.split()[-2])
            return jsonify({"latency": latency})
    return jsonify({"latency": float('inf')})

if __name__ == '__main__':
    app.run(port=port_number)
