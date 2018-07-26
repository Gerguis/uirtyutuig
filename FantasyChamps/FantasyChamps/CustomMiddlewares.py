# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.conf import settings

# # class AuthRequiredMiddleware(object):
# #     def process_request(self, request):
# #         if not request.user.is_authenticated():
# #             return HttpResponseRedirect(reverse('home'))
# #         return None


# class StackOverflowMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect(reverse('IndexView'))
#         return response
