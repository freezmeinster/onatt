"""onatt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from attendance.views import index, success, error

admin.site.site_header = "PLB Online Attendance"
admin.site.site_title = "PLB Online Attendance"
admin.site.index_title = "PLB Online Attendance"

urlpatterns = [
    path('', index, name="index"),
    path('success/', success, name="success"),
    path('error/', error, name="error"),
    path('admin/', admin.site.urls),
]
