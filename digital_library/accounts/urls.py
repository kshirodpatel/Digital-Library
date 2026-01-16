from django.urls import path, include
# from accounts import views as views
# from django.contrib.auth import views as auth_views
from . import views
# from .views import RegisterView, MyLoginView, UserProfileView

# urlpatterns = [
#     path("login/", MyLoginView.as_view(), name="login"),
#     path("register/", RegisterView.as_view(), name='register' ),
#     path("logout/", auth_views.LogoutView.as_view(), name='logout' ),
#     path("profile/", UserProfileView.as_view(), name='user-profile'),
# ]

urlpatterns = [
    path("register/", views.RegisterUser, name="register")
]