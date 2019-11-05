from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^about/", views.about, name="blog-about"),
    url(r"", views.home, name="blog-home"),
]
