from django.conf.urls import url, include
from .views import home_page, index_page


urlpatterns = [
    url(r'^$',index_page, name="index_page"),
    url(r'^home/$',home_page, name="home_page"),
]
