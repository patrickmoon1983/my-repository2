from kivy.config import Config
from kivy.uix.screenmanager import SlideTransition, RiseInTransition

Config.set("graphics", "width", "550")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "0")
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker


class Screens(MDScreenManager):


    def clinics(self, *args):
        self.current = 'screen_3'
        #self.transition = RiseInTransition()

    def appointment(self, *args):
        self.current = 'screen_2'

    def doctors(self, *args):
        self.current = 'screen_4'

    def home(self, *args):
        self.current = 'main_screen'

    def cash(self, *args):
        self.current = 'screen_5'

    def login_page(self, *args):
        self.current = 'screen_7'

    def about_page(self, *args):
        self.current = 'screen_6'

    def make_appoint(self, *args):
        self.current = 'screen_1'

    def on_save(self, value, instance, date_range):
        self.ids.show_date.text = f'Date : {instance}'


    def on_cancel(self, value):
        self.ids.show_date = f'No dates'

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        # date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save= self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()




class Scrollview:
    pass

class MyDoctorApp(MDApp):

    def __init__(self):
        super().__init__()

        self.dialog = None
        self.dialog_2 = None
        self.dct = {'Ivanov SergeiSt / St Petersburg, Kuzia str.21': 1,
                    'Malicheva Aleksandra / St Petersburg, Slava str.17': 2,
                    'Sergeev mikhail / Moscow, Arbat street 2':3,
                    'Antonova Uliyana / Moscow,Pionerskaya 12' : 4,
                    'Kuzmina Olga / Ekaterineburg,Plaza place' : 5,
                    'Mironov Sergei / Rostov on Don,Korolev st. 9' : 6

                    }

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.material_style = "M2"
        return Builder.load_file('CallDoctor.kv')

    def show_current_appoint(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Current appointment', text='',
                                   buttons=[MDRectangleFlatButton(text='Ok',
                                                                 text_color=self.theme_cls.primary_color,
                                                                  on_release= self.close_dialog),
                                            MDRectangleFlatButton(text='Clear',
                                                                  text_color=self.theme_cls.primary_color)
                                            ])

        self.dialog.open()

    def show_all_appoint(self):
        if not self.dialog_2:
            self.dialog_2 = MDDialog(title='All appointments', text='',
                                   buttons=[MDRectangleFlatButton(text='Ok',
                                                                 text_color=self.theme_cls.primary_color
                                                                  , on_release= self.close_dialog_2)])
        self.dialog_2.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def close_dialog_2(self, instance):
        self.dialog_2.dismiss()


    def add_appoint(self):
        self.root.ids.show_doc.text = f'Doctor: {self.root.ids.doctor1.text}'
        self.root.ids.show_hosp.text = 'Clinic: SPB, Kuzia str.21\n tel: 0325412'

    def add_appoint_2(self):
        self.root.ids.show_doc.text = f'Doctor: {self.root.ids.doctor2.text}'
        self.root.ids.show_hosp.text = 'Clinic: SPB, Slava str. 17\n tel: 0626412'

    def add_appoint_3(self):
        self.root.ids.show_doc.text = f'Doctor :{self.root.ids.doctor3.text}'
        self.root.ids.show_hosp.text = 'Clinic: Moscow,Arbat street 2\n tel: 0126472'

    def add_appoint_4(self):
        self.root.ids.show_doc.text = f'Doctor :{self.root.ids.doctor4.text}'
        self.root.ids.show_hosp.text = 'Clinic: Moscow,Pionerskaya 12\n tel: 0826512'

    def add_appoint_5(self):
        self.root.ids.show_doc.text = f'Doctor :{self.root.ids.doctor5.text}'
        self.root.ids.show_hosp.text = 'Clinic: Ekaterineburg,Plaza place\n tel: 0526412'

    def add_appoint_6(self):
        self.root.ids.show_doc.text = f'Doctor :{self.root.ids.doctor6.text}'
        self.root.ids.show_hosp.text = 'Clinic: Rostov on Don,Korolev st. 9\n tel: 0926912'




        # #self.dct.update({self.root.ids.doctor1.text: 1})
        #
        # self.dialog = MDDialog(title='Current appointments', text='',
        #                          buttons=[MDRectangleFlatButton(text='Ok',
        #                                                         text_color=self.theme_cls.primary_color
        #                                                         , on_release=self.close_dialog)])
        #
        #
        # for key, value in self.dct.items():
        #
        #     a, b = key, value
        # self.dialog.text = a
        #
        #
        # #self.dialog.text = f'{self.root.ids.doctor2.text}'
        #
        # print(self.dct)


    # def add_appoint2(self):
    #     self.dialog = MDDialog(title='Current appointments', text='',
    #                              buttons=[MDRectangleFlatButton(text='Ok',
    #                                                             text_color=self.theme_cls.primary_color
    #                                                             , on_release=self.close_dialog)])
    #     self.dialog.text = f'{self.root.ids.doctor2.text}'






MyDoctorApp().run()
#
# MDBottomNavigationItem:
# name: 'screen 1'
# text: 'Main page'
# icon: 'home'
#
# MDLabel:
# text: 'Hello World'
# halign: 'center'
#
# MDBottomNavigationItem:
# name: 'screen 2'
# text: 'appointment'
# icon: 'book-open-outline'
#
# MDBottomNavigationItem:
# name: 'screen 3'
# text: 'Doctors'
# icon: 'doctor'
#
# MDBottomNavigationItem:
# name: 'screen 4'
# text: 'clinics'
# icon: 'hospital'
#
# MDBottomNavigationItem:
# name: 'screen 5'
# text: 'My profile'
# icon: 'account'

