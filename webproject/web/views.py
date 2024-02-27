from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import modelform

# Create your views here.

def demo(request):
    movies=Movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'demo.html',context)
def detail(request,taskid):
    movie=Movie.objects.get(id=taskid)
    return render(request,'detail.html',{'movie':movie})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,des=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
        movie=Movie.objects.get(id=id)
        form=modelform(request.POST or None,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'update.html',{'movie':movie,'form':form})
def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return  render(request,'delete.html')



