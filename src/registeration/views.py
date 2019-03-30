from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
# for error messages
from django.contrib import messages
# authentication functions
from django.contrib.auth import authenticate, login, logout

# models and forms
from .models import UserProfile, GuestEmail
from .forms import RegisterForm, LoginForm, GuestForm

# decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables,sensitive_post_parameters

@sensitive_post_parameters()
def SignUp(request):
    registered=False
    if request.method == 'POST':
        userform = RegisterForm(request.POST)

        if userform.is_valid():
            form = userform.save(commit=False)
            form.set_password(form.password)
            form.save()
            registered=True
            return redirect('registration:login')
        else:
            print(userform.errors)
    else:
        userform = RegisterForm()
    context =   {'userform': userform,
                'registered':registered}

    return render(request, 'registration/signup.html', context)

@sensitive_variables('username', 'password', 'user')
def login_user(request):
    next_get = request.GET.get('next')
    next_post =request.POST.get('next')
    print(next_get, next_post)
    redirect_path = next_get or next_post or None

    if request.method=='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user=authenticate(request,username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    try:
                        del request.session['guest_email_id']
                    except:
                        pass
                    if is_safe_url(redirect_path, request.get_host()):
                        return redirect(redirect_path)
                    else:
                        return redirect('Home:home_page')
                else:
                    return HttpResponse('<h2>Your Account is not active</h2>')
            else:
                context={}
                return render(request, 'registration/error.html', context)
    else:
        login_form = LoginForm()
    context={"login_form":login_form}
    return render(request, 'registration/login.html', context)

def guest_register_view(request):
    next_get = request.GET.get('next')
    next_post =request.POST.get('next')
    print(next_get, next_post)
    redirect_path = next_get or next_post or None

    if request.method=='POST':
        guest_form = GuestForm(request.POST)
        if guest_form.is_valid():
            email=guest_form.cleaned_data.get('email')
            name=guest_form.cleaned_data.get('name')
            new_guest_email=GuestEmail.objects.create(email=email, name=name)
            request.session['guest_email_id']=new_guest_email.id
                    # return redirect('Home:home_page')
                    # try:
                    #     del request.session['guest_email_id']
                    # except:
                    #     pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('registration:signup')
    else:
        guest_form = GuestForm()
    context={"guest_form":guest_form}
    return redirect('registration:signup')


@login_required
def logout_user(request):
    logout(request)
    return redirect('registration:login')
