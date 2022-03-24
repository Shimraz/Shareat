#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
import json

receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
imageFile = "receipt.png" # // Modify this to use your own file if necessary
r = requests.post(receiptOcrEndpoint, data = {   'client_id': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})

# print(r.text) # result in JSON


y = json.loads(r.text)

items = y['receipts'][0]['items']

des = []
for item in items:
    des.append(item['description']) 

print(des)


# In[39]:


# Get Name, quantity and cost 
all_items = {}
for de in des:
    quantity = de.split('x')[0]
    name = de.split('x')[1].split('à')[0]
#     name = name.split('à')[0]
    all_items[name] = {'quantity':quantity}


print(all_items)


# In[ ]:




