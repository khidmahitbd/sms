from django.urls import path
from .views import *


urlpatterns = [
    path('s_name/', class_name, name = 'class_name'),
    path('c_list/', class_list, name = 'class_list'),
    path('subject/', subject, name = 'subject'),
    path('subject_list/', subject_list, name = 'subject_list')
]