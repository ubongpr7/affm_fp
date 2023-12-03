from flet import *
import requests

import flet as fl
import time,threading

base_url='http://127.0.0.1:8000/'


project_='e-around'       

project_name='A Farm For Me'
def get_user_id(self):
    return str(self.page.client_storage.get(f'{project_}.pk'))


def get_access_token(self):
    try :
        if self.page:
            return self.page.client_storage.get(f'{project_}.access_token')
        # else:
        #     return page.client_storage.get('access_token')

    except :
        return False
def get_access_email(self):
    try:
        if self.page:

            return self.page.client_storage.get(f'{project_}.email')
    except :
        return False
def is_authenticated(self):
    try:
        if self.page:

            return self.page.client_storage.get(f'{project_}.authenticated')
    except :
        return False



def make_authenticated_get_request(self,url,cookie,key):
    cookies={str(key):str(cookie)}
    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.get(url=f'{base_url}{url}/',headers=headers,cookies=cookies)
    return response

def make_authenticated_post_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.post(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response

def make_authenticated_put_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.put(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response

def make_authenticated_patch_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.patch(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response

def make_authenticated_delete_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.delete(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response

class User():
    def __init__(self, selfed ):
        self.selfed=selfed
        self.id=get_user_id(self=self.selfed)
        self.email=get_access_email(self=self.selfed)
        self.token = get_access_token(self=self.selfed)
        self.is_logged_in = is_authenticated(self=self.selfed)

def go_to_page(self, route,app_name):
    if app_name:
        return self.page.go(route=f'/{project_}/{app_name}/{route}')
    else:
        return self.page.go(route=f'/{project_}/{route}')
def go_to_paged(self, route):
    return self.selfed.page.go(route=f'/{project_}/{route}')

