import json
from config import Settings
from device import mqtt_client
import uvicorn
from fastapi import FastAPI, Request


app = FastAPI()


@app.post("/motor/control")
def control_motor(request: Request):
    message = {
        "MesType": "Request",
        "ClientId": "1",
        "DeviceID": "10001",
        "Function": "0",
        "Set": request.json(),
        "Get": {
            "NowPos": "null"
        },
        "Status": {
            "Work": "Done",
            "AlarmMes": "null"
        }
    }
    
    mqtt_client.publish(Settings().motor_topic, json.dumps(message))
    
    return {"status_code": 200, "msg": "操作成功"}


@app.post("/claw/control")
def control_claw(request: Request):
    message = {
        "MesType": "Request",
        "ClientId": "2",
        "DeviceID": "14001",
        "Function": "5",
        "Set": request.json(),
        "Get": {
            "NowPos": "null",
            "NowRotateDeg": "null"
        },
        "Status": {
            "Work": "NG",
            "AlarmMes": "1001"
        }
    }
    
    mqtt_client.publish(Settings().claw_topic, json.dumps(message))
    
    return {"status_code": 200, "msg": "操作成功"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)