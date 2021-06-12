from django.contrib import messages
from app1.models import Student, Teacher
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    student = Student.objects.all()
    return render(request,'index.html',locals())
    

def add(request):
    teacher = Teacher.objects.all()

    if request.POST:
       Student.objects.create(sname=request.POST['sname'], sgender=request.POST['sgender'], sage = request.POST['sage'], s_t_id=request.POST['tid'])
       return HttpResponseRedirect("/")
    return render(request,'add.html',locals())


def update(request,pk):
    #model = Student
    #選取特定欄位
    #fields = ['sname', 'sage', 'sgender', 's_t']

    teacher = Teacher.objects.all()
    data = Student.objects.get(id=pk)
    if request.POST:
        Student.objects.filter(id=pk).update(sname=request.POST['sname'],sgender=request.POST['sgender'], sage = request.POST['sage'])
        return HttpResponseRedirect("/")
    return render(request,'update.html',locals())


def delete(request,pk):
    Student.objects.filter(id=pk).delete()
    return HttpResponseRedirect("/")
    
    

