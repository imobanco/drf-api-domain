"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

from users.urls import urlpatterns as users


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include_docs_urls(title="Minha API de demostração"))
]


urlpatterns.extend(users)


if settings.DEBUG:
    from debug_toolbar import urls as debug_urls

    urlpatterns.append(path("__debug__", include(debug_urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

