from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.LoginPage, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_view, name='logout'),
    path('work/<int:item_id>/', views.work, name="work"),
    path('create/', views.create, name="create"),
    path('addwork/<int:pk>/', views.addWork, name='addwork'),
]
