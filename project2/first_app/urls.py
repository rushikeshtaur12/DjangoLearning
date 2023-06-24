from django.urls import  path
from first_app import  views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.home,name='home'),
    path('balance/',views.balance,name='balance'),
    path('payment/',views.payment,name='payment'),
]
