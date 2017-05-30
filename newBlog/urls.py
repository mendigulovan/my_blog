"""newBlog URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from newBlog import settings
from newapp import views
urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^reg/$',views.reg),
    url(r'^auth/$',views.auth),
    url(r'^login/$',views.log_in),
    url(r'^log_out/$',views.log_out),
    url(r'^comments/',views.all_comments),
    url(r'^article/(\d+)/',views.article),
    url(r'^add_comment/(\d+)/',views.add_comment),
    url(r'^add_user/',views.add_user),
    url(r'^category/(\d+)/',views.category),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^redactor/', include('redactor.urls'))
]
