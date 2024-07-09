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
from random import *



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





# Config.set("graphics", "width", "400")
# Config.set("graphics", "height", "500")
# Config.set("graphics", "resizable", "0")
# Window.clearcolor = (0.6, 0.25, 0.25, 0.5)
# Window.clearcolor = (0.2, 0.1, 0.1, 1)
# Window.size = (800, 700)
# class MyMenuApp(App):
#     def __init__(self):
#         super().__init__()
#
#         self.menu ={}
#         self.show_orders = Label(text='No orders')
#         self.lbl_ord_show = Label(text='')
#         self.lbl_00 = Label(text='1', font_size=25)
#         self.lbl_01 = Label(text='1', font_size=25)
#         self.lbl_02 = Label(text='1', font_size=25)
#         self.lbl_03 = Label(text='1', font_size=25)
#         self.lbl_04 = Label(text='1', font_size=25)
#         self.lbl_05 = Label(text='1', font_size=25)
#         self.lbl_06 = Label(text='1', font_size=25)
#         self.lbl_07 = Label(text='1', font_size=25)
#         self.lbl_08 = Label(text='1', font_size=25)
#         self.lbl_09 = Label(text='1', font_size=25)
#         self.lbl_010 = Label(text='1', font_size=25)
#         self.lb_1 = Label(text='Sushi hot one\nIngred: fish, milk\n100g\nPrice 10$', italic=True, size_hint_x=0.2)
#         self.lb_2 = Label(text='Sushi cold one\nIngred: fish, milk\n100g\n Price 12$', italic=True, size_hint_x=0.2)
#         self.lb_3 = Label(text='Midle sushi cold one\nIngred: fish, milk, cheese\n100g\nPrice 15$',
#                           italic=True, size_hint_x=0.2)
#         self.lb_4 = Label(text='Hot Sushi one\nIngred: fish,tomato, milk\n100g\nPrice 13$', italic=True,
#                           size_hint_x=0.2)
#         self.lb_5 = Label(text='Sushi for one bigest\nIngred: fish, chesse\n100g\nPrice 12$', italic=True,
#                           size_hint_x=0.2)
#         self.lb_6 = Label(text='Burger for two\nIngred:bread, meat,\ncheese, frie\n200g\nPrice 20$',
#                           italic=True, size_hint_x=0.2)
#         self.lb_7 = Label(text='Burger set\nIngred:bread, meat, cheese,\nfrie, drink\n200g\nPrice 25$',italic=True,
#                               size_hint_x=0.2)
#         self.lb_8 = Label(text='Burger set\nIngred:bread, meat, \ncheese, frie, drink\n200g\nPrice 25$', italic=True,
#                           size_hint_x=0.2)
#         self.lb_9 = Label(text='Pizza margarita\nIngred:pizza,\n tomatos, cheese\n100g\nPrice 13$', italic=True,
#                           size_hint_x=0.2)
#         self.lb_10 = Label(text='Pizza 5 cheeses\nIngred:pizza, chicken,\n tomatos, cheese\n100g\nPrice 15$',
#                                italic=True, size_hint_x=0.2)
#
#         self.chb_1 = CheckBox(size_hint_x=0.05)
#         self.chb_2 = CheckBox(size_hint_x=0.05)
#         self.chb_3 = CheckBox(size_hint_x=0.05)
#         self.chb_4 = CheckBox(size_hint_x=0.05)
#         self.chb_5 = CheckBox(size_hint_x=0.05)
#         self.chb_6 = CheckBox(size_hint_x=0.05)
#         self.chb_7 = CheckBox(size_hint_x=0.05)
#         self.chb_8 = CheckBox(size_hint_x=0.05)
#         self.chb_9 = CheckBox(size_hint_x=0.05)
#         self.chb_10 = CheckBox(size_hint_x=0.05)
#
#
#     def build(self):
#         def add0(instance):
#             self.lbl_00.text = str(int(self.lbl_01.text)+1)
#
#         def sub0(instance):
#             self.lbl_00.text = str(int(self.lbl_01.text)-1)
#
#         def add(instance):
#             self.lbl_01.text = str(int(self.lbl_01.text)+1)
#
#         def sub(instance):
#             self.lbl_01.text = str(int(self.lbl_01.text)-1)
#
#
#         def add2(instance):
#             self.lbl_02.text = str(int(self.lbl_02.text) + 1)
#
#         def sub2(instance):
#             self.lbl_02.text = str(int(self.lbl_02.text) - 1)
#
#
#         def add3(instance):
#             self.lbl_03.text = str(int(self.lbl_03.text) + 1)
#
#         def sub3(instance):
#             self.lbl_03.text = str(int(self.lbl_03.text) - 1)
#
#
#         def add4(instance):
#             self.lbl_04.text = str(int(self.lbl_04.text) + 1)
#
#         def sub4(instance):
#             self.lbl_04.text = str(int(self.lbl_04.text) - 1)
#
#         def add5(instance):
#             self.lbl_05.text = str(int(self.lbl_05.text) + 1)
#
#         def sub5(instance):
#             self.lbl_05.text = str(int(self.lbl_05.text) - 1)
#
#
#         def add6(instance):
#             self.lbl_06.text = str(int(self.lbl_06.text) + 1)
#
#         def sub6(instance):
#             self.lbl_06.text = str(int(self.lbl_06.text) - 1)
#
#         def add7(instance):
#             self.lbl_07.text = str(int(self.lbl_07.text) + 1)
#
#         def sub7(instance):
#             self.lbl_07.text = str(int(self.lbl_07.text) - 1)
#
#         def add8(instance):
#             self.lbl_08.text = str(int(self.lbl_08.text) + 1)
#
#         def sub8(instance):
#             self.lbl_08.text = str(int(self.lbl_08.text) - 1)
#
#         def add9(instance):
#             self.lbl_09.text = str(int(self.lbl_09.text) + 1)
#
#         def sub9(instance):
#             self.lbl_09.text = str(int(self.lbl_09.text) - 1)
#
#         def add10(instance):
#             self.lbl_010.text = str(int(self.lbl_010.text) + 1)
#
#         def sub10(instance):
#             self.lbl_010.text = str(int(self.lbl_010.text) - 1)
#
#         def checkbox1(instance, value):
#             if  value:
#                 if int(str(self.lbl_01.text)) >=0:
#                     self.menu[(self.lb_1.text)] = str(self.lbl_01.text)
#                     self.lbl_01.text = '1'
#                     print(self.menu)
#                     show_popup_order(instance)
#                     print(self.lbl_ord_show.text)
#                 else:
#                     self.menu[(self.lb_1.text)] ='0'
#
#             else:
#                 if self.lb_1.text in self.menu:
#                     self.menu.pop(self.lb_1.text)
#                     self.lbl_01.text = '1'
#                     bn1.background_color = [1, 1, 0, 0.5]
#                     bn1.text = 'Add\nitems'
#                     # print(self.menu)
#
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox2(instance, value):
#
#             if value:
#                 self.menu[(self.lb_2.text)] =str(self.lbl_02.text)
#                 self.lbl_02.text = '1'
#                 print(self.menu)
#                 show_popup_order(instance)
#                 print(self.lbl_ord_show.text)
#
#             else:
#                 if self.lb_2.text in self.menu:
#                     self.menu.pop(self.lb_2.text)
#                     self.lbl_02.text = '1'
#                     bn2.background_color = [1, 1, 0, 0.5]
#                     bn2.text = 'Add\nitems'
#                     # print(self.menu)
#
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox3(instance, value):
#             if value:
#                 self.menu[(self.lb_3.text)] =str(self.lbl_03.text)
#                 self.lbl_03.text = '1'
#                 # print(self.menu)
#                 show_popup_order(instance)
#             else:
#                 if self.lb_3.text in self.menu:
#                     self.menu.pop(self.lb_3.text)
#                     self.lbl_03.text = '1'
#                     bn3.background_color = [1, 1, 0, 0.5]
#                     bn3.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox4(instance, value):
#             if value:
#                 self.menu[(self.lb_4.text)] = str(self.lbl_04.text)
#                 self.lbl_04.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#
#             else:
#                 if self.lb_4.text in self.menu:
#                     self.menu.pop(self.lb_4.text)
#                     self.lbl_04.text = '1'
#                     bn4.background_color = [1, 1, 0, 0.5]
#                     bn4.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox5(instance, value):
#             if value:
#                 self.menu[(self.lb_5.text)] =str(self.lbl_05.text)
#                 self.lbl_05.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_5.text in self.menu:
#                     self.menu.pop(self.lb_5.text)
#                     self.lbl_05.text = '1'
#                     bn5.background_color = [1, 1, 0, 0.5]
#                     bn5.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox6(instance, value):
#             if value:
#                 self.menu[(self.lb_6.text)] = str(self.lbl_06.text)
#                 self.lbl_06.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_6.text in self.menu:
#                     self.menu.pop(self.lb_6.text)
#                     self.lbl_06.text = '1'
#                     bn6.background_color = [1, 1, 0, 0.5]
#                     bn6.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox7(instance, value):
#             if value:
#                 self.menu[(self.lb_7.text)] = str(self.lbl_07.text)
#                 self.lbl_07.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_7.text in self.menu:
#                     self.menu.pop(self.lb_7.text)
#                     self.lbl_07.text = '1'
#                     bn7.background_color = [1, 1, 0, 0.5]
#                     bn7.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def checkbox8(instance, value):
#             if value:
#                 self.menu[(self.lb_8.text)] =str(self.lbl_08.text)
#                 self.lbl_08.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_7.text in self.menu:
#                     self.menu.pop(self.lb_8.text)
#                     self.lbl_08.text = '1'
#                     bn8.background_color = [1, 1, 0, 0.5]
#                     bn8.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#         def checkbox9(instance, value):
#             if value:
#                 self.menu[(self.lb_9.text)] = str(self.lbl_09.text)
#                 self.lbl_09.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_9.text in self.menu:
#                     self.menu.pop(self.lb_9.text)
#                     self.lbl_09.text = '1'
#                     bn9.background_color = [1, 1, 0, 0.5]
#                     bn9.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#         def checkbox10(instance, value):
#             if value:
#                 self.menu[(self.lb_10.text)] = str(self.lbl_010.text)
#                 self.lbl_010.text = '1'
#                 # print(self.menu)
#                 # show_popup_order()
#                 show_popup_order(instance)
#             else:
#                 if self.lb_10.text in self.menu:
#                     self.menu.pop(self.lb_10.text)
#                     self.lbl_010.text = '1'
#                     bn10.background_color = [1, 1, 0, 0.5]
#                     bn10.text = 'Add\nitems'
#                     # print(self.menu)
#                     # show_popup_order()
#                 else:
#                     print('item not in order')
#                     print(self.menu)
#
#         def change_color(instance):
#             instance.background_color = [0.1, 0.2, 0, 1]
#
#         def added1(instance):
#             bn1.text = 'Added'+'\n '+str(self.lbl_01.text)+'pcs'
#         def added2(instance):
#             bn2.text = 'Added' +'\n '+str(self.lbl_02.text)+'pcs'
#         def added3(instance):
#             bn3.text = 'Added'+'\n '+str(self.lbl_03.text)+'pcs'
#         def added4(instance):
#             bn4.text = 'Added'+'\n '+str(self.lbl_04.text)+'pcs'
#         def added5(instance):
#             bn5.text = 'Added'+'\n '+str(self.lbl_05.text)+'pcs'
#         def added6(instance):
#             bn6.text = 'Added'+'\n '+str(self.lbl_06.text)+'pcs'
#         def added7(instance):
#             bn7.text = 'Added'+'\n '+str(self.lbl_07.text)+'pcs'
#         def added8(instance):
#             bn8.text = 'Added'+'\n '+str(self.lbl_08.text)+'pcs'
#         def added9(instance):
#             bn9.text = 'Added'+'\n '+str(self.lbl_09.text)+'pcs'
#         def added10(instance):
#             bn10.text = 'Added'+'\n '+str(self.lbl_010.text)+'pcs'
#
#         def show_popup1(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub)
#                 for el in (btn_0, self.lbl_01, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added1)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 try:
#                     popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1),
#                                   title_size=20,
#                                   size_hint=(0.2, 0.15), auto_dismiss=False)
#                     bl_0 = BoxLayout()
#                     bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                     btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add0)
#                     btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub0)
#                     for el in (btn_0, self.lbl_00, btn_01):
#                         bl_01.add_widget(el)
#                     bl_0.add_widget(bl_01)
#                     bl_0.add_widget(Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss))
#                     popup.content = bl_0
#                     popup.open()
#                 except:
#                      pass
#
#
#
#         def show_popup2(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add2)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub2)
#                 for el in (btn_0, self.lbl_02, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added2)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#
#
#         def show_popup3(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add3)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub3)
#                 for el in (btn_0, self.lbl_03, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added3)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#
#
#         def show_popup4(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add4)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub4)
#                 for el in (btn_0, self.lbl_04, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added4)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#         def show_popup5(instance):
#             try:
#
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add5)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub5)
#                 for el in (btn_0, self.lbl_05, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added5)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#
#         def show_popup6(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add6)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub6)
#                 for el in (btn_0, self.lbl_06, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added6)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#
#             except:
#                 pass
#
#
#         def show_popup7(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add7)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub7)
#                 for el in (btn_0, self.lbl_07, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added7)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#
#         def show_popup8(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add8)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub8)
#                 for el in (btn_0, self.lbl_08, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added8)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#         def show_popup9(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add9)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub9)
#                 for el in (btn_0, self.lbl_09, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added9)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#         def show_popup10(instance):
#             try:
#                 popup = Popup(title="Items", title_align='center', background_color=(0.1, 0.5, 0.4, 1), title_size=20,
#                               size_hint=(0.2, 0.15), auto_dismiss=False)
#                 bl_0 = BoxLayout()
#                 bl_01 = BoxLayout(orientation='horizontal', size_hint=(1, 1))
#                 btn_0 = Button(text='+', font_size=25, background_color=[1, 1, 0, 0.5], on_press=add10)
#                 btn_01 = Button(text='-', font_size=25, background_color=[1, 1, 0, 0.5], on_press=sub10)
#                 for el in (btn_0, self.lbl_010, btn_01):
#                     bl_01.add_widget(el)
#                 bl_0.add_widget(bl_01)
#                 btn_02 = Button(text='add', size_hint=(0.5, 1), on_press=popup.dismiss)
#                 btn_02.bind(on_press=added10)
#                 bl_0.add_widget(btn_02)
#                 popup.content = bl_0
#                 popup.open()
#             except:
#                 pass
#
#         def order():
#             for key, value in self.menu.items():
#                 self.lbl_ord_show.text = (f'{key},\n {value}pc(s)')
#
#         def show_popup_order(instance):
#             order()
#             total_order()
#             popup = Popup(title='Added', title_align='center', size_hint=(0.3, 0.3), auto_dismiss=True)
#             stlout = StackLayout()
#             scrv= ScrollView(size_hint_x=1, size_hint_y=1, bar_color=[1, 1, 1, 1],
#                         bar_margin=2, bar_width=10)
#             lbl_show_ord =Label(text=self.lbl_ord_show.text, size_hint_y=None)
#             # lbl_show_ord.bind(minimum_height=lbl_show_ord.setter("height"))
#             scrv.add_widget(lbl_show_ord)
#             stlout.add_widget(scrv)
#             # stlout.add_widget(Button(text='Close', size_hint=(1,0.1), on_press=popup.dismiss))
#             popup.content = stlout
#             popup.open()
#
#         def clear_first(instance):
#             with open('orders.txt', 'w') as order:
#                 self.show_orders = order.write('')
#
#             popup = Popup(title='Start', title_align='center', title_size=25, size_hint=(0.6, 0.6),
#                           auto_dismiss=True)
#             fl = FloatLayout(size_hint=(1, 0.8) )
#             lbl_show_ords = Label(text='WELCOME TO OUR APP\n \n1-add items\n2-check box for confirmation'
#                                        '\n3-Review your order or delete\n4-send for your order\n \n'
#                                        '\n !!EASY WAY FOR ORDERING!!!',
#                                   font_size= 20, size_hint=(None, None), x=300, y=300)
#             fl.add_widget(lbl_show_ords)
#             popup.content = fl
#             popup.open()
#
#         def total_order():
#             with open('orders.txt', 'a+') as order:
#                 ord = order.write(self.lbl_ord_show.text +'\n \n')
#
#         def show_popup_orders(instance):
#             with open('orders.txt', 'r') as order:
#                 self.show_orders = order.read()
#             popup = Popup(title='Your orders', title_align='center', title_size=25, size_hint=(0.7, 0.7), auto_dismiss=False)
#             stlout = StackLayout(size_hint=(0.8, 0.9))
#             lbl_show_ords = Label(text=self.show_orders, size_hint_y=None)
#             fl = FloatLayout(size_hint_y=None)
#             fl.add_widget(lbl_show_ords)
#             scrv = ScrollView(size_hint_x=1, size_hint_y=1, bar_color=[1, 1, 1, 1],
#                               bar_margin=2, bar_width=10)
#             scrv.add_widget(fl)
#             stlout.add_widget(scrv)
#             stlout.add_widget(Button(text='Close', size_hint=(1,0.1), on_press=popup.dismiss))
#             popup.content = stlout
#             popup.open()
#
#         def delete_orders(instance):
#             with open('orders.txt', 'w') as order:
#                 self.show_orders = order.write('')
#
#             with open('orders.txt', 'r') as order:
#                 self.show_orders = order.read()
#
#             popup = Popup(title='No orders', title_align='center', title_size=25, size_hint=(0.7, 0.7), auto_dismiss=False)
#             stlout = StackLayout(size_hint=(0.8, 0.9))
#             lbl_show_ords = Label(text=str(self.show_orders), size_hint_y=None)
#             fl = FloatLayout(size_hint_y=None)
#             fl.add_widget(lbl_show_ords)
#             scrv = ScrollView(size_hint_x=1, size_hint_y=1, bar_color=[1, 1, 1, 1],
#                               bar_margin=2, bar_width=10)
#             scrv.add_widget(fl)
#             stlout.add_widget(scrv)
#             stlout.add_widget(Button(text='Close', size_hint=(1,0.1), on_press=popup.dismiss))
#             popup.content = stlout
#             popup.open()
#
#         def send_order(instance):
#
#             with open('orders.txt', 'r') as order:
#                 self.show_orders = order.read()
#
#
#             if len(self.show_orders) != 0:
#                 popup = Popup(title='Orders sended', title_align='center', title_size=25, size_hint=(0.7, 0.7),
#                               auto_dismiss=False)
#                 stlout = StackLayout(size_hint=(0.8, 0.9))
#                 lbl_show_ords = Label(text='Your order sended!\n Congratulations!!', font_size=40, size_hint_y=None)
#                 fl = FloatLayout(size_hint_y=None)
#                 fl.add_widget(lbl_show_ords)
#                 scrv = ScrollView(size_hint_x=1, size_hint_y=1, bar_color=[1, 1, 1, 1],
#                                   bar_margin=2, bar_width=10)
#                 scrv.add_widget(fl)
#                 stlout.add_widget(scrv)
#                 stlout.add_widget(Button(text='Close', size_hint=(1, 0.1), on_press=popup.dismiss))
#                 popup.content = stlout
#                 popup.open()
#             else:
#                 popup = Popup(title='Orders sended', title_align='center', title_size=25, size_hint=(0.7, 0.7),
#                               auto_dismiss=False)
#                 stlout = StackLayout(size_hint=(0.8, 0.9))
#                 lbl_show_ords = Label(text='Do your order', font_size=40, size_hint_y=None)
#                 fl = FloatLayout(size_hint_y=None)
#                 fl.add_widget(lbl_show_ords)
#                 scrv = ScrollView(size_hint_x=1, size_hint_y=1, bar_color=[1, 1, 1, 1],
#                                   bar_margin=2, bar_width=10)
#                 scrv.add_widget(fl)
#                 stlout.add_widget(scrv)
#                 stlout.add_widget(Button(text='Close', size_hint=(1, 0.1), on_press=popup.dismiss))
#                 popup.content = stlout
#                 popup.open()
#
#         self.chb_1.bind(active=checkbox1)
#         self.chb_2.bind(active=checkbox2)
#         self.chb_3.bind(active=checkbox3)
#         self.chb_4.bind(active=checkbox4)
#         self.chb_5.bind(active=checkbox5)
#         self.chb_6.bind(active=checkbox6)
#         self.chb_7.bind(active=checkbox7)
#         self.chb_8.bind(active=checkbox8)
#         self.chb_9.bind(active=checkbox9)
#         self.chb_10.bind(active=checkbox10)
#
#         for key, value in self.menu.items():
#             self.lbl_ord_show.text = (f'{key},\n {value}pc(s)')
#
#         fl = FloatLayout()
#         sv = ScrollView(size_hint_x=0.8, size_hint_y=1, x=150, bar_color=[1, 1, 1, 1],
#                         bar_margin=2, bar_width=10)
#
#
#         #panels
#         bl = BoxLayout(orientation='vertical', size_hint_x=0.15, size_hint_y=1, x=0, y=0, spacing=6, padding=10)
#         bl.add_widget(Button(text='Press\nto start\norder', bold=True,italic=True, font_size= 18, padding=5,
#                              background_color=[1, 1, 0, 0.5], on_press=clear_first))
#         bl.add_widget(Button(text='Send order', bold=True,italic=True, font_size= 18, padding=5,
#                              background_color=[0.9, 0.9, 0, 0.5], on_press=send_order))
#         bl.add_widget(Button(text='Delete order', bold=True,italic=True, font_size= 18, padding=5,
#                              background_color=[0.8, 0.8, 0, 0.5], on_press=delete_orders))
#         bl.add_widget(Button(text='Show your\n order', bold=True,italic=True, font_size= 18, padding=5,
#                              background_color=[0.7, 0.7, 0, 0.5], on_press=show_popup_orders))
#         bl.add_widget(Button(text='Call\npersonal', bold=True,italic=True, font_size= 18, padding=5,
#                              background_color=[0.6, 0.6, 0, 0.5]))
#         bl.add_widget(Button(text='Call\nTaxi', background_color=[1, 1, 0, 0.5], bold=True,italic=True,
#                              font_size=18, padding=5))
#         bl.add_widget(Widget())
#
#         #image panels
#         sl = StackLayout( size_hint_y=None)
#         sl_1 = StackLayout(size_hint_y=None)
#         sl_1.add_widget(self.chb_1)
#         sl_1.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi1.JPG', size_hint_y=0.95, size_hint_x=0.5))
#         sl_1.add_widget(self.lb_1)
#         bn1 = Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8,background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup1)
#         bn1.bind(on_press=change_color)
#         sl_1.add_widget(bn1)
#
#
#         sl_2 = StackLayout(size_hint_y=None)
#         sl_2.add_widget(self.chb_2)
#         sl_2.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi2.JPG', size_hint_y=0.95, size_hint_x=0.5))
#         sl_2.add_widget(self.lb_2)
#         bn2 = Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup2)
#         bn2.bind(on_press=change_color)
#         sl_2.add_widget(bn2)
#
#
#         sl_3 = StackLayout(size_hint_y=None)
#         sl_3.add_widget(self.chb_3)
#         sl_3.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi4.JPG', size_hint_y=0.95,size_hint_x=0.5))
#         sl_3.add_widget(self.lb_3)
#         bn3 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup3))
#         bn3.bind(on_press=change_color)
#         sl_3.add_widget(bn3)
#
#         sl_4 = StackLayout(size_hint_y=None)
#         sl_4.add_widget(self.chb_4)
#         sl_4.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi3.JPG', size_hint_y=0.95,size_hint_x=0.5))
#         sl_4.add_widget(self.lb_4)
#         bn4 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup4))
#         bn4.bind(on_press=change_color)
#         sl_4.add_widget(bn4)
#
#         sl_5 = StackLayout(size_hint_y=None)
#         sl_5.add_widget(self.chb_5)
#         sl_5.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi5.JPG', size_hint_y=0.95,size_hint_x=0.5))
#         sl_5.add_widget(self.lb_5)
#         bn5 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup5))
#         bn5.bind(on_press=change_color)
#         sl_5.add_widget(bn5)
#
#         sl_6 = StackLayout(size_hint_y=None)
#         sl_6.add_widget(self.chb_6)
#         sl_6.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger1.JPG', size_hint_y=0.95,size_hint_x=0.5))
#         sl_6.add_widget(self.lb_6)
#         bn6 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup6))
#         bn6.bind(on_press=change_color)
#         sl_6.add_widget(bn6)
#
#         sl_7 = StackLayout(size_hint_y=None)
#         sl_7.add_widget(self.chb_7)
#
#         sl_7.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger2.JPG', size_hint_y=0.95,
#                               size_hint_x=0.5))
#         sl_7.add_widget(self.lb_7)
#         bn7 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup7))
#         bn7.bind(on_press=change_color)
#         sl_7.add_widget(bn7)
#
#
#         sl_8 = StackLayout(size_hint_y=None)
#         sl_8.add_widget(self.chb_8)
#
#         sl_8.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger3.JPG', size_hint_y=0.95,
#                               size_hint_x=0.5))
#         sl_8.add_widget(self.lb_8)
#         bn8 =(Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup8))
#         bn8.bind(on_press=change_color)
#         sl_8.add_widget(bn8)
#
#         sl_9 = StackLayout(size_hint_y=None)
#         sl_9.add_widget(self.chb_9)
#         sl_9.add_widget(Image(source='C:/Users/Patrick moon/Downloads/pizza1.JPG', size_hint_y=0.95, size_hint_x=0.5))
#         sl_9.add_widget(self.lb_9)
#         bn9 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup9))
#         bn9.bind(on_press=change_color)
#         sl_9.add_widget(bn9)
#
#         sl_10 = StackLayout(size_hint_y=None)
#         sl_10.add_widget(self.chb_10)
#         sl_10.add_widget(Image(source='C:/Users/Patrick moon/Downloads/pizza2.JPG', size_hint_y=0.95, size_hint_x=0.5))
#         sl_10.add_widget(self.lb_10)
#         bn10 = (Button(text='Add\nitems', size_hint_x=0.1, size_hint_y=0.8, background_color=[1, 1, 0, 0.5],
#                                on_press=show_popup10))
#         bn10.bind(on_press=change_color)
#         sl_10.add_widget(bn10)
#
#         for el in (sl_1, sl_2, sl_3,sl_4, sl_5, sl_6, sl_7, sl_8, sl_9, sl_10):
#             sl.add_widget(el)
#
#
#         sl.bind(minimum_height=sl.setter('height'))
#         sv.add_widget(sl)
#         fl.add_widget(bl)
#         fl.add_widget(sv)
#
#         # print(self.menu)
#
#
#         return fl
# if __name__ == '__main__':
#     MyMenuApp().run()
#




#
# Window.clearcolor = (0.2, 0.4, 0.1, 1)
# Window.size = (300, 500)
#
# class Examinator(App):
#
#     def __init__(self):
#         super().__init__()
#         self.label = Label(text='Press next\n  for\n'
#                                 'the game', size_hint=(1, 0.3), font_size=30, italic=True)
#         self.label_1 = Label(text='Score:', size_hint=(1, 0.2), font_size=25, italic=True)
#         self.input_ans = TextInput(hint_text='Answer' ,size_hint=(1, 0.1), font_size=25)
#         self.count = 0
#         self.score = 0
#         self.rigth = 0
#         self.wrong = 0
#
#     def build(self):
#         # def on_text(instance, *args):
#         #     self.input_ans.text = str(eval(self.label.text))
#
#         def next(instance):
#             try:
#                 if self.input_ans.text == str(eval(self.label.text)):
#                     self.score += 10
#                     self.rigth +=1
#                     self.label_1.text = f'Score = {self.score}\nCorrect: {self.rigth}\n Wrong: {self.wrong}'
#                 elif self.input_ans.text != str(eval(self.label.text)):
#                     self.score -= 10
#                     self.wrong += 1
#                     self.label_1.text = f'Score = {self.score}\nCorrect: {self.rigth}\n Wrong: {self.wrong}'
#
#                 self.input_ans.text = ''
#
#             except:
#                 self.input_ans.text = ''
#
#             operation(instance)
#             self.count +=1
#
#
#         def stop(instance):
#             self.label.text = 'End of session'
#             self.label_1.text= f'Exercices:{self.count}\nCorrect answers: {self.rigth}\n Wrong answers: {self.wrong}\n' \
#                            f'Your score = {self.score}'
#             self.count = 0
#             self.wrong = 0
#             self.rigth = 0
#             self.score = 0
#
#
#         def operation(instance, *args):
#             self.a = randint(0, 50)
#             self.b = randint(1, 50)
#             sign = randint(0, 3)
#             if sign == 0:
#                 z = self.a + self.b
#                 self.label.text = f'{self.a} + {self.b} '
#
#             elif sign == 1:
#                 if self.a >= self.b:
#                     z = self.a - self.b
#                     self.label.text = f'{self.a} - {self.b}'
#                 else:
#                     z = self.b - self.a
#                     self.label.text = f'{self.b} - {self.a} '
#             elif sign == 2:
#                 z = self.a * self.b
#                 self.label.text = f'{self.a} * {self.b} '
#             elif sign == 3:
#                 if self.a >0 and self.b > 0 :
#                     if self.a>self.b and self.a//self.b ==0:
#                         z = self.a / self.b
#                         self.label.text = f'{self.a} / {self.b} '
#                     else:
#                         z = self.a % self.b
#                         self.label.text = f'{self.b} % {self.a} '
#
#         stack = StackLayout()
#         stack.add_widget(self.label)
#         stack.add_widget(self.input_ans)
#         btn_1 = Button(text='Send', size_hint=(1, 0.1), font_size=25,
#                                 background_color=[0.1, 0.4, 0.4, 0.5], italic=True, on_press=next)
#         # btn_1.bind(on_press= operation)
#         stack.add_widget(btn_1)
#         stack.add_widget(Button(text='Next', size_hint=(1, 0.1), font_size=25,
#                                 background_color=[0.1, 0.4, 0.4, 0.5], italic=True, on_press=operation ))
#         stack.add_widget(Button(text='Stop', size_hint=(1, 0.1), font_size=25,
#                                 background_color=[0.1, 0.4, 0.4, 0.5], italic=True, on_press=stop))
#
#         stack.add_widget(self.label_1)
#         # self.input_ans.bind(text=on_text)
#
#         return stack
#
# if __name__ == '__main__':
#     Examinator().run()
#
# class MyApp(App):
#     def build(self):
#         main_layout = ScreenManager()
#         screen1 = Screen(name="screen_1")
#         button1 = Button(text="Переход на второй экран", size_hint=(0.3, 0.3), pos=(250, 250))
#         def go_second_page(instance):
#             main_layout.current = "screen_2"
#         button1.bind(on_press=go_second_page)
#         screen1.add_widget(button1)
#         main_layout.add_widget(screen1)
#
#         screen2 = Screen(name="screen_2")
#         button2 = Button(text="Переход на первый экран", size_hint=(0.3, 0.3), pos=(250, 250), background_color=[1, 0, 0, 1])
#         def go_first_page(instance):
#             main_layout.current = "screen_1"
#         button2.bind(on_press=go_first_page)
#         screen2.add_widget(button2)
#         main_layout.add_widget(screen2)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()




Window.clearcolor = (0.5, 0.2, 0.1, 0.4)
Window.size = (800, 700)
class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Choose fishy sushi', halign='center', font_size=30, italic=True, size_hint=(1, 0.1))
        self.label_scr_1 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_2 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_3 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_4 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_5 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_6 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_7 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_8 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))

        #page_1
        self.label_pop_1 = Label(text='Sushi set cold\n ingredient: Fish ,Rice,\n cheese, pepper\n\n'
                                      '     5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_01 = Label(text='Sushi set cold\n ingredient: Fish, Rice,\n cheese, pepper\n\n'
                                      '     2$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.btn_1 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                       size_hint=(0.2, 1), on_press=self.popup_1)
        self.btn_01 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.rmved_1)

        # page_2
        self.label_pop_2 = Label(text='Sushi lovers\n ingredient: Fish, Rice, salad\nmilk, pepper\n\n'
                                      '     5.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_02 = Label(text='Sushi lovers\n ingredient: Fish, Rice, salad\nmilk, pepper\n\n'
                                       '     5.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_2 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_2)
        self.btn_02 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_2)

        # page_3
        self.label_pop_3 = Label(text='Sushi fresh\n ingredient: Fish, Rice, salad\npepper, ginger\n\n'
                                      '     4$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_03 = Label(text='Sushi fresh\n ingredient: Fish, Rice, salad\npepper, ginger\n\n'
                                       '     4$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_3 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_3)
        self.btn_03 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_3)

        # page_4
        self.label_pop_4 = Label(text='Japan sushi \n ingredient: Fish, Rice,\nlemon, eggs \nwassabi\n\n'
                                      '     6$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_04 = Label(text='Sushi fresh\n ingredient: Fish, Rice,\nlemon, eggs\nwassabi\n\n'
                                       '     6$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_4 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_4)
        self.btn_04 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_4)

        # page_5

        self.label_pop_5 = Label(text='Sushi philadelphia \n ingredient: Fish, Rice, \ncucumber \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_05 = Label(text='Sushi philadelphia\n ingredient: Fish, Rice,\n cucumber\nwassabi\n\n'
                                       '     3.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_5 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_5)
        self.btn_05 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_5)

        # page_6

        self.label_pop_6 = Label(text='Sushi original \n ingredient: Fish, Rice, \nginger \nwassabi\n\n'
                                      '     6$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_06 = Label(text='Sushioriginal\n ingredient: Fish, Rice,\n ginger\nwassabi\n\n'
                                       '     6$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_6 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_6)
        self.btn_06 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_6)



    #add-sub_1
    def add_scr_1(self, instance):
        self.label_scr_1.text = str(int(self.label_scr_1.text) + 1)
    def sub_scr_1(self, instance):
        if int(self.label_scr_1.text) < 1:
            self.label_scr_1.text = '0'
        self.label_scr_1.text = str(int(self.label_scr_1.text) - 1)

    # add-sub_2
    def add_scr_2(self, instance):
        self.label_scr_2.text = str(int(self.label_scr_2.text) + 1)
    def sub_scr_2(self, instance):
        if int(self.label_scr_2.text) < 1:
            self.label_scr_2.text = '0'
        self.label_scr_2.text = str(int(self.label_scr_2.text) - 1)

    # add-sub_3
    def add_scr_3(self, instance):
        self.label_scr_3.text = str(int(self.label_scr_3.text) + 1)
    def sub_scr_3(self, instance):
        if int(self.label_scr_3.text) < 1:
            self.label_scr_3.text = '0'
        self.label_scr_3.text = str(int(self.label_scr_4.text) - 1)

    # add-sub_4
    def add_scr_4(self, instance):
        self.label_scr_4.text = str(int(self.label_scr_4.text) + 1)
    def sub_scr_4(self, instance):
        if int(self.label_scr_4.text) < 1:
            self.label_scr_4.text = '0'
        self.label_scr_4.text = str(int(self.label_scr_4.text) - 1)

    # add-sub_5
    def add_scr_5(self, instance):
        self.label_scr_5.text = str(int(self.label_scr_5.text) + 1)
    def sub_scr_5(self, instance):
        if int(self.label_scr_5.text) < 1:
            self.label_scr_5.text = '0'
        self.label_scr_5.text = str(int(self.label_scr_5.text) - 1)

    # add-sub_6
    def add_scr_6(self, instance):
        self.label_scr_6.text = str(int(self.label_scr_6.text) + 1)

    def sub_scr_6(self, instance):
        if int(self.label_scr_6.text) < 1:
            self.label_scr_6.text = '0'
        self.label_scr_6.text = str(int(self.label_scr_6.text) - 1)

    # add-sub_7
    def add_scr_7(self, instance):
        self.label_scr_7.text = str(int(self.label_scr_7.text) + 1)

    def sub_scr_7(self, instance):
        if int(self.label_scr_7.text) < 1:
            self.label_scr_7.text = '0'
        self.label_scr_7.text = str(int(self.label_scr_7.text) - 1)

    # add-sub_8
    def add_scr_8(self, instance):
        self.label_scr_8.text = str(int(self.label_scr_8.text) + 1)

    def sub_scr_8(self, instance):
        if int(self.label_scr_8.text) < 1:
            self.label_scr_8.text = '0'
        self.label_scr_8.text = str(int(self.label_scr_8.text) - 1)


    # popup_1
    def popup_1(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_1)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_1))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_01)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_1))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_1(self, instance):
        self.btn_1.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_1.text = 'Added'

    def rmved_1(self, instance):
        self.btn_1.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_1.text = 'Add'
        self.label_scr_1.text = '0'

    # popup_2
    def popup_2(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_2)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_2))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_02)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_2))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_2(self, instance):
        self.btn_2.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_2.text = 'Added'

    def rmved_2(self, instance):
        self.btn_2.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_2.text = 'Add'
        self.label_scr_2.text = '0'

    # popup_3

    def popup_3(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_3)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_3))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_03)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_3))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_3(self, instance):
        self.btn_3.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_3.text = 'Added'

    def rmved_3(self, instance):
        self.btn_3.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_3.text = 'Add'
        self.label_scr_3.text = '0'

    # popup_4

    def popup_4(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_4)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_4))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_04)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_4))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_4(self, instance):
        self.btn_4.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_4.text = 'Added'

    def rmved_4(self, instance):
        self.btn_4.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_4.text = 'Add'
        self.label_scr_4.text = '0'

    # popup_5
    def popup_5(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_5)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_5))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_05)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_5))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_5(self, instance):
        self.btn_5.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_5.text = 'Added'

    def rmved_5(self, instance):
        self.btn_5.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_5.text = 'Add'
        self.label_scr_5.text = '0'

    # popup_6
    def popup_6(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_6)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_6))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_06)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_6))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_6(self, instance):
        self.btn_6.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_6.text = 'Added'

    def rmved_6(self, instance):
        self.btn_6.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_6.text = 'Add'
        self.label_scr_6.text = '0'








    def build(self):

        stack = StackLayout()
        scr = ScreenManager(size_hint=(1, 0.9))

    #screen_page_1

        scr_1 = Screen(name='page_1')
        img_1 = Image(source='C:/Users/Patrick moon/Downloads/sushi1.JPG',size_hint=(0.8, 0.9), x=20, y=100)
        scr_1.add_widget(img_1)
        stack_scr_1 = StackLayout(size_hint=(1, 0.1), x=20 , y=0)
        stack_scr_1.add_widget(Button(text='+',font_size=20, italic=True,background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_1))
        stack_scr_1.add_widget(self.label_scr_1)
        stack_scr_1.add_widget(Button(text='-',font_size=20, italic=True,background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_1))
        stack_scr_1.add_widget(self.btn_1)
        stack_scr_1.add_widget(self.btn_01)
        scr_1.add_widget(stack_scr_1)

        def page_1(instance):
            scr.current = 'page_1'
            self.label.text = 'Sushi set cold\n 5$'

    # screen_page_2

        scr_2 = Screen(name='page_2')
        scr_2.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi2.JPG',size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_2 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_2.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_2))
        stack_scr_2.add_widget(self.label_scr_2)
        stack_scr_2.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_2))
        stack_scr_2.add_widget(self.btn_2)
        stack_scr_2.add_widget(self.btn_02)
        scr_2.add_widget(stack_scr_2)

        def page_2(instance):
            scr.current = 'page_2'
            self.label.text = 'Sushi lover\n  5.5$'
            # Window.clearcolor = (0.7, 0.2, 0.3, 0.4)

        # screen_page_3

        scr_3 = Screen(name='page_3')
        scr_3.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi3.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_3 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_3.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_3))
        stack_scr_3.add_widget(self.label_scr_3)
        stack_scr_3.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_3))
        stack_scr_3.add_widget(self.btn_3)
        stack_scr_3.add_widget(self.btn_03)
        scr_3.add_widget(stack_scr_3)

        def page_3(instance):
            scr.current = 'page_3'
            self.label.text = 'Sushi fresh\n 4$'

            # Window.clearcolor = (0.6, 0.1, 0.4, 0.4)

        # screen_page_4

        scr_4 = Screen(name='page_4')
        scr_4.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi4.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_4 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_4.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_4))
        stack_scr_4.add_widget(self.label_scr_4)
        stack_scr_4.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_4))
        stack_scr_4.add_widget(self.btn_4)
        stack_scr_4.add_widget(self.btn_04)
        scr_4.add_widget(stack_scr_4)
        def page_4(instance):
            scr.current = 'page_4'
            self.label.text = 'Japan sushi\n 6$'

        # screen_page_5

        scr_5 = Screen(name='page_5')
        scr_5.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi5.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_5 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_5.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_5))
        stack_scr_5.add_widget(self.label_scr_5)
        stack_scr_5.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_5))
        stack_scr_5.add_widget(self.btn_5)
        stack_scr_5.add_widget(self.btn_05)
        scr_5.add_widget(stack_scr_5)
        def page_5(instance):
            scr.current = 'page_5'
            self.label.text = 'Sushi philadelphia\n 3.5$'

        # screen_page_5

        scr_6 = Screen(name='page_6')
        scr_6.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi6.JPG',size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_6 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_6.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_6))
        stack_scr_6.add_widget(self.label_scr_6)
        stack_scr_6.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_6))
        stack_scr_6.add_widget(self.btn_6)
        stack_scr_6.add_widget(self.btn_06)
        scr_6.add_widget(stack_scr_6)
        def page_6(instance):
            scr.current = 'page_6'
            self.label.text = 'Sushi origin\n 6$'

        scr_7 = Screen(name='page_7')
        scr_7.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi7.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_7 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_7.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.2, 1), on_press=self.add_scr_7))
        stack_scr_7.add_widget(self.label_scr_7)
        stack_scr_7.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.2, 1), on_press=self.sub_scr_7))
        stack_scr_7.add_widget(Button(text='add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1)))
        scr_7.add_widget(stack_scr_7)
        def page_7(instance):
            scr.current = 'page_7'
            self.label.text = 'Hot sushi\n 5$'

        scr_8 = Screen(name='page_8')
        scr_8.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi8.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_8 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_8.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.2, 1), on_press=self.add_scr_8))
        stack_scr_8.add_widget(self.label_scr_8)
        stack_scr_8.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.2, 1), on_press=self.sub_scr_8))
        stack_scr_8.add_widget(Button(text='add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1)))
        scr_8.add_widget(stack_scr_8)
        def page_8(instance):
            scr.current = 'page_8'
            self.label.text = 'Sushi prestige\n 5$'

        for el in (scr_1, scr_2, scr_3, scr_4, scr_5, scr_6, scr_7, scr_8):
            scr.add_widget(el)

        stack_1 = StackLayout(size_hint=(0.8, 1))
        stack_1.add_widget(self.label)
        stack_1.add_widget(scr)

        scroll = ScrollView(size_hint=(0.2, 1), bar_width=10)
        box = BoxLayout(orientation='vertical', size_hint_y=None, padding=20)
        box.bind(minimum_height=box.setter('height'))
        scroll.add_widget(box)

        btn_1 = Button(text='Sushi\nset cold', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_1)

        btn_2 = Button(text='Sushi\nlover', size_hint_y=None,font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_2)

        btn_3 = Button(text='Sushi\nfresh', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_3)
        btn_4 = Button(text='Japan\nsushi', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_4)
        btn_5 =Button(text='Sushi\nPhiladelphia', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_5)
        btn_6 = Button(text='Sushi\nOrigin', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_6)
        btn_7 = Button(text='Hot\nsushi', size_hint_y=None, font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_7)
        btn_8 = Button(text='Prestige\nsushi', size_hint_y=None,font_size=20, italic=True, bold=True,
        background_color=[0.1, 0.3, 0.4, 0.7], on_press=page_8)

        for el in(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8):
            box.add_widget(el)


        stack.add_widget(scroll)
        stack.add_widget(stack_1)


        return stack


if __name__ == '__main__':
    MyApp().run()

