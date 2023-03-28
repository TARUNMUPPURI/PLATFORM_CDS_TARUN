import cv2
import numpy as np
import pytesseract
from PIL import Image as im
image = cv2.imread('download6.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
thresh1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
plt.imshow(thresh1)
# data = pytesseract.image_to_string(thresh1, lang='eng', config='--psm 9')
# print(data)
import easyocr
reader = easyocr.Reader(['en'],gpu=False)
result=reader.readtext(thresh1)
result=result[0][1].upper()
result = result.replace(" ","")
result = result.replace("'","")


result=result[:1]+result[1].replace('G','6')+result[2:]
result=result[:1]+result[1].replace('Z','2')+result[2:]

result=result[:4]+result[4].replace('#','4')
result=result[:4]+result[4].replace('*','4')
result=result[:4]+result[4].replace('}','2')
print(result)

