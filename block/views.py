from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature,Latest
from .forms import ContactForm
# Create your views here.
def index(request):
    feature = Feature.objects.all()
    latest = Latest.objects.all()
    context = {
        'feature': feature,
        'latest': latest,
    }

    return render(request,'index.html',context=context)

def latestDetail(request,id):
    latest = Latest.objects.get(id=id)
    context = {
        'latest' : latest
    }
    return render(request,'latestDetail.html',context=context)

def FEATURE(request,id):
    feature = Feature.objects.get(id=id)
    context = {
        'feature' : feature
    }
    return render(request,'feature.html',context=context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Sizning malumotingiz qabul qilindi</h1>")
    context = {
        'form': form
    }
    return render(request,'contact.html',context=context)
    