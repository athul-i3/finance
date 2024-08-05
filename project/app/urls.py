from django.urls import path
from app import views

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('delete_item/int<delid>',views.delete_item,name='delete_item'),
    path('signup',views.signup,name='signup'),
    path('add_expenses',views.add_expenses,name='add_expenses'),
    path('edit/int<editid>',views.edit,name='edit'),
    path('update/int<updateid>',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('filter1', views.filter1, name='filter1'),


   
          


    
]