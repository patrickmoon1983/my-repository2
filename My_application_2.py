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
        self.total_price_all = 0
        self.label = Label(text='Choose tasty burger', halign='center', font_size=30, italic=True, size_hint=(1, 0.1))
        self.label_tp = Label(text='Total:', size_hint_y=None, font_size=30, italic=True)
        self.label_scr_1 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_2 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_3 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_4 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_5 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_6 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_7 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.label_scr_8 = Label(text='0', font_size=20, italic=True, size_hint=(0.2, 1))
        self.btn1 = Button(text='Burger\nhot', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn2 = Button(text='Burger\nmodesty', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn3 = Button(text='Burger\nmexicana', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn4 = Button(text='Juicy\nburger', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn5 = Button(text='Burger\npeppe', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn6 = Button(text='Burger\ntwin', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn7 = Button(text='Big\nKombo', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        self.btn8 = Button(text='Black\nangus', size_hint_y=None, font_size=20, italic=True, bold=True,
                      background_color=[0.1, 0.3, 0.4, 0.7])
        #page_1

        self.label_pop_1 = Label(text='Burger hot\n ingredient: beef,oignon\n cheese, pepper\n\n'
                                      '     2$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_01 = Label(text='Burger hot\n ingredient: Beef, salad,\n cheese, pepper\n\n'
                                      '     2$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.btn_1 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                       size_hint=(0.2, 1), on_press=self.popup_1)
        self.btn_01 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.rmved_1)

        # page_2
        self.label_pop_2 = Label(text='Burger modesty\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     1.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_02 = Label(text='Burger modesty\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     1.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_2 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_2)
        self.btn_02 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_2)
        self.label_tp_2 = Label(text='total:', font_size=20, italic=True, size_hint=(0.3, 1))

        # page_3
        self.label_pop_3 = Label(text='Burger mexicana\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     3$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_03 = Label(text='Burger mexicana\n ingredient: Meat, salad\ncherries, pepper\n\n'
                                      '     3$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_3 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_3)
        self.btn_03 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_3)

        # page_4
        self.label_pop_4 = Label(text='Juicy Burger \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     4$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_04 = Label(text='Juicy Burger \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     4$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_4 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_4)
        self.btn_04 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_4)

        # page_5

        self.label_pop_5 = Label(text='Burger peppe \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_05 = Label(text='Burger peppe \n ingredient: Meat, cherries,\n eggs \nwassabi\n\n'
                                      '     3.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_5 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_5)
        self.btn_05 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_5)

        # page_6

        self.label_pop_6 = Label(text='Burger twin \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     9$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_06 = Label(text='Burger twin \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     9$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_6 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_6)
        self.btn_06 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_6)

        # page_7

        self.label_pop_7 = Label(text='Burger Kombo \n ingredient: Meat, cherries,\n eggs\n\n'
                                      '     8.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_07 = Label(text='Burger kombo \n ingredient: Meat, cherries,\n eggs\n\n'
                                       '     8.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_7 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_7)
        self.btn_07 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_7)

        # page_8

        self.label_pop_8 = Label(text='Black Angus \n ingredient: Meat, cherries,\n tomatoes\n\n'
                                      '     8.5$', font_size=25,
                                 italic=True, size_hint=(1, 0.7))
        self.label_pop_08 = Label(text='Black Angus \n ingredient: Meat, cherries,\n tomatoes\n\n'
                                       '     8.5$', font_size=25,
                                  italic=True, size_hint=(1, 0.7))
        self.btn_8 = Button(text='Add', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                            size_hint=(0.2, 1), on_press=self.popup_8)
        self.btn_08 = Button(text='Clear', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
                             size_hint=(0.2, 1), on_press=self.rmved_8)

        self.menu = {self.label_pop_1.text: 2,
                     self.label_pop_2.text: 1.5,
                     self.label_pop_3.text: 3,
                     self.label_pop_4.text: 4,
                     self.label_pop_5.text: 3.5,
                     self.label_pop_6.text: 9,
                     self.label_pop_7.text: 8.5,
                     self.label_pop_8.text: 8.5

                     }
   # Function for total price:
    def total_price(self):
        total_price = 0
        for el in self.card.keys():
            price = float(self.card[el]) * float(self.menu[el])
            total_price += price
        self.label_tp.text = f'Total:\n{total_price} $'

    # For adding or substracting qty on screens

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

    # For popping up messages on screens:

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
    def added_1(self, instance):     #For confirm button

        self.btn_1.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_1.text = 'Added'
        self.card[self.label_pop_1.text] = self.label_scr_1.text
        if self.card[self.label_pop_1.text] == '-1':
            self.card[self.label_pop_1.text] = '0'

        self.btn1.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn1.text = f'Burger\nhot \n{self.label_scr_1.text} pc(s)'

        print(self.card)
        self.total_price()

    def rmved_1(self, instance):     #for clear button
        self.btn_1.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_1.text = 'Add'
        self.label_scr_1.text = '0'
        try:
            self.card.pop(self.label_pop_1.text)
            self.total_price()
        except:
            self.card
            self.total_price()

        self.btn1.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn1.text = f'Burger\nhot'

        print(self.card)

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
        self.card[self.label_pop_2.text] = self.label_scr_2.text
        if self.card[self.label_pop_2.text] == '-1':
            self.card[self.label_pop_2.text] = '0'

        self.btn2.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn2.text = f'Burger\nmodesty \n{self.label_scr_2.text} pc(s)'

        print(self.card)
        self.total_price()
    def rmved_2(self, instance):
        self.btn_2.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_2.text = 'Add'
        self.label_scr_2.text = '0'
        try:
            self.card.pop(self.label_pop_2.text)
            self.total_price()
        except:
            self.card
            self.total_price()

        self.btn2.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn2.text = f'Burger\nmodesty'

        print(self.card)

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
        self.card[self.label_pop_3.text] = self.label_scr_3.text
        if self.card[self.label_pop_3.text] == '-1':
            self.card[self.label_pop_3.text] = '0'

        self.btn3.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn3.text = f'Burger\nmexicana  \n{self.label_scr_3.text} pc(s)'

        print(self.card)
        self.total_price()
    def rmved_3(self, instance):
        self.btn_3.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_3.text = 'Add'
        self.label_scr_3.text = '0'
        try:
            self.card.pop(self.label_pop_3.text)
            self.total_price()
        except:
            self.card
            self.total_price()

        self.btn3.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn3.text = f'Burger\nmexicana'

        print(self.card)

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
        self.card[self.label_pop_4.text] = self.label_scr_4.text

        self.btn4.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn4.text = f'Juicy\nburger  \n{self.label_scr_4.text} pc(s)'

        print(self.card)
        self.total_price()
    def rmved_4(self, instance):
        self.btn_4.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_4.text = 'Add'
        self.label_scr_4.text = '0'
        try:
            self.card.pop(self.label_pop_4.text)
        except:
            self.card

        self.total_price()

        self.btn4.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn4.text = f'Juicy\nburger'

        print(self.card)
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
        self.card[self.label_pop_5.text] = self.label_scr_5.text

        self.btn5.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn5.text = f'Burger\npeppe  \n{self.label_scr_5.text} pc(s)'

        print(self.card)
        self.total_price()
    def rmved_5(self, instance):
        self.btn_5.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_5.text = 'Add'
        self.label_scr_5.text = '0'
        try:
            self.card.pop(self.label_pop_5.text)
        except:
            self.card

        self.btn5.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn5.text = f'Burger\npeppe'

        self.total_price()

        print(self.card)

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
        self.card[self.label_pop_6.text] = self.label_scr_6.text

        self.btn6.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn6.text = f'Burger\ntwin  \n{self.label_scr_6.text}pc(s)'

        print(self.card)
        self.total_price()
    def rmved_6(self, instance):
        self.btn_6.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_6.text = 'Add'
        self.label_scr_6.text = '0'
        try:
            self.card.pop(self.label_pop_6.text)
        except:
            self.card

        self.btn6.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn6.text = f'Burger\ntwin'

        self.total_price()

        print(self.card)

    # popup_7
    def popup_7(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_7)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_7))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_07)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_7))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
    def added_7(self, instance):
        self.btn_7.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_7.text = 'Added'
        self.card[self.label_pop_7.text] = self.label_scr_7.text

        self.btn7.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn7.text = f'Burger\nkombo  \n{self.label_scr_7.text}pc(s)'
        print(self.card)
        self.total_price()
    def rmved_7(self, instance):
        self.btn_7.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_7.text = 'Add'
        self.label_scr_7.text = '0'
        try:
            self.card.pop(self.label_pop_7.text)
        except:
            self.card

        self.total_price()

        self.btn7.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn7.text = f'Burger\nkombo'

        print(self.card)

    # popup_8
    def popup_8(self, instance):

        try:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_8)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_8))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
        except:
            popup = Popup(title='confirmation', title_align='center', title_size=30, size_hint=(0.5, 0.5),
                          auto_dismiss=False)
            content_box = StackLayout()
            content_box.add_widget(self.label_pop_08)
            content_box.add_widget(Button(text='Confirm', size_hint=(1, 0.15), on_press=self.added_8))
            content_box.add_widget(Button(text='ok', size_hint=(1, 0.15), on_press=popup.dismiss))
            popup.add_widget(content_box)
            popup.open()
    def added_8(self, instance):
        self.btn_8.background_color = [0.4, 0.4, 0.4, 1]
        self.btn_8.text = 'Added'
        self.card[self.label_pop_8.text] = self.label_scr_8.text

        self.btn8.background_color = [0.5, 0.3, 0.7, 0.7]
        self.btn8.text = f'Black\nangus  \n{self.label_scr_8.text} pc(s)'

        print(self.card)
        self.total_price()

    def rmved_8(self, instance):
        self.btn_8.background_color = [0.3, 0.5, 0.6, 0.7]
        self.btn_8.text = 'Add'
        self.label_scr_8.text = '0'
        try:
            self.card.pop(self.label_pop_8.text)
        except:
            self.card

        self.total_price()

        self.btn8.background_color = [0.1, 0.3, 0.4, 0.7]
        self.btn8.text = f'Black\nangus'

        print(self.card)

    def build(self):

        stack = StackLayout()
        scr = ScreenManager(size_hint=(1, 0.9))

    #screen_page_1

        scr_1 = Screen(name='page_1')
        img_1 = Image(source='C:/Users/Patrick moon/Downloads/burger1.JPG',size_hint=(0.8, 0.95), x=20, y=100)
        scr_1.add_widget(img_1)
        stack_scr_1 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_1.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_1))
        stack_scr_1.add_widget(self.label_scr_1)
        stack_scr_1.add_widget(Button(text='-', font_size=20, italic=True,background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_1))
        stack_scr_1.add_widget(self.btn_1)
        stack_scr_1.add_widget(self.btn_01)
        # stack_scr_1.add_widget(self.label_tp_1)
        scr_1.add_widget(stack_scr_1)

        def page_1(instance): #for listing button
            scr.current = 'page_1'
            self.label.text ='Burger hot  2$'

    # screen_page_2

        scr_2 = Screen(name='page_2')
        scr_2.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger2.JPG',size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_2 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_2.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_2))
        stack_scr_2.add_widget(self.label_scr_2)
        stack_scr_2.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_2))
        stack_scr_2.add_widget(self.btn_2)
        stack_scr_2.add_widget(self.btn_02)
        # stack_scr_2.add_widget(self.label_tp_2)
        scr_2.add_widget(stack_scr_2)

        def page_2(instance):
            scr.current = 'page_2'
            self.label.text = 'Burger modesty  1.5$'

        # screen_page_3

        scr_3 = Screen(name='page_3')
        scr_3.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger3.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_3 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
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
            self.label.text = 'Burger mexicana  3$'

        # screen_page_4

        scr_4 = Screen(name='page_4')
        scr_4.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger4.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_4 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
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
            self.label.text = 'Burger Juicy 4$'

        # screen_page_5

        scr_5 = Screen(name='page_5')
        scr_5.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger5.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_5 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
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
            self.label.text ='Burger peppe 3.5$'

        # screen_page_5

        scr_6 = Screen(name='page_6')
        scr_6.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger7.JPG',size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_6 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
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
            self.label.text ='Burger twin  9$'

        scr_7 = Screen(name='page_7')
        scr_7.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger5.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_7 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_7.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_7))
        stack_scr_7.add_widget(self.label_scr_7)
        stack_scr_7.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_7))
        stack_scr_7.add_widget(self.btn_7)
        stack_scr_7.add_widget(self.btn_07)
        scr_7.add_widget(stack_scr_7)

        def page_7(instance):
            scr.current = 'page_7'
            self.label.text ='Burger kombo  8.5$'

        scr_8 = Screen(name='page_8')
        scr_8.add_widget(Image(source='C:/Users/Patrick moon/Downloads/burger6.JPG', size_hint=(0.8, 0.9), x=20, y=100))
        stack_scr_8 = StackLayout(size_hint=(1, 0.1), x=20, y=10)
        stack_scr_8.add_widget(Button(text='+', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.add_scr_8))
        stack_scr_8.add_widget(self.label_scr_8)
        stack_scr_8.add_widget(Button(text='-', font_size=20, italic=True, background_color=[0.3, 0.5, 0.6, 0.7],
        size_hint=(0.1, 1), on_press=self.sub_scr_8))
        stack_scr_8.add_widget(self.btn_8)
        stack_scr_8.add_widget(self.btn_08)
        scr_8.add_widget(stack_scr_8)

        def page_8(instance):
            scr.current = 'page_8'
            self.label.text = 'Black Angus 8.5$'

        for el in (scr_1, scr_2, scr_3, scr_4, scr_5, scr_6, scr_7, scr_8):
            scr.add_widget(el)

        stack_1 = StackLayout(size_hint=(0.8, 1))
        stack_1.add_widget(self.label)
        stack_1.add_widget(scr)

        scroll = ScrollView(size_hint=(0.2, 1), bar_width=10)
        box = BoxLayout(orientation='vertical', size_hint_y=None, padding=20)
        box.bind(minimum_height=box.setter('height'))

        self.btn1.bind(on_press=page_1)
        self.btn2.bind(on_press=page_2)
        self.btn3.bind(on_press=page_3)
        self.btn4.bind(on_press=page_4)
        self.btn5.bind(on_press=page_5)
        self.btn6.bind(on_press=page_6)
        self.btn7.bind(on_press=page_7)
        self.btn8.bind(on_press=page_8)

        # Buttons on scrolling bar

        for el in (self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.label_tp):
            box.add_widget(el)

        scroll.add_widget(box)
        stack.add_widget(scroll)
        stack.add_widget(stack_1)

        return stack

if __name__ == '__main__':
    MyApp().run()