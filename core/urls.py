from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from core.views import RegisterView

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
]