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
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'  
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()