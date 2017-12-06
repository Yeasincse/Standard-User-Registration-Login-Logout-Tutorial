from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from registration.forms import UserForm



def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        user.save()
        return redirect('registration/login_user/')
    else:
        context = {"form":form}
        return render(request, 'registration/register_form.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            return render(request, 'registration/user_profile.html')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)
