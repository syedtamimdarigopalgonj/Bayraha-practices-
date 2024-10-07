from django.contrib import admin
from django.urls import path
from delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delivery/', views.delivery_view, name='delivery'),
]