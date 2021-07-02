from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, CreateView

from user.form import UserModelForm
from user.models import UserModel


class UserListView(ListView):
    template_name = 'Class_view.html'

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q:
            news = UserModel.objects.filter(name__icontains=q
                                            ).order_by('-pk')
        else:
            news = UserModel.objects.all()
        return news


class UserCreateView(CreateView):
    # name of form variable is  -  form
    template_name = 'forms.html'
    form_class = UserModelForm
    success_url = '/user/'
