from django.urls import path
from users.views import authorization_api_view, registration_api_view, confirm_api_view

urlpatterns = [
    path("login/", authorization_api_view),
    path("register/", registration_api_view),
    path("confirm/", confirm_api_view),

]
