from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

# urls and the functions in case of the url machtes
urlpatterns = [
    path("admin", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),
    path('about/', views.about),
    path('', views.home),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
