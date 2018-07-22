from django.shortcuts import render
from . forms import UserForm, ProfileForm
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# @login_required
# def LogoutView(request):
#     logout(request)



# def RegisterView(request):

#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = ProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             registered = True

#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = ProfileForm()
#     return render(request, 'index.html',
#                           {'user_form': user_form,
#                            'profile_form': profile_form,
#                            'registered': registered})

# def RegisterView(request):

#     registered = False

#     if request.method == 'POST':

#         user_form = UserForm(data=request.POST)

#         if user_form.is_valid:

#             user = user_form.save()

#             user.set_password(user.password)

#             user.save()

#     else:
#         user_form = UserForm()

#     return render(request, 'accounts/registration.html', {'user_form': user_form, 'registered': registered})


# def LogInView(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 q = User.objects.get(pk=request.user.pk)
#                 q.balance = q.balance+10
#                 return HttpResponseRedirect(reverse('accounts:register'))
#             else:
#                 return HttpResponse("Your account is not active.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")

#     else:
#         return render(request, 'accounts/login.html', {})
# # 