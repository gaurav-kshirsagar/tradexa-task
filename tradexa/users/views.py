from django.shortcuts import render,redirect

from .models import PostUser,Post

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        uname = request.POST.get('uname')
        password = request.POST.get('pass')
        user = PostUser(first_name=fname,
                       last_name=lname,
                       email=email,
                       username=uname,
                       password=password)
        user.save()
        
        return redirect("login")
    return render(request,"home.html")


def login(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('pass')
        result = PostUser.objects.filter(username=uname,password=password)
        if result:
            request.session['username']=uname
            return redirect("post")
        else:
            return redirect("login")
        print(result[0],"text")
        
        
    return render(request,"login.html")

def post(request):
    if request.session.has_key('username'):
        
        if request.method=='POST':
            text = request.POST.get('text')
            uname = request.session['username']
            user = PostUser.objects.get(username=uname)
            po = Post(username=user,text=text)
            po.save()
        return render(request,"post.html")
    return redirect("login") 