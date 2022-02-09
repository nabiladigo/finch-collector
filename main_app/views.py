from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View 
from .models import Print

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class PrintList(TemplateView):
    template_name = "print_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["prints"] = Print.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["prints"] = Print.objects.all()
            # default header for not searching 
            context["header"] = "Trending Artists"
        return context


class PrintCreate(CreateView):
    model = Print
    fields = ['name', 'image', 'price']
    template_name = "artist_create.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})



class PrintDetail(DetailView):
    model = Print
    template_name = "print_detail.html"

class PrintUpdate(UpdateView):
    model = Print
    fields = ['name', 'image', 'price']
    template_name = "print_update.html"
    def get_success_url(self):
        return reverse('print_detail', kwargs={'pk': self.object.pk})

class PrintDelete(DeleteView):
    model = Print
    template_name = "print_delete_confirmation.html"
    success_url = "/prints/"



