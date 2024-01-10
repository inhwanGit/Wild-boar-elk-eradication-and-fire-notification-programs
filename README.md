# 인공지능 YOLO기술을 활용한 멧돼지, 고라니 퇴치 및  화재 알림 프로그램
##### • 개발 기간 : 2023.03 ~ 2023.06
##### • 한 줄 소개 : 유해동물과 화재로 인한 피해를 줄이기 위해 인공지능 CNN을 활용하여 인식후 알림 프로그램
##### • Skills : Python
##### • 팀 구성 : 2명
##### • 관련 활동 : 오픈소스 활용 창의 SW 경진대회

## 📌 개발 목적
##### • 매 년 발생하는 야생동물 및 화재로 인한 피해를 감소하여 많은 사람들에게 도움을 줄 수 있는 프로그램을 개발하였습니다. 일상생활에서 이러한것을 막기 위해서 실시간으로 객체를 탐지하여 인식하고 야생동물이 싫어하는 저주파음(150~800HZ)을 송출하여 멧돼지 및 고라니를 퇴치하며 관계자에게 알림을 주는 서비스를 개발하게 되었습니다. 또한 화재의 객체를 탐지하게 된다면 경보음 소리를 송출하여 주변 사람들이 빠른 인식으로 인명 피해는 물론 초기 화재 진압을 토대로 최소한에 손해를 목표로 개발하였습니다.

## 🖥️ 담당한 기능
##### • YOLO 학습에 필요한 데이터 이미지 라벨링
##### • YOLO 학습
##### • LINE API 연동 및 메세지 전송

## 📄 프로그램 구성도 및 YOLO 학습 결과
![123](https://github.com/inhwanGit/Wild-boar-elk-eradication-and-fire-notification-programs/assets/132810591/e059425e-36e7-4759-861b-af71f2b899af)
<img width="647" alt="345" src="https://github.com/inhwanGit/Wild-boar-elk-eradication-and-fire-notification-programs/assets/132810591/34a54081-cec3-4bd2-a6fc-36473c2dfeff">

## 👀 서비스 화면
![4555](https://github.com/inhwanGit/Wild-boar-elk-eradication-and-fire-notification-programs/assets/132810591/1612f179-a37b-407d-b10b-cead15dd2ec5)
##### • 멧돼지 객체 탐지 후 LINE에 전송
![ㅁㄴㅇ](https://github.com/inhwanGit/Wild-boar-elk-eradication-and-fire-notification-programs/assets/132810591/7d1bf363-1c8b-433a-9ea9-dfc9c859c67e)
##### • 고라니 객체 탐지 후 LINE에 전송 
![ㅇㅁㄴㅇㅁ](https://github.com/inhwanGit/Wild-boar-elk-eradication-and-fire-notification-programs/assets/132810591/0f4e7dec-1502-41d6-bc59-da023da4b806)
##### • 화재 객체 탐지 후 LINE에 전송
