from django.urls import path
from . import views
# from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView

urlpatterns = [
  path('',views.home, name='users-home'),
  path('register/',RegisterView.as_view(),name='users-register')
]