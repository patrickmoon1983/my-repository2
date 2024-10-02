from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 580)

KV = '''
      
MDScreen:
    name: 'pre-splash'
    MDFloatLayout:
        md_bg_color: 226/255, 0, 48/255, 1
        AsyncImage:
            source:'https://cdn-icons-png.freepik.com/256/16835/16835425.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
            size_hint: 0.26, 0.26
            pos_hint: {'center_x':0.5, 'center_y':0.55}
            canvas.before:
                Color:
                    rgb: 1, 1, 1, 1
                Ellipse:
                    size: 130, 130
                    pos: 110, 250
                    
        MDLabel:
            text: 'Durar HR'
            pos_hint: {'center_x':0.5, 'center_y':0.2}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_size: 35
            font_name: 'Gothic'
            
        MDLabel:
            text: 'The Complete HR Solutions'
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            font_size:13
            font_name: 'Gothic'

'''

KV_1 = '''
MDScreen:
    name: 'login'
    MDFloatLayout:
        md_bg_color:  1, 1, 1, 1
        MDIconButton:
            icon: 'chevron-left'
            user_font_size: 35
            pos_hint: {'center_y':0.95} 
        MDLabel:
            text: 'Back'
            font_size: 18
            font_name: 'Gothic'
            pos_hint: {'center_x':0.615, 'center_y':0.95} 
        AsyncImage:
            source:'https://cdn-icons-png.freepik.com/256/16835/16835425.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
            size_hint: 0.26, 0.26
            pos_hint: {'center_x':0.22, 'center_y':0.8}
                
        MDLabel:
            text: 'Proceed with your'
            font_size: 22
            font_name: 'Gothic'
            color: 120/255, 120/255, 120/255, 1
            pos_hint: {'center_x':0.6, 'center_y':0.65} 
            
        MDLabel:
            text: 'Login'
            font_size: 28
            font_name: 'Gothic'
            bold: True
            pos_hint: {'center_x':0.6, 'center_y':0.58} 
            
        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint:{'center_x':0.5, 'center_y':0.42} 
            MDLabel:
                text: 'Username'
                font_size: 14
                font_name: 'Gothic'
                pos_hint:{'center_x':0.5, 'center_y':0.9} 
            TextInput:
                size_hint_y: 0.75
                font_name: 'Gothic'
                pos_hint:{'center_x':0.49, 'center_y':0.4} 
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: 2
                foreground_color: 120/255, 120/255, 120/255, 1
                font_size: '17' 
                multiline: False
            AsyncImage:
                source:'https://cdn-icons-png.freepik.com/256/10852/10852416.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                size_hint: 0.6, 0.6
                pos_hint: {'center_x':0.96, 'center_y':0.5}
                
            MDFloatLayout:
                pos_hint: {'center_x':0.5, 'center_y':0}
                size_hint_y: 0.03
                md_bg_color: 120/255, 120/255, 120/255, 1
        MDFloatLayout:
            size_hint: 0.79, 0.08
            pos_hint:{'center_x':0.5, 'center_y':0.28} 
            MDLabel:
                text: 'Password'
                font_size: 14
                font_name: 'Gothic'
                pos_hint:{'center_x':0.5, 'center_y':0.9} 
            TextInput:
                size_hint_y: 0.75
                font_name: 'Gothic'
                pos_hint:{'center_x':0.49, 'center_y':0.4} 
                background_color: 0, 0, 0, 0
                cursor_color: 0, 0, 0, 1
                cursor_width: 2
                font_size: '17' 
                multiline: False
                password: True
            AsyncImage:
                source:'https://cdn-icons-png.freepik.com/256/7750/7750485.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                size_hint: 0.6, 0.6
                pos_hint: {'center_x':0.96, 'center_y':0.5}
                
            MDFloatLayout:
                pos_hint: {'center_x':0.5, 'center_y':0}
                size_hint_y: 0.03
                md_bg_color: 120/255, 120/255, 120/255, 1
                
        Button:
            text: 'Login'
            background_color: 0, 0, 0, 0
            font_name: 'Gothic'
            size_hint: 0.79, 0.08
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            canvas.before:
                Color:
                    rgb: 226/255, 0, 48/255, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [2]
        MDTextButton:
            text: 'Forget Password ?'
            font_size: 13
            pos_hint: {'center_x':0.5, 'center_y':0.07}
            halign: 'center'
            color: 120/255, 120/255, 120/255, 1
                      
'''

class LoginPage(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        screen_manager.add_widget(Builder.load_string(KV_1))
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        screen_manager.current = 'login'

LoginPage().run()
