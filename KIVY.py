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
from  kivy.uix.togglebutton import ToggleButton
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
s = []
s = ['1000', '700', '1000', '700', '1000', '900', '900', '20000', '900', '600', '900', '600',
     '900', '1000', '1000', '20000', '1000', '700', '1000', '700', '1000', '900', '900', '20000', '900',
     '600', '900', '600', '900', '1000']
class MainApp(App):
    def build(self):
        main_layout = FloatLayout()

        box_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.5),
                               pos_hint={'x': 0, 'y': 0.5})

        restart_button = Button(text='Restart sound track', background_color=[1, 0, 1, 1], italic=True,
                                bold=True, font_size=30)

        restart_button.bind(on_press=self.restart_solution)
        box_layout.add_widget(restart_button)

        start_button = Button(text='start', background_color=[1, 1, 0, 1], italic=True,
                                bold=True, font_size=30)

        start_button.bind(on_press=self.start_solution)
        box_layout.add_widget(start_button)
        main_layout.add_widget(box_layout)

        grid_layout = GridLayout(rows=1, size_hint=(1, 0.5))
        buttons = ['90', '100', '110', '120', '130', '200', '300', '400', '500', '600', '700',
                   '800', '900', '1000', '25000']

        color_switch = 0
        for i in buttons:
            if color_switch == 0:
                color = [0, 0.5, 0.5, 1]
                color_switch = 1
            else:
                color = [0.1, 0.5, 0.8, 1]
                color_switch = 0

            button = Button(text=str(i), background_color=color, italic=True, font_size=15)
            button.bind(on_press=self.sound_solution)
            grid_layout.add_widget(button)

        main_layout.add_widget(grid_layout)

        return main_layout

    def restart_solution(self, instance):
        global s
        # s = []
        s = ['1000', '700', '1000', '700', '1000', '900', '900', '20000', '900', '600', '900', '600',
             '900', '1000', '1000', '20000', '1000', '700', '1000', '700', '1000', '900', '900', '20000', '900',
             '600', '900', '600', '900', '1000']
    def start_solution(self, instance):
        for i in s:
            winsound.Beep(int(i), 300)

    def sound_solution(self, instance):
        winsound.Beep(int(instance.text), 300)
        s.append(instance.text)
if __name__ == '__main__':
    MainApp().run()


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


from kivy.app import App
from kivy.uix.button import Button
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

