from django.shortcuts import render
from .models import movie
from django.http import HttpResponse
from .forms import MovieForm
from django.shortcuts import redirect

# Create your views here
def index(request):
    obj=movie.objects.all()
    return render(request,"index.html",{'movie_list':obj})

def details(request,movie_id):
    ob=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie_list':ob})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        image=request.FILES['img']
        obj=movie(name=name,desc=desc,year=year,img=image)
        obj.save();
    return render(request,"add.html")



# def details(request,movie_id):
#     return HttpResponse("this is%s "%movie_id)

def update(request,id):
    moviee=movie.objects.get(id=id)
    forms=MovieForm(request.POST or None,request.FILES,instance=moviee)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'movie':moviee})


def delete(request,id):
    if request.method=='POST':
        move = movie.objects.get(id=id)
        move.delete()
        return redirect('/')
    return render(request,"delete.html")




