from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.
def index(request):
    context = {}
    form = UserForm()
    obj = User.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('index')
            return render(request,'enroll/index.html',{'form':form,'obj':obj})
        else:
            return render(request,'enroll/index.html',{'form':form,'obj':obj})

    
    return render(request,'enroll/index.html',{'form':form,'obj':obj})