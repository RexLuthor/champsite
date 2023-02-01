# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, EventsPageView

urlpatterns = [
    path('events/', EventsPageView.post_list, name='events'),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]