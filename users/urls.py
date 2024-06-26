from rest_framework.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change_password/', ChangePasswordView.as_view()),
    path('lose_password/', ForgotPasswordView.as_view()),
    path('lose_confirm/', ForgotPasswordCompleteView.as_view(), name='forgot'),
    path('facebook-login/', FacebookLogin.as_view(), name='fb_login'),
    path('google-login/', GoogleLogin.as_view(), name='google_login'),
]