from django.shortcuts import render, redirect
from .models import Applications, Work, WorkType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#registration view.
def register(request):
    if request.method == "POST":
        #get data from form
        a = request.POST["username"]
        b = request.POST["password"]
        c = request.POST["type"]
        d = request.POST["FirstName"]
        e = request.POST["contactno"]

        p = User(username=a, first_name=d, password=b)
        p.save()    # making User object.

        m = User.objects.get(username=a)    #retrive same user object.

        obj = Applications(user=m, contact_no=e, type=c)    #creating Application object.
        obj.save()
        #validations
        return redirect("login")
    return render(request, 'app1/register.html')


#login view
def LoginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        passw = request.POST["password"]
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)
            return redirect('home')  # this will call home fun.
        else:
            return render(request, 'app1/login.html', {"WA" : "Incorrect Credentials"})
    return render(request, 'app1/login.html')

@login_required(login_url='login')
def home(request):
    l1 = []
    obj = WorkType.objects.all()
    for item in obj:
        l1.append(item)
    return render(request, "app1/home.html", {"works" : l1})

@login_required(login_url='login')
def work(request, item_id):
    a = Work.objects.all().filter(work_id=item_id)
    return render(request, "app1/description.html", {"work" : a, 'id' : item_id})

def create(request):
    a = WorkType(TypeOfWork=request.POST["worktype"])
    a.save()
    return redirect('home')

def addWork(request, pk):
    if request.method == "GET":
        return  render(request, "app1/addwork.html", {"id" : pk})
    else:
        #validation remaining add only if not exist.
        var1 = request.POST["descrip"]
        var2 = request.POST["wages"]
        var3 = request.POST["hours"]
        var4 = request.POST["Location"]
        temp = WorkType.objects.get(pk=pk)
        obj = Work(work_id=temp, Hours=var3, city=var4, Wages=var2,Description=var1)
        obj.save()
        return redirect('work', pk, permanent=True)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "app1/login.html")
    else:
        return redirect('login')
