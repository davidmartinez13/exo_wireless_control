import requests

#replace url according to raspberry ip:
url_detections = 'http://192.168.1.137:5000/detections'

while True:
    angle1 = input('set angle1 to 0 or 180\n')
    angle2 = input('set angle2 to 0 or 180\n')
    data = {"move_command": [True],
            "angle": [int(angle1),180-int(angle2)]
            }

    try:
        server_return = requests.post(url_detections,json=data)
        print('[INFO]: Detections posted.')
    except:
        print('not able to connect')
        break
    