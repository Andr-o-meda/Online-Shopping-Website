from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"), 
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("index",views.index,name="home"),
    path("logins",views.logins,name="logins"),
    path("loginc",views.loginc,name="loginc"),
    path("signup",views.signup,name="signup"),
    path("logt",views.logt,name="logt"),
    path("prod/",views.prod,name="prod"),
    path("cart/",views.cart,name="cart"),
    path("search/",views.search,name="search"),
    path("prod/<int:myid>",views.prodview,name="prodview"),
]
