import kivy.app
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.text import LabelBase
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from kivy.uix.spinner import Spinner
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.carousel import Carousel
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.scatter import Scatter
from kivy.uix.actionbar import ActionBar, ActionButton, ActionView, ActionPrevious, ActionGroup, ActionCheck, ActionSeparator
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.filechooser import FileChooserListLayout, FileChooserListView, FileChooserIconView
from kivy.uix.effectwidget import EffectWidget, InvertEffect, HorizontalBlurEffect, VerticalBlurEffect, \
    MonochromeEffect, ChannelMixEffect, ScanlinesEffect, PixelateEffect, FXAAEffect
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Bezier, Rectangle, BoxShadow, Rotate
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.config import Config
from random import random
from math import *
import winsound
import webbrowser

Config.set("graphics", "width", "400")
Config.set("graphics", "height", "500")
Config.set("graphics", "resizable", "0")
Window.clearcolor = (0.5, 0.9, 0.9, 0.3)

class MyComplexApp(App):
    def __init__(self):
        super().__init__()
        self.lbl_conv = Label(text='Converter', font_size=40, underline=True)
        self.miles = Label(text='miles', font_size=30)
        self.ft = Label(text='feet', font_size=30)
        self.inch = Label(text='inches', font_size=30)
        self.input_data = TextInput(hint_text='Enter in kilometer', multiline=False, font_size=30)
        self.lbl = Label(text='0', font_size=60, size_hint=(1, 0.3), valign='center', halign='right',
                         text_size=(400 - 50, 500 * 0.4 - 50))
        self.lbl_rect_1 = Label(text='Surface=', font_size=20)
        self.lbl_rect_2 = Label(text='Perimeter=', font_size=20)
        self.lbl_elps_1 = Label(text='Surface=', font_size=20)
        self.lbl_elps_2 = Label(text='Perimeter=', font_size=20)
        self.lbl_tr_1 = Label(text='Surface=', font_size=20)
        self.lbl_tr_2 = Label(text='Perimeter=', font_size=20)
        self.lbl_poly_1 = Label(text='Surface=', font_size=20)
        self.lbl_poly_2 = Label(text='Perimeter=', font_size=20)
        self.input_text_rect_1 = TextInput(hint_text='a=', font_size=20)
        self.input_text_rect_2 = TextInput(hint_text='b=', font_size=20)
        self.input_text_elps_1 = TextInput(hint_text='a=', font_size=20)
        self.input_text_elps_2 = TextInput(hint_text='b=', font_size=20)
        self.input_text_tr_1 = TextInput(hint_text='a=', font_size=20)
        self.input_text_tr_2 = TextInput(hint_text='b=', font_size=20)
        self.input_text_poly_1 = TextInput(hint_text='a=', font_size=20)
        self.input_text_poly_2 = TextInput(hint_text='n=', font_size=20)


    def build(self):

        #calculator
        def add_num(instance):
            if self.lbl.text == '0':
                self.lbl.text= ''
            self.lbl.text += str(instance.text)

        def add_operation(instance):
            if str(instance.text).lower() == 'x':
                self.lbl.text += '*'
            else:
                self.lbl.text += str(instance.text)

        def calculation(instance):
            self.lbl.text = str(eval(self.lbl.text))

        def clear(instance):
            self.lbl.text = '0'

        def undo(instance):
            try:
                s = list(str(self.lbl.text))
                s.pop(len(s) - 1)
                self.lbl.text = ''.join(s)
            except:
                self.lbl.text = '0'

        # Unit converter

        def on_text(instance, *args):
            try:
                data = self.input_data.text
                self.miles.text = 'miles = ' + str(float(data) * 0.62)
                self.ft.text = 'feet = ' + str(float(data) * 3280)
                self.inch.text = 'inches = ' + str(float(data) * 39370)
            except:
                self.input_data.text = ''

        #Geo.surfaces

        def on_text_1(instance, *args):
            try:
                a = self.input_text_rect_1.text
                b = self.input_text_rect_2.text
                self.lbl_rect_1.text = 'Surface =' + str(float(a) * float(b))
                self.lbl_rect_2.text = 'Perimeter =' + (str(2 * float(a) + 2 * float(b)))
            except:
                self.lbl_rect_1.text = '0'
                self.lbl_rect_2.text = '0'

        def on_text_2(instance, *args):
            try:
                a = self.input_text_elps_1.text
                b = self.input_text_elps_2.text
                self.lbl_elps_1.text = 'Surface =' + str(f'{float(a) * float(b) * pi :.2f}')
                self.lbl_elps_2.text = 'Perimeter =' + str(f'{2 * pi * sqrt(float(a) ** 2 + float(b) ** 2) / 2 :.2f}')
            except:
                self.lbl_elps_1.text = '0'
                self.lbl_elps_2.text = '0'

        def on_text_3(instance, *args):
            try:
                a = self.input_text_tr_1.text
                b = self.input_text_tr_2.text
                self.lbl_tr_1.text = 'Surface =' + str((float(a) * float(b))/2)
                self.lbl_tr_2.text = 'Perimeter =' + (str(2 * float(a) + float(b)))
            except:
                self.lbl_tr_1.text = '0'
                self.lbl_tr_2.text = '0'

        def on_text_4(instance, *args):
            try:
                a = self.input_text_poly_1.text
                n = self.input_text_poly_2.text
                self.lbl_poly_1.text = 'Surface =' + str(f'{1.5 * sqrt(3) * float(a) ** 2 :.2f}')

                self.lbl_poly_2.text = 'Perimeter =' + str(float(a) * float(n))
            except:
                self.lbl_poly_1.text = '0'
                self.lbl_poly_2.text = '0'

        tb = TabbedPanel(
            do_default_tab=True, tab_pos='top_left', default_tab_text='Main page',height=200, width=300,
            background_color=(0.1, 0.1, 0.25, 0.5))

        #calculator
        tbi = TabbedPanelItem(text='Calculator', font_size=15, background_color=(0.5, 0.8, 0.8, 1),
                              height=100, width=500, underline=True)
        bl = BoxLayout(orientation='vertical', padding=20)
        gl = GridLayout(cols=4, spacing=2, size_hint=(1, 0.6))

        bl.add_widget(self.lbl)
        btn_1 = Button(text='7',font_size=25 ,  on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_2 = Button(text='8',font_size=25 , on_press=add_num)
        btn_3 = Button(text='9',font_size=25 , on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_4 = Button(text='x' ,font_size=25 , on_press=add_operation)
        btn_5 = Button(text='4',font_size=25 , on_press=add_num)
        btn_6 = Button(text='5',font_size=25 , on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_7 = Button(text='6',font_size=25 , on_press=add_num)
        btn_8 = Button(text='-',font_size=25 , on_press=add_operation)
        btn_9 = Button(text='1',font_size=25 , on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_10 = Button(text='2',font_size=25 , on_press=add_num)
        btn_11 = Button(text='3',font_size=25 , on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_12 = Button(text='+',font_size=25 , on_press=add_operation)
        btn_13 = Button(text='0',font_size=25 , on_press=add_num)
        btn_14 = Button(text='.', font_size=25 ,on_press=add_num, background_color=(0.1, 0.1, 0, 0.5))
        btn_15 = Button(text='=', font_size=25 ,on_press=calculation)
        for el in (
                btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9,
                btn_10, btn_11, btn_12, btn_13, btn_14,
                btn_15):
            gl.add_widget(el)
        gl.add_widget(Button(text='/', background_color=(0.1, 0.1, 0, 0.5), on_press=add_operation))
        bl.add_widget(gl)
        bl.add_widget(Button(text='Clear',font_size=25 , size_hint=(1, 0.1), background_color=(0.1, 0.5, 0.1, 0.4), on_press=clear))
        bl.add_widget(Button(text='Undo',font_size=25 , size_hint=(1, 0.1), background_color=(0.1, 0.5, 0.1, 0.4), on_press=undo))
        tbi.add_widget(bl)

        # unit converter
        tbi2 = TabbedPanelItem(text='Unit Converter', font_size=15, background_color=(0.5, 0.8, 0.8, 1),
                               height=100, width=500, underline=True)
        box = BoxLayout(orientation='vertical', padding=15, spacing=10)
        box.add_widget(self.lbl_conv)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.ft)
        box.add_widget(self.inch)
        tbi2.add_widget(box)
        self.input_data.bind(text=on_text)

        #Geometry
        tbi3 = TabbedPanelItem(text='Geo.surfaces', font_size=15, background_color=(0.5, 0.8, 0.8, 1),
                               height=100, width=500, underline=True)
        grid = GridLayout(cols=5, spacing=10, padding=10)

        box_1 = BoxLayout(orientation='vertical')
        for el in (self.input_text_rect_1, self.input_text_rect_2):
            box_1.add_widget(el)

        box_2 = BoxLayout(orientation='vertical')
        for el in (self.input_text_elps_1, self.input_text_elps_2):
            box_2.add_widget(el)

        box_3 = BoxLayout(orientation='vertical')
        for el in (self.input_text_tr_1, self.input_text_tr_2):
            box_3.add_widget(el)

        box_4 = BoxLayout(orientation='vertical')
        for el in (self.input_text_poly_1, self.input_text_poly_2):
            box_4.add_widget(el)

        grid.add_widget(Label(text='Rectangle', font_size=25))
        grid.add_widget(
            Image(
                source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Rectangle.PNG',
                  size_hint=(0.8, 0.8)))
        grid.add_widget(box_1)
        grid.add_widget(self.lbl_rect_1)
        grid.add_widget(self.lbl_rect_2)
        grid.add_widget(Label(text='Ellipse', font_size=25))
        grid.add_widget(
            Image(
                source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Ellipse.PNG',
                  size_hint=(0.8, 0.8)))
        grid.add_widget(box_2)
        grid.add_widget(self.lbl_elps_1)
        grid.add_widget(self.lbl_elps_2)
        grid.add_widget(Label(text='Triangle', font_size=25))
        grid.add_widget(
            Image(
                source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Triangle.PNG',
                  size_hint=(0.8, 0.8)))
        grid.add_widget(box_3)
        grid.add_widget(self.lbl_tr_1)
        grid.add_widget(self.lbl_tr_2)
        grid.add_widget(Label(text='Polygon', font_size=25))
        grid.add_widget(
            Image(
                source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Polygon.PNG',
                  size_hint=(0.8, 0.8)))
        grid.add_widget(box_4)
        grid.add_widget(self.lbl_poly_1)
        grid.add_widget(self.lbl_poly_2)
        tbi3.add_widget(grid)

        self.input_text_rect_1.bind(text=on_text_1)
        self.input_text_rect_2.bind(text=on_text_1)
        self.input_text_elps_1.bind(text=on_text_2)
        self.input_text_elps_2.bind(text=on_text_2)
        self.input_text_tr_1.bind(text=on_text_3)
        self.input_text_tr_2.bind(text=on_text_3)
        self.input_text_poly_1.bind(text=on_text_4)
        self.input_text_poly_2.bind(text=on_text_4)


        for el in (tbi, tbi2, tbi3):
            tb.add_widget(el)

        return tb

if __name__ == '__main__':
    MyComplexApp().run()