# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:53:44 2022

@author: Shimraz
"""

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
import random


Window.size = (357, 667)

KV = '''
Screen:
    BoxLayout:
        MDLabel:
            text: 'SCORE'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            underline: 'true'
            bold: 'true'
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.9}
    BoxLayout:
        orientation : 'horizontal'
        MDLabel:
            id : your_points
            text: 'You: 0'
            font_name: "assets/JetBrainsMono.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.35, 'center_y' : 0.85}
        MDLabel:
            id : ai_points
            text: 'AI: 0'
            font_name: "assets/JetBrainsMono.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.65, 'center_y' : 0.85}
    BoxLayout:
        orientation : 'vertical'
        spacing : 10
        padding : 20
        MDRectangleFlatButton:
            text: 'R'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.3}
            on_release : app.play('r')
        MDRectangleFlatButton:
            text: 'P'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.2}
            on_release : app.play('p')
        MDRectangleFlatButton:
            text: 'S'
            font_name: "assets/JetBrainsMono-Medium.ttf"
            halign: 'center'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.1}
            on_release : app.play('s')
        MDFlatButton:
            text : 'Reset Score'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.84}
            font_name: "assets/JetBrainsMono-Medium.ttf"
            on_release : app.reset_score()
        MDFlatButton:
            id : ai_play
            text : 'Let AI play 1000 Times against itself'
            pos_hint : {'center_x' : 0.5, 'center_y' : 0.84}
            font_name: "assets/JetBrainsMono-Medium.ttf"
            on_release : 
                app.auto_play()
    BoxLayout:
        orientation : 'horizontal'
        Image:
            id : user_move
            allow_stretch : True
            keep_ratio : True
            source: "assets/rL.png"
        Image:
            id : ai_move
            allow_stretch : True
            keep_ratio : True
            source: "assets/rR.png"
        
            
        
'''