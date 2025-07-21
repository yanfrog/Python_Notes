# OpenCV (cv2) 教學筆記

OpenCV（Open Source Computer Vision Library）是一個跨平台、開源的電腦視覺與影像處理函式庫，常用於影像處理、物件偵測、追蹤與機器學習應用。

---

## 安裝方式

```bash
pip install opencv-python
# 如不需 GUI 顯示，可使用 headless 版本
pip install opencv-python-headless
```

---

## 基本操作

### 讀取、顯示、儲存影像

```python
import cv2

img = cv2.imread('image.jpg', flags = cv2.IMREAD_COLOR) # 讀取影像 (BGR)
    # IMREAD_COLOR：彩色讀取
    # IMREAD_GRAYSCALE：灰階讀取
    # IMREAD_UNCHANGED：包含 alpha 通道
    # IMREAD_REDUCED_COLOR_2(4, 8)：壓縮版本（1/2、1/4、1/8）
cv2.imshow('Window', img)                               # 顯示影像
    # 'Window' 為視窗名稱(GUI),
cv2.waitKey(0)                                          # 等待鍵盤輸入，若無輸入則回傳 -1
    # 0 表示無限等待直到有鍵盤輸入，1~n 表示等待 n 毫秒
cv2.destroyAllWindows()                                 # 關閉視窗
    # 也可以使用 cv2.destroyWindow(window_name)
cv2.imwrite('output.jpg', img)                          # 儲存影像
```

### 攝影機 / 影片擷取

```python
cap = cv2.VideoCapture(0)  # 參數為 0 表示使用預設攝影機
while True:
    ret, frame = cap.read()
    # ret 表示是否成功讀取，frame 為影像陣列
    if not ret:
        break
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```

---

## 🎨 色彩空間與轉換

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

---

## ✂️ 基本影像處理

```python
resized = cv2.resize(img, (300, 300))
cropped = img[50:200, 100:300]  # 裁切
flipped = cv2.flip(img, 1)      # 水平翻轉
```

---

## 🖌️ 圖形繪製與文字

```python
cv2.line(img, (10,10), (100,100), (0,255,0), 2)
cv2.circle(img, (150,150), 40, (255,0,0), -1)
cv2.putText(img, 'Hello', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
```

---

## 🔍 濾波與邊緣偵測

```python
blur = cv2.GaussianBlur(img, (5,5), 0)
edges = cv2.Canny(img, 100, 200)
```

---

## 📐 幾何變換

```python
M = cv2.getRotationMatrix2D((100, 100), 45, 1.0)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
```

---

## 🎯 閾值與二值化

```python
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                 cv2.THRESH_BINARY, 11, 2)
```

---

## 🧱 輪廓與形狀分析

```python
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)
```

---

## 🧠 特徵偵測與匹配（例如 ORB）

```python
orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(img, None)
img_kp = cv2.drawKeypoints(img, kp, None, color=(0,255,0))
```

---

## 📹 背景移除與目標追蹤（簡單示例）

```python
fgbg = cv2.createBackgroundSubtractorMOG2()
mask = fgbg.apply(frame)
```

---

## 🔍 臉部偵測（Haar Cascade）

```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
```

---

## 📚 資源

- 官方文件: https://docs.opencv.org/
- PyImageSearch: https://pyimagesearch.com
- GitHub 範例: https://github.com/opencv/opencv

---

## 📌 備註

- OpenCV 使用 BGR 色彩順序，不是 RGB。
- `cv2.imshow()` 僅在支援 GUI 的環境可用（Jupyter Notebook 建議使用 `matplotlib` 顯示影像）。