from .views import Students, MytokenObtainPairView, Crud
from django.urls import path
from rest_framework_simplejwt.views import(TokenRefreshView)

urlpatterns = [
    path('api/token/', MytokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', Students),
    path('crud/<int:id>', Crud),
]
