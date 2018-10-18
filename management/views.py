from django.shortcuts import render
from .forms import ClassForm, SubjectForm
from .models import StudentClass, Subject

# Create your views here.


def class_name(request):
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():

            forms.save()    


    forms = ClassForm()
    context = {'form':forms}
    return render(request, 'management/class_name.html', context)



def class_list(request):
    class_list = StudentClass.objects.all()
    context = {'c_list':class_list}
    return render(request, 'management/class_list.html', context)


def subject(request):
    if request.method == 'POST':
        forms = SubjectForm(request.POST)
        if forms.is_valid():

            forms.save()


    forms = SubjectForm()
    context = {'form':forms}
    return render(request, "management/subject.html", context)


def subject_list(request):
    subject_list = Subject.objects.all()
    context = {'sub_list':subject_list}
    return render(request, 'management/subject_list.html', context)
