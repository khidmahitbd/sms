from django.shortcuts import render, redirect
from .forms import ClassForm, SubjectForm
from .models import StudentClass, Subject

# Create your views here.


def class_name(request):
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():

            cls_name = forms.cleaned_data['class_name']

            StudentClass.objects.create(class_name = cls_name)
            return redirect('class_list')
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

            subject = forms.cleaned_data['subject']
            class_name = forms.cleaned_data['class_name']

            StudentClass.objects.create(subject='subject', class_name= 'class_name')
            return redirect('subject_list')


    forms = SubjectForm()
    context = {'form':forms}
    return render(request, "management/subject.html", context)


def subject_list(request):
    subject_list = Subject.objects.all()
    context = {'sub_list':subject_list}
    return render(request, 'management/subject_list.html', context)
