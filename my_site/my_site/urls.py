from django.contrib import admin
from django.urls import path, include
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('main.urls')),
   path('catalog/', include('main.urls')),
   path('sheetthree/', include('main.urls')),
   path('sheetfour/', include('main.urls'))]