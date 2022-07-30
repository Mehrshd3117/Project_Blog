from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('', include('home.urls')),
    path('', include('account.urls')),
    path('about/', include('about_us.urls')),
    path('articles/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

