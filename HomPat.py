from kivy.config import Config

Config.set("graphics", "width", "550")
Config.set("graphics", "height", "850")
Config.set("graphics", "resizable", "0")

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.icon_definitions import md_icons
import os, sys
from firebase import firebase
from kivymd.uix.pickers import MDDatePicker
from kivy_garden.mapview import MapSource
from firebase_admin import db, credentials



KV = '''
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import MapSource kivy_garden.mapview.MapSource


#MAIN SCREEN
Screens:
# MAIN PAGE
    MDScreen:
        name:'main'
        MDFloatLayout:
            #md_bg_color: 106/255, 118/255, 135/255, 1
            md_bg_color: 1, 1, 1, 1
            AsyncImage:
                source: 'https://cdn-icons-png.freepik.com/256/7918/7918355.png?uid=R158607450&ga=GA1.1.255225494.1726349966'
                pos_hint: {'center_x':0.18, 'center_y':0.9 }
                size_hint: 0.2, 0.2

            MDTextButton:
                text: 'About us'
                italic: True
                bold: True
                underline: True
                font_size: 25
                font_name: 'Gothic'
                pos_hint: {'center_x':0.8, 'center_y':0.9 }
                theme_text_color: "Custom"
                text_color: (0.5, 0.5, 0.7, 1)
                on_release:
                    root.current = 'about_us'
                    root.transition.direction = 'left'

            AsyncImage:
                source: 'https://img.freepik.com/premium-vector/medical-clipboard-prescription-insurance-document-health-check-doctor-diagnosis-record-med_926199-4120286.jpg?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                pos_hint: {'center_x':0.5, 'center_y':0.62}
                size_hint: 0.65, 0.65

            MDLabel:
                text: 'HiTech'
                font_name: 'Gothic'
                font_size: 40
                pos_hint: {'center_y': 0.4}
                halign: 'center'
                color: 0.15, 0.15, 0.15, 1
                
            MDLabel:
                text: 'doctor'
                font_name: 'verdana'
                font_size: 15
                pos_hint: { 'center_x': 1 , 'center_y': 0.37}
                #halign: 'center'
                color: 0.15, 0.15, 0.15, 1

            MDLabel:
                text: 'We take care of you and your Family'
                font_name: 'Verdana'
                font_size: 20
                size_hint_x: 0.8
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                halign: 'center'
                color: 0.5, 0.5, 0.5, 1

            MDFillRoundFlatIconButton:
                icon:'car-emergency'
                text: 'Applications'
                font_size: 17
                pos_hint: {'center_x':0.3, 'center_y':0.22 }
                on_release:
                    app.admin_form()
                    root.current = 'applications'
                    root.transition.direction = 'left'

            MDFillRoundFlatIconButton:
                icon:'account'
                text: 'My account'
                font_size: 17
                pos_hint: {'center_x':0.7, 'center_y':0.22 }
                on_release:
                    app.my_account()
                    root.current = 'profile'
                    root.transition.direction = 'left'

            MDFillRoundFlatIconButton:
                icon:'wallet'
                text: 'My Wallet'
                font_size: 17
                pos_hint: {'center_x':0.3, 'center_y':0.15 }
                on_release:
                    root.current = 'wallet'
                    root.transition.direction = 'left'

            MDFillRoundFlatIconButton:
                icon:'calendar'
                text: 'Appointments'
                font_size: 17
                pos_hint: {'center_x':0.7, 'center_y':0.15 }
                #on_release:
                    #app.to_clinics()
                    #root.transition.direction = 'left'
                    
# ABOUT PAGE
    MDScreen:
        name:'about_us'
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1

            AsyncImage:
                source: 'https://cdn-icons-png.freepik.com/256/16970/16970864.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                pos_hint: {'center_x':0.8, 'center_y':0.9 }
                size_hint: 0.15, 0.15

            MDIconButton:
                icon: 'arrow-left'
                pos_hint:{'center_x':0.1, 'center_y':0.9}
                on_release:
                    root.current = 'main'
                    root.transition.direction = 'right'

            MDLabel:
                text: 'Who we are'
                italic: True
                bold: True
                underline: True
                font_size: 32
                halign: 'center'
                pos_hint: {'center_x':0.5, 'center_y':0.85 }
                theme_text_color: "Custom"
                text_color: (0.5, 0.5, 0.5, 1)

            AsyncImage:
                source: 'https://img.freepik.com/free-vector/health-professional-team_23-2148495378.jpg?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                pos_hint: {'center_x':0.5, 'center_y':0.65}
                size_hint: 0.6, 0.6

            MDLabel:
                text: 'Each our services is on a mission to provide compassionate, world-class care to each person, in every connection. That includes 1.3 million patients from over 13 countries who visit our Clinic campuses each year. We also train future health leaders who share our drive to transform health care'
                font_name: 'Verdana'
                font_size: 18
                size_hint: 0.8, 0.3
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                halign: 'center'
                color: 0.5, 0.5, 0.7, 1

            MDTextButton:
                text: 'Contact us'
                font_size: 18
                italic: True
                bold: True
                underline: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.25}

            MDLabel:
                text: 'Join us '
                italic: True
                bold: True
                font_size: 15
                halign: 'center'
                pos_hint: {'center_x':0.5, 'center_y':0.17 }
                theme_text_color: "Custom"
                text_color: (0.5, 0.5, 0.5, 1)

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: 0.5, 0.05
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                AsyncImage:
                    source: 'https://cdn-icons-png.freepik.com/256/14857/14857368.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                AsyncImage:
                    source: 'https://cdn-icons-png.freepik.com/256/2504/2504903.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                AsyncImage:
                    source: 'https://cdn-icons-png.freepik.com/256/2111/2111463.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    
# APPLICATION
    MDScreen:
        name:'applications'
        md_bg_color:   100/255, 118/255, 118/255, 0.6
        MDLabel:
            text: 'APPLICATIONS'
            font_size: 32
            font_name: 'Gothic'
            halign: 'center'
            pos_hint: {'center_y': 0.95}
            
        MDIconButton:
            icon: 'arrow-left'
            pos_hint:{'center_x':0.1, 'center_y':0.9}
            on_release:
                root.current = 'main'
                root.transition.direction = 'right'
                
        MDIconButton:
            icon: 'google-maps'
            pos_hint:{'center_x':0.7, 'center_y':0.87}
            on_release:
                app.on_location()
                root.current = 'location'
                root.transition.direction = 'right'
            
        MDLabel:
            text: 'To do'
            font_size: 25
            italic: True
            underline: True
            bold: True
            halign: 'center'
            pos_hint: {'center_y': 0.87}
            
        MDCard:
            id: card_todo
            size_hint:None, None
            size: 420, 300
            pos_hint: {'center_x':0.5, 'center_y':0.65}
            elevation: 5
            padding: 20
            spacing: 5
            radius: 20
            orientation: 'horizontal'
            MDBoxLayout:
                orientation: 'vertical'
                cols: 1
                size_hint_x : 1
                MDLabel:
                    id: todo_app_num
                    text: 'App#: '
                    italic: True
                    halign: 'center'
                    font_size: 20
                    bold: True
                    color: 0.5, 0.5, 0.5, 1
                MDLabel:
                    id: todo_name
                    text: 'Name: '
                    italic: True
                    bold: True
                    font_size: 17
                    color: 0.5, 0.5, 0.5, 1
                MDLabel:
                    id: todo_age
                    text: 'Age: '
                    italic: True
                    bold: True
                    color: 0.5, 0.5, 0.5, 1
                    font_size: 17
                MDLabel:
                    id: todo_gender
                    text: 'Gender: '
                    italic: True
                    bold: True
                    color: 0.5, 0.5, 0.5, 1
                    font_size: 17
                MDLabel:
                    id: todo_address
                    text: 'Address: '
                    italic: True
                    bold: True
                    color: 0.5, 0.5, 0.5, 1
                MDLabel:
                    id: todo_comments
                    text: 'Comments: '
                    italic: True
                    bold: True
                    color: 0.5, 0.5, 0.5, 1
                    font_size: 17
        
        MDFillRoundFlatIconButton:
            text: 'Accept'
            icon: 'check-circle'
            font_size: 17
            pos_hint: {'center_x':0.8, 'center_y':0.4}
            on_release:
                app.accepted()
        MDFillRoundFlatIconButton:
            text: 'Ignore'
            icon: 'close-circle'
            font_size: 17
            pos_hint: {'center_x':0.2, 'center_y':0.4}
            on_release:
                app.ignored()
            
        MDLabel:
            text: 'To close'
            font_size: 25
            italic: True
            underline: True
            bold: True
            halign: 'center'
            pos_hint: {'center_y': 0.35}
            
        MDCard:
            id: card_to_close
            size_hint:None, None
            size: 420, 100
            pos_hint: {'center_x':0.5, 'center_y':0.25}
            elevation: 5
            padding: 20
            spacing: 5
            radius: 20
            orientation: 'horizontal'
            MDLabel:
                id: to_close
                text: 'App#:'
                font_size: 32
                italic: True
                bold: True
                halign: 'center'
                pos_hint: {'center_y': 0.35}
            
        MDFillRoundFlatIconButton:
            text: 'Close'
            icon: 'check-all'
            font_size: 17
            pos_hint: {'center_x':0.8, 'center_y':0.15}
            on_release:
                app.closed()
            
        MDFillRoundFlatIconButton:
            text: 'refresh'
            icon: 'refresh'
            font_size: 17
            pos_hint: {'center_x':0.2, 'center_y':0.07}
            on_release:
                app.refresh_app()
                
                
#SHOW ALL_APPLICATIONS

    MDScreen:
        name:'all_application'
        md_bg_color: 100/255, 118/255, 118/255, 0.6
        MDFloatLayout:
            MDIconButton:
                icon: 'arrow-left'
                pos_hint:{'center_x':0.1, 'center_y':0.9}
                on_release:
                    root.current = 'profile'
                    root.transition.direction = 'left'
            MDLabel:
                text: 'HISTORY APPLICATIONS'
                font_size: 32
                font_name: 'Gothic'
                halign: 'center'
                pos_hint: {'center_y': 0.9}
            ScrollView
                bar_width: 20
                size_hint: (0.8, 0.7)
                pos_hint: {'center_x':0.5, 'center_y':0.5 }
                MDLabel:
                    id: show_all_app
                    text: ' '
                    size_hint_y: None
                    adaptive_height: True
                    font_size: 20
                    bold: True
                    halign :'center'
                    padding: 20
            
            

#SHOW ALL_TRANSACTIONS

    MDScreen:
        name:'all_transactions'
        md_bg_color: 100/255, 118/255, 118/255, 0.6
        MDFloatLayout:
            MDIconButton:
                icon: 'arrow-left'
                pos_hint:{'center_x':0.1, 'center_y':0.9}
                on_release:
                    root.current = 'profile'
                    root.transition.direction = 'left'
            MDLabel:
                text: 'HISTORY TRANSACTIONS'
                font_size: 32
                font_name: 'Gothic'
                halign: 'center'
                pos_hint: {'center_y': 0.9}
            ScrollView
                bar_width: 20
                size_hint: (0.8, 0.7)
                pos_hint: {'center_x':0.5, 'center_y':0.5 }
                MDLabel:
                    id: show_all_trans
                    size_hint_y: None
                    adaptive_height: True
                    font_size: 20
                    bold: True
                    halign :'center'
                    padding: 20

#WALLET
 
    MDScreen:
        name:'wallet'
        md_bg_color:  100/255, 118/255, 118/255, 0.6
        MDLabel:
            id: wallet_label
            text: 'MY WALLET'
            font_name: 'Gothic'
            font_size: 32
            halign: 'center'
            size_hint_y: None
            pos_hint: {'center_x':0.5, 'center_y':0.93}
            
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':0.1, 'center_y':0.91}
            on_release:
                root.current = 'main'
                root.transition.direction = 'right' 
      
        MDCard:
            size_hint: None, None
            size: 400, 600
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            elevation: 10
            padding: 20
            spacing: 8
            radius: 30
            orientation: 'vertical'      
            AsyncImage:
                source:'https://cdn-icons-png.freepik.com/256/7844/7844508.png?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                
            MDLabel:
                text: 'You have:'
                font_name: 'Verdana'
                font_size: 25
                halign: 'center'
                size_hint_y: None
                color: 0.5, 0.5, 0.5, 1
                height: self.texture_size[1]
                padding_y: 1

            MDLabel:
                id: wallet_med
                text: '0 meds'
                font_name: 'Verdana'
                font_size: 25
                halign: 'center'
                size_hint_y: None
                color: 0.5, 0.8, 0.5, 1
                height: self.texture_size[1]
                padding_y: 1

            MDFillRoundFlatIconButton:
                icon:'refresh'
                text: 'refresh meds'
                pos_hint:{'center_x':0.5}
                on_release:
                    app.refresh()
                    
            MDTextField:
                id: med_date
                mode: 'line'
                hint_text: 'YY/MM/DD'
                icon_right: 'numeric'
                size_hint_x: None
                width: 200
                font_size: 20
                pos_hint:{'center_x':0.5}
                on_double_tap:
                    app.show_date_picker()

            MDTextField:
                id: med_contrat
                mode: 'line'
                hint_text: 'request#'
                icon_right: 'numeric'
                size_hint_x: None
                width: 200
                font_size: 20
                pos_hint:{'center_x':0.5}

            MDTextField:
                id: sum
                mode: 'line'
                hint_text: 'sum '
                icon_right: 'cash-multiple'
                size_hint_x: None
                width: 200
                font_size: 20
                pos_hint:{'center_x':0.5}

        MDFillRoundFlatIconButton:
            text: 'SEND'
            icon: 'send-check'
            font_size: 17
            pos_hint:{'center_x':0.5, 'center_y':0.08}
            on_release:
                app.wallet_transaction()
                root.transition.direction = 'left'
                       
#ACCOUNT

    MDScreen:
        name:'profile'
        md_bg_color:  100/255, 118/255, 118/255, 0.6
        MDLabel:
            id: profile
            text: 'MY ACCOUNT'
            font_name: 'Gothic'
            font_size: 32
            halign: 'center'
            size_hint_y: None
            pos_hint: {'center_x':0.5, 'center_y':0.95}
            
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_x':0.1, 'center_y':0.91}
            on_release:
                root.current = 'main'
                root.transition.direction = 'right' 
        
        MDCard:
            size_hint: None, None
            size: 500, 550
            pos_hint: {'center_x':0.5, 'center_y':0.55}
            elevation: 10
            padding:5
            spacing:1
            radius: 30
            orientation: 'vertical'  
            MDBoxLayout:
                orientation: 'horizontal'
                cols: 3
                AsyncImage:
                    id: account_pic
                    source: 'https://img.freepik.com/premium-vector/confident-female-medical-professional-portrait_1324825-1615.jpg?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        id: name
                        text: 'Name:'
                        font_size: 17
                    MDLabel:
                        text: 'Age:'
                        id: age
                        font_size: 17
                    MDLabel:
                        text: 'Gender:'
                        id: gender
                        font_size: 17
                    MDLabel:
                        text: 'City:'
                        id: city
                        font_size: 17
                    MDLabel:
                        text: 'Order#:'
                        id: order
                        font_size: 17
                    MDLabel:
                        id: education
                        text: 'Education:'
                        font_size: 17
                        
        MDFillRoundFlatIconButton:
            text: 'All transactions'
            font_size: 17
            icon: 'cash-multiple'
            pos_hint: {'center_x':0.75, 'center_y':0.1}
            on_release:
                app.all_transactions()
                root.current = 'all_transactions'
                root.transition.direction = 'right'
                
            
        MDFillRoundFlatIconButton:
            text: 'All Applications'
            icon: 'file-multiple'
            font_size: 17
            pos_hint: {'center_x':0.25, 'center_y':0.1}
            on_release:
                app.all_applications()
                root.current = 'all_application'
                root.transition.direction = 'right'
                
#SHOW LOCATION

    MDScreen:
        name: 'location'
        md_bg_color: 106/255, 118/255, 135/255, 1
        MDFloatLayout:
            MDIconButton:
                icon:'arrow-left'
                size_hint: 0.1, 0.1
                pos_hint:{'center_x': 0.2, 'center_y': 0.9}
                on_release:
                    root.current = 'applications'
                    root.transition.direction = 'right'
            MDLabel:
                size_hint: 0.9, 0.1
                pos_hint:{'center_x': 0.7, 'center_y': 0.9}
                text: 'CLINIC LOCATIONS'
                font_size: 25
            MapView:
                id: maps
                size_hint: 0.9, 0.6
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                zoom: 15
                MapMarkerPopup:
                    id: maps_1
                    popup_size: dp(230), dp(130)
                    #on_release:
                        #app.choose_cl3()
                        #app.appointment()
                        #root.transition = SlideTransition(direction='right')
                    MDBoxLayout:
                        padding:'4dp'
                        MDLabel:
                            text:'Moscow,Arbat street 2'
                            markup: True
                            halign: 'center'
 
            
'''

class Screens(MDScreenManager):
    pass
class Home_docApp(MDApp):


    def __init__(self):
        super().__init__()
        self.firebase = None
        self.data = {
            'My profile': ['account'],
            'Home': ['home']
        }

        self.data_2 = {
            'Home': ['home']
        }
        self.c = False
        self.x = False
        self.dialog_error = None

    def my_account(self):
        try:
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            doctors = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/Doctors', '')

            for el in doctors:
                if doctors[el]['order'] == '3256':
                    self.root.ids.name.text = f'Name: {doctors[el]["name"]} '
                    self.root.ids.age.text = f'Age: {doctors[el]["age"]} '
                    self.root.ids.gender.text = f'Gender: {doctors[el]["gender"]} '
                    if doctors[el]['gender'] == 'male':
                        self.root.ids.account_pic.source = 'https://img.freepik.com/premium-vector/young-man-white-coat-stands-office-environment-holding-several-colorful-files-documents-he-exudes-confidence-with-friendly-smile_520881-14821.jpg?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                    else:
                        self.root.ids.account_pic.source = 'https://img.freepik.com/premium-vector/confident-female-medical-professional-portrait_1324825-1615.jpg?uid=R158607450&ga=GA1.1.255225494.1726349966&semt=ais_hybrid'
                    self.root.ids.city.text = f'City: {doctors[el]["city"]} '
                    self.root.ids.order.text = doctors[el]["order"]
                    self.root.ids.education.text = f'Education: {doctors[el]["education"]} '

        except:
            self.dialog_Error()
    def dialog_Error(self):

        if not self.dialog_error:
            self.dialog_error = MDDialog(title='Message',
                                         text='An error occured or \n!!Not internet connection!!\n Maybe application will not correctly work')

            self.dialog_error.open()

    def admin_form(self):
        if self.c == False:
            try:
                self.firebase = firebase.FirebaseApplication(
                    'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

                forms = self.firebase.get(
                    'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/admin_form', '')


                for el in forms:
                    if forms[el]['App num'] == '1':
                        self.root.ids.todo_name.text = f'Name: {forms[el]["Name"]} '
                        self.root.ids.todo_age.text = f'Age: {forms[el]["Age"]} '
                        self.root.ids.todo_gender.text = f'Gender: {forms[el]["Gender"]} '
                        self.root.ids.todo_address.text = f'Address: {forms[el]["Address"]} '
                        self.root.ids.todo_comments.text = f'Comments: {forms[el]["Comments"]} '
                        self.root.ids.todo_app_num.text = f'App#: {forms[el]["App num"]} '

            except:
                self.dialog_Error()
        else:
            self.root.ids.todo_name.text = f'Name: '
            self.root.ids.todo_age.text = f'Age: '
            self.root.ids.todo_gender.text = f'Gender:  '
            self.root.ids.todo_address.text = f'Address: '
            self.root.ids.todo_comments.text = f'Comments: '
            self.root.ids.todo_app_num.text = f'App#: '


    def accepted(self):

        try:
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            forms = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/admin_form', '')


            for el in forms:
                if forms[el]['App num'] == '1':
                    self.root.ids.to_close.text = f'App#: {forms[el]["App num"]} '

            self.root.ids.todo_name.text = f'Name: '
            self.root.ids.todo_age.text = f'Age: '
            self.root.ids.todo_gender.text = f'Gender:  '
            self.root.ids.todo_address.text = f'Address: '
            self.root.ids.todo_comments.text = f'Comments: '
            self.root.ids.todo_app_num.text = f'App#: '
            self.c = True
            self.x = True
            self.root.ids.card_to_close.md_bg_color = 13/255, 238/255, 144/255, 0.7

        except:
            self.dialog_Error()

    def closed(self):
        try:
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            forms = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/admin_form', '')

            for el in forms:
                if forms[el]['App num'] == '1':
                    data = {
                        'id_doc': f'{self.root.ids.order.text}',
                        'Name': f'{forms[el]["Name"]} ',
                        'Age': f'{forms[el]["Age"]} ',
                        'Gender': f'{forms[el]["Gender"]} ',
                        'Address': f'{forms[el]["Address"]} ',
                        'Comments': f'{forms[el]["Comments"]} '
                    }
                    self.firebase.post(
                        'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/store_form', data)

        except:
            self.dialog_Error()

        self.c = False
        self.x = False
        self.root.ids.card_to_close.md_bg_color = 1, 1, 1, 1
        self.root.ids.to_close.text = f'App#: '

    def ignored(self):
        self.root.ids.todo_name.text = f'Name: '
        self.root.ids.todo_age.text = f'Age: '
        self.root.ids.todo_gender.text = f'Gender:  '
        self.root.ids.todo_address.text = f'Address: '
        self.root.ids.todo_comments.text = f'Comments: '
        self.root.ids.todo_app_num.text = f'App#: '
        self.c = True
        self.x = False

    def refresh_app(self):
        if self.x == True:
            self.c = True
        else:
            self.c = False
            self.admin_form()

    def wallet_transaction(self):
        try:
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            doctors = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/Doctors', '')

            for el in doctors:
                if doctors[el]['order'] == '3256':
                    self.root.ids.order.text = f'{doctors[el]["order"]} '
                    a = self.root.ids.med_date.text
                    b = self.root.ids.med_contrat.text
                    c = self.root.ids.sum.text
                    d = self.root.ids.order.text

                    data = {
                        'date_trans': a,
                        'contrat_trans': b,
                        'sum': c,
                        'doc_order': d,
                    }
                    self.firebase.post(
                        'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/Doctor_transaction',data)

                    self.erase_current_transaction()

        except:
            self.dialog_Error()

    def erase_current_transaction(self):
        self.root.ids.med_date.text = ''
        self.root.ids.med_contrat.text = ''
        self.root.ids.sum.text = ''

    def all_applications(self):

        try:
            word = ''
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            forms = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/store_form', '')

            for el in forms:
                num = len(forms)
                if forms[el]['id_doc'] == self.root.ids.order.text:
                    word = f'{word}\n\nName: {forms[el]["Name"]}\nAge: {forms[el]["Age"]}\nGender: {forms[el]["Gender"]}\nAddress: {forms[el]["Address"]}\nComments: {forms[el]["Comments"]}'
                    self.root.ids.show_all_app.text = f'{word}'
                    num += 1

        except:
            self.root.ids.show_all_app.text = 'Not applications yet or internet failed'


    def all_transactions(self):

        try:
            word = ''
            self.firebase = firebase.FirebaseApplication(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/', None)

            forms = self.firebase.get(
                'https://my-fourth-project-25e49-default-rtdb.europe-west1.firebasedatabase.app/Doctor_transaction', '')

            for el in forms:
                if forms[el]['doc_order'] != self.root.ids.order.text:
                    word = f'{word}\n\nRequest#: {forms[el]["contrat_trans"]}\nDate of request: {forms[el]["date_trans"]}\nSum: {forms[el]["sum"]}$'
                    self.root.ids.show_all_trans.text = f'{word}'

        except:
            self.root.ids.show_all_trans.text = 'Not request yet or internet failed'


    def on_location(self):

        self.root.ids.maps.lat = -4.301467
        self.root.ids.maps.lon = 15.316689
        self.root.ids.maps_1.lat = -4.301467
        self.root.ids.maps_1.lon = 15.316689

    def on_save(self, value, instance, date_range):
        self.root.ids.med_date.text = f'{instance}'

    def on_cancel(self, value, instance):
        self.root.ids.med_date.text = f'No dates'

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        # date_dialog = MDDatePicker(mode='range')
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()



    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)


Home_docApp().run()
