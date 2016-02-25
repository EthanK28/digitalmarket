from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import (
        TagDetailViev,
        TagListView,

        )

urlpatterns = [
    url(r'^$', TagListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', TagDetailViev.as_view(), name='detail'),
]



