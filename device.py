import json
import threading
import time
from typing import Deque
from config import Settings
import paho.mqtt.client as mqtt


message_queue = Deque()
def handle_mqtt_message(client, userdata, message):
    message_queue.append(json.loads(message.payload.decode("utf-8")))
    

def handle_thread():
    while True:
        if len(message_queue) > 0:
            message = message_queue.popleft()
            if message.topic == Settings().motor_topic: # 处理电机控制消息
                process_motor_message(message)
            elif message.topic == Settings().claw_topic: # 处理夹爪控制消息
                process_claw_message(message)
        time.sleep(0.1)
thread = threading.Thread(target=handle_thread)
thread.daemon = True
thread.start()


def process_motor_message(message):
    # TODO 处理电机
    pass


def process_claw_message(message):
    # TODO 处理夹爪
    pass


mqtt_client = mqtt.Client()
mqtt_client.connect(Settings().mqtt_server_ip, Settings().mqtt_server_port)
mqtt_client.subscribe(Settings().motor_topic)
mqtt_client.subscribe(Settings().claw_topic)
mqtt_client.on_message = handle_mqtt_message
mqtt_client.loop_start()
