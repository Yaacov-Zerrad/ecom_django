from django.urls import path
from .views import generate, form, index, verification, download
urlpatterns = [
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('verification/<int:phone>/', verification, name='verification'),
    path('<int:pk>/generate', generate, name='generate'),
    path('download', download, name='download'),
    ]