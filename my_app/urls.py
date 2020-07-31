from django.urls import path
from . import views


urlpatterns = [
    path('table/<int:id>/',views.table,name='timetable'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('',views.home,name='home'),
    path('savestudent',views.savestudent,name='savestudent')
    ]