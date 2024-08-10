from kivy.config import Config
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "1")
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class UI(ScreenManager):
    pass
class CoolApApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('new_app.kv')

        return UI()

    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style ='Dark'
        else:
            self.theme_cls.theme_style = 'Light'


CoolApApp().run()