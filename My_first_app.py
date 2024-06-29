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
import winsound
import webbrowser
from math import *



# class MagicApp(App):
#     # def add_num(self, instance):
#     #     self.formula += str(instance.text)
#     #     print(self.formula)
#
#     def build(self):
#
#         def add_num(instance):
#             if self.lbl.text == '0':
#                 self.lbl.text= ''
#             self.lbl.text += str(instance.text)
#
#         def add_operation(instance):
#             if str(instance.text).lower() == 'x':
#                 self.lbl.text += '*'
#             else:
#                 self.lbl.text += str(instance.text)
#
#         def calculation(instance):
#             self.lbl.text = str(eval(self.lbl.text))
#
#         def clear(instance):
#             self.lbl.text = '0'
#
#         def undo(instance):
#             try:
#                 s = list(str(self.lbl.text))
#                 s.pop(len(s) - 1)
#                 self.lbl.text = ''.join(s)
#             except:
#                 self.lbl.text = '0'
#
#         bl = BoxLayout(orientation='vertical', padding=20)
#         gl = GridLayout(cols=4, spacing=2, size_hint=(1, 0.6))
#         self.lbl = Label(text='0', font_size=60, size_hint=(1, 0.3), valign='center', halign='right', text_size=(400-50, 500*0.4-50))
#         bl.add_widget(self.lbl)
#         btn_1 = Button(text='7', on_press=add_num)
#         btn_2 = Button(text='8',on_press=add_num)
#         btn_3 = Button(text='9',on_press=add_num)
#         btn_4 = Button(text='X', on_press=add_operation)
#         btn_5 = Button(text='4',on_press=add_num)
#         btn_6 = Button(text='5',on_press=add_num)
#         btn_7 = Button(text='6',on_press=add_num)
#         btn_8 = Button(text='-', on_press=add_operation)
#         btn_9 = Button(text='1',on_press=add_num)
#         btn_10 = Button(text='2',on_press=add_num)
#         btn_11 = Button(text='3',on_press=add_num)
#         btn_12 = Button(text='+', on_press=add_operation)
#         btn_13 = Button(text='0',on_press=add_num)
#         btn_14 = Button(text='.', on_press=add_num)
#         btn_15 = Button(text='=', on_press=calculation)
#         for el in(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_10, btn_11, btn_12, btn_13, btn_14, btn_15):
#             gl.add_widget(el)
#         gl.add_widget(Button(text='/', on_press=add_operation))
#         bl.add_widget(gl)
#         bl.add_widget(Button(text='Clear', size_hint=(1, 0.1), background_color=(0.1, 0.5, 0.1, 0.4), on_press=clear))
#         bl.add_widget(Button(text='Undo', size_hint=(1, 0.1), background_color=(0.1, 0.5, 0.1, 0.4), on_press=undo))
#
#         return bl
#
# if __name__ == '__main__':
#     MagicApp().run()

#
# class MyApp(App):
#
#     def __init__(self):
#         super().__init__()
#         self.lbl_conv = Label(text='Converter', font_size=40)
#         self.miles = Label(text='miles', font_size=30)
#         self.ft = Label(text='feet', font_size=30)
#         self.inch = Label(text='inches', font_size=30)
#         self.input_data = TextInput(hint_text='Enter in kilometer', multiline=False, font_size=30)
#
#     def build(self):
#         def on_text(instance, *args):
#             data = self.input_data.text
#             if data.isnumeric():
#                 self.miles.text = 'miles: ' + str(float(data) * 0.62)
#                 self.ft.text = 'feet: ' + str(float(data) * 3280)
#                 self.inch.text = 'inches: ' + str(float(data) * 39370)
#             else:
#                 self.input_data.text = ''
#
#         box = BoxLayout(orientation='vertical', padding=15, spacing=10)
#         box.add_widget(self.lbl_conv)
#         box.add_widget(self.input_data)
#         box.add_widget(self.miles)
#         box.add_widget(self.ft)
#         box.add_widget(self.inch)
#         self.input_data.bind(text=on_text)
#
#         return box
#
#
#
#
# if __name__ == '__main__':
#     MyApp().run()
#
# class MyApp(App):
#     def __init__(self):
#         super().__init__()
#         self.lbl_rect_1 = Label(text='Surface=')
#         self.lbl_rect_2 = Label(text='Perimeter=')
#         self.lbl_elps_1 = Label(text='Surface=')
#         self.lbl_elps_2 = Label(text='Perimeter=')
#         self.lbl_tr_1 = Label(text='Surface=')
#         self.lbl_tr_2 = Label(text='Perimeter=')
#         self.lbl_poly_1 = Label(text='Surface=')
#         self.lbl_poly_2 = Label(text='Perimeter=')
#         self.input_text_rect_1 = TextInput(hint_text='a=')
#         self.input_text_rect_2 = TextInput(hint_text='b=')
#         self.input_text_elps_1 = TextInput(hint_text='a=')
#         self.input_text_elps_2 = TextInput(hint_text='b=')
#         self.input_text_tr_1 = TextInput(hint_text='a=')
#         self.input_text_tr_2 = TextInput(hint_text='b=')
#         self.input_text_poly_1 = TextInput(hint_text='a=')
#         self.input_text_poly_2 = TextInput(hint_text='n=')
#
#
#     def build(self):
#         grid = GridLayout(cols=5, spacing=10, padding=10)
#
#         box_1 = BoxLayout(orientation='vertical')
#         for el in(self.input_text_rect_1, self.input_text_rect_2):
#             box_1.add_widget(el)
#
#         box_2 = BoxLayout(orientation='vertical')
#         for el in(self.input_text_elps_1, self.input_text_elps_2):
#             box_2.add_widget(el)
#
#         box_3 = BoxLayout(orientation='vertical')
#         for el in(self.input_text_tr_1, self.input_text_tr_2):
#             box_3.add_widget(el)
#
#         box_4 = BoxLayout(orientation='vertical')
#         for el in(self.input_text_poly_1, self.input_text_poly_2):
#             box_4.add_widget(el)
#
#         def on_text_1(instance, *args):
#             try:
#                 a = self.input_text_rect_1.text
#                 b = self.input_text_rect_2.text
#                 self.lbl_rect_1.text = 'Surface =' + str(float(a) * float(b))
#                 self.lbl_rect_2.text = 'Perimeter =' + (str(2 * float(a) + 2 * float(b)))
#             except:
#                 self.lbl_rect_1.text = '0'
#                 self.lbl_rect_2.text = '0'
#
#         def on_text_2(instance, *args):
#             try:
#                 a = self.input_text_elps_1.text
#                 b = self.input_text_elps_2.text
#                 self.lbl_elps_1.text = 'Surface =' + str(f'{float(a) * float(b) * pi :.2f}')
#                 self.lbl_elps_2.text = 'Perimeter =' + str(f'{2 * pi * sqrt(float(a) ** 2 + float(b) ** 2) / 2 :.2f}')
#             except:
#                 self.lbl_elps_1.text = '0'
#                 self.lbl_elps_2.text = '0'
#
#         def on_text_3(instance, *args):
#             try:
#                 a = self.input_text_tr_1.text
#                 b = self.input_text_tr_2.text
#                 self.lbl_tr_1.text = 'Surface =' + str((float(a) * float(b))/2)
#                 self.lbl_tr_2.text = 'Perimeter =' + (str(2*float(a) +float(b)))
#             except:
#                 self.lbl_tr_1.text = '0'
#                 self.lbl_tr_2.text = '0'
#
#         def on_text_4(instance, *args):
#             try:
#                 a = self.input_text_poly_1.text
#                 n = self.input_text_poly_2.text
#                 self.lbl_poly_1.text = 'Surface =' + str(f'{1.5 * sqrt(3) * float(a) ** 2 :.2f}')
#                 self.lbl_poly_2.text = 'Perimeter =' + str(float(a)* float(n))
#             except:
#                 self.lbl_poly_1.text = '0'
#                 self.lbl_poly_2.text = '0'
#
#         # fl.add_widget(Image(source='E:/G/link.GIF', size_hint=(0.8, 0.6), pos=(85, 200)))
#
#         grid.add_widget(Label(text='Rectangle', font_size=25))
#         grid.add_widget(Image(
#             source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Rectangle.PNG',
#                               size_hint=(0.8, 0.8)))
#         grid.add_widget(box_1)
#         grid.add_widget(self.lbl_rect_1)
#         grid.add_widget(self.lbl_rect_2)
#         grid.add_widget(Label(text='Ellipse', font_size=25))
#         grid.add_widget(Image(
#             source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Ellipse.PNG',
#                               size_hint=(0.8, 0.8)))
#         grid.add_widget(box_2)
#         grid.add_widget(self.lbl_elps_1)
#         grid.add_widget(self.lbl_elps_2)
#         grid.add_widget(Label(text='Triangle', font_size=25))
#         grid.add_widget(Image(
#             source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Triangle.PNG',
#                               size_hint=(0.8, 0.8)))
#         grid.add_widget(box_3)
#         grid.add_widget(self.lbl_tr_1)
#         grid.add_widget(self.lbl_tr_2)
#         grid.add_widget(Label(text='Polygon', font_size=25))
#         grid.add_widget(Image(
#             source='C:/Users/Patrick moon/PycharmProjects/Patrick_Project 1/MyFirstApp/Second_app/Polygon.PNG',
#                               size_hint=(0.8, 0.8)))
#         grid.add_widget(box_4)
#         grid.add_widget(self.lbl_poly_1)
#         grid.add_widget(self.lbl_poly_2)
#         self.input_text_rect_1.bind(text=on_text_1)
#         self.input_text_rect_2.bind(text=on_text_1)
#         self.input_text_elps_1.bind(text=on_text_2)
#         self.input_text_elps_2.bind(text=on_text_2)
#         self.input_text_tr_1.bind(text=on_text_3)
#         self.input_text_tr_2.bind(text=on_text_3)
#         self.input_text_poly_1.bind(text=on_text_4)
#         self.input_text_poly_2.bind(text=on_text_4)
#
#         return grid
#
#
# if __name__ == '__main__':
#     MyApp().run()
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "500")
Config.set("graphics", "resizable", "0")
# Window.clearcolor = (0.6, 0.25, 0.25, 0.5)
Window.clearcolor = (0.2, 0.1, 0.1, 1)
class MyMenuApp(App):
    def __init__(self):
        super().__init__()
        self.items = []
        self.qte = []
        self.menu ={}
        self.lbl_0 = Label(text='0', font_size=25)
        self.lb_1 = Label(text='Sushi hot one\nIngred: fish, milk\n100g\n \nPrice 10$', italic=True, size_hint_x=0.4)
        self.lb_2 = Label(text='Sushi cold one\nIngred: fish, milk\n100g\n \nPrice 12$', italic=True, size_hint_x=0.4)
        self.lb_3 = Label(text='Midle sushi cold one\nIngred: fish, milk, cheese\n100g\n \nPrice 15$',
                          italic=True, size_hint_x=0.4)
        self.lb_4 = Label(text='Hot Sushi one\nIngred: fish,tomato, milk\n100g\n \nPrice 13$', italic=True,
                          size_hint_x=0.4)
        self.lb_5 = Label(text='Sushi for one bigest\nIngred: fish, chesse\n100g\n \nPrice 12$', italic=True,
                          size_hint_x=0.4)
        self.lb_6 = Label(text='Burger for two\nIngred:bread, meat, cheese, frie\n200g\n \nPrice 20$',
                          italic=True, size_hint_x=0.4)
        self.lb_7 = Label(text='Burger set\nIngred:bread, meat, cheese, frie, drink\n200g\nPrice 25$',italic=True,
                              size_hint_x=0.4)
        self.lb_8 = Label(text='Burger set\nIngred:bread, meat, cheese, frie, drink\n200g\nPrice 25$', italic=True,
                          size_hint_x=0.4)
        self.lb_9 = Label(text='Pizza margarita\nIngred:pizza, tomatos, cheese\n100g\nPrice 13$', italic=True,
                          size_hint_x=0.4)
        self.lb_10 = Label(text='Pizza 5 cheeses\nIngred:pizza, chicken, tomatos, cheese\n100g\nPrice 15$',
                               italic=True, size_hint_x=0.4)

        self.chb_1 = CheckBox(size_hint_x=0.1)
        self.chb_2 = CheckBox(size_hint_x=0.1)
        self.chb_3 = CheckBox(size_hint_x=0.1)
        self.chb_4 = CheckBox(size_hint_x=0.1)
        self.chb_5 = CheckBox(size_hint_x=0.1)
        self.chb_6 = CheckBox(size_hint_x=0.1)
        self.chb_7 = CheckBox(size_hint_x=0.1)
        self.chb_8 = CheckBox(size_hint_x=0.1)
        self.chb_9 = CheckBox(size_hint_x=0.1)
        self.chb_10 = CheckBox(size_hint_x=0.1)


    def build(self):
        def add(instance):
            self.lbl_0.text = str(int(self.lbl_0.text)+1)

        def sub(instance):
            self.lbl_0.text = str(int(self.lbl_0.text)-1)


        def checkbox1(instance, value):
            if  value:
                self.menu[(self.lb_1.text)] = '0'
                print(self.menu)
            else:
                if self.lb_1.text in self.menu:
                    self.menu.pop(self.lb_1.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)

        def checkbox2(instance, value):
            if value:
                self.menu[(self.lb_2.text)] = '0'
                print(self.menu)
            else:
                if self.lb_2.text in self.menu:
                    self.menu.pop(self.lb_2.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)
        def checkbox3(instance, value):
            if value:
                self.menu[(self.lb_3.text)] = '0'
                print(self.menu)
            else:
                if self.lb_3.text in self.menu:
                    self.menu.pop(self.lb_3.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)

        def checkbox4(instance, value):
            if value:
                self.menu[(self.lb_4.text)] = '0'
                print(self.menu)
            else:
                if self.lb_4.text in self.menu:
                    self.menu.pop(self.lb_4.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)

        def checkbox5(instance, value):
            if value:
                self.menu[(self.lb_5.text)] = '0'
                print(self.menu)
            else:
                if self.lb_5.text in self.menu:
                    self.menu.pop(self.lb_5.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)

        def checkbox6(instance, value):
            if value:
                self.menu[(self.lb_6.text)] = '0'
                print(self.menu)
            else:
                if self.lb_6.text in self.menu:
                    self.menu.pop(self.lb_6.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)
        def checkbox7(instance, value):
            if value:
                self.menu[(self.lb_7.text)] = '0'
                print(self.menu)
            else:
                if self.lb_7.text in self.menu:
                    self.menu.pop(self.lb_7.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)

        def checkbox8(instance, value):
            if value:
                self.menu[(self.lb_8.text)] = '0'
                print(self.menu)
            else:
                if self.lb_7.text in self.menu:
                    self.menu.pop(self.lb_8.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)
        def checkbox9(instance, value):
            if value:
                self.menu[(self.lb_9.text)] = '0'
                print(self.menu)
            else:
                if self.lb_9.text in self.menu:
                    self.menu.pop(self.lb_9.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)
        def checkbox10(instance, value):
            if value:
                self.menu[(self.lb_10.text)] = '0'
                print(self.menu)
            else:
                if self.lb_10.text in self.menu:
                    self.menu.pop(self.lb_10.text)
                    print(self.menu)
                else:
                    print('item not in order')
                    print(self.menu)


        self.chb_1.bind(active=checkbox1)
        self.chb_2.bind(active=checkbox2)
        self.chb_3.bind(active=checkbox3)
        self.chb_4.bind(active=checkbox4)
        self.chb_5.bind(active=checkbox5)
        self.chb_6.bind(active=checkbox6)
        self.chb_7.bind(active=checkbox7)
        self.chb_8.bind(active=checkbox8)
        self.chb_9.bind(active=checkbox9)
        self.chb_10.bind(active=checkbox10)

        # self.chb_2.bind(active=checkbox1_solution)
        # self.chb_3.bind(active=checkbox1_solution)
        # self.chb_4.bind(active=checkbox1_solution)



        fl = FloatLayout()
        sv = ScrollView(size_hint_x=0.5, size_hint_y=1, x=250, bar_color=[1, 1, 1, 1],
                        bar_margin=2, bar_width=10)


        sl_0 = StackLayout( size_hint_x=0.1, size_hint_y=0.05, x=160)
        bl_0 = BoxLayout(orientation='horizontal')
        btn_0 = Button(text='+',font_size=25, background_color=[1, 1, 0, 0.5], on_press=add)
        btn_01=Button(text='-',font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub)
        for el in (btn_0, self.lbl_0, btn_01):
            bl_0.add_widget(el)
        sl_0.add_widget(bl_0)

        #panels
        bl = BoxLayout(orientation='vertical', size_hint_x=0.15, size_hint_y=1, x=0, y=0, spacing=6, padding=10)
        bl.add_widget(Button(text='Add to\norder', bold=True,italic=True, font_size= 18, padding=5, background_color=[1, 1, 0, 0.5]))
        bl.add_widget(Button(text='Send order', bold=True,italic=True, font_size= 18, padding=5, background_color=[0.9, 0.9, 0, 0.5]))
        bl.add_widget(Button(text='Delete order', bold=True,italic=True, font_size= 18, padding=5, background_color=[0.8, 0.8, 0, 0.5]))
        bl.add_widget(Button(text='Show your\n order', bold=True,italic=True, font_size= 18, padding=5, background_color=[0.7, 0.7, 0, 0.5]))
        bl.add_widget(Button(text='Call\npersonal', bold=True,italic=True, font_size= 18, padding=5, background_color=[0.6, 0.6, 0, 0.5]))
        bl.add_widget(Button(text='Call\nTaxi', background_color=[1, 1, 0, 0.5], bold=True,italic=True, font_size=18, padding=5))
        bl.add_widget(Widget())

        #image panels
        sl = StackLayout( size_hint_y=None)
        sl_1 = StackLayout(size_hint_y=None)
        sl_1.add_widget(self.chb_1)
        sl_1.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi1.JPG', size_hint_y=0.95, size_hint_x=0.5))
        sl_1.add_widget(self.lb_1)


        sl_2 = StackLayout(size_hint_y=None)
        sl_2.add_widget(self.chb_2)
        sl_2.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi2.JPG', size_hint_y=0.95, size_hint_x=0.5))
        sl_2.add_widget(self.lb_2)


        sl_3 = StackLayout(size_hint_y=None)
        sl_3.add_widget(self.chb_3)
        sl_3.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi4.JPG', size_hint_y=0.95,size_hint_x=0.5))
        sl_3.add_widget(self.lb_3)

        sl_4 = StackLayout(size_hint_y=None)
        sl_4.add_widget(self.chb_4)
        sl_4.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi3.JPG', size_hint_y=0.95,size_hint_x=0.5))
        sl_4.add_widget(self.lb_4)

        sl_5 = StackLayout(size_hint_y=None)
        sl_5.add_widget(self.chb_5)
        sl_5.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi5.JPG', size_hint_y=0.95,size_hint_x=0.5))
        sl_5.add_widget(self.lb_5)

        sl_6 = StackLayout(size_hint_y=None)
        sl_6.add_widget(self.chb_6)
        sl_6.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger1.JPG', size_hint_y=0.95,size_hint_x=0.5))
        sl_6.add_widget(self.lb_6)

        sl_7 = StackLayout(size_hint_y=None)
        sl_7.add_widget(self.chb_7)
        sl_7.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger2.JPG', size_hint_y=0.95,
                              size_hint_x=0.5))
        sl_7.add_widget(self.lb_7)

        sl_8 = StackLayout(size_hint_y=None)
        sl_8.add_widget(self.chb_8)

        sl_8.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger3.JPG', size_hint_y=0.95,
                              size_hint_x=0.5))
        sl_8.add_widget(self.lb_8)

        sl_9 = StackLayout(size_hint_y=None)
        sl_9.add_widget(self.chb_9)
        sl_9.add_widget(Image(source='C:/Users/Patrick moon/Downloads/pizza1.JPG', size_hint_y=0.95, size_hint_x=0.5))
        sl_9.add_widget(self.lb_9)

        sl_10 = StackLayout(size_hint_y=None)
        sl_10.add_widget(self.chb_10)
        sl_10.add_widget(Image(source='C:/Users/Patrick moon/Downloads/pizza2.JPG', size_hint_y=0.95, size_hint_x=0.5))
        sl_10.add_widget(self.lb_10)

        for el in (sl_1, sl_2, sl_3,sl_4, sl_5, sl_6, sl_7, sl_8, sl_9, sl_10):
            sl.add_widget(el)


        sl.bind(minimum_height=sl.setter("height"))
        sv.add_widget(sl)
        fl.add_widget(bl)
        fl.add_widget(sv)
        fl.add_widget(sl_0)
        # print(self.items)
        print(self.menu)

        return fl
if __name__ == '__main__':
    MyMenuApp().run()