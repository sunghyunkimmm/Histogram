import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/zebra2.jpeg")
print(img.shape)
#(183, 195, 3)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.array(img_gray)
print(img_gray)
print(img_gray.shape)

h = [0 for _ in range(256)]

#원본 사진의 히스토그램 확인
for i in range(img_gray.shape[0]):
    for j in range(img_gray.shape[1]):
        h[img_gray[i][j]]+= 1

print(h)

# # 화소 값
# pixels = list(range(256))
#
# # 그래프 생성
# plt.figure(figsize=(10, 6))
# plt.bar(pixels, h, color='blue', width=1.0)
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.grid(True)
# plt.show()

h = np.array(h)
h1 = h/(500*750)


#누적 진행
for i in range(256):
    if i == 0:
        pass
    h1[i] = h1[i-1] + h1[i]
h1 = 255*h1
h1 = np.round(h1)

print(h1)
img_gray1 = img_gray.copy()



p = [0 for _ in range(256)]


for i in range(img_gray1.shape[0]):
    for j in range(img_gray1.shape[1]):
        img_gray1[i][j] = h1[img_gray1[i][j]]

for i in range(img_gray1.shape[0]):
    for j in range(img_gray1.shape[1]):
        p[img_gray1[i][j]]+= 1

print(p)
# 화소 값
pixels = list(range(256))

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.bar(pixels, p, color='blue', width=1.0)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()
#
# cv2.imshow("img_gray1",img)
# cv2.waitKey(0)
# #
# #
#






