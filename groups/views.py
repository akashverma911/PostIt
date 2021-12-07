from django.shortcuts import render
from django.views import generic
# Create your views here.

from groups.models import Group,GroupMember

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
