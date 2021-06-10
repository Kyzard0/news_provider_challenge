from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from .views import SignUpView

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
