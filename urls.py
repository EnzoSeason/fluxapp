from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ex1/', views.ex1),
    path('createFiles1/',  views.createFiles1),
    path('createFiles2/',  views.createFiles2),
    path('createFiles2/<lbd>/<nbFiles>/',  views.createFiles2, name='createFiles2'),
    path('systemResult/', views.systemResult),
    path('hospital/', views.hospital),
    path('hospital/<lbd>/<nbCliniqueFiles>', views.hospital, name='hospital'),
    path('initHospital/', views.initHosiptal),
]
