import cv2 as cv
import time # 單位：秒
import numpy as np
import os

count = 0
'''
# rename
for image in os.listdir('./sigmaman'):
    if image.endswith('.jpg'):
        count += 1
        new_name = f'sigmaman_{count:02d}.jpg'
        os.rename(os.path.join('./sigmaman', image), os.path.join('./sigmaman', new_name))
'''
'''
# 讀取圖片
for image in os.listdir('./sigmaman'):
    if image.endswith('.jpg'):
        img_path = './sigmaman/' + image
        print(img_path)
        img = cv.imread(img_path)
        cv.imshow(image, img)
        cv.waitKey(0)
        cv.destroyAllWindows()
'''
# 計算FPS並顯示
def show_fps(image, fps):
    cv.putText(img = image,
            text = f"FPS: {fps:.2f}",
            org = (30, 50), # 右上角是座標原點，向右、向下遞增，單位：像素
            fontFace = cv.FONT_HERSHEY_SIMPLEX,
            fontScale = 1,
            color = (255, 255, 255), # BGR
            thickness = 2)
# 讀取影片
prev_time = time.time()
capture = cv.VideoCapture('./sigmaman/sigmaman.mp4') # 影片路徑
while True:
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1)
    # 1：水平翻轉，0：垂直翻轉，-1：水平、垂直翻轉
    if not isTrue:
        break
    # 計算 FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    # 在影像上顯示 FPS
    show_fps(frame, fps)
    # 顯示影片
    cv.imshow('Video', frame)
    # 讀取過程中若按下 q 則離開
    if cv.waitKey(1) != -1:
        break
    # 持續讀取影片，直到讀取完畢
    else:
        continue
capture.release()
cv.destroyAllWindows()