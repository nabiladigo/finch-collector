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
    fields = ['name', 'img', 'price']
    template_name = "print_update.html"
    def get_success_url(self):
        return reverse('print_detail', kwargs={'pk': self.object.pk})

class PrintDelete(DeleteView):
    model = Print
    template_name = "print_delete_confirmation.html"
    success_url = "/prints/"



# Print= [
#     Print("Mugs","https://i.ebayimg.com/images/g/VAQAAOSwVj5bW9YZ/s-l400.jpg","5"),
#     Print("Cards", "https://images.indianexpress.com/2019/02/valentine-day-gift_2amp.jpg","10"),
#     Print("Photo Books", "https://cms.cloudinary.vpsvc.com//image/fetch/q_auto:eco,w_1284,f_auto,dpr_auto/https://s3-eu-west-1.amazonaws.com/sitecore-media-bucket/prod%2Fen%2F%7BF547F61F-A34D-6590-A08C-B443FD688632%7D%3Fv%3D43a51e4a29bdef19203575f899c8deb7", "20"),
#     Print("Puzzles", "https://media.istockphoto.com/photos/hand-of-programmer-holds-puzzle-with-html-programming-language-picture-id497752600?s=612x612", "15")
# ]