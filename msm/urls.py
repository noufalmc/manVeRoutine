
app_name ="user"

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

                  #These 2 urls for JWT token
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  path('admin/', admin.site.urls),
                  path('api/v1/', include('api.v1.user.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
