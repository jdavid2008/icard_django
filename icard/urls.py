"""
URL configuration for icard project.

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

# David. Importación para añadir las rutas estáticas de las imágenes
from django.conf import settings
from django.conf.urls.static import static
# -----------------------------------------------------------------

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.router import router_user
from categories.api.router import router_category
from products.api.router import router_product

schema_view = get_schema_view(
   openapi.Info(
      title="iCard - ApiDoc",
      default_version='v1',
      description="Documentación de la Api de iCard",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jdavid2008@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include(router_user.urls)), # ModelView
    path('api/', include('users.api.router')), # APiView
    path('api/', include(router_category.urls)), # ModelView
    path('api/', include(router_product.urls)), # ModelView

]

# David. Añadimos las rutas estáticas de las imágenes
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT);

