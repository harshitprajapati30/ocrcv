import cv2
import numpy as np
import pytesseract
import os

print("hello")
# C:\Program Files\Tesseract-OCR
per = 25
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

imgQ = cv2.imread('0001.jpg')
h, w, c = imgQ.shape

orb = cv2.ORB_create(10000)
kp1, des1 = orb.detectAndCompute(imgQ, None)

path = 'userformspg1'
mypiclist = os.listdir(path)
print(mypiclist)
# for j, y in enumerate(mypiclist):
#     img = cv2.imread(path + "/" + y)
#     kp2, des2 = orb.detectAndCompute(img, None)
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING)
#     matches = bf.match(des2, des1)
#     matches.sort(key=lambda x: x.distance)
#     good = matches[:int(len(matches) * (per / 100))]
#     imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good[:100], None, flags=2)
#
#     srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
#     dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
#
#     M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
#     imgScan = cv2.warpPerspective(img, M, (w, h))
#     imgScan = cv2.resize(imgScan, (w // 5, h // 5))
#     cv2.imshow(y, imgScan)

text1 = pytesseract.image_to_string('userformspg1/1.jpg')
print(text1)
text2 = pytesseract.image_to_string('userformspg2/2.jpg')
print(text2)
