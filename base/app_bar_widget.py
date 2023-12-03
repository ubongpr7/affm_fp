from flet import *
import requests
from config.utils import *
from widgets.auth_widgets import logout_user
from widgets.buttons_widget import column_set
from widgets.images import affm_logo, width_fitted_image
from apps.account.utils import *
from widgets.text_widget import *
   

class DropDownWidget(Dropdown):
    def __init__(self,options, label):

        super().__init__()
        self.width=90
        self.height=40
        self.options=options
        self.border_width=0
        self.label=label
        # self.prefix_icon=icons.QUESTION_ANSWER_ROUNDED
        # self.icon=icons.QUESTION_ANSWER_ROUNDED
        self.text_size=12
        self.content_padding=5
        self.focused_bgcolor='transparent'
        self.dense=True
           

class SideBarNav(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page=page
        self.width=190
        self.height=750
        self.border_radius=10
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.padding=padding.only(top=5,left=10,right=10,bottom=5)
        self.clip_behavior=ClipBehavior.HARD_EDGE
        self.animate=animation.Animation(400,'decelerate')
        self.item_text=LargeBodyText(text='')
        self.content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.START,
            controls=[
                Row(
                    spacing=1,
                       controls=[
                            
                            TextField(
                                 border_color='transparent',
                                 height=20,
                                 text_size=12,
                                 content_padding=2,
                                 cursor_color=colors.PRIMARY,
                                 color=colors.PRIMARY,
                                 width=150,
                                 hint_text='Search'

                            ),
                            Icon(
                                icons.SEARCH_ROUNDED,
                                size=17,
                                opacity=0.9,
                                color=colors.PRIMARY,
                                

                            ),
                            self.item_text
                            

                    ]

                )
                ,
                Column(
                     scroll='auto',
                     expand=True,

                ),
            ]
        )

class DropDownSearch(Container):
    def __init__(self):
        super().__init__()
        # self.page=page
        self.width=200
        self.height=40
        # self.alignment='center'
        self.border=Border(bottom=BorderSide(0.12,colors.PRIMARY),right=BorderSide(0.102,'black'))
        self.border_radius=10
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.padding=padding.only(top=5,left=10,right=10,bottom=5)
        self.clip_behavior=ClipBehavior.HARD_EDGE
        self.animate=animation.Animation(400,'decelerate')
        self.item_text=LargeBodyText(text='')
        self.content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.START,
            controls=[
                Row(
                    spacing=1,
                    # horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                            
                            TextField(
                                 border_color='transparent',
                                 height=25,
                                 text_size=10,
                                 content_padding=2,
                                 cursor_color=colors.PRIMARY,
                                 color=colors.PRIMARY,
                                 bgcolor='transparent',
                                 width=150,
                                 hint_text='Search'

                            ),
                            Icon(
                                icons.SEARCH_ROUNDED,
                                size=25,
                                opacity=0.9,
                                color=colors.PRIMARY,
                                

                            ),
                            self.item_text
                            

                    ]

                )
                ,
                Column(
                     scroll='auto',
                     expand=True,

                ),
            ]
        )

class LernOnAppBar(AppBar):
    def __init__(self,selfed):
        super().__init__()
        self.auth_links=Row()
        self.center_title=False
        self.selfed=selfed
        self.leading=IconButton(icon=icons.MENU_OPEN_ROUNDED,height=30,tooltip='Open Navigation menu',icon_color=colors.PRIMARY,on_click=self.show_right_drawer)
        self.user_img=width_fitted_image(src='/images/logos/logodl3.png')

        self.bgcolor=colors.PRIMARY_CONTAINER
        self.user_account=Row()
        self.log_btn=ElevatedButton(content=SmallBodyText(text='Login',),bgcolor=colors.SECONDARY,height=30) 
        self.reg_btn=OutlinedButton(content=SmallBodyText(text='Join us',color=colors.PRIMARY),on_click=lambda _:self.selfed.page.go(f'/{project_}/accounts/register'),height=30) 
        self.account_menu=CircleAvatar(
            content=self.user_img,
            # on_click=self.show_left_drawer

        )
        
        self.title=ResponsiveRow(
            expand=1,
            controls=[
                Row(
                    col=column_set(small_phone=12,land_scape_phone=4),
                    controls=[

                
                IconButton(content=Container(
                width=50,
                height=50,
                border_radius=40,
                content=Image(src='images/logos/logodl3.png',fit=ImageFit.CONTAIN,tooltip='Home'),
                ),
                
                style=ButtonStyle(overlay_color={"":"transparent"},),on_click=lambda _:go_to_page(self=self,app_name=None, route='home')),
                
                    ]
                    
                ),
                ]
            )
        

        
        self.actions=[

                                    
            Row(
                    controls=[
                    
                    self.auth_links,
                    
                
                        
                    ]
                ),
            
            # Row(width=10),
            self.user_account,
                                
            
        Row(width=15),

        ]
        
    def background_task(self):
        # while self.running:
            if self.selfed.page.client_storage.get(f'{project_}.authenticated'):
                self.log_btn.on_click=self.logout_user 
                self.log_btn.content=LargeLabelText(text='Logout',color=colors.SECONDARY) 
                self.auth_links.controls=[] 
                res=make_authenticated_get_request(self=self,url=f'account_api/user/{User(selfed=self).id}',cookie=get_access_email(self=self),key='email')
                if res.status_code==200:
                    for item in res.json():
                        if item=='picture':
                            if res.json()[item]:
                                self.user_img.src=f'{str(res.json()[item])}'
                           
                self.user_account.controls=[self.account_menu] 
                self.update()

            else: 
                self.log_btn.on_click=lambda _: self.selfed.page.go(f'/{project_}/accounts/login')
                self.log_btn.content=LargeLabelText(text='Login',color=colors.PRIMARY)    
                self.auth_links.controls=[self.log_btn,self.reg_btn]
                self.user_account.controls=  []
                self.update()
   
    def show_left_drawer(self,e):
        if self.selfed.end_drawer:
            self.selfed.end_drawer.open=True
            self.selfed.update()
        else:
           go_to_page(self=self.selfed,app_name='accounts',route='login')
    
   
    def show_right_drawer(self,e):
        if self.selfed.drawer:
            self.selfed.drawer.open=True
            self.selfed.update()
        else:
           go_to_page(self=self.selfed,app_name='accounts',route='login')
        
    def did_mount(self):
        self.running=True
        self.tasker_1=threading.Thread(target=self.background_task, daemon=True,args=())
        self.tasker_1.start()
    
    def will_unmount(self):
        self.running=False
        
    def logout_user(self,e):     
        logout_user(self=self.selfed)    
    def mode_change(self,e):
        if self.selfed.page.client_storage.get(f'{project_}.mode')=='dark':
            self.selfed.page.client_storage.set(f'{project_}.mode','light')
            self.mode_toggle.icon=icons.LIGHT_MODE
            self.selfed.page.update()
        elif self.selfed.page.client_storage.get(f'{project_}.mode')=='light':
            self.selfed.page.client_storage.set('affm.mode','dark')
            self.mode_toggle.icon=icons.DARK_MODE
            self.selfed.page.update()
        else:    
            self.selfed.page.client_storage.set(f'{project_}.mode','dark')
            self.mode_toggle.icon=icons.DARK_MODE
            self.selfed.page.update()
