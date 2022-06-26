from django.urls import path
from .views import activate, index, login_user, register, logout_user

urlpatterns = [
    path('', index , name='index'),
    path('register', register , name='register'),
    path('login/', login_user , name='login'),
    path('logout/', logout_user , name='logout'),
    path('activate/<uidb64>/<token>/', activate , name='activate'),
]