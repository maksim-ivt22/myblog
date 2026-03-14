# myblog/urls.py
from django.contrib import admin
from django.urls import path, include # include нам тоже понадобится
from django.conf import settings # Импортируем настройки
from django.conf.urls.static import static # Импортируем функцию static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Эта строчка добавляет возможность видеть картинки в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)