from kivy.config import Config
Config.set("graphics", "width", "550")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", "0")
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import SlideTransition, RiseInTransition
from kivymd.uix.list import *
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker
import firebase_admin
from firebase_admin import db, credentials
cred = credentials.Certificate('my-third-project-a46f2-firebase-adminsdk-s869n-f7b3366d45.json')
firebase_admin.initialize_app(cred,
{'databaseURL': 'https://my-third-project-a46f2-default-rtdb.europe-west1.firebasedatabase.app/'})


class Screens(MDScreenManager):

    login = False

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

    def on_cancel(self, value, instance):
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
        self.dialog_1 = None
        self.dialog_2 = None
        self.login = False
        # self.dict = {}
        ref = db.reference("/doctors")
        self.dict = ref.get()
        self.dict_2 = {}
        self.data = {
                    'My profile': ['account','on_release', self.login_page_1],
                    'Home': ['home', 'on_press', self.home_1],

                }

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Gray'
        self.theme_cls.material_style = "M2"
        return Builder.load_file('CallDoctor.kv')

    def show_current_appoint(self):
        if self.login == False:
            self.root.current = 'screen_7'

        else:
            a = self.root.ids.show_doc.text
            b = self.root.ids.show_hosp.text
            c = self.root.ids.show_date.text

            # ref = db.reference("/doctors")
            #
            # self.dict = ref.get()
            #
            # ref.update({f'{c}': f'{a}/{b}'})
            self.root.ids.show_all_app.text = f'{a} \n {b} \n {c}'
            self.root.current = 'screen_2'

    def home_1(self, *args):
        self.root.current = 'main_screen'

    def dating(self, *args):
        if self.login == False:
            self.root.current = 'screen_7'
        else:
            self.root.current = 'screen_1'

    def login_page_1(self, *args):
        if self.login == False:
            self.root.current = 'screen_7'
        else:
            self.root.current = 'profile'


    def logger(self):
        ref = db.reference("/User")
        self.dict_2 = ref.get()
        for item in self.dict_2:
            if item == self.root.ids.user.text:
                if self.dict_2[item] == self.root.ids.password.text:
                    self.root.current = 'profile'
                    self.root.ids.profile_label.text = self.root.ids.user.text
                    self.login = True
                    print(self.dict_2)
                    print(self.login)

    def log_out(self):
        self.root.current = 'screen_7'
        self.root.ids.user.text = ''
        self.root.ids.password.text= ''
        self.login = False

    def confirm(self):
        if not self.dialog:
            self.dialog = MDDialog(title='Cofirmation', text='Press Ok to confirm',
                                   buttons=[MDRectangleFlatButton(text='Ok',
                                                                 text_color=self.theme_cls.primary_color,
                                                                  on_release= self.save_data),
                                            MDRectangleFlatButton(text='Cancel',
                                                                  text_color=self.theme_cls.primary_color,
                                                                  on_release=self.close_dialog)
                                            ])
        self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()

    def inform(self):
        if not self.dialog_1:
            self.dialog_1 = MDDialog(title='About Doctor',
                                    text='''- Doctor : Specialist / Dentist\n\n- Work stage: About 10 years\n\n- Work place: Moscow, Druzhba place 21,\n\n- Study place: University of Novorosisk,Russia tel: 012345''',
                                   buttons=[ MDRectangleFlatButton(text='Close',
                                                      text_color=self.theme_cls.primary_color,
                                                      on_release=self.close_dialog_1)
                                            ])
        self.dialog_1.open()

    def close_dialog_1(self, instance):
        self.dialog_1.dismiss()

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def inform_2(self):
        if not self.dialog_2:
            self.dialog_2 = MDDialog(title='About Clinic',
                                    text='''- Clinic : Adress  / Moscow city\n\n- Work stage: About 25 years\n\n- Work place: Moscow, Druzhba place 21,\n\n- Contact / tel: 012345''',
                                   buttons=[ MDRectangleFlatButton(text='Close',
                                                      text_color=self.theme_cls.primary_color,
                                                      on_release=self.close_dialog_2)
                                            ])
        self.dialog_2.open()

    def close_dialog_2(self, instance):
        self.dialog_2.dismiss()



    def show_all_appoint(self):

        if self.login:

            ref = db.reference("/doctors")
            self.dict = ref.get()

            word = ''
            for key, value in self.dict.items():
                word = f'{word} \n\n  {key} \n {value} '
                self.root.ids.show_all_app.text =f'{word}'
                self.root.current = 'screen_2'


        else:
            self.root.current = 'screen_7'


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

    def save_data(self,*args):
        a = self.root.ids.show_doc.text
        b = self.root.ids.show_hosp.text
        c = self.root.ids.show_date.text

        ref = db.reference("/doctors")

        self.dict = ref.get()

        ref.update({ f'{c}': f'{a}/{b}'})
        self.root.ids.show_all_app.text = f'{a} \n {b} \n {c}'

    def sign_up(self, **kargs):
        self.root.current = 'screen_8'

    def register(self):
        a = self.root.ids.user_1.text
        b = self.root.ids.password_1.text

        ref = db.reference("/User")
        self.root.current = 'screen_7'
        self.dict = ref.get()

        ref.update({f'{a}': f'{b}'})

        self.login = False

        print(self.dict_2)

    def clear(self):

        self.root.ids.user_1.text = ''
        self.root.ids.password_1.text = ''
        self.root.ids.age_1.text = ''
        self.root.ids.sex_1.text = ''
        self.root.ids.city_1.text = ''

        print(self.dict)
    def clear_current(self):
        self.root.ids.show_doc.text = 'Doctor: '
        self.root.ids.show_hosp.text = 'Clinic: '
        self.root.ids.show_date.text = 'Date: '





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


# {'Ivanov SergeiSt / St Petersburg, Kuzia str.21': 1,
#         'Malicheva Aleksandra / St Petersburg, Slava str.17': 2,
#         'Sergeev mikhail / Moscow, Arbat street 2':3,
#         'Antonova Uliyana / Moscow,Pionerskaya 12' : 4,
#         'Kuzmina Olga / Ekaterineburg,Plaza place' : 5,
#         'Mironov Sergei / Rostov on Don,Korolev st. 9' : 6
#
#         }


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



# MDCard:
    # radius:0
    # padding:50
    # md_bg_color:  0, 0.2, 0.1, 0.4
    # shadow_color:0, 0, 0
    # size_hint:1, 0.9
    # MDFloatLayout:
    #     MDRoundFlatIconButton:
    #         id: choose_doc
    #         text: 'Show my current appointment'
    #         icon: 'book'
    #         text_color: 0.2, 0.2, 0.2, 1
    #         icon_color: 0.2, 0.2, 0.2, 1
    #         font_size: 20
    #         pos_hint: {'center_x':0.5, 'center_y':0.7}
    #         on_press:
    #             app.show_current_appoint()
    #
    #     MDRoundFlatIconButton:
    #         id: choose_doc
    #         text: 'Show all appointments'
    #         icon: 'book'
    #         text_color: 0.2, 0.2, 0.2, 1
    #         icon_color: 0.2, 0.2, 0.2, 1
    #         font_size: 20
    #         pos_hint: {'center_x':0.5, 'center_y':0.5}
    #         on_press:
    #             app.show_all_appoint()
    #
