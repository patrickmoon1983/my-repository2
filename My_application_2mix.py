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

Window.clearcolor = (0.7, 0.5, 0.1, 0.1)
Window.size = (800, 700)
class MyApp(App):
    def __init__(self):
        super().__init__()
        self.card = {}
        # self.total_price_all = 0
        #Attributes for burger
        self.labels = Label(text='Choose tasty burger', halign='center', font_size=30, italic=True, size_hint=(1, 0.1))
        self.label_tps = Label(text='Total:', size_hint_y=None, font_size=30, italic=True)
        self.label_scr_1s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_2s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_3s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_4s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_5s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_6s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_7s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_8s = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))

        self.label = Label(text='Choose fishy sushi', halign='center', font_size=30, italic=True, size_hint=(1, 0.1))
        self.label_tpss = Label(text='Total:', size_hint_y=None, font_size=30, italic=True)
        self.label_scr_1 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_2 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_3 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_4 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_5 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_6 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_7 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_8 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))

        self.btn1s = Button(text='Burger\nhot', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn2s = Button(text='Burger\nmodesty', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn3s = Button(text='Burger\nmexicana', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn4s = Button(text='Juicy\nburger', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn5s = Button(text='Burger\npeppe', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn6s = Button(text='Burger\ntwin', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn7s = Button(text='Big\nKombo', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn8s = Button(text='Black\nangus', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])

        self.btn1 = Button(text='Sushi\nset cold', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])

        self.btn2 = Button(text='Sushi\nlover', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])

        self.btn3 = Button(text='Sushi\nfresh', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn4 = Button(text='Japan\nsushi', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn5 = Button(text='Sushi\nPhiladelphia', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn6 = Button(text='Sushi\nOrigin', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn7 = Button(text='Hot\nsushi', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn8 = Button(text='Prestige\nsushi', size_hint_y=None, font_size=20, italic=True, bold=True,
                           background_color=[0.1, 0.3, 0.4, 0.7])
        #page_1

        self.label_pop_1s = Label(text='Burger hot\n ingredient: beef,oignon\n cheese, pepper\n\n'
                                      '     2$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_01s = Label(text='Burger hot\n ingredient: Beef, salad,\n cheese, pepper\n\n'
                                      '     2$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.btn_1s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                       size_hint=(0.2, 1), on_press=self.popup_1s)
        self.btn_01s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.rmved_1s)

        # page_2
        self.label_pop_2s = Label(text='Burger modesty\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     1.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_02s = Label(text='Burger modesty\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     1.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_2s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_2s)
        self.btn_02s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_2s)
        self.label_tp_2s = Label(text='total:', font_size=20, italic=True, size_hint=(0.3, 1))

        # page_3
        self.label_pop_3s = Label(text='Burger mexicana\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     3$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_03s = Label(text='Burger mexicana\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     3$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_3s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_3s)
        self.btn_03s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_3s)

        # page_4
        self.label_pop_4s = Label(text='Juicy Burger \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     4$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_04s = Label(text='Juicy Burger \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     4$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_4s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_4s)
        self.btn_04s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_4s)

        # page_5

        self.label_pop_5s = Label(text='Burger peppe \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_05s = Label(text='Burger peppe \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_5s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_5s)
        self.btn_05s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_5s)

        # page_6

        self.label_pop_6s = Label(text='Burger twin \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     9$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_06s = Label(text='Burger twin \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     9$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_6s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_6s)
        self.btn_06s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_6s)

        # page_7

        self.label_pop_7s = Label(text='Burger Kombo \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     8.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_07s = Label(text='Burger kombo \n ingredient: Meat, cherries,\n eggs\n\n'
                                       '     8.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_7s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_7s)
        self.btn_07s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_7s)

        # page_8

        self.label_pop_8s = Label(text='Black Angus \n ingredient: Meat, cherries,\n tomatoes\n\n'
                                      '     8.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_08s = Label(text='Black Angus \n ingredient: Meat, cherries,\n tomatoes\n\n'
                                       '     8.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_8s = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_8s)
        self.btn_08s = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_8s)


        # page_1
        self.label_pop_1 = Label(text='Sushi set cold\n ingredient: Fish ,Rice,\n cheese, pepper\n\n'
                                      '     5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_01 = Label(text='Sushi set cold\n ingredient: Fish, Rice,\n cheese, pepper\n\n'
                                       '     5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_1 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup1)
        self.btn_01 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved1)

        # page_2
        self.label_pop_2 = Label(text='Sushi lovers\n ingredient: Fish, Rice, salad\nmilk, pepper\n\n'
                                      '     5.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_02 = Label(text='Sushi lovers\n ingredient: Fish, Rice, salad\nmilk, pepper\n\n'
                                       '     5.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_2 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup2)
        self.btn_02 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved2)

        # page_3

        self.label_pop_3 = Label(text='Sushi fresh\n ingredient: Fish, Rice, salad\npepper, ginger\n\n'
                                      '     4$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_03 = Label(text='Sushi fresh\n ingredient: Fish, Rice, salad\npepper, ginger\n\n'
                                       '     4$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_3 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup3)
        self.btn_03 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved3)

        # page_4
        self.label_pop_4 = Label(text='Japan sushi \n ingredient: Fish, Rice,\nlemon, eggs \nwassabi\n\n'
                                      '     6$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_04 = Label(text='Sushi fresh\n ingredient: Fish, Rice,\nlemon, eggs\nwassabi\n\n'
                                       '     6$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_4 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup4)
        self.btn_04 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved4)

        # page_5

        self.label_pop_5 = Label(text='Sushi philadelphia \n ingredient: Fish, Rice, \ncucumber \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_05 = Label(text='Sushi philadelphia\n ingredient: Fish, Rice,\n cucumber\nwassabi\n\n'
                                       '     3.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_5 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup5)
        self.btn_05 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved5)

        # page_6

        self.label_pop_6 = Label(text='Sushi original \n ingredient: Fish, Rice, \nginger \nwassabi\n\n'
                                      '     6$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_06 = Label(text='Sushioriginal\n ingredient: Fish, Rice,\n ginger\nwassabi\n\n'
                                       '     6$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_6 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup6)
        self.btn_06 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved6)

        self.menu = {self.label_pop_1s.text: 2,
                     self.label_pop_2s.text: 1.5,
                     self.label_pop_3s.text: 3,
                     self.label_pop_4s.text: 4,
                     self.label_pop_5s.text: 3.5,
                     self.label_pop_6s.text: 9,
                     self.label_pop_7s.text: 8.5,
                     self.label_pop_8s.text: 8.5,
                     self.label_pop_1.text: 5,
                     self.label_pop_2.text: 5.5,
                     self.label_pop_3.text: 4,
                     self.label_pop_4.text: 6,
                     self.label_pop_5.text: 3.5,
                     self.label_pop_6.text: 6,

                     }

   # Function for total price:
    def total_prices(self):
        total_price = 0
        for el in self.card.keys():
            price = float(self.card[el]) * float(self.menu[el])
            total_price += price
        self.label_tps.text = f'Total:\n{total_price} $'
        self.label_tpss.text = f'Total:\n{total_price} $'

    # For adding or substracting qty on screens

    #add-sub_1
    def add_scr_1s(self, instance):
        self.label_scr_1s.text = str(int(self.label_scr_1s.text) + 1)
    def sub_scr_1s(self, instance):
        if int(self.label_scr_1s.text) < 1:
            self.label_scr_1s.text = '0'
        self.label_scr_1s.text = str(int(self.label_scr_1s.text) - 1)

    def add_scr_1(self, instance):
        self.label_scr_1.text = str(int(self.label_scr_1.text) + 1)
    def sub_scr_1(self, instance):
        if int(self.label_scr_1.text) < 1:
            self.label_scr_1.text = '0'
        self.label_scr_1.text = str(int(self.label_scr_1.text) - 1)



    # add-sub_2
    def add_scr_2s(self, instance):
        self.label_scr_2s.text = str(int(self.label_scr_2s.text) + 1)
    def sub_scr_2s(self, instance):
        if int(self.label_scr_2s.text) < 1:
            self.label_scr_2s.text = '0'
        self.label_scr_2s.text = str(int(self.label_scr_2s.text) - 1)

    def add_scr_2(self, instance):
        self.label_scr_2.text = str(int(self.label_scr_2.text) + 1)
    def sub_scr_2(self, instance):
        if int(self.label_scr_2.text) < 1:
            self.label_scr_2.text = '0'
        self.label_scr_2.text = str(int(self.label_scr_2.text) - 1)

    # add-sub_3
    def add_scr_3s(self, instance):
        self.label_scr_3s.text = str(int(self.label_scr_3s.text) + 1)
    def sub_scr_3s(self, instance):
        if int(self.label_scr_3s.text) < 1:
            self.label_scr_3s.text = '0'
        self.label_scr_3s.text = str(int(self.label_scr_4s.text) - 1)

    def add_scr_3(self, instance):
        self.label_scr_3.text = str(int(self.label_scr_3.text) + 1)
    def sub_scr_3(self, instance):
        if int(self.label_scr_3.text) < 1:
            self.label_scr_3.text = '0'
        self.label_scr_3.text = str(int(self.label_scr_4.text) - 1)

    # add-sub_4
    def add_scr_4s(self, instance):
        self.label_scr_4s.text = str(int(self.label_scr_4s.text) + 1)
    def sub_scr_4s(self, instance):
        if int(self.label_scr_4s.text) < 1:
            self.label_scr_4s.text = '0'
        self.label_scr_4s.text = str(int(self.label_scr_4s.text) - 1)

    def add_scr_4(self, instance):
        self.label_scr_4.text = str(int(self.label_scr_4.text) + 1)
    def sub_scr_4(self, instance):
        if int(self.label_scr_4.text) < 1:
            self.label_scr_4.text = '0'
        self.label_scr_4.text = str(int(self.label_scr_4.text) - 1)

    # add-sub_5
    def add_scr_5s(self, instance):
        self.label_scr_5s.text = str(int(self.label_scr_5s.text) + 1)
    def sub_scr_5s(self, instance):
        if int(self.label_scr_5s.text) < 1:
            self.label_scr_5s.text = '0'
        self.label_scr_5s.text = str(int(self.label_scr_5s.text) - 1)

    def add_scr_5(self, instance):
        self.label_scr_5.text = str(int(self.label_scr_5.text) + 1)
    def sub_scr_5(self, instance):
        if int(self.label_scr_5.text) < 1:
            self.label_scr_5.text = '0'
        self.label_scr_5.text = str(int(self.label_scr_5.text) - 1)

    # add-sub_6
    def add_scr_6s(self, instance):
        self.label_scr_6s.text = str(int(self.label_scr_6s.text) + 1)
    def sub_scr_6s(self, instance):
        if int(self.label_scr_6s.text) < 1:
            self.label_scr_6s.text = '0'
        self.label_scr_6s.text = str(int(self.label_scr_6s.text) - 1)

    def add_scr_6(self, instance):
        self.label_scr_6.text = str(int(self.label_scr_6.text) + 1)

    def sub_scr_6(self, instance):
        if int(self.label_scr_6.text) < 1:
            self.label_scr_6.text = '0'
        self.label_scr_6.text = str(int(self.label_scr_6.text) - 1)

    # add-sub_7
    def add_scr_7s(self, instance):
        self.label_scr_7s.text = str(int(self.label_scr_7s.text) + 1)

    def sub_scr_7s(self, instance):
        if int(self.label_scr_7s.text) < 1:
            self.label_scr_7s.text = '0'
        self.label_scr_7s.text = str(int(self.label_scr_7s.text) - 1)

    def add_scr_7(self, instance):
        self.label_scr_7.text = str(int(self.label_scr_7.text) + 1)

    def sub_scr_7(self, instance):
        if int(self.label_scr_7.text) < 1:
            self.label_scr_7.text = '0'
        self.label_scr_7.text = str(int(self.label_scr_7.text) - 1)

    # add-sub_8
    def add_scr_8s(self, instance):
        self.label_scr_8s.text = str(int(self.label_scr_8s.text) + 1)
    def sub_scr_8s(self, instance):
        if int(self.label_scr_8s.text) < 1:
            self.label_scr_8s.text = '0'
        self.label_scr_8s.text = str(int(self.label_scr_8s.text) - 1)

    def add_scr_8(self, instance):
        self.label_scr_8.text = str(int(self.label_scr_8.text) + 1)

    def sub_scr_8(self, instance):
        if int(self.label_scr_8.text) < 1:
            self.label_scr_8.text = '0'
        self.label_scr_8.text = str(int(self.label_scr_8.text) - 1)

    # For popping up messages on screens:

    # popup_1
    def popup_1s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_1s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_1s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_01s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_1s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()


    def popup1(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_1)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added1))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_01)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added1))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_1s(self, instance):     #For confirm button

        self.btn_1s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_1s.text = 'Added'
        if self.label_scr_1s.text == '-1':
            self.card[self.label_pop_1s.text] = '0'
        else:
            self.card[self.label_pop_1s.text] = self.label_scr_1s.text

        self.btn1s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn1s.text = f'Burger\nhot \n{self.label_scr_1s.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved_1s(self, instance):     #for clear button
        self.btn_1s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_1s.text = 'Add'
        self.label_scr_1s.text = '0'
        try:
            self.card.pop(self.label_pop_1s.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn1s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn1s.text = f'Burger\nhot'

        print(self.card)

    def added1(self, instance):
        self.btn_1.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_1.text = 'Added'
        if self.label_scr_1.text == '-1':
            self.card[self.label_pop_1.text] = '0'
        else:
            self.card[self.label_pop_1.text] = self.label_scr_1.text

        self.btn1.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn1.text = f'Sushi\nset cold \n{self.label_scr_1.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved1(self, instance):
        self.btn_1.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_1.text = 'Add'
        self.label_scr_1.text = '0'
        try:
            self.card.pop(self.label_pop_1.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn1.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn1.text = f'Sushi\nset cold'

        print(self.card)


    # popup_2
    def popup_2s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_2s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_2s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_02s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_2s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()


    def popup2(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_2)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added2))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_02)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added2))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_2s(self, instance):
        self.btn_2s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_2s.text = 'Added'
        if self.label_scr_2s.text == '-1':
            self.card[self.label_pop_2s.text] = '0'
        else:
            self.card[self.label_pop_2s.text] = self.label_scr_2s.text

        self.btn2s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn2s.text = f'Burger\nmodesty \n{self.label_scr_2s.text} pc(s)'

        print(self.card)
        self.total_prices()
    def rmved_2s(self, instance):
        self.btn_2s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_2s.text = 'Add'
        self.label_scr_2s.text = '0'
        try:
            self.card.pop(self.label_pop_2s.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn2s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn2s.text = f'Burger\nmodesty'

        print(self.card)

    def added2(self, instance):
        self.btn_2.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_2.text = 'Added'
        if self.label_scr_2.text == '-1':
            self.card[self.label_pop_2.text] = '0'
        else:
            self.card[self.label_pop_2.text] = self.label_scr_2.text

        self.btn2.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn2.text = f'Sushi lovers \n{self.label_scr_2.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved2(self, instance):
        self.btn_2.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_2.text = 'Add'
        self.label_scr_2.text = '0'
        try:
            self.card.pop(self.label_pop_2.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn2.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn2.text = f'Sushi\n lovers'

        print(self.card)

    # popup_3
    def popup_3s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_3s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_3s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_03s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_3s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def popup3(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_3)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added3))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_03)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added3))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_3s(self, instance):
        self.btn_3s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_3s.text = 'Added'
        if self.label_scr_3s.text == '-1':
            self.card[self.label_pop_3s.text] = '0'
        else:
            self.card[self.label_pop_3s.text] = self.label_scr_3s.text

        self.btn3s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn3s.text = f'Burger\nmexicana  \n{self.label_scr_3s.text} pc(s)'

        print(self.card)
        self.total_prices()
    def rmved_3s(self, instance):
        self.btn_3s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_3s.text = 'Add'
        self.label_scr_3s.text = '0'
        try:
            self.card.pop(self.label_pop_3s.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn3s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn3s.text = f'Burger\nmexicana'

        print(self.card)

    def added3(self, instance):
        self.btn_3.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_3.text = 'Added'
        if self.label_scr_3.text == '-1':
            self.card[self.label_pop_3.text] = '0'
        else:
            self.card[self.label_pop_3.text] = self.label_scr_3.text

        self.btn3.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn3.text = f'Sushi\n fresh \n{self.label_scr_3.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved3(self, instance):
        self.btn_3.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_3.text = 'Add'
        self.label_scr_3.text = '0'
        try:
            self.card.pop(self.label_pop_3.text)
            self.total_prices()
        except:
            self.card
            self.total_prices()

        self.btn3.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn3.text = f'Sushi\n fresh'

    # popup_4
    def popup_4s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_4s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_4s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_04s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_4s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def popup4(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_4)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added4))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_04)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added4))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_4s(self, instance):
        self.btn_4s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_4s.text = 'Added'
        if self.label_scr_4s.text == '-1':
            self.card[self.label_pop_4s.text] = '0'
        else:
            self.card[self.label_pop_4s.text] = self.label_scr_4s.text

        self.btn4s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn4s.text = f'Juicy\nburger  \n{self.label_scr_4s.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved_4s(self, instance):
        self.btn_4s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_4s.text = 'Add'
        self.label_scr_4s.text = '0'
        try:
            self.card.pop(self.label_pop_4s.text)
        except:
            self.card

        self.total_prices()

        self.btn4s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn4s.text = f'Juicy\nburger'

        print(self.card)

    def added4(self, instance):
        self.btn_4.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_4.text = 'Added'
        if self.label_scr_4.text == '-1':
            self.card[self.label_pop_4.text] = '0'
        else:
            self.card[self.label_pop_4.text] = self.label_scr_4.text

        self.btn4.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn4.text = f'Japan\n sushi \n{self.label_scr_4.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved4(self, instance):
        self.btn_4.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_4.text = 'Add'
        self.label_scr_4.text = '0'
        try:
            self.card.pop(self.label_pop_4.text)
        except:
            self.card

        self.total_prices()

        self.btn4.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn4.text = f'Japan\n sushi'

        print(self.card)
    # popup_5
    def popup_5s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_5s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_5s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_05s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_5s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def popup5(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_5)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added5))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_05)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added5))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def added_5s(self, instance):
        self.btn_5s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_5s.text = 'Added'
        if self.label_scr_5s.text == '-1':
            self.card[self.label_pop_5s.text] = '0'
        else:
            self.card[self.label_pop_5s.text] = self.label_scr_5s.text

        self.btn5s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn5s.text = f'Burger\npeppe  \n{self.label_scr_5s.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved_5s(self, instance):
        self.btn_5s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_5s.text = 'Add'
        self.label_scr_5s.text = '0'
        try:
            self.card.pop(self.label_pop_5s.text)
        except:
            self.card

        self.btn5s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn5s.text = f'Burger\npeppe'

        self.total_prices()

        print(self.card)

    def added5(self, instance):
        self.btn_5.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_5.text = 'Added'
        if self.label_scr_5.text == '-1':
            self.card[self.label_pop_5.text] = '0'
        else:
            self.card[self.label_pop_5.text] = self.label_scr_5.text

        self.btn5.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn5.text = f'Sushi\n philadelphia \n{self.label_scr_5.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved5(self, instance):
        self.btn_5.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_5.text = 'Add'
        self.label_scr_5.text = '0'
        try:
            self.card.pop(self.label_pop_5.text)
        except:
            self.card

        self.btn5.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn5.text = f'Sushi\n philadelphia'

        self.total_prices()

        print(self.card)

    # popup_6
    def popup_6s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_6s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_6s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_06s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_6s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()

    def popup6(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_6)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added6))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_06)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added6))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
    def added_6s(self, instance):
        self.btn_6s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_6s.text = 'Added'
        if self.label_scr_6s.text == '-1':
            self.card[self.label_pop_6s.text] = '0'
        else:
            self.card[self.label_pop_6s.text] = self.label_scr_6s.text


        self.btn6s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn6s.text = f'Burger\ntwin  \n{self.label_scr_6s.text}pc(s)'

        print(self.card)
        self.total_prices()
    def rmved_6s(self, instance):
        self.btn_6s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_6s.text = 'Add'
        self.label_scr_6s.text = '0'
        try:
            self.card.pop(self.label_pop_6s.text)
        except:
            self.card

        self.btn6s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn6s.text = f'Burger\ntwin'

        self.total_prices()

        print(self.card)

    def added6(self, instance):
        self.btn_6.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_6.text = 'Added'
        if self.label_scr_6.text == '-1':
            self.card[self.label_pop_6.text] = '0'
        else:
            self.card[self.label_pop_6.text] = self.label_scr_6.text

        self.btn6.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn6.text = f'Sushi\n original  \n{self.label_scr_6.text}pc(s)'

        print(self.card)
        self.total_prices()

    def rmved6(self, instance):
        self.btn_6.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_6.text = 'Add'
        self.label_scr_6.text = '0'
        try:
            self.card.pop(self.label_pop_6.text)
        except:
            self.card

        self.btn6.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn6.text = f'Sushi\n original'

        self.total_prices()

        print(self.card)

    # popup_7
    def popup_7s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_7s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_7s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_07s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_7s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
    def added_7s(self, instance):
        self.btn_7s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_7s.text = 'Added'
        self.card[self.label_pop_7s.text] = self.label_scr_7s.text

        self.btn7s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn7s.text = f'Burger\nkombo  \n{self.label_scr_7s.text}pc(s)'
        print(self.card)
        self.total_prices()
    def rmved_7s(self, instance):
        self.btn_7s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_7s.text = 'Add'
        self.label_scr_7s.text = '0'
        try:
            self.card.pop(self.label_pop_7s.text)
        except:
            self.card

        self.total_prices()

        self.btn7s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn7s.text = f'Burger\nkombo'

        print(self.card)

    # popup_8
    def popup_8s(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_8s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_8s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_08s)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_8s))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
    def added_8s(self, instance):
        self.btn_8s.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_8s.text = 'Added'
        self.card[self.label_pop_8s.text] = self.label_scr_8s.text

        self.btn8s.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn8s.text = f'Black\nangus  \n{self.label_scr_8s.text} pc(s)'

        print(self.card)
        self.total_prices()

    def rmved_8s(self, instance):
        self.btn_8s.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_8s.text = 'Add'
        self.label_scr_8s.text = '0'
        try:
            self.card.pop(self.label_pop_8s.text)
        except:
            self.card

        self.total_prices()

        self.btn8s.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn8s.text = f'Black\nangus'

        print(self.card)

    def build(self):

        tb = TabbedPanel(
            do_default_tab=True, tab_pos='top_left', default_tab_text='Main page', height=200, width=300,
            background_color=(0.1, 0.1, 0.25, 0.5))
        tbis = TabbedPanelItem(text='Burger', font_size=15, background_color=(0.5, 0.8, 0.8, 1),
                              height=100, width=500, underline=True)
        stacks = StackLayout()
        scrs = ScreenManager(size_hint=(1, 0.9))

        # screen_page_1

        scr_1s = Screen(name='page_1')
        img_1s = Image(source='C:/Users/Patrick moon/Downloads/burger1.JPG', size_hint=(0.8, 0.95), x=20, y=100)
        scr_1s.add_widget(img_1s)
        stack_scr_1s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_1s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_1s))
        stack_scr_1s.add_widget(self.label_scr_1s)
        stack_scr_1s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_1s))
        stack_scr_1s.add_widget(self.btn_1s)
        stack_scr_1s.add_widget(self.btn_01s)
        # stack_scr_1.add_widget(self.label_tp_1)
        scr_1s.add_widget(stack_scr_1s)

        def page_1s(instance):  # for listing button
            scrs.current = 'page_1'
            self.labels.text = 'Burger hot  2$'

        # screen_page_2

        scr_2s = Screen(name='page_2')
        scr_2s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger2.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_2s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_2s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_2s))
        stack_scr_2s.add_widget(self.label_scr_2s)
        stack_scr_2s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_2s))
        stack_scr_2s.add_widget(self.btn_2s)
        stack_scr_2s.add_widget(self.btn_02s)
        # stack_scr_2.add_widget(self.label_tp_2)
        scr_2s.add_widget(stack_scr_2s)

        def page_2s(instance):
            scrs.current = 'page_2'
            self.labels.text = 'Burger modesty  1.5$'

        # screen_page_3

        scr_3s = Screen(name='page_3')
        scr_3s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger3.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_3s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_3s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_3s))
        stack_scr_3s.add_widget(self.label_scr_3s)
        stack_scr_3s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_3s))
        stack_scr_3s.add_widget(self.btn_3s)
        stack_scr_3s.add_widget(self.btn_03s)
        scr_3s.add_widget(stack_scr_3s)

        def page_3s(instance):
            scrs.current = 'page_3'
            self.labels.text = 'Burger mexicana  3$'

        # screen_page_4

        scr_4s = Screen(name='page_4')
        scr_4s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger4.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_4s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_4s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_4s))
        stack_scr_4s.add_widget(self.label_scr_4s)
        stack_scr_4s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_4s))
        stack_scr_4s.add_widget(self.btn_4s)
        stack_scr_4s.add_widget(self.btn_04s)
        scr_4s.add_widget(stack_scr_4s)

        def page_4s(instance):
            scrs.current = 'page_4'
            self.labels.text = 'Burger Juicy 4$'

        # screen_page_5

        scr_5s = Screen(name='page_5')
        scr_5s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger5.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_5s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_5s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_5s))
        stack_scr_5s.add_widget(self.label_scr_5s)
        stack_scr_5s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_5s))
        stack_scr_5s.add_widget(self.btn_5s)
        stack_scr_5s.add_widget(self.btn_05s)
        scr_5s.add_widget(stack_scr_5s)

        def page_5s(instance):
            scrs.current = 'page_5'
            self.labels.text = 'Burger peppe 3.5$'

        # screen_page_5

        scr_6s = Screen(name='page_6')
        scr_6s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger7.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_6s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_6s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_6s))
        stack_scr_6s.add_widget(self.label_scr_6s)
        stack_scr_6s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_6s))
        stack_scr_6s.add_widget(self.btn_6s)
        stack_scr_6s.add_widget(self.btn_06s)
        scr_6s.add_widget(stack_scr_6s)

        def page_6s(instance):
            scrs.current = 'page_6'
            self.labels.text = 'Burger twin  9$'

        scr_7s = Screen(name='page_7')
        scr_7s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger5.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_7s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_7s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_7s))
        stack_scr_7s.add_widget(self.label_scr_7s)
        stack_scr_7s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_7s))
        stack_scr_7s.add_widget(self.btn_7s)
        stack_scr_7s.add_widget(self.btn_07s)
        scr_7s.add_widget(stack_scr_7s)

        def page_7s(instance):
            scrs.current = 'page_7'
            self.labels.text = 'Burger kombo  8.5$'

        scr_8s = Screen(name='page_8')
        scr_8s.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger6.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_8s = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_8s.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_8s))
        stack_scr_8s.add_widget(self.label_scr_8s)
        stack_scr_8s.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_8s))
        stack_scr_8s.add_widget(self.btn_8s)
        stack_scr_8s.add_widget(self.btn_08s)
        scr_8s.add_widget(stack_scr_8s)

        def page_8s(instance):
            scrs.current = 'page_8'
            self.labels.text = 'Black Angus 8.5$'

        for el in (scr_1s, scr_2s, scr_3s, scr_4s, scr_5s, scr_6s, scr_7s, scr_8s):
            scrs.add_widget(el)

        stack_1s = StackLayout(size_hint=(0.8, 1))
        stack_1s.add_widget(self.labels)
        stack_1s.add_widget(scrs)

        scrolls = ScrollView(size_hint=(0.2, 1), bar_width=10)
        boxs = BoxLayout(orientation='vertical', size_hint_y=None, padding=20)
        boxs.bind(minimum_height=boxs.setter('height'))

        self.btn1s.bind(on_press=page_1s)
        self.btn2s.bind(on_press=page_2s)
        self.btn3s.bind(on_press=page_3s)
        self.btn4s.bind(on_press=page_4s)
        self.btn5s.bind(on_press=page_5s)
        self.btn6s.bind(on_press=page_6s)
        self.btn7s.bind(on_press=page_7s)
        self.btn8s.bind(on_press=page_8s)

        # Buttons on scrolling bar

        for el in (
        self.btn1s, self.btn2s, self.btn3s, self.btn4s, self.btn5s, self.btn6s, self.btn7s, self.btn8s, self.label_tps):
            boxs.add_widget(el)

        scrolls.add_widget(boxs)
        stacks.add_widget(scrolls)
        stacks.add_widget(stack_1s)
        tbis.add_widget(stacks)

        tbi2s = TabbedPanelItem(text='Sushi', font_size=15, background_color=(0.5, 0.8, 0.8, 1),
                               height=100, width=500, underline=True)
        # Window.clearcolor = (0.5, 0.2, 0.1, 0.4)

        stack = StackLayout()
        scr = ScreenManager(size_hint=(1, 0.9))

        # screen_page_1

        scr_1 = Screen(name='page_1')
        img_1 = Image(source='C:/Users/Patrick moon/Downloads/sushi1.JPG', size_hint=(0.8, 0.9), x=20, y=100)
        scr_1.add_widget(img_1)
        stack_scr_1 = StackLayout(size_hint=(1, 0.1), x=20, y=0)
        stack_scr_1.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.add_scr_1))
        stack_scr_1.add_widget(self.label_scr_1)
        stack_scr_1.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                                      size_hint=(0.1, 1), on_press=self.sub_scr_1))
        stack_scr_1.add_widget(self.btn_1)
        stack_scr_1.add_widget(self.btn_01)
        scr_1.add_widget(stack_scr_1)

        def page_1(instance):
            scr.current = 'page_1'
            self.label.text = 'Sushi set cold\n 5$'

        # screen_page_2

        scr_2 = Screen(name='page_2')
        scr_2.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi2.JPG', size_hint=(0.8, 0.9), x=20, y=100))
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
        scr_6.add_widget(Image(source='C:/Users/Patrick moon/Downloads/sushi6.JPG', size_hint=(0.8, 0.9), x=20, y=100))
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

        self.btn1.bind(on_press=page_1)
        self.btn2.bind(on_press=page_2)
        self.btn3.bind(on_press=page_3)
        self.btn4.bind(on_press=page_4)
        self.btn5.bind(on_press=page_5)
        self.btn6.bind(on_press=page_6)
        self.btn7.bind(on_press=page_7)
        self.btn8.bind(on_press=page_8)



        for el in (self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.label_tpss):
            box.add_widget(el)

        stack.add_widget(scroll)
        stack.add_widget(stack_1)
        tbi2s.add_widget(stack)


        for el in (tbis, tbi2s):
            tb.add_widget(el)

        return tb

if __name__ == '__main__':
    MyApp().run()