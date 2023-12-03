from .views import *
from flet import Page
urlpatterns=[
    LoginPage(routed='login',page=Page),
    Registration(routed='register',page=Page),
    PasswordResetEmail(routed='reset-email',page=Page),
    PasswordReset(routed='reset-password',page=Page),
    # GetVerifyAuthentication(routed='/get-code',page=None),
    Profile(routed='profile',auth_=True,page=Page),
    ProfileSettings(routed='profile-settings',page=Page,auth_=True),

]

    