import requests
import datetime
import time
api_url = "API"
token = "TokenKEY" # 앞서 발급 받은 토큰을 여기 넣음
def LINE_Animal():

    now = datetime.datetime.now()
    filename = now.strftime("animal_%Y%m%d.jpg")
    headers = {'Authorization':'Bearer '+token}

    message = {
        "message" : "야생동물이 감지 되었습니다."
    }

    files = {
        "imageFile" : open('C:\\Users\\park\\Desktop\\animaldetection\\animaldetect\\'+filename,"rb")
    }
    
    
    requests.post(api_url, headers= headers , data = message, files=files)
    time.sleep(5)

def LINE_Fire():
    
    now = datetime.datetime.now()
    filename = now.strftime("fire_%Y%m%d.jpg")
    headers = {'Authorization':'Bearer '+token}

    message = {
        "message" : "화재가 감지 되었습니다. 이미지를 확인 한 후 119에 신고해주세요."
    }

    files = {
        "imageFile" : open('저장공간'+filename,"rb")
    }
    
    requests.post(api_url, headers= headers , data = message, files=files)
    time.sleep(5)
