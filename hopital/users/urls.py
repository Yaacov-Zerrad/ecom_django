from django.urls import path
from .views import login_user, register, doctor, infirmiere, patient

urlpatterns = [
    path('', login_user , name='index'),
    path('register/', register , name='register'),
    path('doctor/', doctor , name='doctor'),
    path('infirmiere/', infirmiere , name='infirmiere'),
    path('patient/', patient , name='patient'),
    
]