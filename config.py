from pydantic import BaseSettings


class Settings(BaseSettings):
    mqtt_server_ip: str
    mqtt_server_port: int
    motor_topic: str
    claw_topic: str