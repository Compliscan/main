from django.urls import path
from . import views

#URLConf
urlpatterns=[
    path('',views.home),
    path('Instructions',views.instructions),
    path('About',views.about),
    path('test/',views.test,name='test')
]