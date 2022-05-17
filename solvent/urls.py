from django.urls import path
from. import views

app_name = "solvent"
urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("buy/", views.buy, name="buy"),
    path("contactus/", views.contactus, name="contactus"),
    path("forrent/", views.forrent, name="forrent"),
    path("land", views.land, name="land"),
    path("sopro/", views.solventProperty, name="solventProperty")

]