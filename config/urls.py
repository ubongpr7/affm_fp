from .views import *

from flet import View,Page
from apps.account import urls as account_urls    

urlpatterns=[
 
    HomePage(routed='home',page=Page)

]

urlpatterns.extend(account_urls.urlpatterns)
