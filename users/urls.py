from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.Login, name="login"),
    path('register/',views.Signup, name="register" ),
    path('account/', views.account, name="account"),
    path('logout/', views.logout_user, name="logout"),
    path('delete/', views.delete_user, name="delete"),
]