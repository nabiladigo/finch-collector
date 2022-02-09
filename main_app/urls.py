from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('prints/', views.PrintList.as_view(), name ="Print_list"),
    path('prints/new/',  views.PrintCreate.as_view(), name="print_create"),
    path('prints/<int:pk>/', views.PrintDetail.as_view(), name="print_detail"),
    path('prints/<int:pk>/update',views.PrintUpdate.as_view(), name="print_update"),
    path('prints/<int:pk>/delete',views.PrintDelete.as_view(), name="print_delete"), 
]
