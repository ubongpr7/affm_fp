import threading
import time
from flet import *
from functools import partial
from config.utils import go_to_page
import flet as fl
from base.app_bar_widget import DropDownWidget

from config.utils import *
from widgets.auth_widgets import logout_user
from widgets.text_widget import *

        

class NavBottom(NavigationBar):
    def __init__(self,selfed):

        super().__init__()
        self.selfed=selfed
        self.height=48
        self.elevation=2
        self.label_behavior=NavigationBarLabelBehavior.ALWAYS_HIDE
        self.bgcolor=colors.with_opacity(opacity=0.09,color=colors.PRIMARY_CONTAINER)
        self.destinations=[
            NavigationDestination( icon_content=IconButton(icon_color=colors.PRIMARY,icon_size=20,icon=icons.HOME, on_click=lambda _: go_to_page(self=self.selfed,app_name='accounts', route='home'),tooltip='Home')),
            NavigationDestination(icon_content=IconButton(icon_color=colors.PRIMARY,icon_size=20,icon=icons.COMPUTER_ROUNDED, on_click=lambda _: go_to_page(self=self.selfed,app_name='accounts', route='profile'),tooltip='Digital Products')),
            NavigationDestination(icon_content=PopupMenuButton(
                        content=Icon(name=icons.MENU_ROUNDED,color=colors.PRIMARY),
                            items=[
                                PopupMenuItem(icon=icons.POWER_INPUT, text="Check power"),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15'),SmallBodyText(text='Login',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15',tooltip='Login to existing account'),SmallBodyText(text='Login transparent transparent',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                Divider(color='transparent'),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15'),SmallBodyText(text='Login',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15'),SmallBodyText(text='Login',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                Divider(),
                                
                                PopupMenuItem(
                                    content= DropDownWidget(
                label="Exams",
        
        options=[
                
            dropdown.Option("Digital Product",disabled=True),
            dropdown.Option("WAEC Past Question"),
            dropdown.Option("JAMB Past Question"),
            dropdown.Option("IELTS Past Question"),
            dropdown.Option("Student assessment"),
            
        ],
    ),
            ),
                                ]

                    ),
            ),

        
        ]
        
class LeftSideBar(NavigationDrawer):
    def __init__(self,selfed):
        super().__init__()
        self.elevation=40
        self.selfed=selfed
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.indicator_color=colors.SECONDARY_CONTAINER
        self.indicator_shape=StadiumBorder()
        self.shadow_color=colors.SECONDARY
        self.surface_tint_color=colors.SECONDARY_CONTAINER
        selected_index=0
        self.elevation=40
        self.controls=[
            Container(height=12),
            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
            
            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),

            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
        ]
        
  
        
class RightSideBar(NavigationDrawer):
    def __init__(self,selfed):
        super().__init__()
        self.elevation=40
        self.selfed=selfed
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.indicator_color=colors.SECONDARY_CONTAINER
        self.indicator_shape=StadiumBorder()
        self.shadow_color=colors.SECONDARY
        self.surface_tint_color=colors.SECONDARY_CONTAINER
        self.elevation=40
        self.admin_controls=[

        ]
        self.worker_controls=[

        ]
        self.user_controls=[
            [
            Container(height=12),
            NavigationDrawerDestination(

                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
            
            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),

            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Logout user',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.LOGOUT,color=colors.PRIMARY),
                               SmallBodyText(text='Logout')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Logout user',
                     
                     content=Row(
                          controls=[
                               Icon(icons.LOGOUT_ROUNDED,color=colors.SECONDARY),
                               SmallBodyText(text='Logout')
                           ]
                        ,),
                    ),
            ),
           
        ]

        ]
        self.investor_controls=[
            
        ]
        self.all_controls=[
             Container(height=12),
            NavigationDrawerDestination(

                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
            
            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Edit profile',
                     on_click=None,
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS,color=colors.PRIMARY),
                               SmallBodyText(text='Profile Settings')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=None,
                     tooltip='Edit profile',
                     
                     content=Row(
                          controls=[
                               Icon(icons.SETTINGS_APPLICATIONS,color=colors.SECONDARY),
                               SmallBodyText(text='Dashoard')
                           ]
                        ,),
                    ),
            ),
           
            Divider(thickness=2),

            NavigationDrawerDestination(
                icon_content=Container(
                     tooltip='Logout user',
                     on_click=self.logout_user,

                     content=Row(
                          controls=[
                               Icon(icons.LOGOUT,color=colors.PRIMARY),
                               SmallBodyText(text='Logout')
                           ]
                        ,),
                    ),
                selected_icon_content=Container(
                     on_click=self.logout_user,
                    #  on_click=None,
                     tooltip='Logout user',
                     
                     content=Row(
                          controls=[
                               Icon(icons.LOGOUT_ROUNDED,color=colors.SECONDARY),
                               SmallBodyText(text='Logout')
                           ]
                        ,),
                    ),
            ),
        ]

        self.controls=self.all_controls


    def logout_user(self,e):
        logout_user(self=self)