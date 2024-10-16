from django.shortcuts import render
from .models import Member

def func(request):
  mymembers = Member.objects.all().values()
  return render(request,'index.html',{
    'mymembers': mymembers,
  })
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  return render(request,'details.html', {'mymember': mymember,})

def main(request):
  return render(request,'main.html')