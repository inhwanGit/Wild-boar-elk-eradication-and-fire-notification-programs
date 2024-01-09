import cv2
from ultralytics import YOLO
from time import sleep
import serial
import SendMsg
import datetime
import os

cap = cv2.VideoCapture(0)
model = YOLO('best.pt')
fps = int(cap.get(cv2.CAP_PROP_FPS))
show_boxes = True

# 아두이노와의 시리얼 통신을 위한 포트 설정
port = 'COM3'  # 아두이노 포트에 맞게 수정
baudrate = 9600
arduino = serial.Serial(port, baudrate)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
       
        results = model(frame, imgsz=640, stream=True, verbose=False)
        for result in results:
            for box in result.boxes.cpu().numpy():
                if show_boxes:
                    r = box.xyxy[0].astype(int)
                    cv2.rectangle(frame, r[:2], r[2:], (255, 255, 255), 2)
                
                cls = int(box.cls[0])

                print(cls)
                
                # 0 = 고라니, 1 = 멧돼지, 2 = 사람, 3 = 연기(SMOKE), 4 = 불(fire)
                if cls == 0 or cls == 1:
                    serial_number = 1
                    arduino.write(str(serial_number).encode())
                    sleep(2)
                    now = datetime.datetime.now()
                    filename = now.strftime("animal_%Y%m%d.jpg")
                    if not os.path.exists('C:\\Users\\park\\Desktop\\animaldetection\\animaldetect'):
                        os.makedirs('C:\\Users\\park\\Desktop\\animaldetection\\animaldetect')
                    output_path = os.path.join('C:\\Users\\park\\Desktop\\animaldetection\\animaldetect', filename)
                    cv2.imwrite(output_path, frame)
                    sleep(1)
                    SendMsg.LINE_Animal()
                elif cls == 4:        
                    serial_number = 2
                    arduino.write(str(serial_number).encode())      
                    sleep(2)              
                    now = datetime.datetime.now()
                    filename = now.strftime("fire_%Y%m%d.jpg")
                    if not os.path.exists('C:\\Users\\park\\Desktop\\animaldetection\\firedetect'):
                        os.makedirs('C:\\Users\\park\\Desktop\\animaldetection\\firedetect')
                    output_path = os.path.join('C:\\Users\\park\\Desktop\\animaldetection\\firedetect', filename)
                    cv2.imwrite(output_path, frame)
                    sleep(1)
                    SendMsg.LINE_Fire()
        
        

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            arduino.close()
            break        
    else:
        break
        

cap.release()
cv2.destroyAllWindows()

