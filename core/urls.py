from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("customers.urls")),
    path("farmers/", include("famers.urls")),
    path("admin/", admin.site.urls),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# handler404 = 'customers.views.handler404'
# handler500 = 'customers.views.handler500'