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


# Replace this with your
# current version
kivy.require('1.11.1')


# Defining a class
class MyFirstKivyApp(App):

    # Function that returns
    # the root widget
    def build(self):
        data = JsonStore('data.json')

        data.put("bananas", quantity=2)
        data.put("apples", quantity=4)

        url = "https://api.mindee.net/v1/products/mindee/expense_receipts/v3/predict"

        with open("receipt.png", "rb") as myfile:
            files = {"document": myfile}
            headers = {"Authorization": "Token 0239a53e8839c150bf8d3b71d5055c21"}
            response = requests.post(url, files=files, headers=headers)
            print(response.text)

        for key in data:
            print(key, ": ", data.get(key)['quantity'])

        return Label(text="Hello World !")


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()






