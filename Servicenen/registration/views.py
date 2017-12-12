from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from registration.forms import *



def register_user(request):
    form = UserForm()
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect('home')
    else:
        context = {"form":form}
        return render(request, 'registration/register_form.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    form = UserForm()
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)



def profile(request):
    try:
        profile=Profile.objects.get(user = request.user)
        context={'profile':profile}
    except:
        context={'errmsg': "You have no profile"}
    return render( request, "registration/profile.html",context)


def createprofile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile_obj = form.save(commit = False)
            profile_obj.user = request.user
            profile_obj.save()
            return redirect('profile')
    else:
        form = ProfileForm
    return render(request,'registration/createprofile.html',{'form':form})
