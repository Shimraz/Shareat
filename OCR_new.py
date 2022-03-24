#!/usr/bin/env python
# coding: utf-8

# In[57]:


import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk Replace with your working folder
# src_path = "C:\\Users\\<user>\\PycharmProjects\\ImageToText\\input\\"
src_path = "D:\\ANACONDA ENV\\Hackathon\\"
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'D:\\Programs\\Tessaract\\tesseract.exe' 
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract- 
# OCR/tesseract'
# TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("img",img)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
#     img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)
    custom_config = r' -c preserve_interword_spaces=10 '
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"), config=custom_config)

    # Remove template file
    #os.remove(temp)

    return result


print('--- Start recognize text from image ---')
extracted_text = get_string(src_path + "receipt.png")
print(extracted_text)
print("------ Done -------")


# In[44]:


receipt_ocr = {}
splits = extracted_text.splitlines()
restaurant_name = splits[0] + '' + splits[1]

import re
# regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY
date_pattern =r'\d{1,2}[./]\s\d{1,2}[./]\s\d{2,4}'

# date_pattern = r'(?<!0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
# date_pattern = r'^(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)[0-9]{2}$'
date = re.search(date_pattern, extracted_text).group()
receipt_ocr['date'] = date
print(date)


# In[64]:


# get lines with chf
lines_with_chf = []
for line in splits:
  if re.search(r'CHF',line):
    lines_with_chf.append(line)

print(lines_with_chf)


# In[66]:


# get items, total, ignore Incl
items = []
for line in lines_with_chf:
  print(line)
  if re.search(r'Incl',line):
    continue
  if re.search(r'Total', line):
    total = line
  else:
    items.append(line)

# Get Name, quantity and cost 
all_items = {}
for item in items:
  details = item.split()
  quantity_name = details[0]
  quantity = quantity_name.split('x')[0]
  name = quantity_name.split('x')[0]
  cost = details[-1]
  all_items[name] = {'quantity':quantity, 'cost':cost}
  
# total = total.split('CHF')[-1]

# Store the results in the dict
receipt_ocr['items'] = all_items
# receipt_ocr['total'] = total

import json

receipt_json = json.dumps(receipt_ocr)
print(receipt_json)


# In[ ]:




