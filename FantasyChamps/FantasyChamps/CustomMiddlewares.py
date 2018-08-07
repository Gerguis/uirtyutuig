# # # from django.http import HttpResponseRedirect
# # # from django.urls import reverse
# # # from django.conf import settings

# # # # class AuthRequiredMiddleware(object):
# # # #     def process_request(self, request):
# # # #         if not request.user.is_authenticated():
# # # #             return HttpResponseRedirect(reverse('home'))
# # # #         return None


# # # class StackOverflowMiddleware(object):
# # #     def __init__(self, get_response):
# # #         self.get_response = get_response

# # #     def __call__(self, request):
# # #         response = self.get_response(request)
# # #         if not request.user.is_authenticated():
# # #             return HttpResponseRedirect(reverse('IndexView'))
# # #         return response

# import re
# from django.conf import settings
# from django.shortcuts import redirect

# EXEMPT_URLS = ['IndexView']#[re.compile(settings.LOGIN_URL.lstrip('/'))]

# # # if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
# # #     EXEMPT_URL = []


# class LogInRequiredMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         assert hasattr(request, 'user')
#         path = request.path_info
#         print(path)
#         if not request.user.is_authenticated():
#             if path not in EXEMPT_URLS:
#                 return redirect(settings.LOGIN_URL)

# # from django.shortcuts import HttpResponseRedirect


# # class LogInRequiredMiddleware(object):
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Code to be executed for each request before
# #         # the view (and later middleware) are called.

# #         response = self.get_response(request)
# #         if not request.user.is_authenticated():
# #             return HttpResponseRedirect('IndexView')

# #         # Code to be executed for each request/response after
# #         # the view is called.

# #         return response






