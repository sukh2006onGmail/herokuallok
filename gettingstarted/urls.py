from django.urls import path, include

from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

def greet(request):
    return HttpResponse('aa')

urlpatterns = [
    path("", greet),
    path("admin/", admin.site.urls),
]
