from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path, include

from users import views


urlpatterns = [
    path('sign-in', views.LoginView.as_view(), name='token_obtain_pair'),
    path('sign-up', views.RegisterView.as_view(), name="auth_register"),
    path('users/admins', views.AdminsView.as_view({"get": "list", "post": "create"}), name='admins_view'),
    path('users', views.UsersView.as_view({'get': 'list'}), name="user_view"),
    path("users/<int:pk>", views.UsersView.as_view({"delete": "destroy"}), name="user_view_destroy")
]
