from django.shortcuts import render, redirect
from .models import green_table
from .forms import greenForm
# Create your views here.

def add(request):
    feather = green_table.objects.all()
    if request.method =='POST':
        name = request.POST.get('name','')
        desc = request.POST.get('desc','')
        date = request.POST.get('date','')
        img = request.FILES['img']
        leaf = green_table(name=name,desc=desc,date=date,img=img)
        leaf.save();
        return redirect('/')
    return render(request,'index.html',{'feather':feather})


def delete(request,featherid):
    fun = green_table.objects.get(id=featherid)
    if request.method == "POST":
        fun.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    count = green_table.objects.get(id=id)
    form =greenForm(request.POST or None, instance=count)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'edit.html',{'form':form,'count':count})



