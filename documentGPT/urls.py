
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "mysite header"
admin.site.site_title = "mysite title"
admin.site.index_title = "mysite index title"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        