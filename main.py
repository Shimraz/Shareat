# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:36:48 2022

@author: Shimraz
"""
"""
Receipt scanning and table output

"""
import requests
import json

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
data = JsonStore('data.json')

# Replace this with your
# current version
kivy.require('1.11.1')


# Defining a class
class MyFirstKivyApp(App):

    # Function that returns
    # the root widget
    def build(self):
        # Label with text Hello World is
        # returned as root widget
        receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt'  # Receipt OCR API endpoint
        imageFile = "receipt.png"  # // Modify this to use your own file if necessary
        r = requests.post(receiptOcrEndpoint, data={'client_id': 'TEST',  # Use 'TEST' for testing purpose \
                                                    'recognizer': 'auto',  # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
                                                    'ref_no': 'ocr_python_123',  # optional caller provided ref code \
                                                    }, \
                          files={"file": open(imageFile, "rb")})

        # print(r.text) # result in JSON

        y = json.loads(r.text)

<<<<<<< HEAD
print(r.text) # result in JSON
=======
        items = y['receipts'][0]['items']
>>>>>>> 3f550d0c97607a5d428fe96487c4e6c168f1c8db

        des = []
        for item in items:
            des.append(item['description'])

        print(des)

        # Get Name, quantity and cost
        all_items = {}
        for de in des:
            quantity = de.split('x')[0]
            name = de.split('x')[1].split('à')[0]
            data.put(name, quantity=quantity)
            print(name)

        data.put("bananas", quantity=2)
        data.put("apples", quantity=4)

        for key, data in data:
            print(key, ": ", data)

        return Label(text="Hello World !")


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()






