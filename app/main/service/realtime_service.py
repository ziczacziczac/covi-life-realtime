import json

import socketio
from cryptography.fernet import Fernet

sio = None

def get_sio_connection(socket_server):
    global sio
    if sio is None or not sio.connected:
        sio = socketio.Client()
        sio.connect(socket_server)
    return sio


def send_message_to_topic(user_id, data, admin_key, socket_server):
    patient_id = data['patient_id']
    print("Send message", data)
    topic = '{}.{}'.format(user_id, patient_id)
    send_message = json.dumps({
        'topic': topic,
        'data': data
    })

    sio = get_sio_connection(socket_server)

    sio.emit('json', Fernet(admin_key).encrypt(send_message.encode()))

    def handler(_, message):
        print(message)

    sio.on("*", handler)