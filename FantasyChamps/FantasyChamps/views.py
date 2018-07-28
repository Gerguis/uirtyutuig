from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from accounts.forms import UserForm, ProfileForm, UserLogInForm
from django.contrib.auth.decorators import login_required
# class IndexView(TemplateView):
#     template_name = "index.html"


def handler404(request):
    return HttpResponseRedirect(reverse('IndexView'))


@login_required
def UserLogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('IndexView'))


def IndexView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('cricket_center')
    else:
        registered = False
        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        login_form = UserLogInForm(request.POST or None)
        if request.method == 'POST':
            if request.POST.get('submit') == 'Login':
                login_form = UserLogInForm(data=request.POST)
                if login_form.is_valid:
                    username = login_form.data.get("username")
                    password = login_form.data.get("password")
                    user = authenticate(username=username, password=password)
                    if user:
                        # Check it the account is active
                        if user.is_active:
                            # Log the user in.
                            login(request, user)
                            # user.profile.balance = user.profile.balance+10
                            # print(user.profile.balance)
                            user.save()

                            # print(request.user.profile.balance)
                            # print(request.user.profile.balance+10)
                            # request.user.profile.save()
                            # Send the user back to some page.
                            # In this case their homepage.
                            return HttpResponseRedirect('cricket_center')
                        else:
                            # If account is not active:
                            return HttpResponse("Your account is not active.")

                    else:
                        print("Someone tried to login and failed.")
                        print("They used username: {} and password: {}".format(username, password))
                        return HttpResponse("Invalid login details supplied.")
            if request.POST.get('submit') == 'Register':
                user_form = UserForm(data=request.POST)
                profile_form = ProfileForm(data=request.POST)
                if user_form.is_valid() and profile_form.is_valid():
                    user = user_form.save(commit=False)
                    user.set_password(user.password)
                    user.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.save()
                    registered = True
                else:
                    print(user_form.errors, profile_form.errors)
        return render(request, 'index.html',
                              {
                                'user_form': user_form,
                                'profile_form': profile_form,
                                'login_form': login_form,
                                'registered': registered
                              })


#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = ProfileForm(data=request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if username and password is not None:
#             user = authenticate(username=username, password=password)
#             if user:
#             # Check it the account is active
#                 if user.is_active:
#                     # Log the user in.
#                     login(request, user)
#                     user.profile.balance = user.profile.balance+10
#                     print(user.profile.balance)
#                     print(user)
#                     user.save()

#                     # print(request.user.profile.balance)
#                     # print(request.user.profile.balance+10)
#                     # request.user.profile.save()
#                     # Send the user back to some page.
#                     # In this case their homepage.
#                     return HttpResponseRedirect(reverse('index'))
#                 else:
#                     # If account is not active:
#                     return HttpResponse("Your account is not active.")

#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")



#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
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
#                           {
#                             'user_form': user_form,
#                             'profile_form': profile_form,
#                             'registered': registered
#                           })

# # print(context_dict)
