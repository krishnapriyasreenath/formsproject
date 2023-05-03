from django.shortcuts import render,redirect
from formsapp.forms import employeeforms
from formsapp.forms import employee

def addemp(request):
    form=employeeforms()
    return render(request,'addemploy.html',{'form':form})
def addemploy(request):
    if request.method == 'POST':
        form=employeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        
def show(request): 
    empls=employee.objects.all()
    return render(request,'show_employee.html',{'empls':empls})
def update(request,id):
    empl=employee.objects.get(id=id)
    form=employeeforms(instance=empl)
    if request.method == 'POST':
        form=employeeforms(request.POST,instance=empl)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render (request,'update.html',{'form':form})
def delete(request,id):
    emp= employee.objects.get(id=id) 
    emp.delete()   
    return redirect('show')
           

# Create your views here.
