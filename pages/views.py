from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Post



class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"


class EventsPageView(View):
    
    def post_list(request):
        posts = Post.published.all()
        return render(request,
                      'events.html',
                      {'posts': posts})