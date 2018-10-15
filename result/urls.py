from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_result, name="create_result_url"),
    path('chek_result/',cheke_result, name="cheke_result_urls"),
    path('all_result/',allresult, name="all_result_url"),
    path('delete/<int:id>',delete_result, name= "delete_result_urls"),
    path('edit/<int:id>',edit_result, name ="edit_result_urls")


    ]