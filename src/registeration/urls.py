from django.conf.urls import url
from .views import SignUp, login_user, logout_user, guest_register_view

urlpatterns=[
    url(r'^signup/$', SignUp, name='signup'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
]
