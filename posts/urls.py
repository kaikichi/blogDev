from django.conf.urls import url
from django.contrib import admin
import posts.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #home
    url(r'^$',posts.views.home, name='home'),
]
