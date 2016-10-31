from django.shortcuts import render, render_to_response
from app.models import UserProfile
from app.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

#from app.forms import CategoryForm

# Create your views here.


def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'app/register.html', context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Trend!t account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponseRedirect('/invalid')

    else:
        return render(request,'app/login.html', {}, context)


def index(request):
    return render(request, "app/index.html")


def user_details(request):
    return render(request, "app/details.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def invalid_entry(request):
   return render(request, "app/invalid.html")

