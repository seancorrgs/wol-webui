from flask import Flask, request, jsonify, render_template, redirect
import socket
import json
import os
import platform
from ping3 import ping

app = Flask(__name__)

machines = None

def saveconfig():
    for item in machines:
        machines[item]['status'] = 'unknown'
    with open('machines.json', 'w') as f:
        json.dump(machines, f, indent=4)
    checkstatus()
    
def checkstatus():
    for item in machines:
        if ping(machines[item]['ip_address']):
            machines[item]['status'] = 'up'
        else:
            machines[item]['status'] = 'down'

def importconfig():
    global machines
    # Dictionary with machines and their corresponding IP addresses, MAC addresses, and ping checks
    if os.path.exists('machines.json'):
        with open('machines.json', 'r') as f:
            machines = json.load(f)
    else:
        with open('machines.json', 'w') as f:
            f.write("""
    {
        "example1": {
            "ip_address": "192.168.1.2",
            "mac_address": "00:11:22:33:44:55",
            "status": "unknown"
        }
    }
    """)

while machines is None:
    importconfig()

def spin_up_machine(mac_address):
    """
    Spins up a machine using its MAC address.

    Args:
        machine_name (str): The name of the machine.
        mac_address (str): The MAC address of the machine.
    """
    # Construct the magic packet
    mac_address = mac_address.replace(':', '')
    data = 'FF' * 6 + mac_address * 16
    send_data = bytes.fromhex(data)

    # Send the magic packet to the broadcast address using a socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, ('<broadcast>', 9))
    return True

@app.route('/')
def index():
    ## get all args from the URL
    warning = request.args.get('warning')
    success = request.args.get('success')
    return render_template('index.html',warning=warning, success=success, machines=machines)

@app.route('/spin-up/<machine_name>')
def spin_up(machine_name):
    if machines[machine_name]['status'] == 'unknown':
        check_status(machine_name)
    if machines[machine_name]['status'] == 'up':
        return redirect(f"/?warning=Machine: {machine_name} w/ IP: {machines[machine_name]['ip_address']} is already spun up.")
    elif machines[machine_name]['status'] == 'down':
        spin_up_machine(machines[machine_name]['mac_address'])
        return redirect(f"/?success=The {machine_name} is now spinning up.")

@app.route('/wol', methods=['POST'])
def send_wol():
    if 'machines' in request.form:
        for machine, data in json.loads(request.form['machines']).items():
            print(f"Sending WOL command to {data['ip_address']}")

    return redirect("/?success=WOL commands have been sent.")

@app.route('/check-status/<machine_name>')
def check_status(machine_name):
    if machine_name not in machines:
        return jsonify({'error': 'Machine does not exist'}), 400

    status = 'up' if ping(machines[machine_name]['ip_address'], timeout=1) else 'down'
    machines[machine_name]['status'] = status

    return redirect('/')

@app.route('/del-host/<machine_name>')
def del_host(machine_name):
    if machine_name not in machines:
        return jsonify({'error': 'Machine does not exist'}), 400

    del machines[machine_name]

    saveconfig()

    return redirect('/')

@app.route('/add-host', methods=['POST'])
def add_host():
    machine_name = request.form.get('machine')
    ip_address = request.form.get('ip_address')
    mac_address = request.form.get('mac_address')

    if not all([machine_name, ip_address, mac_address]):
        return jsonify({'error': 'Please fill in all fields'}), 400

    if machine_name in machines:
        return jsonify({'error': 'Machine already exists'}), 400
    
    ## save the machines to the machines.json file
    machines[machine_name] = {'ip_address': ip_address, 'mac_address': mac_address}
   
    saveconfig()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)