from django.http import HttpResponse
from django.shortcuts import render, redirect
from A2.models import Link
from .forms import  LinkForm


def home(request):
   return render(request, 'index.html')

def enter(request):
   return render(request, 'enter.html')
def join(request):
   context = {}



   if request.method == 'POST':
      link = LinkForm(request.POST)

      if link.is_valid():
         newLink=link.save(commit=False)
         ins = request.POST['institute']
         dept = request.POST['dept']
         course = request.POST['course']
         password = request.POST['password']
         Linkgo=ins+dept+course+password

         if (Linkgo == ""):
            context['form'] = link
            return render(request, 'join.html', context=context)

         context['link']= Linkgo.upper()
         return render(request, 'meet.html', context=context)
      else:
         context['form'] = link
   else:  # GET request
      link = LinkForm()

      context['form'] = link

   return render(request, 'join.html', context=context)




def create(request):
   context = {}

   if request.method == 'POST':
      link = LinkForm(request.POST)

      if link.is_valid():
         newLink = link.save(commit=False)
         ins = request.POST['institute']
         dept = request.POST['dept']
         course = request.POST['course']
         password = request.POST['password']
         Linkgo = ins + dept + course + password

         if(Linkgo==""):
            context['form'] = link
            return render(request, 'create.html', context=context)


         context['link'] = Linkgo.upper()
         return render(request, 'meet.html', context=context)
      else:
         context['form'] = link
   else:  # GET request
      link = LinkForm()

      context['form'] = link

   return render(request, 'create.html', context=context)




def meet(request):
   context={}





   link=""


   context['Link']=link

   return render(request, 'meet.html', context=context)



