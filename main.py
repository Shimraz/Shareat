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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
import time
import requests
import json
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import WindowBase
from kivy.graphics import Canvas, Translate, Fbo, ClearColor, ClearBuffers
from kivy.utils import platform
from kivy.storage.jsonstore import JsonStore
from kivy.base import EventLoop

if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.CAMERA, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

# Window.size = (357, 667)
# Window.fullscreen = 'auto'

data = {'Latte Macchiato ': {'quantity': '2'},
        'Gloki': {'quantity': '1'},
        'Schweinschnitzel ': {'quantity': '1'},
        'Chässpätzli ': {'quantity': '1'}}

KV = '''
# GridLayout:
    # cols: 1
WindowManager:
    MainWindow:
    SecondWindow:
    cameraWidget:


<MainWindow>:
    name: "main"
    orientation : 'horizontal'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'icon.png'
    BoxLayout:         
    MDLabel:
        text: 'Please scan the receipt'
        halign: 'center'
        pos_hint : {'center_x' : 0.2, 'center_y' : 0.4}

    MDRectangleFlatButton:
        text: "Scan"
        pos_hint : {'center_x' : 0.7, 'center_y' : 0.4}
        on_release:
            app.root.current = "Cameras"
            root.manager.transition.direction = "left"

<cameraWidget>:
    orientation: 'vertical'
    name: "Cameras"
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'icon.png'
    Camera:
        id: camera
        resolution: (1024, 1024)
        play: False
    MDRectangleFlatButton:
        text: 'ON Camera'
        pos_hint : {'center_x' : 0.05, 'center_y' : 0.2}
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'

    MDRectangleFlatButton:
        text: "Capture"
        pos_hint : {'center_x' : 0.2, 'center_y' : 0.2}
        on_press: 
            root.TakePicture()
            # root refers to <cameraWidget>
            # app refers to TestCamera, app.root refers to the GridLayout: at the top

        height: '48dp'

    MDRectangleFlatButton:
        text: "Go Back"
        pos_hint : {'center_x' : 0.7, 'center_y' : 0.2}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

    MDRectangleFlatButton:
        text: "Next"
        pos_hint : {'center_x' : 0.95, 'center_y' : 0.2}
        on_release:
            root.manager.transition.direction = 'left'
            app.root.current = "second"


<SecondWindow>:
    name : "second"
    orientation : 'horizontal'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'icon.png'
    BoxLayout:
    MDRectangleFlatButton:
        text: "Go Back"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.2}
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"

    MDRectangleFlatButton:
        id: btnExit
        pos_hint : {'center_x' : 0.95, 'center_y' : 0.2}
        text: "Exit"
        on_press: app.close_application()

<DataLine>:  # class to hold one line of data
    canvas:
        Color:
            rgb: .3, .3, .3
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    size_hint_y: None
    height: 48
    Label:
        text: root.name
    Label:
        text: root.color
    Label:
        text: root.birthday

    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 48
            text: 'Data List in a Scrollview Example'
        BoxLayout:  # Headings for 
            size_hint_y: None
            height: 48
            Label:
                text: 'Name'
            Label:
                text: 'Favorite Color'
            Label:
                text: 'Birthday'
        ScrollView:
            do_scroll_y: True
            bar_width: dp(10)
            scroll_type: ['bars','content']
            BoxLayout:
                orientation: 'vertical'
                id:scroll_box
                size_hint_y: None
                height: self.minimum_height

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
        filename = "IMG_{}.png".format(timestr)
        self.last_scan = filename
        self.export_to_png(self.ids.camera, filename=filename)
        self.extract_data()

    def extract_data(self):

        data = JsonStore('data.json')
        CLIENT_ID = "vrfV7PAu5YaeLRD4tjGnmtvTVTDtpZVdDyoePTU"
        ENVIRONMENT_URL = "https://api.veryfi.com/"

        username = "domenikmueller"
        api_key = "9bac9fbb0efdfc5951cd72a7884e0ea5"
        process_file_url = '{0}api/v7/partner/documents/'.format(ENVIRONMENT_URL)
        headers = {
            "Accept": "application/json",
            "CLIENT-ID": CLIENT_ID,
            "AUTHORIZATION": "apikey {0}:{1}".format(username, api_key)
        }

        # file path and file name
        file_name = self.last_scan

        # You can send the list of categories that is relevant to your case
        # Veryfi will try to choose the best one that fits this document
        categories = ["Meals & Entertainment", "Utilities", "Automobile"]
        payload = {
            'file_name': file_name,
            'categories': categories
        }

        files = {'file': ('file', open(file_name, 'rb'), 'image/png')}
        response = requests.post(url=process_file_url, headers=headers, data=payload, files=files)
        print(response.json())
        currency = "EUR"
        if response.json()['currency_code']:
            currency = response.json()['currency_code']

        if response.json()['line_items']:
            for item in response.json()['line_items']:
                data.put(item['description'], price=item['price'], quantity=item['quantity'], currency=currency)

        for key in data:
            print(key, ": ", data.get(key)['quantity'])

        data.store_sync()


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class DataLine(BoxLayout):  # class to hold one line of data
    name = StringProperty()
    color = StringProperty()
    birthday = StringProperty()


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
        self.sm.add_widget(SecondWindow(name='second'))
        self.data = JsonStore('data.json')
        # screen = Screen()
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Gray"
        # screen.add_widget(self.kvs)
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
    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()

    #     self.reset()

    # def reset(self):

    #     if not EventLoop.event_listeners:
    #         from kivy.cache import Cache
    #         Window.Window = Window.core_select_lib('window', Window.Window_impl, True)
    #         for cat in Cache._categories:
    #             Cache._objects[cat] = {}

    def on_start(self):
        info = [['Michael', 'Blue', '1/30/2020'],  # simulating what could come out of a database
                ['Carol', 'Green', '12/3/2020'],
                ['Bill', 'Red', '3/12/2020'],
                ['Sue', 'Orange', '7/4/2020'],
                ['John', 'Blue', '5/23/2020'],
                ['Jane', 'Yellow', '3/9/2020'],
                ['Michael', 'Blue', '2/30/2020'],
                ['Carol', 'Green', '4/3/2020'],
                ['Bill', 'Red', '3/12/2020'],
                ['Sue', 'Orange', '8/4/2020'],
                ['John', 'Blue', '10/23/2020'],
                ['Jane', 'Yellow', '6/9/2020']]

        for line in info:
            name, color, bd = line
            # w = DataLine(name=name, color=color, birthday=bd)  # instancing the class
            # self.root.ids.scroll_box.add_widget(w)             # adding the class to the scrollview




if __name__ == '__main__':
    mads = MADSApp()
    mads.run()





