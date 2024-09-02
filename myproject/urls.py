from django.contrib import admin
from django.urls import path
from Weatherapp import views # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('delete/<CName>',views.delete,name="DCity")
]
