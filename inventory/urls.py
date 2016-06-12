from django.conf.urls import url, include
from inventory import views
app_name="game"

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
