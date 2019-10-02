from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api, marshal_with
from flask_socketio import SocketIO,emit,send
import bbbserial as bbb
from threading import Thread
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')
thread = None

def ini_socket():
    b = bbb.Beagle()
    while True:
        print('Sending data from WebSocket')       
        b.GetTemperature()
        print('sending Data: temp: {0}, hum: {1}'.format(b.temperature,b.humidity))
        #socketio.emit('data-tmp', {'temperature': 10, 'humedity':10})
        socketio.emit('data-tmp', {'temperature': b.temperature, 'humedity':b.humidity})
        time.sleep(1)

@app.route('/api/socket')
def index():
    print('Route socket init')
    global thread
    if thread is None:
        thread = Thread(target=ini_socket)
        thread.start()
    return ('{"ok":"success"}')
        
@socketio.on('connect')
def test_connect():
    print('Client connected test')
    #send_data()


#Read data from client
@socketio.on('new-message')
def handle_message(message):
    print('received message' + message)
    send_data()


#Send data to client
@socketio.on('new-message-s')
def send_data():
    b = bbb.Beagle()
    b.GetTemperature()
    print('sending Data: temp: {0}, hum: {1}'.format(b.temperature,b.humidity))
    emit('data-tmp', {'temperature': b.temperature, 'humedity':b.humidity})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == "__main__":
    print("starting webservice")
    socketio.run(app, host='10.42.0.19', port=5000)
