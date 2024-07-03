from django.urls import path
from django.contrib import admin

import phones.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', phones.views.index),
    path('catalog/', phones.views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', phones.views.show_product, name='phone'),
]
