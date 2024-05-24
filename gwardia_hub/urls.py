"""
URL configuration for gwardia_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("genshin", include("genshin.urls")),
    path("panel/", include("gwardia.urls")),
    path("admin/", admin.site.urls),
]

handler403 = "core.views.handling_403"
handler404 = "core.views.handling_404"
handler500 = "core.views.handling_500"
