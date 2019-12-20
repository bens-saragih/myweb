from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('artikel.urls',namespace='artikel')),
    url(r'^account/',include('accounts.urls',namespace='account'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)