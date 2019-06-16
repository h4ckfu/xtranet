from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views


urlpatterns = [
    path('', front_page.views.front_page, name = 'front_page'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('jobs/', include('jobs.urls')),
    path('snippets/', include('snippets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)