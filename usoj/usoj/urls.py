"""usoj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from index.views import search, searchpage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^problem/', include('problem.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^solution/', include('solution.urls')),
    url(r'^group/', include('group.urls')),
    url(r'^judger/', include('judger.urls')),
    url(r'^$', include('index.urls')),
    url(r'^manage/', include('administrate.urls')),

    url(r'^search/', search, name='search'),
    url(r'^searchpage/', searchpage, name='searchpage'),

    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

from django.conf.urls.static import static
import usoj.settings

urlpatterns += static(usoj.settings.MEDIA_URL, document_root=usoj.settings.MEDIA_ROOT)
