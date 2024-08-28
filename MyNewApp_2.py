from kivy.config import Config
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "1")
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests

Window.keyboard_anim_args = {'d': 0.2, 't': 'in_out_expo'}
Window.softInput_mode = 'below_target'

class UI(ScreenManager):
    pass
class CoolApApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepOrange'
        Builder.load_file('new_app_2.kv')
        self.url = 'https://my-new-project-c0bc4-default-rtdb.firebaseio.com/.json'
        self.key = 'rSM2l7BVPLlGXDBkvMy1H97gX7haSSWFmPnsIZBc'

        return UI()

    def data_login(self):
        try:
            users = self.root.ids.user.text
            passwords = self.root.ids.password.text
            state = False
            data = requests.get(self.url + '?auth=' + self.key)


            for key, value in data.json().items():
                user_reg = value['User']
                password_reg = value['Password']

                if users == user_reg:
                    if passwords == password_reg:
                        state = True
                        self.root.ids.signal_login.text = ''
                        self.root.ids.user.text = ''
                        self.root.ids.password = ''

                    else:
                        self.root.ids.signal_login.text = 'Incorrect password'
                        self.root.ids.user.text = ''
                        self.root.ids.password = ''
                else:
                    self.root.ids.signal_login.text = 'Incorrect user'
                    self.root.ids.user.text = ''
                    self.root.ids.password = ''

            return state
        except:
            pass

    # def data_logout(self):
    #     r = requests.session().close()
    #     return r

    def register_data(self):

        state = 'Incorrect data'
        users = self.root.ids.new_user.text
        password_one = self.root.ids.new_password.text
        password_two = self.root.ids.new_password_two.text
        data = requests.get(self.url + '?auth' + self.key)


        if password_one != password_two:
            state = 'no coincide passwords '

        elif len(users) <= 4:
            state = 'Must be more than 4 chars'
        elif password_one == password_two and len(password_two) <= 4:
            state = 'No secure password'
        else:
            for key, value in data.json().items():
                user = value['User']
                if user == users:
                    state = 'Existing account'
                    break
                else:
                    state = 'Successfully registration '
                    data = {users: {'User': users, 'Password': password_one}}
                    requests.patch(url=self.url, json=data)
                    self.root.ids.signal_register.text = state

        self.root.ids.signal_register.text = state
        self.root.ids.new_user.text = ''
        self.root.ids.new_password.text = ''
        self.root.ids.new_password_two.text = ''

        return state

    def clear_signal(self):

        self.root.ids.signal_register.text = ''
        self.root.ids.signal_login.text = ''


    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

CoolApApp().run()




