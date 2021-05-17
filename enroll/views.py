from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
#u can bypass csrf security using csrf_exempt decorator over the post request function
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    context = {}
    form = UserForm()
    obj = User.objects.all()
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         #return redirect('index')
    #         return render(request,'enroll/index.html',{'form':form,'obj':obj})
    #     else:
    #         return render(request,'enroll/index.html',{'form':form,'obj':obj})

    
    return render(request,'enroll/index.html',{'form':form,'obj':obj})

def add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            id = request.POST.get('id')

            if id == '':
                obj = User(name=name,email=email,password=password)
            else:
                obj = User(id=id,name=name,email=email,password=password)
            
            #if id is already present save edits it else adds new data to database
            obj.save()
            read = User.objects.values()
            read_list = list(read)
            # print(read_list)
            return JsonResponse({'status':'data saved','read':read_list})
        else:
            return JsonResponse({'status':'data saving failed'})

def dele(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':'deleted'})
    else:
        return JsonResponse({'status':0})

def edit(request):
    if request.method == "POST":
        id=request.POST.get('sid')
        print(id)
        stud = User.objects.get(pk=id)
        stud_data = {"id":stud.id,"name":stud.name,"email":stud.email,"password":stud.password}
        return JsonResponse(stud_data)
    else:
        return JsonResponse({"status":0})
