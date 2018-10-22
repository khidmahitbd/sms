from django.urls import path
from .views import *


urlpatterns = [
    path('s_name/', class_name, name = 'add_class'),
    path('c_list/', class_list, name = 'class_list'),
    path('subject/', subject, name = 'add_subject'),
    path('subject_list/', subject_list, name = 'subject_list')
]