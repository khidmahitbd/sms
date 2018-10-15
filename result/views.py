from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

#this viwe for Create result 
def create_result(request):
    if request.method =='POST':
        form = AddResultForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddResultForm() # this form is Form.py's
    context = {'forms':form}  
    return render(request,'result/add_result.html',context)
    

def allresult(request):
    result_list = ResultInfo.objects.all()
    context = {
        'resultlist':result_list,
         }
    return render(request,"result/all_result.html",context)

def delete_result(request,id):
    select = ResultInfo.objects.get(id=id)
    select.delete()
    return redirect('all_result_url')

def edit_result(request,id):
    select = ResultInfo.objects.get(id=id)
    form = AddResultForm(request.POST or None,instance = select)
    if request.method =="POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_result_url')
    context ={
        'form':form,
    }
    return render(request,'result/result_update.html',context)






def cheke_result(request):
    if request.method =='POST':
        form =ChakeResultForm(request.POST)
        if form.is_valid():
            class_no = form.cleaned_data["std_class"]
            roll_no = form.cleaned_data["std_roll"]
            
            try:
                roll_obj = ResultInfo.objects.get(std_class=class_no,std_roll=roll_no)
                print("this is ", roll_obj)

                context={
                    'roll': roll_obj.objects.std_roll,
                    'name': roll_obj.objects.std_name,
                    'class': roll_obj.objects.std_class,
                    'subject': roll_obj.objects.subject,
                    'marks': roll_obj.objects.mark,
                    'forms':form,
                     }
                print("context",context)
                render(request,'result/cheke_result.html',context)

            except:

                context = {'Error':"Not found result",
                            'forms':form,
                            }

                return render(request,'result/cheke_result.html',context)



    form = ChakeResultForm()
    context = {'forms':form}
    return render(request,'result/cheke_result.html',context)
