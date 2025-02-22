"""
URL configuration for formaloo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from appstore import urls as appstore_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Appstore API",
        default_version="v1",
        description="API documentation for Appstore",
        terms_of_service="",
        contact=openapi.Contact(email="m.ghaffari662@gmail.com"),
        license=openapi.License(name="Mohammad Ghaffary"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('apps', include(appstore_urls)),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]

