from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='wealthwise/registration/login.html'), name='login'),

]