from django.contrib import admin

# Register your models here.
from .models import StudentClass,Subject


admin.site.register(StudentClass)
admin.site.register(Subject)