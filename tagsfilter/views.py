from django.shortcuts import render

from django.views.generic import TemplateView 



class HomeView(TemplateView):
    template_name = 'tagsfilter/home.htm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Hi my name is Samman" 
        return context
    
    
