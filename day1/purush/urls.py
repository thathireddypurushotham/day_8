from django.urls import path
from purush import views
urlpatterns = [
   path('',views.home),
   path('demo/',views.chk),
   path('home/',views.homepage),
   path('lg/',views.login),
   path('wt/',views.reg),
]