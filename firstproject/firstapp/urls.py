from django.urls import path
from firstapp import views

urlpatterns=[
    path('first/', views.index, name="index"),
    path('second/', views.rishabh, name="index"),
    path('third/', views.example, name="index"),
    path('',views.template_demo, name="index"),
    path('form/',views.form_view, name="index"),

]