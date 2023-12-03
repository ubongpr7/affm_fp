from math import pi
import threading
import requests
import time

from flet import *
import flet as fl

from config.views import HomePage
from base.app_bar_widget import LernOnAppBar 
from .urls import urlpatterns
from .utils import *

def main(page:fl.Page):
        
    def route_change(route):
        page.views.clear()
        seen =False
        
        for url in urlpatterns:

            if page.route == url.route:
                if url.auth_:
                    if page.client_storage.get(f'{project_}.authenticated'):
                        url.page=page
                
                        page.views.append(url) 
                        seen=True         
                        page.update()
                    else:
                        for urled in urlpatterns:
                            if urled.route==f"/{project_}/accounts/login":
                        
                                urled.page=page
                
                                page.views.append(urled) 
                                seen=True         
                                page.update()



                else:
                    url.page=page
                
                    page.views.append(url) 
                    seen=True         
                    page.update()
        if page.route=='/':
            page.views.append(HomePage(routed='home',page=page)) 
            page.go(page.route)
            print(page.route)

            page.update()

        if not  seen :
            # you can add your custom 404
            page.session.set('wrong_route',page.route)
            if len(page.views)>1: 
                page.views.pop()

                top_view=page.views[-1] 
                page.go(top_view.route)
            else :   
                page.go('/')
                page.update()
    

    def view_pop(views):
        page.views.pop()
        top_view=page.views[-1] 
        page.go(top_view.route)
        page.update()

    def refresh_user_token():
        

        while page.client_storage.get(f'{project_}.refresh_token'):
            res=requests.post(
                f'{base_url}api/token/refresh/',
                data={
                    "refresh":str(page.client_storage.get(f'{project_}.refresh_token'))
                    },
                )
            if res.status_code==200:
                page.client_storage.set(f'{project_}.access_token',str(res.json()["access"] ))
                page.client_storage.set(f'{project_}.refresh_token',str(res.json()["refresh"] ))
                page.client_storage.set(f'{project_}.authenticated',True)
                print('user is logged in')
                
                time.sleep(1.5*1200)
                page.update()
            else :
                page.client_storage.remove(f'{project_}.email')
                page.client_storage.remove(f'{project_}.access_token')
                page.client_storage.remove(f'{project_}.refresh_token')
                page.client_storage.set(f'{project_}.authenticated',False)
                print('user is logged out')

                   

    task_1=threading.Thread(target=refresh_user_token,daemon=True, args=())
    task_1.start()

    page.window_bgcolor=colors.PRIMARY_CONTAINER
    page.fonts={
    'heading': 'fonts/Roboto/Roboto-Bold.ttf',
    'body': 'fonts/Roboto/Roboto-Medium.ttf',
    'subheading': 'fonts/Roboto/Roboto-Regular.ttf',
    'styled': 'fonts/Lobster/Lobster-Regular.ttf',
    

    }
    page.title=project_name
    # page.theme_mode='light'
    if page.theme_mode=='light':
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
                primary ='#544B40',
                # primary ='#000154',
                secondary ='#757575',
                tertiary ="#4CAF50",
                on_primary ="#4CAF50",
                on_secondary='#F5F5DC',
                # primary_container ='#1f262f',
                primary_container ='#98FF98',

                secondary_container ='#FFFFFF'
                
                

            )
        )
        # beautiful pink D30347
        # gold D3A247  drak D39047
    else:    
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
                # primary ='white',
                # secondary ='#3FD0B6',
                # tertiary =colors.BLUE,
                # # primary_container ='#000154',
                # # primary_container ='#AFFFFF',
                # primary_container ='#0F0E15',
                # # primary_container ='#1f262f',

                # secondary_container ='#0F121F',
                primary ='#c8e6c9',
                # primary ='#000154',
                secondary ='#f5fdc',
                on_primary ="#4caf50",
                on_secondary='#795548',
                # primary_container ='#1f262f',
                primary_container ='#2d432d',

                secondary_container ='#000000'
                

            )
        )
        

    page.on_view_pop=view_pop
    page.auto_scroll=True

    page.on_route_change=route_change
    page.go(page.route)
    
    page.update()