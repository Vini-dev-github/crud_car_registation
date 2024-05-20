from django.contrib import admin
from django.urls import path
from app_registration.views import home, form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('form/', form)
]
