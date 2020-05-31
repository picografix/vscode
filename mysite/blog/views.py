from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        'author':'Gauransh Soni',
        'title':'Blog Post',
        'Content': 'First post Content',
        'date_posted': 'May 31,2020'
    },
    {
        'author':'Picografix',
        'title':'Blog  2',
        'Content': 'Second post Content',
        'date_posted': 'June 1,2020'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/index.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})