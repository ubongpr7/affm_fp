import datetime
import sqlite3
import threading
from flet import *
import requests
import time
from math import pi
from http import cookies

from base.app_bar_widget import *
from widgets.auth_widgets import *
from base.base_ import  *
from widgets.buttons_widget import column_set
from widgets.images import *
from widgets.page_widget import sections_container
from widgets.text_input_widget import NumberInput
from widgets.text_widget import  * 
from config.utils import *
from .utils import *
from widgets.countdown import CountDown

class  Registration(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()

        
        self.page=page
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.auth_=auth_
        
        self.email= AuthInputField(field_hint='Email',focus_input=True,type='email')              
        self.password= AuthInputField(field_hint='Password',focus_input=True,type='password')              
        self.confirm_email= AuthInputField(field_hint='Confirm Email ',focus_input=False,type='email') 

        self.confirm_password= AuthInputField(field_hint='Confirm password',focus_input=True,type='password')
        

        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.email_verifier=Text(color=colors.RED_300,height=0)

        self.heading=PageHeading_2(main_title='LernOn Registration ',bg_color=None,main_size=22,sub_title='Fill  the required fields apppropriately', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[
                        self.divider,
                        self.heading,
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.email),
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.confirm_email),
                        self.email_verifier,
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.password),
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.confirm_password),
                        self.password_verifier,
                        ElevatedButton('Register',width=300, color=colors.PRIMARY,bgcolor=colors.ON_PRIMARY,on_click=self.fill_validation),
                        TextButton('Login instead', on_click=lambda _:go_to_page(self=self, route='login',app_name=app_name_) ),
                        Divider()
                        ],
                horizontal_alignment='center',
                alignment='center',auto_scroll=True),
            bgcolor=colors.SECONDARY_CONTAINER,
            padding=20,
            border_radius=12,

        )
        
        self.register_card=Card(
            width=400,
            elevation=15,
            content=self.view_container,


            )
        
        self.controls=[self.register_card,]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        self.auto_scroll=True
        self.verification_code=NumberInput(field_hint='Enter verification code',type='num')              

        self.text_info='Code expires after'
        self.timer=CountDown(seconds=90,text_info='')
        self.resend_btn=TextButton(text=f"{self.text_info}", on_click=self.verify_regenerate,disabled=True)
        self.v_head=PageHeading_2(main_title='',bg_color=colors.SECONDARY_CONTAINER,main_size=18,sub_title=' ', text_color=colors.PRIMARY, sub_size=10)
        self.count=0
        self.v_btn=ElevatedButton(text="Verify",bgcolor=colors.ON_PRIMARY, on_click=self.verify_user)


        self.verify_dialog = AlertDialog(
            title=Text("Welcome  To LernOn"),

            content=Column(
                controls=[
                    self.v_head,
                    Row(controls=[self.verification_code,]),
                
                ], 
            tight=True),
        actions=[
                self.v_btn,
                self.resend_btn,
                self.timer,



                 ],
        actions_alignment="center",
    )
    
    def fill_validation(self,e):
        if  self.email.value=='' or self.confirm_email.value=='':
            self.email_verifier.value='The two email fields are required'
            self.email_verifier.height=20
            
            self.email_verifier.update()
        else:
            if self.email.value!= self.confirm_email.value:
                self.email_verifier.value='The two emails do not match'
                self.email_verifier.height=20
                self.email_verifier.update()
            else: 
                self.email_verifier.value=''
                self.email_verifier.height=0
                self.email_verifier.update()
               
        if  self.password.value=='' or self.confirm_password.value=='':
            self.password_verifier.value='The two password fields are required '
            self.password_verifier.height=20
            self.password_verifier.update()
        else:
            if self.password.value!= self.confirm_password.value:
                self.password_verifier.value='The two passwords do not match'
                self.password_verifier.height=20
                self.password_verifier.update()
            else: 
                self.password_verifier.value=''
                self.password_verifier.height=0
                self.password_verifier.update()
        if self.confirm_email.value!='' and self.confirm_password.value!='':        
            if self.password.value==self.confirm_password.value and self.email.value == self.confirm_email.value:
                cookies={'email':str(self.email.value)}

                r=requests.post(
                    f'{base_url}account_api/register/',
                    data={
                        'email':str(self.confirm_email.value),
                        'username':str(self.confirm_email.value),
                        'password':str(self.password.value),
                        },
                        cookies=cookies,

                    ) 
                if r.status_code==201 or r.status_code==200:
                    print(r.text)
                    cookies={'email':str(self.email.value)}
                    response=requests.get(
                    f'{base_url}account_api/verify/',
                    data={},
                    cookies=cookies,
                    
                    )
                    if response.status_code==200:
                        self.page.dialog=self.verify_dialog
                        self.verify_dialog.modal=True
                        self.verify_dialog.open=True
                        self.verification_code.value=''
                        self.v_head.sub_title=f'A verification code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
                        self.page.update()
                    else :
                        return go_to_page(self=self, app_name=app_name_, route='register')    
            
            
    def did_mount(self):
        self.running=True
        self.tasker=threading.Thread(target=self.enable, daemon=True,args=())
        self.tasker.start()


    def will_unmount(self):
        self.running=False
             
            
    def verify_regenerate(self,e):
        regenerate(self=self)
        
    def enable(self):
        enable_resend(self=self)      
   
    def verify_user(self,e):
        verify_finale(self=self,redirect_url='home')
        
class  LoginPage(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        
        self.page=page
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.auth_=auth_

        self.email_text=''
        self.bgcolor=colors.SECONDARY_CONTAINER

        self.verification_code=NumberInput(field_hint='Enter verification code',col=10,type='num')              
        
        # self.scroll='adaptive'
        self.email= AuthInputField(field_hint='Email',focus_input=True,type='email')              
        self.password= AuthInputField(field_hint='Password',focus_input=False,type='password')              
        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.verify=Text(color=colors.RED_300,height=0)
        

        self.heading=PageHeading_2(main_title='Sign In Below',bg_color=None,main_size=22,sub_title='Welcome Back On LernOn', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[
                          
                        self.divider,
                        self.heading,
                        self.divider,
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.email),

                        self.verify,
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.password),

                        self.password_verifier,
                        ElevatedButton('Login',width=300, color=colors.PRIMARY,bgcolor=colors.ON_PRIMARY,on_click=self.fill_validation),
                        
                        Row(controls=[
                            TextButton(text='Forgot Password',on_click=lambda _: go_to_page(self=self, app_name=app_name_, route='reset-email') ),
                            TextButton('New? Join',on_click=lambda _:go_to_page(self=self, app_name=app_name_, route='register') ),
                            ],
                            alignment='center'),
                        
                        Divider()
                        ],
                horizontal_alignment='center',
                alignment='center'),
            bgcolor=colors.SECONDARY_CONTAINER,
            border_radius=12,
            padding=15

        )
        
        self.register_card=Card(
            elevation=15,
            content=self.view_container,
            width=400,
            
            )
        
        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        
        self.verification_info='A verification code has been sent to'
        self.v_head=PageHeading_2(main_title='',bg_color=colors.SECONDARY_CONTAINER,main_size=18,sub_title=' ', text_color=colors.PRIMARY, sub_size=10)
        self.count=0
        self.v_btn=ElevatedButton(text="Verify",color=colors.PRIMARY,bgcolor=colors.ON_PRIMARY, on_click=self.verify_user)

        self.dir_dialog=AlertDialog(
            content=ResponsiveRow(controls=[PageHeading_2(main_title='',bg_color=colors.SECONDARY_CONTAINER,main_size=18,sub_title='Verification sucessful', text_color=colors.PRIMARY, sub_size=10),ElevatedButton(text='Continue',on_click=lambda _:  go_to_page(self=self, app_name=app_name_, route='home'))]),
            actions=[ElevatedButton(text='Continue',on_click=lambda _:  go_to_page(self=self, app_name=app_name_, route='home')),],

        )
        self.text_info='Code expires after:'
        self.timer=CountDown(seconds=90,text_info='',t_align='center')
        self.resend_btn=TextButton(content=Text(value=f"{self.text_info}",size=10,),style=ButtonStyle(color=colors.PRIMARY,bgcolor=''), on_click=self.verify_regenerate,disabled=True)

        self.verify_dialog = AlertDialog(
            title=Text("2FA Authenttication",size=14,weight='bold'),
            content=Container(
                
                bgcolor=colors.SECONDARY_CONTAINER,
                content=ResponsiveRow(
                    alignment='center',
                    expand=1,
                    controls=[
                        self.v_head,
                        ResponsiveRow(col=12,controls=[Row(col=1),self.verification_code,Row(col=1),]),
                        self.v_btn,
                        Row(
                            alignment='center',
                            controls=[

                            self.resend_btn,

                            self.timer
                            ]),
                        
                        
                    
                ],
            ),),
            actions=[

                    ],
            actions_alignment="center",
        )


    def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='Email field is required'
            self.verify.height=20
            
            self.verify.update()
        else:    
            self.verify.value=''
            self.verify.height=0
            
            self.verify.update()
        
        if  self.password.value=='' :
            self.password_verifier.value='Password field is required'
            self.password_verifier.height=20

            self.password_verifier.update()
        else:
            self.password_verifier.value=''
            self.password_verifier.height=0
            self.password_verifier.update()
            cookies={'email':str(self.email.value)}
            r=requests.post(
                f'{base_url}account_api/login/',
                data={
                    'username':str(self.email.value),
                    'password':str(self.password.value),
                    },
                    cookies=cookies
                )
             
            self.page.session.set('email',str(self.email.value))
            self.page.session.set('verified',False)
            if r.status_code==200:
                cookies={'email':str(self.email.value)}


                response=requests.get(
                        f'{base_url}account_api/verify/',
                        data={},
                        cookies=cookies,
                        
                        )
                if response.status_code==200:
                    self.page.dialog=self.verify_dialog
                    self.verify_dialog.modal=True
                    self.verify_dialog.open=True
                    self.verification_code.value=''
                    self.v_head.sub_title=f'A verification code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
                    self.page.update()
            else :
                return go_to_page(self=self, app_name=app_name_, route='login')    
        


    def did_mount(self):
        self.running=True
        self.tasker=threading.Thread(target=self.enable, daemon=True,args=())
        self.tasker.start()
    
    def will_unmount(self):
        self.running=False
             
    def verify_regenerate(self,e):
        regenerate(self=self)
        
    def enable(self):
        enable_resend(self=self)      
   
    def verify_user(self,e):
        verify_finale(self=self,redirect_url='home')
    

class  PasswordResetEmail(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )

        self.page=page
        self.auth_=auth_

        self.route=f'/{project_}/{app_name_}/{routed}'

        self.email= AuthInputField(field_hint='Email',focus_input=True,type='email')              
        self.verify=Text(color=colors.RED_300,height=0)
        

        self.heading=PageHeading_2(main_title='Password Reset Request',bg_color=None,main_size=22,sub_title='Enter registered email address', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[
                        self.heading,
                        self.divider,
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.email),

                        self.verify,

                        
                        ElevatedButton('Get New Password', on_click=self.fill_validation, width=300,color=colors.PRIMARY,bgcolor=colors.ON_PRIMARY),
                        Row(controls=[
                            TextButton(text='Login ',on_click=lambda _: go_to_page(self=self, app_name=app_name_, route='login') ),
                            TextButton('Register for a new account',on_click=lambda _:go_to_page(self=self, app_name=app_name_, route='register') ),
                            ],
                            alignment='center'),
                        

                        ],
                horizontal_alignment='center',
                alignment='center'),
            bgcolor=colors.SECONDARY_CONTAINER,
            border_radius=12,
            padding=20

        )
        
        self.register_card=Card(
            elevation=15,
            content=self.view_container,
            width=400

            )

        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
    def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='Email field is required'
            self.verify.height=20
            
            self.page.update()
        else:    
            self.verify.value=''
            self.verify.height=0
            go_to_page(self=self, app_name=app_name_, route='reset-password')
            self.page.update()
    # 

class  PasswordReset(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()


        self.divider=Divider(
            height=2, color='transparent',
            
        )

        self.page=page
        # self.route=f'/{project_}/{routed}'
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.auth_=auth_
        self.password= AuthInputField(field_hint='Password',focus_input=True,type='password')              

        self.confirm_password= AuthInputField(field_hint='Confirm password',focus_input=True,type='password')

        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.btn= ElevatedButton('Reset Password', color=colors.PRIMARY,bgcolor=colors.BLUE,on_click=self.fill_validation),

        self.heading=PageHeading_2(main_title='LernOn Password Reset ',bg_color=None,main_size=22,sub_title='Enter a strong  new password', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[
                        self.divider,
                        self.heading,
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.password),
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.confirm_password),
                        self.password_verifier,
                        ElevatedButton('Reset Password', color=colors.PRIMARY,bgcolor=colors.BLUE,on_click=self.fill_validation),
                        ],
                horizontal_alignment='center',
                alignment='center',auto_scroll=True),
            bgcolor=colors.SECONDARY_CONTAINER,
            padding=20,
            border_radius=12,

        )
        
        self.register_card=Card(
            elevation=15,
            content=self.view_container,
            width=400
            

            )

        self.controls=[self.register_card,]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        self.auto_scroll=True
        if self.password.valid==True and self.confirm_password.valid==True:
            self.btn.disabled=False
            
    def fill_validation(self,e):
        if  self.password.value=='' or self.confirm_password.value=='':
            self.password_verifier.value='The two password fields are required '
            self.password_verifier.height=20
            self.password_verifier.update()
        else:
            if self.password.value!= self.confirm_password.value:
                self.password_verifier.value='The two passwords do not match'
                self.password_verifier.height=20
                self.password_verifier.update()
            else: 
                self.password_verifier.value=''
                self.password_verifier.height=0
                self.password_verifier.update()
                go_to_page(self=self, app_name=app_name_, route='reset-password') 
 

class  ProfileSettings(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.page=page
        self.route=f'/{project_}/{app_name_}/{routed}'

        self.email= AuthInputField(field_hint='First name',focus_input=True,type='name')              
        self.password= AuthInputField(field_hint='Last Name',focus_input=False,type='name')              
        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.verify=Text(color=colors.RED_300,height=0)
        self.auth_=auth_
        self.account_type=RadioGroup(
            content=ResponsiveRow(
                controls=[

                    Radio(
                        value='is_student',
                        label='Student'
                    ),
                    Radio(
                        value='is_teacher',
                        label='Teacher'
                    ),
                    Radio(
                        value='is_lecturer',
                        label='Lecturer'
                    ),
                ]
            )
        )        
        self.account_type_verifier=Text()

        self.heading=PageHeading_2(main_title='Initial Profile Settings',bg_color=None,main_size=22,sub_title='Fill in your details correctly and as applicable to you', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[

                        # self.stack,
                          
                        self.divider,
                        self.heading,
                        self.divider,
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.email),

                        self.verify,
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.password),

                        self.password_verifier,
                        Text('Account Type'),

                        self.account_type,
                        self.account_type_verifier,

                        ElevatedButton('Next',width=300, color=colors.PRIMARY,bgcolor=colors.BLUE,on_click=self.fill_validation),
                        ],
                horizontal_alignment='center',
                alignment='center'),
            bgcolor=colors.SECONDARY_CONTAINER,
            border_radius=12,

        )
        
        self.register_card=Card(
            elevation=15,
            content=self.view_container,

            )
        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        

        
    def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='First Name field is required'
            self.verify.height=20
            
            self.verify.update()
        else:    
            self.verify.value=''
            self.verify.height=0
            
            self.verify.update()
        
        if  self.password.value=='' :
            self.password_verifier.value='Last name field is required'
            self.password_verifier.height=20

            self.password_verifier.update()
        else:
            self.password_verifier.value=''
            self.password_verifier.height=0
            self.password_verifier.update()
            
            res=make_authenticated_put_request(
                self=self,
                url=f'account_api/user/{User(selfed=self).id}',
                data={
                    'first_name':str(self.email.value),
                    'last_name':str(self.password.value),
                    
                      },
                      cookie=None,
                      key=None

                )
            if res.status_code==200:
                go_to_page(self=self, app_name=app_name_, route='profile')
             

    def did_mount(self):
        self.running=True
        
    def will_unmount(self):
        self.running=False
             



# 
class Profile(View):

    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        
        self.page=page
        self.route=f'/{project_}/{app_name_}/{routed}'

        self.navigation_bar=NavBottom(selfed=self)
        self.auth_=auth_
        self.scroll='always'
        self.auth_links=ElevatedButton()
        self.bgcolor=colors.PRIMARY_CONTAINER        
        self.updateables=[]  
        self.drawer=LeftSideBar(selfed=self)

        
        """
        ################################################### section 1 content: Basic info ##########################################################
        """
        self.user_img=width_fitted_image(src='/images/logos/logodl3.png')
        
        self.first_name=MediumTitleText(text='Full Name', text_align='start',font_family='heading')
        self.house_address=SmallBodyText(text='Address',text_align='start')

        self.phone=SmallBodyText(text='Phone',text_align='start')
        
        self.institution= SmallTitleText(text='Organisation',text_align='start',font_family='heading')
        self.status=SmallBodyText(text='Status',text_align='start')
        self.duration=SmallBodyText(text='Date joined-',text_align='start')
        self.email=SmallBodyText(text='Email-',text_align='start')

        self.basic_info=ResponsiveRow(

            controls=[
                Row(

                    col=column_set(small_phone=12,land_scape_phone=4),
                    controls=[

        Container(
            width=100,
            height=100,
            image_src=self.user_img,
        
            content=Row(controls=[Icon(icons.EDIT,color=colors.PRIMARY)]),
            border=border.all(0.18,colors.PRIMARY),
            border_radius=50,
            padding=10
        ),
            #     Container(
            # border_radius=50,
            # border=border.all(1,colors.PRIMARY_CONTAINER),

            #         # col=column_set(small_phone=3,land_scape_phone=1),

            # # padding=5,

            #         bgcolor=colors.with_opacity(opacity=0.2,color=colors.PRIMARY),
            #     content=self.user_img,

            #         height=100,
            #     ),
        
                
                ResponsiveRow(
                    expand=1,
                    # col=column_set(small_phone=5+1,land_scape_phone=0.5),
                    spacing=0,
                    # col=column_set(small_phone=12,land_scape_phone=1),
                    controls=[

                        self.first_name,
                        self.email,
                        self.phone,
                        self.house_address,


                    
                              ]
                    ),
                 
                 
                 
                    ]
                ),
                
                
                ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=5+1,land_scape_phone=4),
                    spacing=0,
                    controls=[

                        self.institution,
                        Row(controls=[self.status ,self.duration,]),

                    
                              ]
                    ),
                Divider(height=2),

                 ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=12,tablet=5+1, land_scape_phone=4),
                    spacing=0,
                    controls=[

                        SmallTitleText(text=f'Bio',text_align='start',font_family='heading'),
                        SmallBodyText(boldness='bold',text='I am a full stack web and mobile app developer. I develop web apps with Django, a python framework for web development. I build flutter apps with flet for cross platform applications  ',text_align='start'),

                    
                              ]
                    ),
               
                 ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=12,tablet=5+1, land_scape_phone=4),
                    spacing=0,
                    controls=[

                        SmallTitleText(text=f'About',text_align='start',font_family='heading'),
                        SmallBodyText(boldness='bold',text='I am a full stack web and mobile app developer. I develop web apps with Django, a python framework for web development. I build flutter apps with flet for cross platform applications  ',text_align='start'),

                    
                              ]
                    ),
               
                Divider(height=2),

                
                
            ]
        )
        """
        ################################################### section 2 content: Courses ##########################################################
        """
        self.course_type_status=ResponsiveRow(
            controls=[
                Container(
                    col=3,
                    content=SmallBodyText(text='All Courses',font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='FUTA Courses' ,font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='LernOn Courses' ,font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='Other Courses' ,font_family='heading'),
                ),
            ]
        )
        self.courses=ResponsiveRow(
            controls=[

                self.course_type_status,
                Divider(height=1,color=colors.PRIMARY)
            ],
        )


        """
        ################################################### sections definitions ##########################################################
        """

        self.secion_1=sections_container(
            self=self,
            padding=10,
            border_radius=20,
            border=border.all(1,colors.PRIMARY),

            controls=[
                self.basic_info,
            ],
        )
        
        self.secion_2=sections_container(
            self=self,
            padding=10,
            border_radius=0,
            border=border.all(1,colors.PRIMARY),

            controls=[
                self.courses,
            ],
        )
        
        self.main_controls=[self.secion_1,self.secion_2]
        self.main_container=ResponsiveRow(controls=self.main_controls)
        self.appbar=LernOnAppBar(selfed=self)
        self.end_drawer=RightSideBar(selfed=self)


        self.controls=[
            self.main_container
        ]
        
    def did_mount(self):
        self.running=True
        self.tasker_1=threading.Thread(target=self.profile, daemon=True,args=())
        self.tasker_1.start()
    
    def will_unmount(self):
        self.running=False
       
    def resize_page(self,e):
        print(f'acc: {self.page.height}')
    def profile(self):
        while self.running:
            if get_access_token(self=self) and User(selfed=self).is_logged_in :
                # 

                res=make_authenticated_get_request(self=self,url=f'account_api/user/{User(selfed=self).id}',cookie=get_access_email(self=self),key='email')
                if res.status_code==200:

                    for item in res.json():
                        if item=='picture':
                            if res.json()[item]:
                                self.user_img.src=f'{str(res.json()[item])}'
                            
                        if item=='username':
                            if res.json()[item]:
                                self.email.value=f'{str(res.json()[item])}'
                            
                        if item=='phone':
                            if res.json()[item]:
                                self.phone.value=f'{str(res.json()[item])}'
                            
                            
                        if item=='first_name':
                            if res.json()[item]:
                                self.first_name.value=f'{str(res.json()[item])}'
                            
                        if item=='last_name':
                            if res.json()[item]:
                                self.first_name.value +=f' {str(res.json()[item])}'
                            
                        if item=='is_superuser':
                            if res.json()[item]:
                                self.status.value="Super User"
                        elif item=='is_worker':
                            if res.json()[item]:
                                self.status.value="Staff"
                                
                        elif item=='is_stakeholder':
                            if res.json()[item]:
                                self.status.value="Senior Staff"
                        elif item=='is_dep_head':
                            if res.json()[item]:
                                self.status.value="Admin"
                                        
                        elif item=='is_investor':
                            if res.json()[item]:
                                self.status.value="Investor"
                        else:
                                self.status.value="User"
                                self.status.update()
                            
                        if item=='date_joined':
                            if res.json()[item]:
                                self.duration.value=f'{str(res.json()[item])}'
                            
                        
                            
                        if item=='address':
                            if res.json()[item]:
                                self.house_address.value=f'{str(res.json()[item])}'
                        self.main_controls.append(sections_container(
                            self=self,
                            controls=[Text(value=f'{str(item)}: {str(res.json()[item])}',size=14)],
                            bgcolor='blue',
                            )
                        )
                    self.update()
            # time.sleep()

                   
    def logout_user(self,e):
        logout_user(self=self)  
    
             
       

    


