from django.urls import path
from myApp import views


# TEMPLATE URL
app_name='myApp'



urlpatterns=[
  path('register/', views.register, name='register'),
  path('user_login/',views.user_login, name='user_login'),
  

]


