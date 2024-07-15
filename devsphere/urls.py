from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('base.urls'), name="base-urls"),
    path('admin/', admin.site.urls),
]