
import time
from flet import *
import re

import requests

from config.utils import *
from apps.account.utils import *


def email_validator(email_field):
        
        email= email_field.value
        
        d,j,k=0,0,0
        if len(email)!=0:
            if email[0].isalpha():
                if email.count("@")==1:
                    
                    if (email[-4]==".")|(email[-3]=="."):
                        for part in email.split("@"):
                            for i in part:
                                if not i.isspace():
                                    if i=="_"or i=="-" or i.isalnum():

                                        email_field.error_text=''
                                        # email_field.focus()
                                        email_field.valid=True


                                        email_field.update()
                                    else:
                                        email_field.error_text="Invalid characters present in your email "
                                        # email_field.focus()
                                        email_field.update()
                                else:
                                    email_field.error_text="Email cannot contain spaces"
                                    # email_field.focus()
                                    email_field.update()
                                    
                        
                    else:
                        email_field.error_text="Email is invalid with no domain extension"
                else:
                    email_field.error_text="Invalid email format"
                    email_field.focus()
                    email_field.update()
                        
            else:
                email_field.error_text="Email must start with alphabet"
                email_field.focus()
                email_field.update()
        
def password_validator(password_field):
    password=password_field.value
    if len(password)!=0:
        if len(password)>=8:
            if  re.search(r'[a-z]',password):   
                if re.search(r'[A-Z]',password):
                    if  re.search(r'[0-9]',password):
                        if  re.search(r'[!@$%&*()_+-=<>:"?|/\\]',password):

                            password_field.error_text=''
                            password_field.valid=True
                            password_field.update()
                        else:    
                            password_field.error_text='At least one !@$%&*()_+-=<>:"?|/\\ special character is required '
                            password_field.update()
                    else:        
                        password_field.error_text=' At least 1 number is requied'
                        password_field.update()
                else:
                    password_field.error_text='Capital letters are required '
                    password_field.update()
            else:
                password_field.error_text='lowercase letters are required'
                password_field.update()

        else:
            password_field.error_text='At least 8 characters are required '

            password_field.update()
            
def code_verifier(code):
    password=code.value
    if len(password)!=0:
        
            if len(password)==5+1:


                code.error_text=''
                code.valid=True
                code.update()
            else:
                code.error_text=f'Exactly {8-2} characters are required '
                code.update()
                
def name_verifier(name):
    password=name.value
    if len(password)!=0:
       
            if password.isalpha():


                name.error_text=''
                name.valid=True
                name.update()
            else:
                name.error_text=f'Name can only alphabetic character'
                name.update()


def regenerate(self):
    if self.count>=8:
            
        self.verify_dialog.open=False
        self.password.value=''
        self.email.value=''
        self.count=0
        self.page.update()

    else:        

        self.count+=1
        self.timer.seconds=120
        self.verify_dialog.update()
        self.resend_btn.text=self.text_info
        self.resend_btn.disabled=True
        self.v_btn.disabled=False
        self.verification_code.focus()

        self.verify_dialog.open=True
        self.verify_dialog.update()
        cookies={'email':str(self.email.value)}
        response=requests.get(
                f'{base_url}account_api/verify/',
                data={},
                cookies=cookies,
                
                )
        if response.status_code==200:
            self.v_head.sub_title=f'A new code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
            self.v_head.update()
     
def verify_finale(self,redirect_url):
    if self.count<3:
        cookies1={'email':str(self.email.value)}
        try:
            code=str(self.verification_code.value)
            r=requests.post(
                f'{base_url}account_api/verify/',
                data={
                    'code':code,
                    },
                    cookies=cookies1
                )
            if r.status_code==200:
                print('pk' ,str(r.cookies['pk'])  )
                self.page.client_storage.set(f'{project_}.pk',str(r.cookies['pk']) )

                res=requests.post(
                f'{base_url}api/token/',
                data={
                   'username':str(self.email.value),
                    'password':str(self.password.value),
                    },
                )
                self.page.client_storage.set(f'{project_}.email',str(self.email.value) )
                self.page.client_storage.set(f'{project_}.authenticated',True)
                self.page.client_storage.set(f'{project_}.access_token',str(res.json()["access"] ))
                self.page.client_storage.set(f'{project_}.refresh_token',str(res.json()["refresh"] ))

                time.sleep(2)
                print('done')
                go_to_page(route=redirect_url,self=self,app_name=None)
                print('gone')
                self.update()



                            
            
            else:
                self.v_head.sub_title="That doesn't match the code sent to"
                self.page.update()
            if self.count==3:
                self.verify_dialog.open=False
                self.password.value=''
                self.email.value=''
                self.page.update()

        except Exception as ero:
            print(ero)    
                 
def enable_resend(self):
    while self.running:
        if self.timer.seconds==0:

            self.resend_btn.content.value='Resend Code'
            self.resend_btn.disabled=False
            self.v_btn.disabled=True

            # self.v_btn.disabled=False
            # self.v_btn.update()
            # self.verification_code.focus()
            # self.verification_code.valid=''

            self.verify_dialog.actions=[self.v_btn,self.resend_btn]
            self.verify_dialog.update()
        
def refresh_user_token(self):
    while self.page.client_storage.get(f'{project_}.refresh_token') and self.running:
        res=requests.post(
            f'{base_url}api/token/refresh/',
            data={
                "refresh":str(self.page.client_storage.get(f'{project_}.refresh_token'))
                },
            )
        if res.status_code==200:
            self.page.client_storage.set(f'{project_}.access_token',str(res.json()["access"] ))
            self.page.client_storage.set(f'{project_}.refresh_token',str(res.json()["refresh"] ))
            self.page.client_storage.set(f'{project_}.authenticated',True)

        else :
            self.page.go(f'/{project_}/{app_name_}/login')


def logout_user(self):
    r=make_authenticated_post_request(self=self,url='account_api/logout',data=None,cookie=None,key=None) 
    if r.status_code==200: 
        print('Logged out') 
        self.page.client_storage.remove(f'{project_}.email')
        self.page.client_storage.remove(f'{project_}.access_token')
        self.page.client_storage.remove(f'{project_}.refresh_token',)
        self.page.client_storage.set(f'{project_}.authenticated',False)
        print('cleared') 

        self.page.go(f'/{project_}/home')
    else:
        # self.page.go('/afarm/accounts/login')
        self.page.go(f'/{project_}/{app_name_}/login')
            
 
class AuthInputField(TextField):
    def __init__(self,type,field_hint,focus_input):
        super().__init__()
        self.hint_text=field_hint
        self.type=type
        self.valid=False
        self.color=colors.PRIMARY
        self.hint_style=TextStyle(color=colors.PRIMARY,size=12)

        if self.type=='password' or self.type=='code':
            self.password=True
        else:
            self.password=False  
        if self.type=='code':
            self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor='transparent'
        
        self.autofocus=focus_input
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.content_padding=5
        self.on_change=self.validators        
            
    def validators(self,e):
        if self.type=='password':
            return password_validator(password_field=self) 
        elif self.type=='email':
            return email_validator(email_field=self) 
        elif self.type=='code':
            return code_verifier(code=self)
                
        elif self.type=='name':
            return name_verifier(name=self)


class AuthInputContainer(Container):
    def __init__(self,icon_name,input_field:TextField):
        super().__init__()
        self.icon_name=icon_name
        # self.width=300

        self.input_field=input_field
        self.content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=self.icon_name,
                        size=14,
                        opacity=.85,
                        color=colors.PRIMARY

                    ),
                    self.input_field,
                ]

               ) 
        self.border=border.only(bottom=border.BorderSide(0.5,colors.PRIMARY,))
        self.height=43
    
    

    