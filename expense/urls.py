from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views

from expense import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in', auth_views.LoginView.as_view(
        template_name="expense/sign_in.html"
    ), name="signin"),
    # path('logout', views.logout, name='logout'),
    path('logout', auth_views.LogoutView.as_view(
        next_page=settings.LOGIN_REDIRECT_URL
    ), name='logout'),
]

