from django.urls import path,include
from .views import GoogleLogin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('dj/', include('dj_rest_auth.urls')),
    path('dj/registration/', include('dj_rest_auth.registration.urls')),
    path('dj/google/', GoogleLogin.as_view(), name='google_login'),
    path('accounts/', include('allauth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]