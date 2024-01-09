const int buzzer = 8;

void setup() {
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // 시리얼 데이터를 읽음
    long receivedSerialNumber = Serial.parseInt();

    // 읽은 시리얼 넘버와 타겟 시리얼 넘버를 비교
    if (receivedSerialNumber == 1) 
    {
      warning();
    }

    else if(receivedSerialNumber == 2)
    {
      sirenSound();
    }
  }
}

//동물이 싫어하는 가청 주파수 hz ->  20~20,000(HZ) 가청주파수 이외의 18(HZ) 이하의 초저주파 테스트를 위하여 200주파수로 설정
void warning() 
{
  tone(buzzer, 200);
  delay(1000);
  noTone(buzzer);
}


// 화재 경보 알림 소리
void sirenSound() {
  for(int i = 262; i <= 523; i++)
  {
    tone(buzzer, i);
    delay(10);
  }
  for(int i = 523; i >= 262; i--)
  {
    tone(buzzer, i);
    delay(10);
  }
  noTone(buzzer);
}