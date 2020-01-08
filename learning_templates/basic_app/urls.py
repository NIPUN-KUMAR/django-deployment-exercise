from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('basic_app/relative/', views.relative, name='relative'),
    path('basic_app/other/', views.other, name='other'),
]
