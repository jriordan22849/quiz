"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import accounts.views
import quiz.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/',accounts.views.signup, name ="signup"),
    url(r'^login/',accounts.views.loginUser, name ="login"),
    url(r'^logout/',accounts.views.logoutUser, name ="logout"),
    url(r'^quiz/',quiz.views.viewqs, name ="viewqs"),
    url(r'^picked/(?P<quixID>[0-9]+)/$',quiz.views.picked, name ="picked"),
    url(r'^completed/',quiz.views.completed, name ="completed"),
]