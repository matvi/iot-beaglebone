from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api, marshal_with
from flask_socketio import SocketIO,emit,send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='http://localhost:4200')

@socketio.on('connect')
def test_connect():
    print('Client connected test')
    send_data()


#Read data from client
@socketio.on('new-message')
def handle_message(message):
    print('received message' + message)
    send_data()


#Send data to client
@socketio.on('new-message-s')
def send_data():
    print('sendData')
    emit('data-tmp', {'temperature': '20', 'humedity':'53'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == "__main__":
    print("starting webservice")
    socketio.run(app)