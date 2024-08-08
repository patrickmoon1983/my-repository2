from kivy.clock import Clock
import sqlite3
import mysql.connector
from kivy.config import Config
Config.set("graphics", "width", "700")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", "1")
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy_garden.mapview import *
import pickle
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.button import *
from kivymd.uix.list import *
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar, MDBottomAppBar
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.backdrop.backdrop import MDBackdropBackLayer, MDBackdropFrontLayer
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selection import MDSelectionList
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivymd.uix.slider import MDSlider
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen, Screen
from kivy.metrics import dp
#dp - display pixles


# Window.clearcolor = (1, 1, 1, 1)



# MDIconButton
#
# class FirstMDApp(MDApp):
#     def build(self):
#         return MDIconButton(icon='phone',theme_icon_color='Custom', icon_color=(1, 0, 0, 1), size=(50,50),
#                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
# FirstMDApp().run()
# #


# MDFloatingActionButton.


#
# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDFloatingActionButton(icon="plus",
#                                       md_bg_color = (0, 1, 0.7, 0.7),
#                                       theme_icon_color="Custom"
#                                       ,icon_color=(0, 0, 0, 1),
#                                       pos=(37, 27))
#
# MainApp().run()


#MDFlatButton

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDFlatButton(text="Hello World!",
#                             font_size=40,
#                             md_bg_color=(1, 1, 1, 1),
#                             theme_text_color="Custom",
#                             text_color=(0, 0, 0, 1),
#                             x=0,
#                             y=0)
#
# MainApp().run()


#MDRaiseButton

# class MainApp(MDApp):
#     def build(self):
#         return MDRaisedButton(text="Hello World!",
#                               size_hint=(0.3, 0.3),
#                               pos_hint={"center_x": 0.5, "center_y": 0.5},
#                               shadow_color=(1, 0, 0, 1))
#
# MainApp().run()


#MDRectangleFlatButton
#
# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDRectangleFlatButton(text="Hello World!",
#                                      size_hint=(0.3, 0.3),
#                                      pos_hint={"center_x": 0.5, "center_y": 0.5})
#
# MainApp().run()


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def press_button(instance):
#
#             instance.text = f'Button pressed'
#
#             print("Button pressed")
#
#         button = MDRectangleFlatButton(text="Press me",
#                                        on_press=press_button)
#
#         return button
#
# MainApp().run()



##MDRectangleFlatIconButton


# from kivymd.app import MDApp
# from kivymd.uix.button import MDRectangleFlatIconButton
#
# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDRectangleFlatIconButton(icon="credit-card",
#                                      text="Credit-card",
#                                      pos_hint={"center_x": 0.5, "center_y": 0.5})
#
# MainApp().run()



#MDRoundedFlatButton


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDRoundFlatButton(text="Round Button",
#                                  pos_hint={"center_x": 0.5, "center_y": 0.5})

# MainApp().run()



#MDRoundFlatIconButton

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDRoundFlatIconButton(icon="crown",
#                                      text="Crown",
#                                      pos_hint={"center_x": 0.5, "center_y": 0.5})
#
# MainApp().run()


#MDFillRoundFlatButton

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange" #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
#         self.theme_cls.primary_hue = "700"
#         return MDFillRoundFlatButton(text="Click me",
#                                      pos_hint={"center_x": 0.5, "center_y": 0.5})
#
# MainApp().run()


#MDFillRoundFlatIconButton

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         return MDFillRoundFlatIconButton(icon="database",
#                                          text="Database",
#                                          font_style="Button",
#                                          pos_hint={"center_x": 0.5, "center_y": 0.5})
#
# MainApp().run()


#MDTextButton

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return  MDTextButton (text="I'm a TEXT Button. Click me please!",
#                               pos_hint={"center_x": 0.5, "center_y": 0.5},
#                               bold=True,
#                               italic=True,
#                               underline=True,
#                               theme_text_color="Custom",
#                               text_color=(1, 0, 0, 1))
#
# MainApp().run()




#MDFloatingActionButtonSpeedDial

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         return MDFloatingActionButtonSpeedDial(icon="plus",
#                                                root_button_anim=True,
#                                                data={'call': 'phone',
#                                                      'Buy': 'coin',
#                                                      'send': 'mail'})
#
# MainApp().run()


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def line(self):
#             print("Line")
#
#         def bar(self):
#             print("Bar")
#
#         def pie(self):
#             print("Pie")
#
#         button = MDFloatingActionButtonSpeedDial(icon="chart-areaspline",
#                                                  root_button_anim=True,
#                                                  data={'Line': ['chart-line', "on_press", line],
#                                                      'Bar': ['chart-bar', "on_press", bar],
#                                                      'Pie': ['chart-pie', "on_release", pie]})
#         def open(self):
#             print("Open")
#
#         def close(self):
#             print("Close")
#
#         button.bind(on_open=open)
#         button.bind(on_close=close)
#
#         return button
#
# MainApp().run()




#Icons

#
# from kivy.lang import Builder
# from kivy.properties import StringProperty
# from kivy.uix.screenmanager import Screen
#
# from kivymd.icon_definitions import md_icons
# from kivymd.app import MDApp
# from kivymd.uix.list import OneLineIconListItem
#
#
# Builder.load_string(
#     '''
# #:import images_path kivymd.images_path
#
#
# <CustomOneLineIconListItem>
#
#     IconLeftWidget:
#         icon: root.icon
#
#
# <PreviousMDIcons>
#
#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(10)
#         padding: dp(20)
#
#         MDBoxLayout:
#             adaptive_height: True
#
#             MDIconButton:
#                 icon: 'magnify'
#
#             MDTextField:
#                 id: search_field
#                 hint_text: 'Search icon'
#                 on_text: root.set_list_md_icons(self.text, True)
#
#         RecycleView:
#             id: rv
#             key_viewclass: 'viewclass'
#             key_size: 'height'
#
#             RecycleBoxLayout:
#                 padding: dp(10)
#                 default_size: None, dp(48)
#                 default_size_hint: 1, None
#                 size_hint_y: None
#                 height: self.minimum_height
#                 orientation: 'vertical'
# '''
# )
#
#
# class CustomOneLineIconListItem(OneLineIconListItem):
#     icon = StringProperty()
#
#
# class PreviousMDIcons(Screen):
#
#     def set_list_md_icons(self, text="", search=False):
#
#         def add_icon_item(name_icon):
#             self.ids.rv.data.append(
#                 {
#                     "viewclass": "CustomOneLineIconListItem",
#                     "icon": name_icon,
#                     "text": name_icon,
#                     "callback": lambda x: x,
#                 }
#             )
#
#         self.ids.rv.data = []
#         for name_icon in md_icons.keys():
#             if search:
#                 if text in name_icon:
#                     add_icon_item(name_icon)
#             else:
#                 add_icon_item(name_icon)
#
#
# class MainApp(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.screen = PreviousMDIcons()
#
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         return self.screen
#
#     def on_start(self):
#         self.screen.set_list_md_icons()
#
#
#
# MainApp().run()


#Закрытие вашего приложения кнопкой: on_press: app.stop()


# class MainApp(MDApp):
#     def build(self):
#         def press_button(self):
#             self.icon = "microsoft-windows"
#
#         button = MDIconButton(icon="android")
#         button.bind(on_press=press_button)
#
#         return button
#
# MainApp().run()


# class MainApp(MDApp):
#     def build(self):
#         def press_button(self):
#             self.icon = "microsoft-windows"
#
#         button = MDIconButton(icon="android",
#                               on_press=press_button)
#         return button
#
# MainApp().run()


# Widget MDBoxLayout


# class BoxApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "LightGreen"
#
#         def press_but(self):
#             nonlocal label
#             if self.text == "=":
#                 label.text = str(eval(label.text))
#             elif self.text == "C":
#                 label.text = ""
#             else:
#                 label.text += self.text
#
#         bl = MDBoxLayout(orientation="vertical",
#                          padding=60)
#
#         label = MDLabel(halign="right",
#                         text="",
#                         font_style="H2")
#         bl.add_widget(label)
#
#         buttons = [["7", "8", "9", "/"],
#                    ["4", "5", "6", "*"],
#                    ["1", "2", "3", "-"],
#                    ["0", ".", "C", "+"],
#                    ["="]]
#
#         for i in buttons:
#             vr = MDBoxLayout()
#             for j in i:
#                 if j == "=":
#                     but = MDRectangleFlatButton(text=j,
#                                                 size_hint=(1, 1),
#                                                 font_size=50,
#                                                 md_bg_color=(0, 1, 0, 0.02),
#                                                 on_press=press_but)
#                 else:
#                     but = MDRectangleFlatButton(text=j,
#                                                 size_hint=(1 / len(i), 1),
#                                                 font_size=50,
#                                                 md_bg_color=(0, 1, 0, 0.02),
#                                                 on_press=press_but)
#                 vr.add_widget(but)
#             bl.add_widget(vr)
#
#         return bl
#
#
# BoxApp().run()


#GrigLayout

# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         flag = True
#         flag2 = True
#
#         def press_button(instance):
#             nonlocal flag
#             nonlocal flag2
#             if flag2:
#                 if flag and instance.text != "0":
#                     instance.text = "X"
#                     flag = False
#                 elif not flag and instance.text != "X":
#                     instance.text = "0"
#                     flag = True
#             cell = layout.children
#             for i in cell:
#                 if cell[0].text == cell[1].text == cell[2].text and cell[0].text != "":
#                     cell[0].md_bg_color = cell[1].md_bg_color = cell[2].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[3].text == cell[4].text == cell[5].text and cell[3].text != "":
#                     cell[3].md_bg_color = cell[4].md_bg_color = cell[5].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[6].text == cell[7].text == cell[8].text and cell[6].text != "":
#                     cell[6].md_bg_color = cell[7].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[0].text == cell[3].text == cell[6].text and cell[0].text != "":
#                     cell[0].md_bg_color = cell[3].md_bg_color = cell[6].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[1].text == cell[4].text == cell[7].text and cell[1].text != "":
#                     cell[1].md_bg_color = cell[4].md_bg_color = cell[7].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[2].text == cell[5].text == cell[8].text and cell[2].text != "":
#                     cell[2].md_bg_color = cell[5].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[0].text == cell[4].text == cell[8].text and cell[0].text != "":
#                     cell[0].md_bg_color = cell[4].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#                 elif cell[2].text == cell[4].text == cell[6].text and cell[2].text != "":
#                     cell[2].md_bg_color = cell[4].md_bg_color = cell[6].md_bg_color = (1, 0, 0, 0.5)
#                     flag2 = False
#
#         layout = MDGridLayout(cols=3, rows=3)
#         for i in range(9):
#             but = MDRectangleFlatButton(size_hint=(1/3, 1/3),
#                                         font_size=150,
#                                         on_press=press_button)
#             layout.add_widget(but)
#
#         return layout
#
# FirstApp().run()
#

# class MyApp(MDApp):
#     def build(self):
#         layout = MDGridLayout()
#         layout.add_widget(MDRectangleFlatButton(pos=(100, 100)))
#         layout.add_widget(MDRectangleFlatButton(pos=(200, 200)))
#         layout.add_widget(MDRectangleFlatButton())
#         for i in layout.children:
#             print(i.pos)
#         return layout
#
# MyApp().run()


# class GridApp(MDApp):
#     def build(self):
#         main_layout = MDGridLayout(cols=5, rows=5)
#
#         for i in range(30):
#             button = MDRectangleFlatButton(text=f"{i+1}")
#             main_layout.add_widget(button)
#
#         return main_layout
#
# GridApp().run()


# class GridApp(MDApp):
#     def build(self):
#         main_layout = MDGridLayout(cols=5, rows=5)
#
#         def press_button(self):
#             print(main_layout.children.index(self))
#
#         for i in range(25):
#             button = MDRectangleFlatButton(text=f"{i + 1}", on_press=press_button)
#             main_layout.add_widget(button)
#
#         return main_layout
#
#
# GridApp().run()


#MDCircularLayou


# class MyApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         cl = MDCircularLayout(circular_radius=200)
#         for i in range(3):
#             cl.add_widget(MDIconButton(icon="account-circle-outline"))
#         return cl
# MyApp().run()



#Toolbar

#
# class MyApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "LightGreen"
#         self.theme_cls.material_style = "M3"
#
#         def press_home(self):
#             print("You pressed home button")
#
#         def press_dots(self):
#             print("You pressed dots button")
#
#         def press_android(self):
#             print("You pressed android button")
#
#         def press_phone(self):
#             print("You pressed phone button")
#
#         def press_button(self):
#             print(self.text)
#
#         def press_pencil(self):
#             print("You pressed pencil button")
#
#         topbar = MDTopAppBar(title="MDTopAppBar",
#                              left_action_items=[["human", press_home]],
#                              right_action_items=[["phone", press_phone]])
#
#         bl = MDBoxLayout(orientation="vertical")
#
#         bl.add_widget(topbar)
#
#         content = MDGridLayout(cols=3)
#         bl.add_widget(content)
#
#         for i in range(6):
#             content.add_widget(MDRectangleFlatButton(text=f"Button {str(i + 1)}",
#                                                      on_press=press_button))
#
#         bottombar = MDBottomAppBar()
#         topbar2 = MDTopAppBar(title="MDBottomAppBar",
#                               type="bottom",
#                               icon="pencil",
#                               mode="free-end",
#                               left_action_items=[["dots-vertical", press_dots]],
#                               right_action_items=[["android", press_android]])
#
#         topbar2.bind(on_action_button=press_pencil)
#         bottombar.add_widget(topbar2)
#         bl.add_widget(bottombar)
#
#         return bl
#
#
# MyApp().run()

#
#
# class MyApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Indigo"
#         self.theme_cls.material_style = "M3"
#
#         def press_home(self):
#             print("You pressed home button")
#
#         def press_dots(self):
#             print("You pressed dots button")
#
#         def press_android(self):
#             print("You pressed android button")
#
#         def press_phone(self):
#             print("You pressed phone button")
#
#         def press_button(self):
#             print(self.text)
#
#         def press_pencil(self):
#             print("You pressed pencil button")
#
#         fl = MDFloatLayout()
#         img = FitImage(source="C:/Users/Patrick moon/Downloads/drink1.jpg")
#         fl.add_widget(img)
#
#         topbar = MDTopAppBar(title="MDTopAppBar",
#                              left_action_items=[["home", press_home]],
#                              right_action_items=[["phone", press_phone]])
#
#         bl = MDBoxLayout(orientation="vertical")
#         fl.add_widget(bl)
#
#         bl.add_widget(topbar)
#
#         content = MDGridLayout(cols=3)
#         bl.add_widget(content)
#
#         for i in range(6):
#             content.add_widget(MDRectangleFlatButton(text=f"Button {str(i + 1)}",
#                                                      on_press=press_button))
#
#         bottombar = MDBottomAppBar()
#         topbar2 = MDTopAppBar(title="MDBottomAppBar",
#                               type="bottom",
#                               icon="pencil",
#                               mode="free-end",
#                               left_action_items=[["dots-vertical", press_dots]],
#                               right_action_items=[["android", press_android]])
#
#         topbar2.bind(on_action_button=press_pencil)
#         bottombar.add_widget(topbar2)
#         bl.add_widget(bottombar)
#
#         return fl


# MyApp().run()


#MDbackdrop



# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#
#         backdrop = MDBackdrop(title="MDBackDrop panel")
#
#         return backdrop
#
# FirstApp().run()




# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         backdrop = MDBackdrop(title="MDBackDrop panel",
#                               anchor_title="center",
#                               back_layer_color=(0, 0.4, 0.5, 1),
#                               close_icon="arrow-left",
#                               closing_time=1,
#                               closing_transition="in_bounce",
#                               opening_time=1,
#                               opening_transition="in_circ",
#                               disabled=False,
#                               front_layer_color=(0.3, 0.5, 0.5, 1),
#                               header_text="General Content",
#                               right_action_items=[["phone"]],
#                               specific_text_color=(1, 0, 0, 1),
#                               widget_style="ios",
#                               radius_left=50,
#                               radius_right=0,
#                               header="Menu")
#
#
#         return backdrop
#
# FirstApp().run()



#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         self.theme_cls.material_style = "M3"
#
#         front = MDBackdropFrontLayer(orientation="vertical")
#         back = MDBackdropBackLayer()
#
#         def wifi_button(self):
#             print("You pressed WiFi button")
#
#         def download_button(self):
#             print("You pressed Download button")
#
#         def microphone_button(self):
#             print("You pressed Microphone button")
#
#         button_front = MDRoundFlatIconButton(icon="download",
#                                              text="Download",
#                                              on_press=download_button,
#                                              md_bg_color=(0.2, 0.4, 0, 0.1))
#         button2_front = MDRoundFlatIconButton(icon="microphone",
#                                               text="Microphone",
#                                               on_press=microphone_button,
#                                               md_bg_color=(0.2, 0.6, 0, 0.4))
#         button_back = MDRoundFlatIconButton(icon="wifi",
#                                             text="WiFi",
#                                             pos_hint={"center_x": 0.5, "center_y": 0.5},
#                                             on_press=wifi_button,
#                                             md_bg_color=(1, 0, 0.5, 0.2))
#
#         backdrop = MDBackdrop(title="MDBackDrop panel",
#                               anchor_title="center",
#                               back_layer_color=(0, 0.4, 0.5, 1),
#                               close_icon="arrow-left",
#                               closing_time=0.2,
#                               closing_transition="in_bounce",
#                               opening_time=0.2,
#                               opening_transition="in_circ",
#                               disabled=False,
#                               front_layer_color=(0.3, 0.5, 0.5, 1),
#                               header_text="General Content",
#                               right_action_items=[["phone"]],
#                               specific_text_color=(1, 0, 0, 1),
#                               widget_style="desktop",
#                               radius_left=50,
#                               radius_right=0,
#                               header="Menu")
#
#         front.add_widget(button_front)
#         front.add_widget(button2_front)
#         back.add_widget(button_back)
#         backdrop.add_widget(front)
#         backdrop.add_widget(back)
#
#         return backdrop
#
# FirstApp().run()

#MDBottomNavigation

#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.material_style = "M3"
#         self.theme_cls.theme_style = "Dark"
#
#         navigation = MDBottomNavigation()
#
#         message = MDBottomNavigationItem(
#             name="Message",
#             text="Message",
#             icon="chat-outline")
#         navigation.add_widget(message)
#
#         music = MDBottomNavigationItem(
#             name="Music",
#             text="Music",
#             icon="music")
#         navigation.add_widget(music)
#
#         setting = MDBottomNavigationItem(
#             name="Settings",
#             icon="cog-outline")
#         navigation.add_widget(setting)
#
#         return navigation
#
#
# FirstApp().run()


#
#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.material_style = "M3"
#         self.theme_cls.theme_style = "Dark"
#
#         navigation = MDBottomNavigation(panel_color=(1, 0, 0, 0.2),
#                                         selected_color_background=(1, 0.4, 0, 1),
#                                         text_color_active=(0, 1, 0, 1))
#
#         def button_message(self):
#             print("You pressed message button")
#
#         box = MDBoxLayout()
#         lbl = MDLabel(text="Content")
#         box.add_widget(lbl)
#
#         message = MDBottomNavigationItem(
#             name="Message",
#             text="Message",
#             icon="chat-outline",
#             badge_icon="numeric-2",
#             on_tab_press=button_message)
#         message.add_widget(box)
#         navigation.add_widget(message)
#
#         return navigation
#
#
# FirstApp().run()
#
#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.material_style = "M3"
#         self.theme_cls.theme_style = "Dark"
#
#         navigation = MDBottomNavigation()
#
#         def button_message(self):
#             print("You pressed message button")
#
#         box = MDBoxLayout()
#         lbl = MDLabel(text="Content")
#         box.add_widget(lbl)
#
#         message = MDBottomNavigationItem(
#             name="Message",
#             text="Message",
#             icon="chat-outline",
#         on_tab_press=button_message)
#         message.add_widget(box)
#
#         navigation.add_widget(message)
#
#         music = MDBottomNavigationItem(
#             name="Music",
#             text="Music",
#             icon="music")
#         navigation.add_widget(music)
#
#         setting = MDBottomNavigationItem(
#             name="Settings",
#             icon="cog-outline")
#         navigation.add_widget(setting)
#
#         return navigation
#
#
# FirstApp().run()



#
# class FirstApp(MDApp):
#     def build(self):
#         return MDBottomNavigationItem(
#             name="Message",
#             text="Message",
#             icon="chat-outline")
#
# FirstApp().run()
#
#
# class FirstApp(MDApp):
#     def build(self):
#         navi = MDBottomNavigation()
#         but = MDBottomNavigationItem(
#             name="Message",
#             text="Message",
#             icon="chat-outline")
#         navi.add_widget(but)
#         return navi
#
# FirstApp().run()

#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def press_tab(self):
#             print("sport-car")
#
#         return MDBottomNavigation(MDBottomNavigationItem(icon="car",
#                                                          on_tab_press=press_tab))
#
#
# FirstApp().run()


#MDSmartTile

# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def on_like(self):
#             if self.icon == "thumb-up-outline":
#                 self.icon = "thumb-up"
#                 dislike.icon = "thumb-down-outline"
#             elif self.icon == "thumb-up":
#                 self.icon = "thumb-up-outline"
#             elif self.icon == "thumb-down-outline":
#                 self.icon = "thumb-down"
#                 like.icon = "thumb-up-outline"
#             elif self.icon == "thumb-down":
#                 self.icon = "thumb-down-outline"
#         imagelist = MDSmartTile(source="C:/Users/Patrick moon/Downloads/drink1.jpg",
#                                 radius=15,
#                                 box_radius=(0, 0, 15, 15),
#                                 box_color=(0.04, 0.1, 0.1, 0.7),
#                                 size_hint=(0.7, 0.7),
#                                 pos_hint={"center_x": 0.5, "center_y": 0.5},
#                                 box_position="footer")
#         like = MDIconButton(icon="thumb-up-outline",
#                             theme_icon_color="Custom",
#                             icon_color=(1, 0, 0, 1),
#                             pos_hint={"center_y": 0.5},
#                             on_release=on_like)
#         imagelist.add_widget(like)
#
#         dislike = MDIconButton(icon="thumb-down-outline",
#                                theme_icon_color="Custom",
#                                icon_color=(1, 0, 0, 1),
#                                pos_hint={"center_y": 0.5},
#                                on_release=on_like)
#         imagelist.add_widget(dislike)
#         name = MDLabel(text="Fresh drink",
#                        halign="center")
#         imagelist.add_widget(name)
#
#         return imagelist
#
# FirstApp().run()
#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         main_layout = MDGridLayout(cols=2, spacing=10, padding=10)
#
#         def on_like(self):
#             if self.icon == "heart-outline":
#                 self.icon = "heart"
#             else:
#                 self.icon = "heart-outline"
#
#         imagelist_1 = MDSmartTile(MDIconButton(icon="heart-outline",
#                                                pos_hint={"center_y": 0.5},
#                                                on_release=on_like),
#                                   MDLabel(text="BMW E92"),
#                                   source="C:/Users/Patrick moon/Downloads/drink1.jpg",
#                                   radius=24,
#                                   box_radius=(0, 0, 24, 24))
#         main_layout.add_widget(imagelist_1)
#
#         imagelist_2 = MDSmartTile(MDIconButton(icon="heart-outline",
#                                                pos_hint={"center_y": 0.5},
#                                                on_release=on_like),
#                                   MDLabel(text="BMW E39"),
#                                   source="C:/Users/Patrick moon/Downloads/drink2.jpg",
#                                   radius=24,
#                                   box_radius=(0, 0, 24, 24))
#         main_layout.add_widget(imagelist_2)
#
#         imagelist_3 = MDSmartTile(MDIconButton(icon="heart-outline",
#                                                pos_hint={"center_y": 0.5},
#                                                on_release=on_like),
#                                   MDLabel(text="BMW F10"),
#                                   source="C:/Users/Patrick moon/Downloads/drink3.jpg",
#                                   radius=24,
#                                   box_radius=(0, 0, 24, 24))
#         main_layout.add_widget(imagelist_3)
#
#         return main_layout
#
# FirstApp().run()


#MDlist

#
# class Example(MDApp):
#     def build(self):
#
#         def press(self):
#             print("OneLineAvatarListItem")
#
#         def avatar(self):
#             print("Pressed avatar")
#
#         list = MDList()
#         line = OneLineAvatarListItem(text="General line",
#                                      on_press=press)
#         avatar = ImageLeftWidget(source="C:/Users/Patrick moon/Downloads/drink3.jpg",
#                                  on_press=avatar)
#         line.add_widget(avatar)
#         list.add_widget(line)
#         return list

# Example().run()


#
# class Example(MDApp):
#     def build(self):
#         def press_line(self):
#             print("OneLineAvatarIconListItem")
#
#         def press_icon(self):
#             print("Pressed icon")
#
#         def press_avatar(self):
#             print("Pressed avatar")
#
#         list = MDList(OneLineAvatarIconListItem(ImageLeftWidget(source="C:/Users/Patrick moon/Downloads/drink3.jpg",
#                                                                 on_release=press_avatar),
#                                                 IconRightWidget(icon="menu",
#                                                                 on_release=press_icon),
#                                                 text="General line",
#                                                 on_press=press_line))
#         return list
#
# Example().run()



#MDDropdownMenu


#
#
# class MenuApp(MDApp):
#     def build(self):
#         button = MDRectangleFlatButton(text="Open Menu",
#                                        pos_hint={"center_x": 0.5, "center_y": 0.5})
#         menu_items = [
#     {"viewclass": "OneLineListItem", "text": "Item 1", "divider_color": (0.3, 0.3, 0.3, 1), "divider": "Full"},
#     {"viewclass": "OneLineListItem", "text": "Item 2", "divider_color": (0.3, 0.3, 0.3, 1), "divider": "Full"},
#     {"viewclass": "OneLineListItem", "text": "Item 3", "divider_color": (0.3, 0.3, 0.3, 1), "divider": "Full"}]
#         menu = MDDropdownMenu(caller=button,
#                               items=menu_items,
#                               width_mult=2,
#                               max_height=145,
#                               position="auto",
#                               elevation=4,
#                               opening_time=0.5,
#                               opening_transition="in_bounce",
#                               radius=[0, 15, 15, 15])
#         def press(self):
#             menu.open()
#         button.bind(on_release=press)
#
#         return button
#
# MenuApp().run()



#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Orange"
#         self.theme_cls.theme_style = "Dark"
#
#         def press_item1():
#             text_field.text = "100"
#             menu.dismiss()
#
#         def press_item2():
#             text_field.text = "200"
#             menu.dismiss()
#
#         def focus(self, value):
#             if value:
#                 menu.open()
#
#         text_field = MDTextField(hint_text="Value")
#         text_field.bind(focus=focus)
#
#         menu_items = [{"viewclass": "MDRectangleFlatIconButton", "text": "100", "icon": "cog",  "on_release": press_item1},
#                       {"viewclass": "MDRectangleFlatIconButton", "text": "200", "icon": "cog",  "on_release": press_item2}]
#         menu = MDDropdownMenu(caller=text_field,
#                               items=menu_items,
#                               width_mult=3,
#                               max_height=80)
#
#         return text_field
#
# FirstApp().run()



#
#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Orange"
#         self.theme_cls.theme_style = "Dark"
#
#         def press_item1():
#             text_field.text = "100"
#             menu.dismiss()
#
#         def press_item2():
#             text_field.text = "200"
#             menu.dismiss()
#
#         def focus(value):
#             if value:
#                 menu.open()
#
#         fl = MDFloatLayout()
#
#         text_field = MDTextField(hint_text="Value", pos_hint={"center_x":0.6})
#
#         menu_items = [{"viewclass": "MDRectangleFlatIconButton", "text": "100", "icon": "cog",  "on_release": press_item1},
#                       {"viewclass": "MDRectangleFlatIconButton", "text": "200", "icon": "cog",  "on_release": press_item2}]
#
#         btn = MDIconButton(icon="menu", pos_hint={"bottom": 0}, on_press=focus)
#
#         menu = MDDropdownMenu(caller=btn,
#                               items=menu_items,
#                               width_mult=3,
#                               max_height=80)
#
#         fl.add_widget(text_field)
#         fl.add_widget(btn)
#
#         return fl
#
# FirstApp().run()

# class MenuApp(MDApp):
#     def build(self):
#         def press(self):
#             menu.open()
#         button = MDRectangleFlatButton(on_release=press,
#                                        pos_hint={"center_x": 0.5, "center_y": 0.5})
#
#         menu_items = [{"viewclass": "OneLineListItem"}]
#
#         menu = MDDropdownMenu(items=menu_items)
#         return button
#
# MenuApp().run()

#


#
#
# class FirstApp(MDApp):
#     def build(self):
#         box = FloatLayout()
#
#         sl = MDSelectionList(cols=3,
#                              spacing=20,
#                              overlay_color=(1, 0, 0, 0.3),
#                              icon_bg_color=(0, 1, 0, 1),
#                              progress_round_color=(1, 1, 1, 1),
#                              selected_mode=False,
#                              progress_round_size=30)
#         box.add_widget(sl)
#
#         def delete_widget(self):
#             lst = sl.get_selected_list_items()
#             for i in lst:
#                 sl.remove_widget(i)
#             # topbar.title = "MDSelectionList"
#             sl.selected_mode = False
#
#         def select_all(self):
#             if len(sl.get_selected_list_items()) < len(sl.children):
#                 sl.selected_all()
#             else:
#                 sl.unselected_all()
#
#         def select(self, item):
#             topbar.title = str(len(self.get_selected_list_items()))
#
#         def unselect(self, item):
#             if len(self.get_selected_list_items()) == 0:
#                 topbar.title = "MDSelectionList"
#             else:
#                 topbar.title = str(len(self.get_selected_list_items()))
#
#         sl.bind(on_selected=select)
#         sl.bind(on_unselected=unselect)
#
#         topbar = MDTopAppBar(title="MDSelectionList",
#                              left_action_items=[["trash-can-outline", delete_widget],
#                                                 ["bookmark-check-outline", select_all]],
#                              pos=(0, 540))
#
#         box.add_widget(topbar)
#
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/drink1.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/drink2.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/sushi1.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/sushi2.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/burger1.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#         sl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/burger2.JPG",
#                                size_hint=(None, None), size=(250, 150)))
#
#         return box
#
# FirstApp().run()


# MDSwiper


#
# class FirstApp(MDApp):
#     def build(self):
#
#         def swipe(self):
#             print(swiper.get_current_index())
#
#         swiper = MDSwiper(MDSwiperItem(FitImage(source="C:/Users/Patrick moon/Downloads/sushi2.JPG", radius=(50, 50, 50, 50))),
#                           MDSwiperItem(FitImage(source="C:/Users/Patrick moon/Downloads/burger2.JPG", radius=(50, 50, 50, 50))),
#                           MDSwiperItem(
#                               FitImage(source="C:/Users/Patrick moon/Downloads/burger1.JPG", radius=(50, 50, 50, 50))),
#                           MDSwiperItem(
#                               FitImage(source="C:/Users/Patrick moon/Downloads/sushi1.JPG", radius=(50, 50, 50, 50))),
#                           bar_width=10,
#                           bar_color=(1, 0, 0, 1),
#                           bar_inactive_color=(0, 0, 1, 1),
#                           bar_margin=10,
#                           bar_pos_x="bottom",
#                           swipe_on_scroll=True,
#                           items_spacing=40,
#                           transition_duration=0.5,
#                           on_swipe=swipe)
#         custom_slide = MDSwiperItem()
#         fl = MDFloatLayout()
#         fl.add_widget(FitImage(source="C:/Users/Patrick moon/Downloads/sushi3.JPG",
#                                pos_hint={"center_x": 0.5, "center_y": 0.5}))
#         fl.add_widget(MDLabel(text="MDLabel",
#                               font_style="H3",
#                               pos_hint={"center_x": 0.9, "center_y": 0.1},
#                               theme_text_color="Custom",
#                               text_color=(1, 1, 1, 1)))
#         fl.add_widget(MDRaisedButton(text="button",
#                                      pos_hint={"center_x": 0.54, "center_y": 0.2}))
#         custom_slide.add_widget(fl)
#         swiper.add_widget(custom_slide)
#         swiper.set_current(0)
#         return swiper
#
# FirstApp().run()




#MDTapTargetView


#
# class FirstApp(MDApp):
#     def build(self):
#         global tap_flag
#         tap_flag = True
#
#         def tap_start(self):
#             global tap_flag
#             if tap_flag == True:
#                 tap.start()
#                 tap_flag = False
#             else:
#                 # tap.start()
#                 print("Button action")
#
#         but = MDIconButton(icon="dots-vertical",
#                            pos=(10, 10),
#                            md_bg_color=(1, 0.5, 0, 1),
#                            on_release=tap_start)
#
#         tap = MDTapTargetView(widget=but,
#                               title_text="Название кнопки",
#                               title_text_bold=False,
#                               title_text_color=(0, 0, 0, 1),
#                               title_text_size=35,
#                               description_text="Описание кнопки",
#                               widget_position="left_bottom",
#                               target_radius=40,
#                               cancelable=True,
#                               description_text_bold=False,
#                               description_text_color=(0, 0, 1, 1),
#                               description_text_size=25,
#                               outer_circle_color=(1, 0, 0),
#                               outer_circle_alpha=0.8,
#                               outer_radius=300,
#                               target_circle_color=(0.8, 0.8, 0.8))
#
#         return but
#
# FirstApp().run()

# class FirstApp(MDApp):
#     def build(self):
#         global tap_flag
#         tap_flag = True
#
#         def tap_start(self):
#             global tap_flag
#             if tap_flag == True:
#                 tap.start()
#                 tap_flag = False
#                 flag = {"tap_flag": False}
#                 with open('first_start.pickle', 'wb') as f:
#                     first = pickle.dumps(flag)
#                     f.write(first)
#             else:
#                 print("Button action")
#
#         but = MDIconButton(icon="dots-vertical",
#                            pos=(10, 10),
#                            md_bg_color=(1, 0.5, 0, 1),
#                            on_release=tap_start)
#
#         tap= MDTapTargetView(widget=but,
#                              title_text="Название кнопки",
#                              title_text_bold=False,
#                              title_text_color=(0, 0, 0, 1),
#                              title_text_size=35,
#                              description_text="Описание кнопки",
#                              widget_position="left_bottom",
#                              target_radius=40,
#                              cancelable=False,
#                              description_text_bold=False,
#                              description_text_color=(0, 0, 1, 1),
#                              description_text_size=25,
#                              outer_circle_color=(1, 0, 0),
#                              outer_circle_alpha=0.8,
#                              outer_radius=300,
#                              target_circle_color=(0, 0.8, 0.8))
#         return but
#
#     def on_start(self):
#         global tap_flag
#         try:
#             with open('first_start.pickle', 'rb') as f:
#                 first = f.read()
#             flag = pickle.loads(first)
#             tap_flag = flag["tap_flag"]
#         except FileNotFoundError:
#             pass

# FirstApp().run()



# class FirstApp(MDApp):
#     def build(self):
#         def tap_start(self):
#             tap.start()
#
#         but = MDIconButton(on_release=tap_start)
#
#         tap = MDTapTargetView(widget=but,
#                               description_text="Описание кнопки")
#
#         return but
#
# FirstApp().run()



#MDTextField



# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         text_field = MDTextField(size_hint=(0.4, None),
#                                  pos_hint={"center_x": 0.5, "center_y": 0.5},
#                                  mode="rectangle",
#                                  hint_text="Никнейм",
#                                  max_text_length=16,
#                                  active_line=True,
#                                  allow_copy=False,
#                                  base_direction="ltr",
#                                  cursor_blink=True,
#                                  icon_left="account")
#
#         return text_field
#
# FirstApp().run()

# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         box = FloatLayout()
#
#         text_field = MDTextField(size_hint=(0.4, None),
#                                  pos_hint={"center_x": 0.5, "center_y": 0.8},
#                                  mode="rectangle",
#                                  hint_text="Никнейм",
#                                  icon_left="account",
#                                  max_text_length=16)
#
#         text_field2 = MDTextField(size_hint=(0.4, None),
#                                   pos_hint={"center_x": 0.5, "center_y": 0.65},
#                                   mode="rectangle",
#                                   hint_text="Email",
#                                   icon_left="email-outline",
#                                   validator="email")
#
#         text_field3 = MDTextField(size_hint=(0.4, None),
#                                   pos_hint={"center_x": 0.5, "center_y": 0.5},
#                                   mode="rectangle",
#                                   hint_text="Пароль",
#                                   icon_left="lock-outline",
#                                   helper_text="Минимальная длинна 8 символов.",
#                                   helper_text_mode="on_error",
#                                   password=True,
#                                   password_mask="X",
#                                   error=True)
#
#         box.add_widget(text_field)
#         box.add_widget(text_field2)
#         box.add_widget(text_field3)
#
#         return box
#
# FirstApp().run()
#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         box = FloatLayout()
#
#         def on_error(self):
#             if len(text_field3.text) < 8:
#                 text_field3.error = True
#                 text_field3.text_validate_unfocus = False
#             else:
#                 text_field3.text_validate_unfocus = True
#             if ((len(text_field.text) > 0) and not text_field.error) and not text_field2.error and not text_field3.error:
#                 confirm.disabled = False
#             else:
#                 confirm.disabled = True
#         Clock.schedule_interval(on_error, 1/5)
#
#         def next_field(self):
#             if text_field.focus == True:
#                 text_field2.focus = True
#             elif text_field2.focus == True:
#                 text_field3.focus = True
#
#         def show_password(self):
#             if text_field3.password == True:
#                 text_field3.password = False
#                 self.icon = "eye-off-outline"
#             else:
#                 text_field3.password = True
#                 self.icon = "eye-outline"
#
#         def on_confirm(self):
#             print("Поздравляем с регистрацией!")
#
#         text_field = MDTextField(size_hint=(0.4, None),
#                                  pos_hint={"center_x": 0.5, "center_y": 0.8},
#                                  mode="rectangle",
#                                  hint_text="Никнейм",
#                                  icon_left="account",
#                                  max_text_length=16,
#                                  on_text_validate=next_field)
#
#         text_field2 = MDTextField(size_hint=(0.4, None),
#                                   pos_hint={"center_x": 0.5, "center_y": 0.65},
#                                   mode="rectangle",
#                                   hint_text="Email",
#                                   icon_left="email-outline",
#                                   validator="email",
#                                   on_text_validate=next_field)
#
#         text_field3 = MDTextField(size_hint=(0.4, None),
#                                   pos_hint={"center_x": 0.5, "center_y": 0.5},
#                                   mode="rectangle",
#                                   hint_text="Пароль",
#                                   icon_left="lock-outline",
#                                   helper_text="Минимальная длинна 8 символов.",
#                                   helper_text_mode="on_error",
#                                   password=True,
#                                   password_mask="X")
#
#         box.add_widget(text_field)
#         box.add_widget(text_field2)
#         box.add_widget(text_field3)
#
#         box.add_widget(MDIconButton(icon="eye-outline",
#                                     pos_hint={"center_x": 0.67, "center_y": 0.49},
#                                     on_press=show_password))
#
#         confirm = MDRectangleFlatButton(text="Продолжить",
#                                         pos_hint={"center_x": 0.5, "center_y": 0.35},
#                                         disabled=True,
#                                         on_press=on_confirm)
#         box.add_widget(confirm)
#
#         return box
#
# FirstApp().run()


# class FirstApp(MDApp):
#     def build(self):
#         return MDTextField(fill_color_focus=(1, 0, 0, 1),
#                            mode="round")
#
# FirstApp().run()


# class FirstApp(MDApp):
#     def build(self):
#         return MDTextField(fill_color_focus=(1, 0, 0, 1),
#                            mode="fill")
#
# FirstApp().run()


#MDProgressBar

# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         fl = MDFloatLayout()
#         progress = MDProgressBar(value=20,
#                                  max=100,
#                                  back_color=(0, 0.5, 1, 0.2),
#                                  color=(0, 0.5, 1, 1),
#                                  orientation="horizontal",
#                                  reversed=False)
#         def upgrade(self):
#             progress.value += 1
#             # print((progress.parent))
#         Clock.schedule_interval(upgrade, 1/10)
#
#         fl.add_widget(progress)
#         return fl
#
# FirstApp().run()


# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         fl = MDFloatLayout()
#         progress = MDProgressBar(type="indeterminate",
#                                  running_duration=0.5,
#                                  catching_duration=1)
#         fl.add_widget(progress)
#         progress.start()
#         return fl
#
# FirstApp().run()


#MDSpinner


# class FirstApp(MDApp):
#
#     def build(self):
#         spinner = MDSpinner(size_hint=(None, None),
#                             size=(45, 45),
#                             pos_hint={"center_x": 0.5, "center_y": 0.5},
#                             palette=[[0.2, 0.8, 0.5, 1],
#                                 [0.3, 0.3, 0.8, 1],
#                                 [0.8, 0.3, 0.5, 1],
#                                 [0.8, 0.9, 0.4, 1],
#                                 [1, 0, 0, 1],
#                                 [0, 0, 0, 1]])
#         return spinner
#
# FirstApp().run()



#MDCheckbox




#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def active_checkbox(instance):
#             print(instance.state)
#             print(instance.active)
#
#         checkbox = MDCheckbox(size_hint=(0.05, 0.05),
#                               color_active=(1, 0, 0, 1),
#                               checkbox_icon_down="checkbox-marked-circle-outline",
#                               checkbox_icon_normal="checkbox-blank-circle-outline",
#                               on_press=active_checkbox)
#         checkbox.color_active = (1, 0, 0, 1)
#         checkbox.color_inactive = (0, 1, 0, 1)
#         checkbox.on_active = active_checkbox
#
#         return checkbox
#
# FirstApp().run()

#
# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         box = MDBoxLayout()
#         checkbox1 = MDCheckbox(size_hint=(None, None), size=(50, 50), group="test")
#         checkbox2 = MDCheckbox(size_hint=(None, None), size=(50, 50), group="test")
#         checkbox3 = MDCheckbox(size_hint=(None, None), size=(50, 50), group="test")
#         box.add_widget(checkbox1)
#         box.add_widget(checkbox2)
#         box.add_widget(checkbox3)
#         return box
#
# FirstApp().run()


#MDSwitch

# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         box = MDBoxLayout()
#         switch_android = MDSwitch(widget_style="android")
#         switch_ios = MDSwitch(widget_style="ios")
#         switch_desktop = MDSwitch(widget_style="desktop")
#         box.add_widget(switch_android)
#         box.add_widget(switch_ios)
#         box.add_widget(switch_desktop)
#
#         return box
#
# FirstApp().run()


# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         def press_switch(self, value):
#             print(value)
#
#         switch = MDSwitch()
#         switch.bind(active=press_switch)
#
#         return switch
#
# FirstApp().run()


# class FirstApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.material_style = "M3"
#         switch = MDSwitch(icon_active="check",
#                           icon_inactive="close",
#                           icon_active_color=(0, 1, 0, 1),
#                           icon_inactive_color=(1, 0, 0, 1))
#
#         return switch
#
# FirstApp().run()


#MDSlider



#
# class MyApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#
#         slider = MDSlider(color=(1, 0.3, 0, 1),
#                           hint_bg_color=(0, 0.3, 1, 1),
#                           hint_radius=(25, 25, 0, 0),
#                           min=50,
#                           max=150,
#                           orientation="horizontal",
#                           show_off=True,
#                           step=5,
#                           value=80)
#
#         def value_slider(self, value):
#             print(value)
#
#
#         slider.bind(value=value_slider)
#
#         return slider
#
# MyApp().run()


from kivy.lang import Builder

#Login screen

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('login.kv')
#
#     def logger(self):
#         self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
#
#     def clear(self):
#         self.root.ids.welcome_label.text = 'WELCOME'
#         self.root.ids.user.text = ''
#         self.root.ids.password.text = ''
#
# MainApp().run()


#Create a Bottom bar Button


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('bbutton.kv')
#
#     def presser(self):
#         self.root.ids.my_label.text = f'GIT HUB '
#
# MainApp().run()


#Navbar with icon

# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('bbar.kv')
#
#     def press_home(self):
#
#         print("You pressed home button")
#
# MainApp().run()



#Speed dial button
#
# class MainApp(MDApp):
#
#
#     def callback(self, instance):
#
#         if instance.icon == 'language-python':
#             lg = 'Python'
#         elif instance.icon == 'language-ruby':
#             lg= 'Ruby'
#         elif instance.icon == 'language-javascript':
#             lg = 'JS'
#         self.root.ids.my_label.text = f'You pressed {lg}'
#
#     def open(self):
#
#         self.root.ids.my_label.text = f'You open !!'
#
#     def close(self):
#
#         self.root.ids.my_label.text = f'You close !!'
#
#
#     def build(self):
#
#         self.data = {
#             'Python': ['language-python', 'on_press', self.callback],
#             'Ruby': ['language-ruby', 'on_press', self.callback],
#             'JS': ['language-javascript', 'on_press', self.callback]
#         }
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('sd.kv')
#
# MainApp().run()


#Alert Dialog

#
# class MainApp(MDApp):
#
#     dialog = None
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('alert.kv')
#
#     def show_dialog(self):
#         if not self.dialog:
#             self.dialog = MDDialog(title='Pretyy Neat, Right', text='This is some text ', buttons= [
#                 MDFlatButton(text='Cancel', text_color=self.theme_cls.primary_color, on_release= self.close_diolag),
#                 MDRectangleFlatButton(text='Yes It is Neat!', text_color=self.theme_cls.primary_color,
#                                       on_release= self.neat_dialog)
#             ]
#         )
#         self.dialog.open()
#     def close_diolag(self, obj):
#         self.dialog.dismiss()
#
#     def neat_dialog(self, obj):
#         self.dialog.dismiss()
#
#         self.root.ids.my_label.text = f'Yes it is Neat!'
#
#
# MainApp().run()



#Swiper1


# class MainApp(MDApp):
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('swiper.kv')
#
#
# MainApp().run()



#swiper2
#
# class MainApp(MDApp):
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('swiper2.kv')
#
#     def on_swipe_left(self):
#         self.root.ids.toolbar.title = f'You swiped left!!'
#         # print('You swiped left!!')
#
#     def on_swipe_right(self):
#         self.root.ids.toolbar.title = f'You swiped right!!'
#         # print('You swiped right!!')
#
#
# MainApp().run()


#Date picker

# class MainApp(MDApp):
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('date.kv')
#
#     def on_save(self, instance, value, date_range):
#         print(instance, value, date_range)
#
#         # self.root.ids.date_label.text = f'{value}'
#         self.root.ids.date_label.text = f'{date_range[0]} to {date_range[-1]}'
#
#
#     def on_cancel(self,instance, value):
#
#         self.root.ids.date_label.text = f'You clicked cancel'
#         print(f'{instance}, {value}')
#
#
#
#     def show_date_picker(self):
#         # date_dialog = MDDatePicker()
#         date_dialog = MDDatePicker(mode='range')
#         date_dialog.bind(on_save= self.on_save, on_cancel=self.on_cancel)
#         date_dialog.open()
#
#
#
# MainApp().run()

## Time picker

# class MainApp(MDApp):
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Light'
#         self.theme_cls.primary_palette = 'BlueGray'
#         return Builder.load_file('time.kv')
#
#     def get_time(self, instance, time):
#         self.root.ids.time_label.text = f'{time}'
#
#     def on_cancel(self, instance, time):
#         self.root.ids.time_label.text = f'You clicked cancel'
#
#     def show_time_picker(self):
#         from datetime import datetime
#
#         default_time = datetime.strptime('4:20:00', '%H:%M:%S').time()
#         time_dialog = MDTimePicker()
#
#         #set defaul time
#         time_dialog.set_time(default_time)
#
#         time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
#         time_dialog.open()
#
#
# MainApp().run()


#Data Table

#
# class MainApp(MDApp):
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Light'
#         self.theme_cls.primary_palette = 'BlueGray'
#         # return Builder.load_file('time.kv')
#
#         screen = Screen()
#
#         table = MDDataTable(
#
#             pos_hint={'center_x': 0.5, 'center_y': 0.5},
#             size_hint=(0.9, 0.6),
#             check=True,
#             use_pagination=True,
#             rows_num= 5,
#             pagination_menu_height='240dp',
#
#             column_data=[
#                 ('First Name', dp(40)),
#                 ('Last Name', dp(30)),
#                 ('Email adress', dp(50)),
#                 ('Phone number', dp(30))
#
#             ],
#             row_data=[
#                 ('Patrick', 'Asumani', 'patassumani@gmail.com', '+7(981)-799-31-00'),
#                 ('Yulia', 'Asumani', 'Yusik@mail.ru', '+7(981)-799-31-00'),
#                 ('Gabriela', 'Asumani', 'gaby@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00'),
#                 ('Adelina', 'Asumani', 'ade@mail.ru', '+7(981)-799-31-00'),
#                 ('Anna', 'Asumani', 'An@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00'),
#                 ('Patrick', 'Asumani', 'patassumani@gmail.com', '+7(981)-799-31-00'),
#                 ('Yulia', 'Asumani', 'Yusik@mail.ru', '+7(981)-799-31-00'),
#                 ('Gabriela', 'Asumani', 'gaby@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00'),
#                 ('Patrick', 'Asumani', 'patassumani@gmail.com', '+7(981)-799-31-00'),
#                 ('Adelina', 'Asumani', 'ade@mail.ru', '+7(981)-799-31-00'),
#                 ('Anna', 'Asumani', 'An@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00'),
#                 ('Patrick', 'Asumani', 'patassumani@gmail.com', '+7(981)-799-31-00'),
#                 ('Yulia', 'Asumani', 'Yusik@mail.ru', '+7(981)-799-31-00'),
#                 ('Gabriela', 'Asumani', 'gaby@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00'),
#                 ('Patrick', 'Asumani', 'patassumani@gmail.com', '+7(981)-799-31-00'),
#                 ('Adelina', 'Asumani', 'ade@mail.ru', '+7(981)-799-31-00'),
#                 ('Anna', 'Asumani', 'An@gmail.com', '+7(981)-799-31-00'),
#                 ('Richard', 'Asumani', 'richy@gmail.com', '+7(981)-799-31-00')
#             ]
#         )
#
#         table.bind(on_check_press=self.checked)
#         table.bind(on_row_press= self.row_checked)
#
#         screen.add_widget(table)
#
#         return screen
#
#     def checked(self, instance_table, current_row):
#         print(instance_table, current_row)
#     def row_checked(self, instance_table, current_row):
#
#         print(instance_table, current_row)
#
#
# MainApp().run()


#Using sqLite3 database

#
# class MainApp(MDApp):
#
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#
#         #create a database or connect to one
#
#         conn = sqlite3.connect('first_db.db')
#
#
#         #create a Cursor
#
#         c = conn.cursor()
#
#         #create A table
#
#         c.execute('''CREATE TABLE if not exists customers(name text)''')
#
#         #Commit our change
#
#         conn.commit()
#
#         #Close our connection
#
#         conn.close()
#
#
#
#         return Builder.load_file('first_db.kv')
#
#     def submit(self):
#
#         conn = sqlite3.connect('first_db.db')
#         c = conn.cursor()
#         #Add a record
#         c.execute('INSERT INTO customers VALUEs (:first)', {
#             'first':self.root.ids.word_input.text,
#         })
#
#         #Add a message to label
#
#         self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added'
#
#         #clear input box
#
#         self.root.ids.word_input.text = ''
#
#         conn.commit()
#         conn.close()
#
#     def show_records(self):
#         conn = sqlite3.connect('first_db.db')
#         c = conn.cursor()
#         # Grab records from database
#         c.execute('SELECT * FROM customers')
#         records = c.fetchall()
#
#         word = ''
#
#         for record in records:
#             word = f'{word}\n {record[0]}'
#             self.root.ids.word_label.text = f'{word}'
#
#         conn.commit()
#         conn.close()
#
#
# MainApp().run()



# Using MySQL database

#
# class MainApp(MDApp):
#
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#
#         #create a database or connect to one
#
#         #define a DB stuff
#
#         mydb = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='patrickmoon',
#             database='second_db',
#
#         )
#
#
#         #create a Cursor
#
#         c = mydb.cursor()
#
#         # create an actual database
#
#         c.execute('CREATE DATABASE IF NOT EXISTS second_db')
#
#         #check to see if db was created
#
#         # c.execute('SHOW DATABASES')
#         #
#         # for db in c:
#         #     print(db)
#
#
#         #create A table
#
#         c.execute('''CREATE TABLE if not exists customers(name VARCHAR(50))''')
#
#         #check to see if table created
#
#         # c.execute('SELECT * FROM customers')
#         # print(c.description)
#         #
#
#
#         # #Commit our change
#         #
#         mydb.commit()
#         #
#         # #Close our connection
#         #
#         mydb.close()
#
#
#
#         return Builder.load_file('first_db.kv')
#
#
#     def submit(self):
#
#         mydb = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='patrickmoon',
#             database='second_db',
#
#         )
#
#         # create a Cursor
#
#         c = mydb.cursor()
#
#         #Add a record
#
#         sql_command = 'INSERT INTO customers (name) VALUES(%s) '
#         values = (self.root.ids.word_input.text,)
#
#         #execute SQL command
#
#         c.execute(sql_command, values)
#
#         #Add a message to label
#
#         self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added'
#
#         #clear input box
#
#         self.root.ids.word_input.text = ''
#
#         mydb.commit()
#         mydb.close()
#
#     def show_records(self):
#         mydb = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='patrickmoon',
#             database='second_db',
#
#         )
#
#         # create a Cursor
#
#         c = mydb.cursor()
#
#         # Grab records from database
#         c.execute('SELECT * FROM customers')
#         records = c.fetchall()
#
#         word = ''
#
#         for record in records:
#             word = f'{word}\n {record[0]}'
#             self.root.ids.word_label.text = f'{word}'
#
#         mydb.commit()
#         mydb.close()
#
#
# MainApp().run()


#
# #Add matplotlib Graph
#
#
# # Define what we want to graph
#
# x = [1, 2, 3, 4, 5]
#
# y = [5, 12, 6, 9, 15]
#
# plt.plot(x, y)
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
#
#
# class Matty(FloatLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#         box = self.ids.box
#         box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
#
#
#     def save_it(self):
#
#         name = self.ids.namer.text
#         if name:
#             plt.savefig(name)
#
#
# class MainApp(MDApp):
#
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         Builder.load_file('matty.kv')
#
#         return Matty()
#
# MainApp().run()


#Add a map to kivy


# class MapViewApp(MDApp):
#
#     def build(self):
#         # self.theme_cls.theme_style = 'Dark'
#         # self.theme_cls.primary_palette = 'BlueGray'
#         mapview = MapView(zoom=10, lat=36 , lon=115 )
#
#         return mapview
#
# MapViewApp().run()




# class MainApp(MDApp):
#
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#
#         return Builder.load_file('map.kv')
#
# MainApp().run()




# Using python code on a KV


#
# class MainApp(MDApp):
#     str = 'Hello world!'
#     lst = ['Patrick', 'Yulia', 'Gaby']
#
#     def build(self):
#
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#
#         return Builder.load_file('code.kv')
#
# MainApp().run()



# Add Keybord with Vkeybord


# class MainApp(MDApp):
#
#     def build(self):
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'BlueGray'
#         self.label = Label(text='Type something!', font_size=32)
#
#         #define our layout
#
#         layout = GridLayout(cols=1)
#
#         #define our vkeyboard
#         keyboard = VKeyboard(on_key_up=self.key_up)
#
#         layout.add_widget(self.label)
#         layout.add_widget(keyboard)
#
#
#         return layout
#
#
#     def key_up(self, keyboard, keycode, *args):
#
#         if isinstance(keycode, tuple):
#             print(keycode)
#             keycode = keycode[1]
#         # Tracking what was already in the label
#         str = self.label.text
#
#         #Run some logic
#         if str == 'Type something!':
#             str = ''
#         #backspace
#         if keycode == 'backspace':
#             str = str[:-1]
#             keycode = ''
#         #spacebar
#         if keycode == 'spacebar':
#             keycode = '  '
#
#
#         self.label.text = f'{str}{keycode}'
#
#
# MainApp().run()


#List with kivymd


class MainApp(MDApp):

    title = 'Simple list'

    def build(self):

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'

        return Builder.load_file('lists.kv')

    def presser(self, pressed, list_id):
        pressed.secondary_text = f'You pressed {list_id}'
        pressed.tertiary_text = f'Yes !! You pressed {list_id}'

MainApp().run()

