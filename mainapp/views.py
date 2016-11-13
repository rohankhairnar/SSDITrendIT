from django.shortcuts import render, render_to_response
from mainapp.models import UserProfile
from mainapp.forms import UserForm, UserProfileForm, ResetPasswordForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mainapp.forms import ContactForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



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


def forgot_password(request):
    context = RequestContext(request)


    if request.method == 'POST':
        email1 = request.POST['email']
        print(email1)
        try:
            username = User.objects.get(email=email1)
            print(username)
        except User.DoesNotExist:
            username = None

        if username:
            password_reset_message = '\n' + 'Hello ' +username.get_username()+ ',' + '\n\n' + 'To reset your password click on the following link:' + '\n\n' + 'http://127.0.0.1:8000/resetpassword' + '\n\n' + 'Regards' + '\n\n' + '-Trend!t Team'
            send_mail("Reset your Trend!t password",
                      password_reset_message,
                      settings.EMAIL_HOST_USER,
                      [email1],
                      fail_silently=False, )
            return HttpResponseRedirect('/email')
        else:
            print("Invalid email: {0}".format(email1))
            return HttpResponseRedirect('/invalidemail')

    else:
        return render(request, "app/forgotpassword.html", {}, context)


def forgot_username(request):
    context = RequestContext(request)

    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        try:
            username = User.objects.get(email=email)
            print(username)
        except User.DoesNotExist:
            username = None

        if username:
            username_salutation = 'Hello,' +'\n\n'
            username_signature = '\n\n'+'Regards' + '\n\n' + '-Trend!t Team'
            send_mail("Reset your Trend!t password",
                      username_salutation+'Your registered username is {0}'.format(username)+username_signature,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False, )
            return HttpResponseRedirect('/email')
        else:
            print("Invalid email: {0}".format(email))
            return HttpResponseRedirect('/invalidemail')

    else:
        return render(request, "app/forgotusername.html", {}, context)


def invalid_email(request):
    return render(request, "app/invalidemail.html")


def reset_password(request):
    if request.method == 'POST':
        reset_form = ResetPasswordForm(data=request.POST)

        # user=reset_form.save()
        # print(user)
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            username1 = User.objects.get(username=username)

            print(username, username1, password)
        except User.DoesNotExist:
            username1 = None

        # ResetPasswordForm.clean_password2(reset_form)
        # print(reset_form.errors)


        if username1 != None and password == password2:
            username1.set_password(password)
            username1.save()
            return HttpResponseRedirect('/passwordchange')
        elif username1 != None and password != password2:
            return HttpResponse("Your passwords do not match, try again!")
            # print(reset_form.errors)
        else:
            print("Invalid login details: {0}".format(username))
            return HttpResponseRedirect('/invalidusername')

    else:
        reset_form = ResetPasswordForm()

    context = {'reset_form': reset_form}
    return render(request, 'app/resetpassword.html', context)


def invalid_username(request):
    return render(request, "app/invalidusername.html")


def email(request):
    return render(request,"app/email.html")


def password_change(request):
    return render(request,"app/passwordchange.html")



def contact(request):
    form_class = ContactForm        #grabbing a form from forms.py

    if request.method=='POST':
        form=form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')

            contact_subject = request.POST.get(
                'contact_subject'
                , '')
            contact_message = request.POST.get('contact_message', '')

        else:
            print(ContactForm.errors)

        contact_message1= '\033 New Support Email \n From: ' + contact_name+' \n\n' + 'Subject: ' + contact_subject + \
                          '\n Email: ' + contact_email + ' \n\n Message: \n ' + contact_message;
        send_mail(
            "New Support Email received",
            contact_message1,
            'admin@trendit.com',
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    return render(request, 'app/contact.html', {
        'form': form_class}) #passing it to template.



class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context
#
# def contact(request):
#     send_mail(
#         'Hello!',
#         "Message body, Test Email",
#         settings.EMAIL_HOST_USER,
#         [''],
#         #  send_to email ID in ['']
#         fail_silently=False,
#     )
#     return render(request, "app/contact.html")