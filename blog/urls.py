from django.conf.urls import url
from django.contrib import admin
import posts.views

#以下の定義を追加
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #home
    url(r'^$',posts.views.home, name='home'),
#以下の定義を追加
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
