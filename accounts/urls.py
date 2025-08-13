from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.registration,name='register'),
    path('login/',views.user_login,name='login'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('update/',views.update,name='update'),
    path('forgot/',views.forgot_pwd,name='forgot'),
    path('pwdchange/',views.pwd_change_success,name='pwdchange'),
]