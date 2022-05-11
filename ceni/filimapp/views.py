from os import name
import re
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse

from filimapp.models import Movie
from . form import MovieForm
#user passwod 1234 uname cenima
# Create your views here.

def home(request):
	movie=Movie.objects.all()
	Context={
		'movie_list':movie
	}
	return render(request,'home.html',Context)# Create your views here.
def detail(request,movie_id):
	movie=Movie.objects.get(id=movie_id)
	return render(request,"detail.html",{'movie':movie})
def add_movie(request):
	if request.method=="POST":
		name = request.POST.get('name',)
		desc = request.POST.get('desc',)
		year = request.POST.get('year',)
		img = request.FILES['img']
		movie = Movie(name=name,desc=desc,year=year,img=img)
		movie.save()

	return render(request,'add_movie.html')#type add when for see url
def update(request,id):
	movie=Movie.objects.get(id=id)
	form=MovieForm(request.POST or None, request.FILES,instance=movie)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
	if request.method=='POST':
		movie=Movie.objects.get(id=id)
		movie.delete()
		return redirect('/')
	return render(request,'delete.html')