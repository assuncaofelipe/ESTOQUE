from django.contrib import admin
from django.urls import path, include
from app.views import handler404, home, produtos, form, create, view, edit, update, delete


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('produtos/', produtos, name='produtos'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>', view, name='view'),
    path('edit/<int:pk>', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('', include('usuarios.urls')),
]

handler404 = "app.views.handler404"
