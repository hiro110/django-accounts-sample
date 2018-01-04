from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'accounts/index.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('id')
        else:
            return User.objects.filter(pk=self.request.user.id)


def new(request):
    form = CustomUserCreationForm()
    return render(request, 'accounts/new.html', {'form': form,})


def create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../login')
        return render(request, 'accounts/new.html', {'form': form,})
    else:
        raise Http404

