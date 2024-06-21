import kivy.app
from kivy.app import App
from kivy.config import Config
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
from kivy.graphics import Color, Ellipse, Line, Bezier, Rectangle
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from random import random
import winsound
import webbrowser


#1

# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '700')
# Config.set('graphics', 'resizable', '0')
#
#
# class FirstApp(App):
#     def build(self):
#         return Button(text='Button_1', italic=True, bold= True, font_size= 40, color=[0, 0, 0.75, 1],
#                       background_color=[0.9, 0.6, 0, 1], background_normal='', size_hint_x=0.48,
#                       size_hint_y=0.15, x=104, y=297.5, on_press=self.press_button)
#
#     def press_button(self, instance):
#         instance.text = ':)'
#         instance.background_color = [1, 0, 0, 1]
#
#
#
# if __name__ == '__main__':
#     FirstApp().run()




#2

# Config.set('graphics', 'width', '300')
# Config.set('graphics', 'height', '650')
# Config.set('graphics', 'resizable', '0')
#
# class SgApp(App):
#     def build(self):
#         return Button(text='Hello', bold=True, font_size=20, color=[0.5, 1, 0.5, 1],
#                       background_color=[0.8, 0.5, 1, 1], background_normal='', size_hint=(None, None),
#                       size=(200, 70), pos=(70, 275), on_press=self.press_me)
#
#     def press_me(self, instance):
#         instance.text = 'My first app :-) '
#         instance.color = [0, 0, 0.5, 1]
#         instance.underline = True
#
# if __name__ == '__main__':
#     SgApp().run()

#3

# class FirstApp(App):
#     def build(self):
#         main_layout = FloatLayout(size_hint=(0.5, 0.5))
#         button_one = Button(text='Button', italic= True, bold=True, font_size=40
#                             ,color=[0, 0, 0.75, 1], background_color=[0.9, 0.6, 0, 1],
#                             background_normal='', size_hint_x=0.48, size_hint_y=0.15, x=0, y=250,
#                             on_press=self.press_button)
#         button_two = Button(text='Button_2', italic=True, bold=True, font_size=40
#                             , color=[0, 0, 0.75, 1], background_color=[0.9, 0.6, 0, 1],
#                             background_normal='', size_hint_x=0.48, size_hint_y=0.15, x=420, y=250,
#                             on_press=self.press_button_2)
#         main_layout.add_widget(button_one)
#         main_layout.add_widget(button_two)
#         return main_layout
#     def press_button(self, instance):
#         instance.text = ':)'
#         instance.background_color = [1, 0, 0, 1]
#
#     def press_button_2(self, instance):
#         instance.text = ':('
#         instance.background_color = [1, 1, 0, 1]
#
# if __name__ == '__main__':
#     FirstApp().run()


#4

# class FirstApp(App):
#     def build(self):
#         main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
#         self.solution = Label(font_size=60)
#         main_layout.add_widget(self.solution)
#
#         buttons = [['-', '+'], ['50 Hz', '100 Hz', '500 Hz', '1000 Hz'],
#                   ['START']]
#         for lay in buttons:
#             vr = BoxLayout()
#             for name in lay:
#                 button = Button(text=name, pos_hint={'center_x': 0.5, 'center_y': 0.5},
#                                 background_color=[0.9, 0.9, 0, 1], font_size=45)
#                 if name == 'START':
#                     button.bind(on_press=self.start_solution)
#                 else:
#                     button.bind(on_press=self.on_solution)
#                 vr.add_widget(button)
#             main_layout.add_widget(vr)
#         self.solution.text = '50 Hz'
#         return main_layout

#     def on_solution(self, instance):
#         if instance.text == '50 Hz':
#             self.solution.text = '50 Hz'
#         elif instance.text == '100 Hz':
#             self.solution.text = '100 Hz'
#         elif instance.text == '500 Hz':
#             self.solution.text = '500 Hz'
#         elif instance.text == '1000 Hz':
#             self.solution.text = '1000 Hz'
#         elif instance.text == '+':
#             try:
#                 if self.solution.text != 'Error : Incorrect frequency':
#                     self.solution.text = str(int(self.solution.text.split()[0]) + 1) + ' ' + 'Hz'
#                 else:
#                     self.solution.text = '1' + ' ' + 'Hz'
#             except:
#                 self.solution.text = '50 Hz'
#         elif instance.text == '-':
#             try:
#                 if self.solution.text != 'Error : Incorrect frequency':
#                     self.solution.text = str(int(self.solution.text.split()[0]) - 1) + ' ' + 'Hz'
#             except:
#                 self.solution.text = '50 Hz'
#         if self.solution.text != 'Error: Incorrect frequency':
#             if int(self.solution.text.split()[0]) <= 0:
#                 self.solution.text = 'Error: Incorrect frequency'
#     def start_solution(self, instance):
#         if self.solution.text and self.solution.text != 'Error: Incorrect frequency':
#             try:
#                 winsound.Beep(int(self.solution.text.split()[0]), 500)
#
#             except:
#                 self.solution.text = 'Error: Incorrect frequency'
#         else:
#             self.solution.text = 'Error: Incorrect frequency'
#
#
# if __name__ == '__main__':
#     FirstApp().run()

#5
#
# class FirstApp(App):
#
#     def build(self):
#         main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
#         self.display = Label(font_size=60)
#         self.display.text = 'Waiting for press !!'
#         btn1 = Button(text='1', pos_hint={'center_x': 0.5, 'center_y': 0.5},
#                                  background_color=[0.9, 0.9, 0, 1], font_size=40)  #on_press= self.print_1)
#         btn2 = Button(text='2', pos_hint={'center_x': 0.5, 'center_y': 0.5},
#                                  background_color=[0.9, 0.9, 0, 1], font_size=40)  #on_press= self.print_2)
#         btn1.bind(on_press=self.print_1)
#         btn2.bind(on_press=self.print_2)
#         main_layout.add_widget(self.display)
#         main_layout.add_widget(btn1)
#         main_layout.add_widget(btn2)
#
#         return main_layout
#
#     def print_1(self, instance):
#         if instance.text == '1':
#             self.display.text = 'Pressing 1'
#     def print_2(self, instance):
#         if instance.text == '2':
#             self.display.text = 'Pressing 2'
# if __name__ == '__main__':
#     FirstApp().run()

#6


# class MainApp(App):
#     def build(self):
#         self.button_color = []
#         main_layout = GridLayout(cols=30, rows=31)
#         for i in range(30):
#             r, g, b = random(), random(), random()
#             print(r, g, b)
#             button = Button(text='color', background_color=[r, g, b, 1])
#             button.bind(on_press=self.on_color)
#             main_layout.add_widget(button)
#
#         for j in range(30):
#             for k in range(30):
#                 button = Button()
#                 button.bind(on_press=self.on_solution)
#                 main_layout.add_widget(button)
#
#         return main_layout
#
#     def on_solution(self, instance):
#         instance.background_color = self.button_color
#
#     def on_color(self, instance):
#         self.button_color = instance.background_color
#
#
# if __name__ == '__main__':
#     MainApp().run()



# class FirstApp(App):
#     def build(self):
#         layout = GridLayout(cols=2)
#         layout.add_widget(Button(text='Button 1', width=20))
#         layout.add_widget(Button(text='Button 2'))
#         layout.add_widget(Button(text='Button 3', width=20))
#         layout.add_widget(Button(text='Button 4'))
#         return layout
#
# if __name__ == "__main__":
#     FirstApp().run()


# class MainApp(App):
#     def build(self):
#         layout = GridLayout(rows=12)
#         for i in range(1, 51):
#             button = Button(text=str(i))
#             layout.add_widget(button)
#         return layout
#
# if __name__ == "__main__":
#     MainApp().run()


#7
#
# class FirstApp(App):
#     def build(self):
#         main_layout = PageLayout()
#         fl = FloatLayout()
#         fl.add_widget(Button(text='Page 1', size_hint=(None, None), size=(100, 100)))
#         main_layout.add_widget(fl)
#
#         box_one = BoxLayout(orientation='vertical')
#         box_one.add_widget(Button(text='button_1', background_color=[1, 1, 0, 1]))
#
#         box_two = BoxLayout()
#         box_two.add_widget(Button(text='button_2', background_color=[0, 1, 0, 1]))
#
#         box_two.add_widget(Button(text='button_3', background_color=[0, 0, 1, 1]))
#         box_one.add_widget(box_two)
#         main_layout.add_widget(box_one)
#         main_layout.add_widget(Button(text='Page 3', size_hint=(0.9, 0.9)))
#
#
#         return main_layout
#
# if __name__ == '__main__':
#     FirstApp().run()


#
# class FisrtApp(App):
#     def build(self):
#         main_layout = PageLayout()
#         st = StackLayout()
#         st1 = StackLayout()
#         fl = FloatLayout()
#         gd = GridLayout(cols=4)
#         for i in range(4):
#             btn = Button(text='button_1', background_color=[1, 1, 0, 1], size_hint=(None, None),
#                          size=(200, 100))
#             gd.add_widget(btn)
#         lb = Label(font_size=60)
#         lb.text = 'Display here'
#         st.add_widget(Button(text='btn_1', size_hint=(0.2, 0.1)))
#         st.add_widget(Button(text='btn_2', size_hint=(0.2, 0.1)))
#         st.add_widget(Button(text='btn_3      <pull bar>', size_hint=(0.5, 0.1)))
#         st.add_widget(gd)
#         st.add_widget(fl)
#         st1.add_widget(Button(text='btn_4', size_hint=(0.2, 0.1)))
#         st1.add_widget(Button(text='btn_5', size_hint=(0.2, 0.1)))
#         st1.add_widget(Button(text='btn_6', size_hint=(0.5, 0.1)))
#         fl.add_widget(lb)
#         main_layout.add_widget(st)
#         main_layout.add_widget(st1)
#
#         return main_layout
#
# if __name__ == '__main__':
#     FisrtApp().run()
#

#8
# s = []
# s = ['1000', '700', '1000', '700', '1000', '900', '900', '20000', '900', '600', '900', '600',
#      '900', '1000', '1000', '20000', '1000', '700', '1000', '700', '1000', '900', '900', '20000', '900',
#      '600', '900', '600', '900', '1000']
# class MainApp(App):
#     def build(self):
#         main_layout = FloatLayout()
#
#         box_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.5),
#                                pos_hint={'x': 0, 'y': 0.5})
#
#         restart_button = Button(text='Restart sound track', background_color=[1, 0, 1, 1], italic=True,
#                                 bold=True, font_size=30)
#
#         restart_button.bind(on_press=self.restart_solution)
#         box_layout.add_widget(restart_button)
#
#         start_button = Button(text='start', background_color=[1, 1, 0, 1], italic=True,
#                                 bold=True, font_size=30)
#
#         start_button.bind(on_press=self.start_solution)
#         box_layout.add_widget(start_button)
#         main_layout.add_widget(box_layout)
#
#         grid_layout = GridLayout(rows=1, size_hint=(1, 0.5))
#         buttons = ['90', '100', '110', '120', '130', '200', '300', '400', '500', '600', '700',
#                    '800', '900', '1000', '25000']
#
#         color_switch = 0
#         for i in buttons:
#             if color_switch == 0:
#                 color = [0, 0.5, 0.5, 1]
#                 color_switch = 1
#             else:
#                 color = [0.1, 0.5, 0.8, 1]
#                 color_switch = 0
#
#             button = Button(text=str(i), background_color=color, italic=True, font_size=15)
#             button.bind(on_press=self.sound_solution)
#             grid_layout.add_widget(button)
#
#         main_layout.add_widget(grid_layout)
#
#         return main_layout
#
#     def restart_solution(self, instance):
#         global s
#         # s = []
#         s = ['1000', '700', '1000', '700', '1000', '900', '900', '20000', '900', '600', '900', '600',
#              '900', '1000', '1000', '20000', '1000', '700', '1000', '700', '1000', '900', '900', '20000', '900',
#              '600', '900', '600', '900', '1000']
#     def start_solution(self, instance):
#         for i in s:
#             winsound.Beep(int(i), 300)
#
#     def sound_solution(self, instance):
#         winsound.Beep(int(instance.text), 300)
#         s.append(instance.text)
# if __name__ == '__main__':
#     MainApp().run()


#9
#
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.screenmanager import ScreenManager, Screen
#
# class FirstScreen(Screen):
#     def __init__(self, **kwargs):
#         super(FirstScreen, self).__init__(**kwargs)
#         layout = BoxLayout()
#         button = Button(text='Go to Second Screen')
#         button.bind(on_press=self.go_to_second_screen)
#         layout.add_widget(button)
#         self.add_widget(layout)
#
#     def go_to_second_screen(self, instance):
#         self.manager.current = 'second'
#
# class SecondScreen(Screen):
#     def __init__(self, **kwargs):
#         super(SecondScreen, self).__init__(**kwargs)
#         layout = BoxLayout()
#         button = Button(text='Go to First Screen')
#         button.bind(on_press=self.go_to_first_screen)
#         layout.add_widget(button)
#         self.add_widget(layout)
#
#     def go_to_first_screen(self, instance):
#         self.manager.current = 'first'
#
# class MyApp(App):
#     def build(self):
#         screen_manager = ScreenManager()
#         first_screen = FirstScreen(name='first')
#         second_screen = SecondScreen(name='second')
#         screen_manager.add_widget(first_screen)
#         screen_manager.add_widget(second_screen)
#         return screen_manager
#
# if __name__ == '__main__':
#     MyApp().run()


# from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

#
# class MyApp(App):
#     def build(self):
#         main_layout = PageLayout(border=0)
#
#         button1 = Button(text='Go to Second Screen', on_press=self.do_page)
#         main_layout.add_widget(button1)
#
#         button2 = Button(text='Go to First Screen', on_press=self.do_page)
#         main_layout.add_widget(button2)
#
#         self.finish = main_layout
#
#         return main_layout
#
#     def do_page(self, instance: Button):
#         self.finish.page = 1 if instance.text == 'Go to Second Screen' else 0

# if __name__ == '__main__':
#     MyApp().run()


# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.button import Button
#
# class FirstApp(App):
#     def build(self):
#         main_layout = BoxLayout()
#         main_layout.add_widget(FloatLayout())
#         main_layout.add_widget(StackLayout())
#         main_layout.add_widget(Button())
#         return main_layout
#
# if __name__ == "__main__":
#     FirstApp().run()


# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.button import Button
#
# class FirstApp(App):
#     def build(self):
#         main_layout = FloatLayout()
#         main_layout.add_widget(BoxLayout())
#         main_layout.add_widget(StackLayout())
#         main_layout.add_widget(Button())
#         return main_layout
#
# if __name__ == "__main__":
#     FirstApp().run()


#10
#
# class MyApp(App):
#     def build(self):
#         tb = TabbedPanel(do_default_tab=True, tab_pos='top_left', default_tab_text='SRART MENU')
#         gl = GridLayout(rows=1)
#         gl.add_widget(Button(size_hint=(0.2, 0.1), text='Default_tab button1'))
#         gl.add_widget(Button(size_hint=(0.2, 0.1), text='Default_tab button2'))
#         gl.add_widget(Button(size_hint=(0.2, 0.1), text='Default_tab button3'))
#         tb.default_tab_content = gl
#
#         tbi = TabbedPanelItem(text='1', background_color=[1, 0, 0, 1])
#         tbi.add_widget(Label(text='I am label'))
#         tb.add_widget(tbi)
#
#         tbi2 = TabbedPanelItem(text='2')
#         bl = BoxLayout()
#         bl.add_widget(Button(text='btn 1'))
#         bl.add_widget(Button(text='btn 2'))
#         tbi2.add_widget(bl)
#         tb.add_widget(tbi2)
#
#         tbi = TabbedPanelItem(text='3')
#         tbi.add_widget(Button(size_hint=(0.2, 0.1), text='btn 3'))
#         tb.add_widget(tbi)
#
#         return tb
#
# if __name__ == '__main__':
#     MyApp().run()

# 11
#
# class MyApp(App):
#     def build(self):
#         lbl = Label(text='Hello\nLabel', font_size=70, color=[0.8, 0.3, 0, 1], halign='center',
#                     underline=True, strikethrough=True)
#         return lbl
#
# if __name__ == '__main__':
#     MyApp().run()


# class FsApp(App):
#     def build(self):
#         LabelBase.register(name='Custom_name', fn_regular='Radiotechnika_0.ttf')
#         title = Label(text="New Font!", font_name="Custom_name", font_size=50)
#         return title
#
# if __name__ == '__main__':
#     FsApp().run()

# class MyApp(App):
#     def build(self):
#         lbl = Label(text='For new page press [ref=][i][u]here[/u][/i][/ref]',
#                     font_size=30,
#                     color=[0.8, 0.3, 0, 1], markup=True)
#         lbl.bind(on_ref_press=self.link)
#         return lbl
#
#     def link(self, instance, value):
#         webbrowser.open('https://www.youtube.com/watch')
#
# if __name__ == '__main__':
#     MyApp().run()

#
# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         lbl = Label(text='0', font_size=70, size_hint=(1, 0.2))
#         main_layout.add_widget(lbl)
#
#         button1 = Button(text='+',font_size=30,  size_hint=(1, 0.2))
#         def add(instance):
#             lbl.text = str(int(lbl.text) + 1)
#         button1.bind(on_press=add)
#         main_layout.add_widget(button1)
#
#         button2 = Button(text='-',font_size=30, size_hint=(1, 0.2))
#         def sub(instance):
#             lbl.text = str(int(lbl.text) - 1)
#         button2.bind(on_press=sub)
#         main_layout.add_widget(button2)
#
#         button3 = Button(text='0',font_size=30, size_hint=(1, 0.2))
#         def zero(instance):
#             lbl.text += '0'
#         button3.bind(on_press=zero)
#         main_layout.add_widget(button3)
#
#         button4 = Button(text='Initialized',font_size=30, size_hint=(1, 0.2))
#         def init(instance):
#             lbl.text = '0'
#         button4.bind(on_press=init)
#         main_layout.add_widget(button4)
#
#         return main_layout
# if __name__ == '__main__':
#     MyApp().run()


# from kivy.app import App
# from kivy.uix.label import Label
#
# class MyApp(App):
#     def build(self):
#         lbl = Label(text="[s]Hello[/s]", markup=True)
#         return lbl
#
# if __name__ == "__main__":
#     MyApp().run()

#
# from kivy.app import App
# from kivy.uix.label import Label
#
# class MyApp(App):
#     def build(self):
#         lbl = Label(text='Hello World!', font_size=100)
#         return lbl
#
# if __name__ == "__main__":
#     MyApp().run()

#12
#
# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         lbl = Label(text='ON', size_hint=(0.2, 0.1))
#         main_layout.add_widget(lbl)
#         switch = Switch(size_hint=(0.2, 0.1), active=True)
#
#         def on_active(instance, value):
#             if value:
#                 lbl.text = 'ON'
#             else:
#                 lbl.text = 'OFF'
#
#         switch.bind(active=on_active)
#         main_layout.add_widget(switch)
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         tgbutton1 = ToggleButton(text='btn flag 1', size_hint=(0.2, 0.1), group='test')
#         tgbutton2 = ToggleButton(text='btn flag 2', size_hint=(0.2, 0.1), group='test')
#         tgbutton3 = ToggleButton(text='btn flag 3', size_hint=(0.2, 0.1), group='test')
#         main_layout.add_widget(tgbutton1)
#         main_layout.add_widget(tgbutton2)
#         main_layout.add_widget(tgbutton3)
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyApp().run()

# class MyApp(App):
#     def build(self):
#         sw = Switch()
#         def state(self, value):
#             print(value)
#         sw.bind(active=state)
#         return sw
#
# if __name__ == "__main__":
#     MyApp().run()



#13


# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         checkbox1 = CheckBox(size_hint=(0.1, 0.1), group="group1", active=[1, 2, 3])
#         label1 = Label(text=checkbox1.state, size_hint=(0.1, 0.1))
#         def checkbox1_solution(instance, value):
#             if value:
#                 label1.text="on"
#             else:
#                 label1.text = "off"
#         checkbox1.bind(active=checkbox1_solution)
#         main_layout.add_widget(checkbox1)
#         main_layout.add_widget(label1)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()




# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         progressbar = ProgressBar(max=100, value=0, size_hint=(1, 0.2))
#         main_layout.add_widget(progressbar)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         progressbar = ProgressBar(max=100, value=0, size_hint=(1, 0.2))
#         main_layout.add_widget(progressbar)
#         lbl = Label(text=str(int(progressbar.value)), size_hint=(1, 0.2))
#         main_layout.add_widget(lbl)
#         button = Button(text="+", size_hint=(1, 0.2))
#
#         def button_press(instanse):
#             progressbar.value += 1
#             lbl.text = str(int(progressbar.value))
#
#         button.bind(on_press=button_press)
#         main_layout.add_widget(button)
#
#         return main_layout
#
#
# if __name__ == "__main__":
#     MyApp().run()

# from kivy.app import App
# from kivy.uix.progressbar import ProgressBar
#
# class MyApp(App):
#     def build(self):
#         pbar = ProgressBar(min=0, max=100, value=50)
#         return pbar
#
# if __name__ == "__main__":
#     MyApp().run()

#14
#
# class MyApp(App):
#     def build(self):
#         spinner = Spinner(text='Menu', values=('Menu 1', 'Menu 2', 'Menu 3', 'Menu 4', 'Menu 5'),
#                           size_hint=(0.2, 0.1), pos=(0, 540))
#
#
#         return spinner
#
#
# if __name__ == "__main__":
#     MyApp().run()

# class AccordionApp(App):
#     def build(self):
#         main_layout = Accordion(orientation='vertical')
#
#         item = AccordionItem(title= 'First toggle')
#         bl = BoxLayout(orientation='vertical')
#         lb = Label(text='My content')
#         btn1 = Button(text='button 1', size_hint=(0.2, 0.1))
#         btn2 = Button(text='button 2', size_hint=(0.2, 0.1))
#         lst = [lb, btn1, btn2]
#         for el in lst:
#             bl.add_widget(el)
#         item.add_widget(bl)
#         main_layout.add_widget(item)
#
#         item2 = AccordionItem(title='Second toogle')
#         item2.add_widget(Label(text='My seg content'))
#         main_layout.add_widget(item2)
#
#         return main_layout
#
# if __name__ == '__main__':
#     AccordionApp().run()


#15

# class MyApp(App):
#     def build(self):
#         main_layout = ScreenManager()
#
#         screen_1 = Screen(name='Screen 1')
#         screen_2 = Screen(name='Screen 2')
#         for el in (screen_1, screen_2):
#             main_layout.add_widget(el)
#
#         main_layout.current = 'Screen 2'
#
#         return main_layout
# if __name__ == '__main__':
#     MyApp().run()
#
# class MyApp(App):
#     def build(self):
#         main_layout = ScreenManager()
#
#         screen1 = Screen(name="screen_1")
#         button1 = Button(text='Go to Screen 2', size_hint=(0.3, 0.3), pos=(250, 250))
#         def go_seg_page(instance):
#             main_layout.current = 'screen_2'
#         button1.bind(on_press=go_seg_page)
#         screen1.add_widget(button1)
#         main_layout.add_widget(screen1)
#
#         screen2 = Screen(name="screen_2")
#         button2 = Button(text='Go to Screen 1', size_hint=(0.3, 0.3), pos=(250, 250),
#                          background_color=[1, 0, 0, 1])
#
#         def go_frst_page(instance):
#             main_layout.current = 'screen_1'
#
#         button2.bind(on_press=go_frst_page)
#         def screen_action(instance):
#             button2.text = 'Changing button label'
#             button2.background_color = (1, 0, 1, 1)
#         screen2.bind(on_enter= screen_action)
#         screen2.add_widget(button2)
#         main_layout.add_widget(screen2)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         main_layout = ScreenManager(transition=SlideTransition(duration=2))
#         screen1 = Screen(name="screen_1")
#         screen1.add_widget(Button(text="screen_1"))
#         main_layout.add_widget(screen1)
#         screen2 = Screen(name="screen_2")
#         screen2.add_widget(Button(text="screen_2"))
#         main_layout.add_widget(screen2)
#         main_layout.current = "screen_2"
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()

#16


# class CarouselApp(App):
#     def build(self):
#         carousel = Carousel(direction='right', anim_cancel_duration=0.3, min_move=0,
#                             anim_move_duration=0.3, anim_type='in_circ', ignore_perpendicular_swipes= False,
#                             loop=True)
#         carousel.add_widget(Button(text='button 1', size_hint=(0.5, 0.5)))
#         carousel.add_widget(Button(text='button 2', size_hint=(0.2, 0.2)))
#
#         return carousel
#
# if __name__ == '__main__':
#     CarouselApp().run()


# class MyApp(App):
#     def build(self):
#         main_layout = TextInput(text="Input here:",
#                                 multiline=False, background_color=(1, 0.2, 0.3, 1),
#                                 readonly=False,
#                                 halign="center",
#                                 font_size=60,
#  padding=100,
#                                 size_hint=(1, 0.5))
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()

#17


# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout()
#         slider = Slider(size_hint= (0.5, 0.1))
#
#         lbl = Label(text=str(int(slider.value)), size_hint=(0.2, 0.1), font_size=40, bold=True)
#         main_layout.add_widget(lbl)
#
#         def on_value(instance, value):
#             lbl.text = str(int(value))
#
#         slider.bind(value=on_value)
#         main_layout.add_widget(slider)
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyApp().run()

#
# class MyApp(App):
#     def build(self):
#         main_layout = StackLayout(orientation="tb-lr")
#         slider1 = Slider(size_hint=(0.5, 0.1), min=0, max=255, value=255, value_track=True,
#                          value_track_color=[0, 0.7, 0, 1])
#         slider2 = Slider(size_hint=(0.5, 0.1), min=0, max=255, value=255, value_track=True,
#                          value_track_color=[0, 0.7, 0, 1])
#         slider3 = Slider(size_hint=(0.5, 0.1), min=0, max=255, value=255, value_track=True,
#                          value_track_color=[0, 0.7, 0, 1])
#         slider4 = Slider(size_hint=(0.5, 0.1), min=0, max=100, value=100, value_track=True,
#                          value_track_color=[0, 0.7, 0, 1])
#         button = Button(background_normal="")
#         lbl = Label(text=f"{str(int(slider1.value))} : {str(int(slider2.value))} : {str(int(slider3.value))} / {100}%",
#                     size_hint=(0.5, 0.1), font_size=30, bold=True)
#
#         def on_value(instance, value):
#             button.background_color = [int(slider1.value) / 255, int(slider2.value) / 255, int(slider3.value) / 255,
#                                        int(slider4.value) / 100]
#             lbl.text = f"{str(int(slider1.value))} : {str(int(slider2.value))} : {str(int(slider3.value))} / {str(int(slider4.value))}%"
#
#         slider1.bind(value=on_value)
#         slider2.bind(value=on_value)
#         slider3.bind(value=on_value)
#         slider4.bind(value=on_value)
#
#         main_layout.add_widget(slider1)
#         main_layout.add_widget(slider2)
#         main_layout.add_widget(slider3)
#         main_layout.add_widget(slider4)
#         main_layout.add_widget(lbl)
#         main_layout.add_widget(button)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         slider = Slider()
#         return slider
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         slider = Slider(min=0,
#                         max=100,
#                         step=1,
#                         value=75,
#                         orientation='vertical')
#         return slider
#
# if __name__ == "__main__":
#     MyApp().run()


#no good(_vertical='orientation')

# class MyApp(App):
#     def build(self):
#         slider = Slider(min=0,
#                         max=100,
#                         step=1,
#                         value=75,
#                         vertical="orientation")
#         return slider
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         slider = Slider(size_hint=(0.5, 0.5),
#                         step=1,
#                         value=75,
#                         orientation="vertical")
#         return slider
#
# if __name__ == "__main__":
#     MyApp().run()


#18

# class ScatterLayoutApp(App):
#     def build(self):
#         ml = BoxLayout()
#         ml.add_widget(Button(text="Button"))
#         scatter_layout = Scatter()
#         scatter_layout.add_widget(Button(text="Button",
#                                          size_hint=(0.25, 0.25)))
#         ml.add_widget(scatter_layout)
#         return ml
#
# if __name__ == '__main__':
#     ScatterLayoutApp().run()


#19
#
# class MyApp(App):
#     def build(self):
#         main_layout = ActionBar(pos=(0, 560))
#         actionview = ActionView()
#         check = ActionCheck(size_hint=(0.1, 1))
#         sep = ActionSeparator()
#         group = ActionGroup(text='Group', dropdown_width=100)
#         for i in range(10):
#             group.add_widget(ActionButton(text=str(f'button-{i}')))
#         actionview.add_widget(check)
#         actionview.add_widget(sep)
#         actionview.add_widget(group)
#         main_layout.add_widget(actionview)
#
#         actionview.add_widget(ActionPrevious(app_icon='E:/G/butterfly_338337.PNG'))
#         actionview.add_widget(ActionButton(text='btn'))
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         main_layout = ActionBar()
#         actionview = ActionView()
#         # actionprev = ActionPrevious()
#         actionview.add_widget(ActionCheck())
#         # actionview.add_widget(actionprev)
#         main_layout.add_widget(actionview)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()

from kivy.lang import Builder
# class TestApp(kivy.app.App):
#     pass
#
# app = TestApp()
# app.run()

#20
# class MyApp(App):
#     def build(self):
#         fl = FloatLayout()
#         label = Label(text='No information')
#         button = Button(text='Show information', size_hint=(1, 0.1))
#         main_layout = TreeView(root_options=dict(text='Cars catalog'), pos=(200, 0))
#         level_1 = main_layout.add_node(TreeViewLabel(text='BMW'))
#         line1 = main_layout.add_node(TreeViewLabel(text='e46'), level_1)
#         main_layout.add_node(TreeViewLabel(text='volume : 2.5l'), line1)
#         main_layout.add_node(TreeViewLabel(text='power : 192 hp'), line1)
#         main_layout.add_node(TreeViewLabel(text='0-100: 7.2 sec'), line1)
#
#         level_2 = main_layout.add_node(TreeViewLabel(text='Mercedes Benz'))
#         line2 = main_layout.add_node(TreeViewLabel(text='W203'), level_2)
#         main_layout.add_node(TreeViewLabel(text='volume : 2.5l'), line2)
#         main_layout.add_node(TreeViewLabel(text='power : 204 hp'), line2)
#         main_layout.add_node(TreeViewLabel(text='0-100: 8.3 sec'), line2)
#
#         fl.add_widget(main_layout)
#         fl.add_widget(label)
#         fl.add_widget(button)
#
#         def info(instance):
#             try:
#                 label.text = main_layout.selected_node.text
#             except:
#                 pass
#         button.bind(on_press=info)
#
#         return fl
#
# if __name__ == '__main__':
#     MyApp().run()



# class MyApp(App):
#
#     def build(self):
#         lst = []
#         main_layout = FloatLayout()
#         screen = Label(text='Show information', font_size=20)
#         button = Button(text='add to menu', size_hint=(1, 0.1))
#         tv = TreeView(root_options=dict(text='Our menu'), pos=(200, 0))
#         level1 = tv.add_node(TreeViewLabel(text='Fish'))
#         tv.add_node(TreeViewLabel(text='price: 50'), level1)
#         level2 = tv.add_node(TreeViewLabel(text='Pepper'))
#         tv.add_node(TreeViewLabel(text='price: 30'), level2)
#         level3 = tv.add_node(TreeViewLabel(text='Rice'))
#         tv.add_node(TreeViewLabel(text='price: 10'), level3)
#         main_layout.add_widget(tv)
#         main_layout.add_widget(screen)
#         main_layout.add_widget(button)
#
#         def info(instance):
#             lst.append(tv.selected_node.text)
#             screen.text = str(lst)
#
#         button.bind(on_press=info)
#
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()



# class MyApp(App):
#     def build(self):
#         main_layout = TreeView(root_options=dict(text="Корневая папка"))
#         print(main_layout.selected_node.text)
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()

# class MyApp(App):
#     def build(self):
#         main_layout = TreeView(root_options=dict(text="Корневая папка"))
#         level1 = main_layout.add_node(TreeViewLabel(text="Уровень 1"), level2)
#         level2 = main_layout.add_node(TreeViewLabel(text="Уровень 2"))
#         return main_layout
#
# if __name__ == "__main__":
#     MyApp().run()

#21


# class MyApp(App):
#     def build(self):
#         img = Image(source='E:/G/link.GIF', allow_stretch=True, keep_ratio=False)
#         return img
#
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         img = AsyncImage(source='http://fotorelax.ru/wp-content/uploads/2016/12/Best-photos-of-the-2016-National-Geographic-02.jpg', allow_stretch=True, keep_ratio=False)
#         return img
#

# class MyApp(App):
#     def build(self):
#         gl = GridLayout(cols=30, rows=30, size_hint_y=None, size_hint_x=None)
#         for i in range(900):
#             gl.add_widget(Button(text=str(i), size_hint_y=None, size_hint_x=None, size=(200, 200)))
#         gl.bind(minimum_height=gl.setter("height"), minimum_width=gl.setter("width") )
#         ml = ScrollView(bar_color=[0, 0, 1, 1], bar_inactive_color=[1, 0, 0, 1], bar_margin=3,
#                         bar_pos_y='right', bar_width=10, effect_cls='ScrollEffect', scroll_type=['bars'] )
#         ml.add_widget(gl)
#         return ml
#
# if __name__ == '__main__':
#     MyApp().run()

#22
#
# class MyApp(App):
#     def build(self):
#         button = Button(text='Open popup', size_hint=(1, 0.2))
#         def show_popup(instance):
#             popup = Popup(title='Popup message', size_hint=(0.8, 0.5), auto_dismiss=False)
#             content_box = BoxLayout(orientation='vertical', spacing=3)
#             content_box.add_widget(Label(text='Cool car', size_hint=(1, 0.1)))
#             content_box.add_widget(Image(source='E:/G/link.GIF', size_hint=(1, 0.5)))
#             content_box.add_widget(Button(text='OK', size_hint=(1, 0.1)))
#             close_button = Button(text='Close', size_hint=(1, 0.1))
#             close_button.bind(on_press=popup.dismiss)
#             content_box.add_widget(close_button)
#
#             popup.content = content_box
#             popup.open()
#         button.bind(on_press=show_popup)
#         return button
#
# if __name__ == '__main__':
#     MyApp().run()

#23

# class MyApp(App):
#     def build(self):
#         fl = FloatLayout()
#         audio = SoundLoader.load('E:/G/skype-call meloboom.mp3')
#
#         pb = ProgressBar(size_hint=(0.7, 1),
#                          pos_hint={"center_x": 0.5, "center_y": 0.15},
#                          max=int(audio.length))
#         fl.add_widget(pb)
#         lb = Label(pos_hint={"center_x": 0.83, "center_y": 0.13})
#         fl.add_widget(lb)
#         def play(instance):
#             pb.value = audio.get_pos()
#             m = int(pb.value // 60)
#             s = int(pb.value % 60)
#             lb.text = f"{str(m).rjust(2,'0')}:{str(s).rjust(2,'0')}"
#         Clock.schedule_interval(play, 0.1)
#
#         b_start = Button(text="start",
#                          size_hint=(0.1, 0.1),
#                          pos=(240, 0))
#         def start(instance):
#             fl.add_widget(Image(source="E:/G/butterfly_338337.PNG",
#                                 size_hint=(0.8, 0.6),
#                                 pos=(85, 200)))
#             fl.add_widget(Label(text=str(audio.source.split("\\")[-1]),
#                                 size_hint=(1, 0.05),
#                                 pos=(0, 100)))
#             x = audio.get_pos()
#             audio.seek(x)
#             audio.play()
#             # audio.loop = True
#
#         b_start.bind(on_press=start)
#         fl.add_widget(b_start)
#
#         b_stop = Button(text="stop",
#                         size_hint=(0.1, 0.1),
#                         pos=(320, 0))
#         def stop(instance):
#             audio.seek(0)
#             audio.stop()
#         b_stop.bind(on_press=stop)
#         fl.add_widget(b_stop)
#
#         b_pause = Button(text="pause",
#                          size_hint=(0.1, 0.1),
#                          pos=(400, 0))
#         def pause(instance):
#             audio.stop()
#         b_pause.bind(on_press=pause)
#         fl.add_widget(b_pause)
#
#         b_rewind = Button(text="rewind",
#                           size_hint=(0.1, 0.1),
#                           pos=(480, 0))
#         def rewind(instance):
#             rew = audio.get_pos()
#             rew += 10
#             audio.seek(rew)
#             audio.play()
#         b_rewind.bind(on_press=rewind)
#         fl.add_widget(b_rewind)
#         return fl
#
# if __name__ == '__main__':
#     MyApp().run()





#
# class MyApp(App):
#     def build(self):
#         fl = FloatLayout()
#         audio = SoundLoader.load('E:/G/skype-call meloboom.mp3')
#
#         pb = ProgressBar(size_hint=(0.7, 1), pos_hint={'center_x':0.5, 'center_y':0.15},
#                          max=int(audio.length))
#         fl.add_widget(pb)
#         lb = Label(pos_hint={'center_x':0.83, 'center_y':0.13})
#         fl.add_widget(lb)
#         def play(instance):
#             pb.value = audio.get_pos()
#             m = int(pb.value//60)
#             s = int(pb.value % 60)
#             lb.text = f'{str(m).rjust(2, "0")}:{str(s).rjust(2, "0")}'
#         Clock.schedule_interval(play, 0.1)
#
#         b_start = Button(text='start', size_hint=(0.1, 0.1), pos=(240, 0))
#
#         def start(instance):
#             fl.add_widget(Image(source='E:/G/link.GIF', size_hint=(0.8, 0.6), pos=(85, 200)))
#             fl.add_widget(Label(text=str(audio.source.split('//')[-1]), size_hint=(1, 0.05), pos=(0, 100)))
#
#             x = audio.get_pos()
#             audio.seek(x)
#             audio.play()
#
#         b_start.bind(on_press=start)
#         fl.add_widget(b_start)
#
#         b_stop = Button(text="stop",
#                         size_hint=(0.1, 0.1),
#                         pos=(320, 0))
#
#         def stop(instance):
#             audio.seek(0)
#             audio.stop()
#
#         b_stop.bind(on_press=stop)
#         fl.add_widget(b_stop)
#
#         b_pause = Button(text="pause",
#                          size_hint=(0.1, 0.1),
#                          pos=(400, 0))
#
#         def pause(instance):
#             audio.stop()
#
#         b_pause.bind(on_press=pause)
#         fl.add_widget(b_pause)
#
#         b_rewind = Button(text="rewind",
#                           size_hint=(0.1, 0.1),
#                           pos=(480, 0))
#
#         def rewind(instance):
#             rew = audio.get_pos()
#             rew += 10
#             audio.seek(rew)
#             audio.play()
#
#         b_rewind.bind(on_press=rewind)
#         fl.add_widget(b_rewind)
#         return fl
#
#
# if __name__ == '__main__':
#     MyApp().run()


# 24

# class MyApp(App):
#     def build(self):
#         video = Video(source='E:/G/video1.mp4', size_hint=(0.8, 0.8), pos=(100, 100), eos='loop')
#         video.state = 'play'
#         return video
#
#
# if __name__ == '__main__':
#     MyApp().run()

from kivy.app import App
from kivy.uix.video import Video

# class MyApp(App):
#     def build(self):
#         video = Video(source='E:/G/video1.mp4')
#         # video.state = 'play'
#         return video
#
# if __name__ == '__main__':
#     MyApp().run()




# class MyApp(App):
#     def build(self):
#         video = VideoPlayer(source='E:/G/video1.mp4', allow_fullscreen=True, state='pause',
#                             options={'eos': 'loop'})
#
#         return video
#
# if __name__ == '__main__':
#     MyApp().run()


#25
#
# class MyApp(App):
#     def build(self):
#         cp =ColorPicker()
#
#         def on_color(instance, value):
#             print('RGBA =', str(instance.color))
#             print('HSV =', str(instance.hsv))
#             print('HEX =', str(instance.hex_color))
#
#         cp.bind(color=on_color)
#
#         return cp
#
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         fc = FileChooserListView()
#         return fc
#
# if __name__ == '__main__':
#     MyApp().run()


#
# class MyApp(App):
#     def build(self):
#         fc = FileChooserIconView()
#         return fc
#
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         filechooser = GridLayout(cols=2)
#         fc = FileChooserIconView()
#         im = Image()
#
#         def selected(instance, filename):
#             try:
#                 im.source = filename[0]
#             except:
#                 pass
#
#         fc.bind(selection=selected)
#         filechooser.add_widget(fc)
#         filechooser.add_widget(im)
#
#         return filechooser
#
# if __name__ == '__main__':
#     MyApp().run()


#
# class MyApp(App):
#     def build(self):
#         gl = GridLayout(cols=2)
#         gl.add_widget(FileChooserIconView())
#         gl.add_widget(FileChooserListView())
#         return gl
#
# if __name__ == '__main__':
#     MyApp().run()


#26

# class TestApp(App):
#     def build(self):
#         ew = EffectWidget()
#         image = Image(source='E:/G/link.GIF')
#         bl = BoxLayout(orientation='vertical')
#         bl.add_widget(ew)
#         btn = Button(text='Mono', font_size=20, size_hint=(0.2, 0.1))
#         btn1 = Button(text='Scanline', font_size=20, size_hint=(0.2, 0.1))
#         btn2 = Button(text='Chanel', font_size=20, size_hint=(0.2, 0.1))
#         btn3 = Button(text='Pixel', font_size=20, size_hint=(0.2, 0.1))
#         for el in (btn, btn1, btn2, btn3):
#             bl.add_widget(el)
#         ew.add_widget(image)
#
#         def mono(instance):
#             ew.effects = [MonochromeEffect()]
#
#         def scan_line(instance):
#             ew.effects = [ScanlinesEffect()]
#
#         def chanel(instance):
#             ew.effects = [ChannelMixEffect()]
#
#         def pixel(instance):
#             ew.effects = [PixelateEffect()]
            # ew.effects = {PixelateEffect(), ScanlinesEffect()}
            # ew.effects = [PixelateEffect(), ScanlinesEffect()]
            # ew.effects = (PixelateEffect(), ScanlinesEffect())
            # ew.effects = PixelateEffect(), ScanlinesEffect()


#         btn.bind(on_press=mono)
#         btn1.bind(on_press=scan_line)
#         btn2.bind(on_press=chanel)
#         btn3.bind(on_press=pixel)
#
#         return bl
#
# if __name__ == '__main__':
#     TestApp().run()

#
# class TestApp(App):
#     def build(self):
#         ew = EffectWidget()
#         image = Image(source='E:/G/link.GIF')
#         ew.add_widget(image)
#         ew.effects = [PixelateEffect(pixel_size=1)] # неверно pixel_size=1
#         return ew
#
# if __name__ == '__main__':
#     TestApp().run()


#27
# class testApp(App):
#     pass
#
# if __name__ == '__main__':
#     testApp().run()
# KV file

'''BoxLayout:
    orientation: "vertical"
    Button:
        text: "Button 1"
        background_color: 1, 0, 0, 1
    Button:
        text: "Button 2"
        background_color: 1, 0, 0, 1
    Button:
        text: "Button 3"
        background_color: 1, 0, 0, 1
    Label:
        text: 'Hello world'
'''
#
# class MyButton(Button):
#     pass
#
# class testApp(App):
#     def build(self):
#         return MyButton()
#
# if __name__ == "__main__":
#     testApp().run()

'''<MyButton>:
    id: B1
    text: "Button 1"
    on_press:
        print("Button pressed")
'''

# class MyButton(Button):
#     def press_button(self):
#         print("Button pressed")
#
# class MyApp(App):
#     def build(self):
#         return MyButton()
#
# if __name__ == "__main__":
#     MyApp().run()

'''<MyButton>:
    id: B1
    text: "Button 1"
    on_press: root.press_button()'''

# class MyApp(App):
#     def build(self):
#         button = Button(text="Button 1")
#         def press_button(self):
#             button.background_color = (1, 0, 0, 1)
#         button.bind(on_press= press_button)
#         return button
#
# if __name__ == "__main__":
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         button = Button(text="Button 1")
#         def press_button(self):
#             button.background_color = (1, 0, 0, 1)
#         button.bind(on_press= press_button)
#         return button
#
# if __name__ == "__main__":
#     MyApp().run()

#
# class MyButton(Button):
#     pass
# class testApp(App):
#     def build(self):
#         return MyButton()
#
# if __name__ == "__main__":
#     testApp().run()

'''<MyButton>:
    text: "Button 1"
    on_press: self.background_color = (1, 0, 0, 1)
    
or 

<MyButton>:
    id: B1
    text: "Button 1"
    on_press: B1.background_color = (1, 0, 0, 1)
'''

# class MySlider(BoxLayout):
#     pass
#
# class testApp(App):
#     def build(self):
#         return MySlider()
#
# if __name__ == '__main__':
#     testApp().run()


'''<MySlider>:
    orientation: 'vertical'
    Slider:
        id: my_slider
        value: 50.5
    Label:
        text: str(int(my_slider.value))
'''


# class testApp(App):
#     def build(self):
#         pass
#
# if __name__ == '__main__':
#     testApp().run()

'''StackLayout:
    ToggleButton:
        id: tb
        text: "ToggleButton"
        size_hint: 0.2, 0.2
        state: "down"
        on_press:
            if self.state == "down": lb.text = "Кнопка нажата!"
            else: lb.text = "Нажми кнопку!"
    Label:
        id: lb
        size_hint: 0.2, 0.2
        font_size: 15
        bold: True
        
or 

    StackLayout:
    ToggleButton:
        id: tb
        text: "ToggleButton"
        size_hint: 0.2, 0.2
        state: "down"
    Label:
        id: lb
        size_hint: 0.2, 0.2
        font_size: 15
        bold: True
        text: "Кнопка нажата!" if tb.state == "down" else "Нажми кнопку!"
'''

# str_1 = '123'
# print(list(str_1))
# print(''.join(list(str_1)))


# class MyApp(App):
#     def build(self):
#         return Builder.load_file("test.kv")
#
# if __name__ == "__main__":
#     MyApp().run()

'''BoxLayout:
    #:set text_color 1, 0, 0, 1
    #:set font_size 46
    Label:
        text: "Label 1"
        color: text_color
        font_size: font_size
    Label:
        text: "Label 2"
        color: text_color
        font_size: font_size
 or 
 
 '''
# class MyApp(App):
#     def build(self):
#         return Builder.load_string('''
# BoxLayout:
#     #:set text_color 1, 0, 0, 1
#     #:set font_size 46
#     Label:
#         text: "Label 1"
#         color: text_color
#         font_size: font_size
#     Label:
#         text: "Label 2"
#         color: text_color
#         font_size: font_size
# ''')
#
# if __name__ == "__main__":
#     MyApp().run()

# class MyApp(App):
#     def build(self):
#         return Builder.load_string('''
# BoxLayout:
#     #:set text_color 0, 1, 1, 1
#     #:set text_color2 1, 0, 1, 1
#     #:set font_size 30
#     #:set label_name 'Label_1'
#     #:set label_name 'Label_2'
#     Label:
#         text: label_name
#         color: text_color
#         font_size: font_size
#     Label:
#         text: label_name
#         color: text_color2
#         font_size: font_size
# ''')
#
# if __name__ == "__main__":
#     MyApp().run()

#28
#
# class MyPaintApp(App):
#     def build(self):
#         main_layout = Widget()
#         def touch(self, touch):
#             print(touch)
#             print(touch.spos)
#             print(touch.spos)
#             print(touch.spos[0])
#             print(touch.spos[1])
#             print(touch.pos)
#             print(touch.pos[0])
#             print(touch.x)
#             print(touch.pos[1])
#             print(touch.y)
#             print(touch.time_start)
#             print(touch.time_update)
#             print(touch.time_end)
#             print(touch.uid)
#             print(touch.is_double_tap)
#             print(touch.is_triple_tap)
#             print(touch.is_mouse_scrolling)
#         main_layout.bind(on_touch_down=touch)
#         return main_layout
#
# if __name__ == '__main__':
#     MyPaintApp().run()
#

# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.graphics import Color, Ellipse, Line
#
# class MyPaintApp(App):
#     def build(self):
#         main_layout = Widget()
#         size_pen = 5
#
#         def on_touch_down(self, touch):
#             with self.canvas:
#                 Color(1, 0, 0 , 1)
#                 Ellipse(pos=(touch.x - size_pen / 2, touch.y - size_pen / 2),
#                         size=(size_pen, size_pen))
#                 touch.ud['line'] = Line(points=(touch.x, touch.y),
#                                         width=size_pen)
#         main_layout.bind(on_touch_down=on_touch_down)
#
#         def on_touch_move(self, touch):
#             touch.ud['line'].points += [touch.x, touch.y]
#         main_layout.bind(on_touch_move=on_touch_move)
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyPaintApp().ru

# class MyPaintApp(App):
#     def build(self):
#         main_layout = BoxLayout(orientation="vertical")
#         gr = GridLayout(cols = 5, size_hint=(1, 0.1))
#
#         size_pen = Slider(min=1,
#                           max=20)
#         gr.add_widget(size_pen)
#
#         b1 = Button(background_color=(1, 0, 0, 1),
#                     background_normal="")
#         b2 = Button(background_color=(0, 1, 0, 1),
#                     background_normal="")
#         b3 = Button(background_color=(0, 0, 1, 1),
#                     background_normal="")
#         b4 = Button(text="Clear", background_color=(0.5, 0.5, 0.5, 1),
#                     background_normal="")
#         def clear_canvas(self):
#             widget.canvas.clear()
#         global pen_color
#         pen_color = (1, 0, 0, 1)
#         def press_color(self):
#             global pen_color
#             pen_color = self.background_color
#         b1.bind(on_press=press_color)
#         b2.bind(on_press=press_color)
#         b3.bind(on_press=press_color)
#         b4.bind(on_press=clear_canvas)
#         gr.add_widget(b1)
#         gr.add_widget(b2)
#         gr.add_widget(b3)
#         gr.add_widget(b4)
#
#         main_layout.add_widget(gr)
#         widget = Widget()
#         main_layout.add_widget(widget)
#         def on_touch_down(self, touch):
#             if widget.collide_point(*touch.pos):
#                 with self.canvas:
#                     Color(pen_color[0], pen_color[1], pen_color[2], pen_color[3])
#                     Ellipse(pos=(touch.x - size_pen.value / 2, touch.y - size_pen.value / 2),
#                             size=(size_pen.value, size_pen.value))
#                     touch.ud['line'] = Line(points=(touch.x, touch.y),
#                                             width=size_pen.value)
#         widget.bind(on_touch_down=on_touch_down)
#         def on_touch_move(self, touch):
#             if widget.collide_point(*touch.pos):
#                 touch.ud['line'].points += [touch.x, touch.y]
#         widget.bind(on_touch_move=on_touch_move)
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyPaintApp().run()

# class MyPaintApp(App):
#     def build(self):
#         main_layout = Widget()
#         with main_layout.canvas:
#             Color(1, 0, 1, 1)
#             Bezier(points=(0, 0, 100, 200, 300, 100, 400, 400))
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyPaintApp().run()

# class testApp(App):
#     def build(self):
#         pass
#
# if __name__ == '__main__':
#     testApp().run()


#29
#
# class MyApp(App):
#     def build(self):
#         button = Button(text='Press me', background_color=(0, 0, 1, 1))
#         def press_button(self):
#             anim = Animation(background_color=(1, 0, 0, 1), duration=2,
#                              size_hint=(0.5, 0.5),
#                              pos=(200, 150))
#             anim.start(button)
#         button.bind(on_press=press_button)
#
#         return button
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         button = Button(text='Press me', background_color=(0, 0, 1, 1))
#         def press_button(self):
#             anim = Animation(background_color=(1, 0, 0, 1), duration=2,
#                              size_hint=(0.5, 0.5),
#                              pos=(200, 150),
#                              font_size=55,
#                              t='in_out_bounce')
#             anim.start(button)
#         button.bind(on_press=press_button)
#
#         return button
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         button = Button(text='Press me', background_color=(0, 0, 1, 1))
#         def press_button(instance):
#             anim1 = Animation(background_color=(1, 0, 0, 1),
#                               duration=0.5, t="in_bounce")
#             anim2 = Animation(duration=5,
#                               size_hint=(0.5, 0.5),
#                               pos=(200, 150),
#                               t="in_out_back")
#             anim = anim1 & anim2
#             anim.start(instance)
#         button.bind(on_press=press_button)
#
#         return button
# if __name__ == '__main__':
#     MyApp().run()


# class MyApp(App):
#     def build(self):
#         button = Button(size=(100,100), pos=(100, 100))
#         anim1 = Animation(pos=(400, 400), duration=2)
#         anim2 = Animation(pos=(100, 100), duration=2)
#         anim = anim1 + anim2
#         anim.repeat = True
#         anim.start(button)
#
#         return button
# if __name__ == '__main__':
#      MyApp().run()


# class MyApp(App):
#     def build(self):
#         button = Button(background_color=(0,0,1,1))
#         anim = Animation(background_color=(0,0,1,1), duration=0.5) + \
#                Animation(background_color=(1,0,0,1), duration=0.5) + \
#                Animation(background_color=(0,1,0,1), duration=0.5)
#         anim.repeat=True
#         anim.start(button)
#         return button
#
# if __name__ == '__main__':
#     MyApp().run()

# class MyApp(App):
#     def build(self):
#         main_layout = Widget()
#
#         with main_layout.canvas:
#             Color(1, 0, 0, 1)
#             Ellipse(pos=(main_layout.pos), size=(50, 50))

#         def on_touch_down(instance, touch):
#             with instance.canvas:
#                 instance.canvas.clear()
#                 Color(1, 0, 0, 1)
#                 instance.circle = Ellipse(pos=(main_layout.pos), size=(50, 50))
#                 anim = Animation(x=touch.x-25, y=touch.y-25, duration=0.5)
#                 anim.start(instance)
#             main_layout.bind(pos=update_circle)
#         main_layout.bind(on_touch_down=on_touch_down)
#
#         def update_circle(instance, *args):
#                 instance.circle.pos = instance.pos
#
#         return main_layout
#
# if __name__ == '__main__':
#     MyApp().run()


#
# class MyApp(App):
#     def build(self):
#         main_layout = Widget()
#
#         with main_layout.canvas:
#             Color(1, 0, 0, 1)
#             Ellipse(pos=(main_layout.pos), size=(50, 50))
#
#         keyboard = Window.request_keyboard(None, self)
#         def on_keyboard_down(self, keyboard, keycode, text):
#             x, y = 0, 0
#             print(keyboard[1])
#
#             if keyboard[1] == "up":
#                 x = 50
#             elif keyboard[1] == "down":
#                 x = -50
#             elif keyboard[1] == "left":
#                 y = -50
#             elif keyboard[1] == "right":
#                 y = 50
#             with main_layout.canvas:
#                 main_layout.canvas.clear()
#                 Color(1, 0, 0, 1)
#                 main_layout.circle = Ellipse(pos=(main_layout.pos), size=(50, 50))
#                 anim = Animation(x=main_layout.pos[0] + y, y=main_layout.pos[1] + x, duration=0.3)
#                 anim.start(main_layout)
#             main_layout.bind(pos=update_circle)
#         keyboard.bind(on_key_down=on_keyboard_down)
#         def update_circle(self, *args):
#                 self.circle.pos = self.pos
#         return main_layout
# if __name__ == '__main__':
#     MyApp().run()



# class MyApp(App):
#     def build(self):
#         label = Label(text="")
#         keyboard = Window.request_keyboard(None, self)
#         def on_keyboard_down(self, keyboard, keycode, text):
#             label.text = str(keycode)
#         keyboard.bind(on_key_down=on_keyboard_down)
#         return label
#
# if __name__ == '__main__':
#     MyApp().run()

#
# class MyApp(App):
#     def build(self):
#         fl = FloatLayout()
#         widget = Widget()
#         fl.add_widget(widget)
#         flag1, flag2 = True, True
#
#         def clear(self):
#             widget.canvas.clear()
#         Clock.schedule_interval(clear, 1 / 60)
#
#         def circle(self):
#             nonlocal flag1, flag2
#             with widget.canvas:
#                 speed = 1
#                 ball_size=50
#
#                 if widget.pos[1] >= Window.height-ball_size or flag1 == False:
#                     flag1 = False
#                     widget.pos[1] -= speed
#                     if widget.pos[1] <= 0:
#                         flag1 = True
#                         widget.pos[1] += speed
#                 else:
#                     widget.pos[1] += speed
#
#                 if widget.pos[0] >= Window.width-ball_size or flag2 == False:
#                     flag2 = False
#                     widget.pos[0] -= speed
#                     if widget.pos[0] <= 0:
#                         flag2 = True
#                         widget.pos[0] += speed
#                 else:
#                     flag2 = True
#                     widget.pos[0] += speed
#
#                 Color(1, 0, 0, 1)
#                 widget.circle = Ellipse(pos=(widget.pos), size=(ball_size, ball_size))
#
#         Clock.schedule_interval(circle, 1 / 60)
#
#         return fl
#
# if __name__ == '__main__':
#     MyApp().run()


#
# class MyApp(App):
#     def build(self):
#         fl = FloatLayout()
#         lb1 = Label(text="0", size_hint=(0.1, 0.1), pos=(150, 450), font_size=55)
#         lb2 = Label(text="0", size_hint=(0.1, 0.1), pos=(570, 450), font_size=55)
#         fl.add_widget(lb1)
#         fl.add_widget(lb2)
#         widget = Widget(pos=(350, 300))
#         fl.add_widget(widget)
#         flag1, flag2 = True, True
#
#         def clear(self):
#             widget.canvas.clear()
#         Clock.schedule_interval(clear, 1 / 60)
#
#         def circle(self):
#             nonlocal flag1, flag2
#             with widget.canvas:
#                 speed = 10
#                 ball_size=50
#                 # ОСЬ Y
#                 if widget.pos[1] >= Window.height-ball_size or flag1 == False:
#                     flag1 = False
#                     widget.pos[1] -= speed
#                     if widget.pos[1] <= 0:
#                         flag1 = True
#                         widget.pos[1] += speed
#                 else:
#                     widget.pos[1] += speed
#                 # ОСЬ X
#                 if widget.pos[0] >= Window.width - ball_size or flag2 == False:
#                     flag2 = False
#                     widget.pos[0] -= speed
#                     if widget.pos[0] <= 0 or (widget.pos[0] <= rect_left.pos[0] + 20 and (
#                             rect_left.pos[1] + 150 > widget.pos[1] > rect_left.pos[1])):
#                         flag2 = True
#                 else:
#                     if widget.pos[0] + ball_size >= rect_right.pos[0] and (
#                             rect_right.pos[1] + 150 > widget.pos[1] > rect_right.pos[1]):
#                         flag2 = False
#                     else:
#                         widget.pos[0] += speed
#                 if widget.pos[0] >= Window.width - ball_size:
#                     lb1.text = str(int(lb1.text) + 1)
#                 if widget.pos[0] <= 0:
#                     lb2.text = str(int(lb2.text) + 1)
#                 Color(1, 0, 0, 1)
#                 widget.circle = Ellipse(pos=(widget.pos), size=(ball_size, ball_size))
#
#         dx = 0
#         dy = 0
#
#         def rect(self):
#             with widget.canvas:
#                 global rect_left
#                 global rect_right
#                 Color(0, 0, 1, 1)
#                 rect_left = Rectangle(size=(20, 150), pos=(0, dx))
#                 rect_right = Rectangle(size=(20, 150), pos=(780, dy))
#
#         Clock.schedule_interval(rect, 1 / 60)
#         Clock.schedule_interval(circle, 1 / 60)
#
#         def on_touch_move(self, touch):
#             nonlocal dx, dy
#             if touch.x < self.width / 2:
#                 dx = touch.pos[1] - 75
#             if touch.x > self.width / 2:
#                 dy = touch.pos[1] - 75
#
#         widget.bind(on_touch_move=on_touch_move)
#
#         return fl
#
# if __name__ == '__main__':
#     MyApp().run()