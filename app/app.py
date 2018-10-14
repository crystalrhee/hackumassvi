from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000
app.debug = True
socketio = SocketIO(app)
clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    global clients
    client_id = request.sid
    clients.append(client_id)
    print('Client connected', client_id)

@socketio.on('disconnect')
def test_disconnect():
    global clients
    client_id = request.sid
    print('Client disconnected', client_id)
    clients.remove(client_id)

@app.route('/send', methods=['POST'])
def send_message():
    global clients
    print(request.json)
    for client_id in clients:
        socketio.emit('output', request.json['data'], room=client_id)
    msg = 'forwarding that to ' + str(clients)
    print(msg)
    return msg

if __name__ == '__main__':
    socketio.run(app)