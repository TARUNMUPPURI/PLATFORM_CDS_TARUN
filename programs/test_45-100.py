from selenium import webdriver
from requestium import Session
from time import sleep
import re
from io import BytesIO
import xlsxwriter
import PIL.Image as Image
import io
import base64
from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image as im
import easyocr

def download_captcha(i):
        
    s = Session('/usr/local/bin/chromedriver', browser='chrome', default_timeout=15, webdriver_options={'arguments': [
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36',
            "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection",
            "--disable-blink-features=AutomationControlled",'no-sandbox']})
    s.driver.set_window_size(1920, 1080)
    driver = s.driver
    driver.get('https://online.canarabank.in/?module=login')
    sleep(10)
    code =driver.page_source
    with open('canara_source.html','w') as f:
        f.write(driver.page_source)
    with open('canara_source.html') as html_file:
        soup = BeautifulSoup(html_file,'lxml')
    try:
        link = soup.find("img",class_="customCaptcha oj-sm-12 oj-md-12").get('src')
    except:
            pass
    pat1 = re.compile(r'(data:image/gif;base64,)(.*)')
    mat1=pat1.finditer(link)
    for match in mat1:
            img_src = match.group(2)   
    url = img_src
    b=base64.b64decode(url)
    with open(r"image"+str(i)+".png", 'wb') as f:
        f.write(b)


def convert_image(i):
    image = cv2.imread('image'+str(i)+'.png')
    # image=cv2.imread('output.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    thresh1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    plt.imshow(thresh1)
    # data = pytesseract.image_to_string(thresh1, lang='eng', config='--psm 9')
    # print(data)
    # thresh1.save('output.png')
    reader = easyocr.Reader(['en'],gpu=False)
    result=reader.readtext(thresh1)
    result=result[0][1].upper()
    return result

def training_output(result):
    result = result.replace(" ","")
    result = result.replace("'","")
    if len(result)<5:
        pass    
    elif len(result)==5:  
        # 1sr index character
        result=result[0].replace('#','H')+result[1:]
        result=result[0].replace('1','L')+result[1:]
        result=result[0].replace('7','T')+result[1:]
        result=result[0].replace('2','Z')+result[1:]
        result=result[0].replace('6','G')+result[1:]
        result=result[0].replace('8','B')+result[1:]
        # 2nd index character
        result=result[0]+result[1].replace('G','6')+result[2:]
        result=result[0]+result[1].replace('Z','2')+result[2:]
        result=result[0]+result[1].replace('?','7')+result[2:]
        result=result[0]+result[1].replace('B','3')+result[2:]
        result=result[0]+result[1].replace('J','3')+result[2:]
        result=result[0]+result[1].replace('Z','7')+result[2:]
        result=result[0]+result[1].replace('>','7')+result[2:]
        result=result[0]+result[1].replace('X','4')+result[2:]
        result=result[0]+result[1].replace('A','4')+result[2:]
        result=result[0]+result[1].replace('T','4')+result[2:]
        result=result[0]+result[1].replace('+','4')+result[2:]
        result=result[0]+result[1].replace('&','8')+result[2:]
        # 3rd index character
        result=result[:2]+result[2].replace('*','X')+result[3:]
        result=result[:2]+result[2].replace('€','E')+result[3:]
        result=result[:2]+result[2].replace('8','B')+result[3:]
        result=result[:2]+result[2].replace('+','V')+result[3:]
        result=result[:2]+result[2].replace('0','D')+result[3:]
        result=result[:2]+result[2].replace('4','A')+result[3:]
        result=result[:2]+result[2].replace('1','K')+result[3:]
        # 4th index integer
        result=result[:3]+result[3].replace('&','G')+result[4]
        result=result[:3]+result[3].replace(']','J')+result[4]
        result=result[:3]+result[3].replace('[','J')+result[4]
        result=result[:3]+result[3].replace('€','E')+result[4]
        result=result[:3]+result[3].replace('6','K')+result[4]
        result=result[:3]+result[3].replace('0','D')+result[4]
        result=result[:3]+result[3].replace('8','B')+result[4]
        # 5th digit character
        result=result[:4]+result[4].replace('#','4')
        result=result[:4]+result[4].replace('*','4')
        result=result[:4]+result[4].replace('}','2')
        result=result[:4]+result[4].replace('F','7')
        result=result[:4]+result[4].replace('$','8')
        result=result[:4]+result[4].replace('S','8')
        result=result[:4]+result[4].replace('T','2')
        result=result[:4]+result[4].replace('Z','2')
        result=result[:4]+result[4].replace('&','6')
        result=result[:4]+result[4].replace('-','7')
        result=result[:4]+result[4].replace('?','2')
        result=result[:4]+result[4].replace('.','7')
        result=result[:4]+result[4].replace('=','7')
        result=result[:4]+result[4].replace('/','7')
        result=result[:4]+result[4].replace('S','8')
        return result

def write_in_excel(i,result):  
    filename = 'image'+str(i)+'.png'
    # filename='output.png'
    file = open(filename, 'rb')
    data = BytesIO(file.read())
    file.close()
    # worksheet.insert_image('A+str(2*i)', filename)
    # worksheet.insert_image(2, i, filename)
    # worksheet.insert_image(2*i,'A', filename, {'image_data': data})
    worksheet.insert_image(str('A'+str(2*i)), filename)
    worksheet.write(str('D'+str(2*i)), result)

def resize_image_remove_border(i):
    filename='image'+str(i)+'.png'
    image = Image.open(filename)
    right = 10
    left = 10
    top = 10
    bottom = 10
    
    width, height = image.size  
    new_width = width + right + left
    new_height = height + top + bottom  
    result1 = Image.new(image.mode, (new_width, new_height), "white")  
    result1.paste(image, (left, top))  
    result1.save('image'+str(i)+'.png')


workbook = xlsxwriter.Workbook('test_full.xlsx')
worksheet = workbook.add_worksheet()
for i in range(1,100):
    # download_captcha(i)    
    result=convert_image(i)
    if len(result)<5:
        resize_image_remove_border(i)
        result=convert_image(i)
    res = training_output(result)
    print(res)  
    write_in_excel(i,res)
workbook.close()
# cv2.dilate
# cv2.resize