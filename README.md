히스토그램(Histogram)

직접 평활화를 구현하였음.

히스토그램을 사용하는 이유는 다양하게 있는데

1. 영상의 특성을 파악하기 위해서 사용한다.

![image](https://github.com/user-attachments/assets/2ced2d45-21d0-43a0-87f1-87165634fd25)




2. 영상 조작을 통해 영상 품질 개선
   ex)히스토그램 평활화
   
   원본사진
   ![원본사진](https://github.com/user-attachments/assets/1a779e99-4ca4-42db-87d3-041bbcea1550)


   
   평활화 진행사진
   ![평활화 진행 사진](https://github.com/user-attachments/assets/91ee9e8d-1b42-4f5e-a523-6ac44d25a3aa)



왼쪽은 원본 사진의 히스토그램이고 오른쪽은 평활화를 진행해준 히스토그램이다.

![히스토그램 평활화](https://github.com/user-attachments/assets/0b643b8c-d676-440c-bca4-74b8dcd17598)


3.히스토그램 역투영 연산을 통해 물체 검출 가능

ex) 기준으로 정할 얼굴영상을 히스토그램으로 표현하고 입력영상이 주어지면 둘의 히스토그램을 비교하여 얼굴을 검출함.
