import json
import os

from cryptography.fernet import Fernet
from google.cloud import pubsub_v1

class RealtimeService:
    def __init__(self, topic: str):
        self.topic = topic
        self.publisher = pubsub_v1.PublisherClient()

    def publish(self, user_id: str, admin_key: str, data: dict):
        patient_id = data['patient_id']
        print("Send message", data)
        topic = '{}.{}'.format(user_id, patient_id)
        send_message = json.dumps({
            'topic': topic,
            'data': data
        })

        send_message_encode = Fernet(admin_key).encrypt(send_message.encode())
        self.publisher.publish(self.topic, send_message_encode)