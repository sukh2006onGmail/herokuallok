from django.urls import path, include

from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


# admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

def greet(request):
    return HttpResponse('aa')

def stat(request):
    q = Question.objects.all()
    # return render(request, 'index.html')
    return render(request, 'index.html', {'data': q})

urlpatterns = [
    path("", greet),
    path("stat", stat),
    # path("admin/", admin.site.urls),
]
