
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Products
from .forms import ProductsForm

def succeed(request):
    return render(request, 'form_complete.html')

class ProductCreateView(View):
    form_class = ProductsForm
    template_name = 'form.html'
    is_valid = True

    def get_form_list(self):
        form_data = self.request.POST.copy()
        form_list = []
        for address in self.request.POST.getlist("address"):
            form_data.setlist("address", address)
            form = self.form_class(form_data, self.request.FILES)
            if form.is_valid():
                form_list.append(form.save(commit=False))
            else:
                self.is_valid = False 
        return form_list

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request, *args, **kwargs):
        form_list = self.get_form_list()
        if self.is_valid:
            Products.objects.bulk_create(form_list)
            return HttpResponseRedirect(reverse_lazy('succeed'))
        else:
            return render(request, self.template_name, {"form": self.form_class(request.POST, request.FILES)})
            
