from django.shortcuts import render

# Create your views here.
def jinja_printtag(request):
    d={'name':'Ashu','age':3}
    return render (request,'jinja_printtag.html',context=d)
