from django.urls import path,include
from .import views
from django.contrib import admin
app_name='movieapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('movie/<int:movie_id>',views.details ,name="details"),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]