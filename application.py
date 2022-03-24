# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:57:49 2022

@author: Shimraz
"""

# from kivy.uix.screenmanager import Screen

# from kivymd.app import MDApp
# from kivymd.uix.button import MDRectangleFlatButton


# class MainApp(MDApp):
#     def build(self):
#         screen = Screen()
#         screen.add_widget(
#             MDRectangleFlatButton(
#                 text="Hello, World",
#                 pos_hint={"center_x": 0.5, "center_y": 0.5},
#             )
#         )
#         return screen


# MainApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
import random
import time
import requests
import json
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import WindowBase
from kivy.graphics import Canvas, Translate, Fbo, ClearColor, ClearBuffers
 

       
KV = '''
WindowManager:
    MainWindow:
    SecondWindow:
    cameraWidget:

<MainWindow>:
    name: "main"
    orientation : 'horizontal'
    
    BoxLayout:         
    MDLabel:
        text: 'Please scan the receipt'
        halign: 'center'
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.85}
        
    MDRectangleFlatButton:
        text: "Scan"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
        on_release:
            app.root.current = "Cameras"
            root.manager.transition.direction = "left"

<cameraWidget>:
    name: "Cameras"
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    MDRectangleFlatButton:
        text: 'ON Camera'
        on_press: camera.play #= not camera.play
        size_hint_y: None
        height: '48dp'
    MDRectangleFlatButton:
        text: "Capture"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.2}
        on_press: root.TakePicture()
        height: '48dp'


<SecondWindow>:
    name: "second"

    Button:
        text: "Go Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"


    
'''

''''
KV = '''
# Screen:
#     cameraWidget:
    # AnchorLayout:
    #     anchor_x: 'center'
    #     # anchor_y = 'top'
    #     MDToolbar:
    #         title: "MADS"
    
# <cameraWidget>:
#         orientation: 'vertical'
#         Camera:
#             id: camera
#             resolution: (640, 480)
#             play: False
#         ToggleButton:
#             text: 'ON Camera'
#             on_press: camera.play = not camera.play
#             size_hint_y: None
#             height: '48dp'
#         Button:
#             text: "Capture"
#             on_press: root.TakePicture()
#             height: '48dp'
        
#     BoxLayout:
#         MDLabel:
#             text: 'Scan'
#             #font_name: "assets/JetBrainsMono-Medium.ttf"
#             underline: 'true'
#             bold: 'true'
#             halign: 'center'
#             pos_hint : {'center_x' : 0.5, 'center_y' : 0.9}
            
    # BoxLayout:
    #     orientation: 'vertical'
    #     Camera:
    #         id: 'camera'
    #         resolution: (640, 480)
    #         play: True
    #     ToggleButton:
    #         text: 'Scan_now'
    #         on_press: camera.play #= not camera.play
    #         size_hint_y: None
    #         height: '48dp'  
    #     Button:
    #         # id = 'capture'
    #         text: 'Capture'
    #         size_hint_y: None
    #         height: '48dp'
    #         on_press: app.capture()

'''
'''
# kv = '''
# cameraWidget:
#     orientation: 'vertical'
#     Camera:
#         id: camera
#         resolution: (640, 480)
#         play: False
#     ToggleButton:
#         text: 'Play'
#         on_press: camera.play = not camera.play
#         size_hint_y: None
#         height: '48dp'
#     Button:
#         text: "Take picture"
#         on_press: root.TakePicture()
#         height: '48dp'
# '''
class cameraWidget(Screen):
    def TakePicture(self, *args):
        self.export_to_png = export_to_png
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.export_to_png(self.ids.camera, filename="IMG_{}.png".format(timestr))
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass



def export_to_png(self, filename, *args):
    '''Saves an image of the widget and its children in png format at the
    specified filename. Works by removing the widget canvas from its
    parent, rendering to an :class:`~kivy.graphics.fbo.Fbo`, and calling
    :meth:`~kivy.graphics.texture.Texture.save`.
    .. note::
        The image includes only this widget and its children. If you want to
        include widgets elsewhere in the tree, you must call
        :meth:`~Widget.export_to_png` from their common parent, or use
        :meth:`~kivy.core.window.Window.screenshot` to capture the whole
        window.
    .. note::
        The image will be saved in png format, you should include the
        extension in your filename.
    .. versionadded:: 1.8.1
    '''

    if self.parent is not None:
        canvas_parent_index = self.parent.canvas.indexof(self.canvas)
        self.parent.canvas.remove(self.canvas)

    fbo = Fbo(size=self.size)

    with fbo:
        ClearColor(0, 0, 0, 1)
        ClearBuffers()
        Translate(-self.x, -self.y, 0)

    fbo.add(self.canvas)
    fbo.draw()
    fbo.texture.save(filename)
    fbo.remove(self.canvas)

    if self.parent is not None:
        self.parent.canvas.insert(canvas_parent_index, self.canvas)

    return True

class MADSApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainWindow(name='main'))
        self.sm.add_widget(cameraWidget(name='Cameras'))
        # screen = Screen()
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Gray"
        #screen.add_widget(self.kvs)
        return self.sm
    
    # def capture(self):
    #     '''
    #     Function to capture the images and give them the names
    #     according to their captured time and date.
    #     '''
    #     capture = self.ids['camera']
    #     # camera = self.kvs.ids['camera']
    #     timestr = time.strftime("%Y%m%d_%H%M%S")
    #     capture.export_to_png("IMG_{}.png".format(timestr))
    #     print("Captured")
    #     return True
    
    def func(self):

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
        
        
        
        # Get Name, quantity and cost 
        Table_items = {}
        for de in des:
            quantity = de.split('x')[0]
            name = de.split('x')[1].split('à')[0]
        #     name = name.split('à')[0]
            Table_items[name] = {'quantity':quantity}
    

if __name__ == '__main__':
    mads = MADSApp()
    mads.run()
    
    
    
    
    
