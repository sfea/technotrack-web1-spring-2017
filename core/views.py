from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView


def test(request, post_id=None, blog_id=None):
    #return HttpResponse('Test passed, post_id = {}, blog_id = {}'. format(post_id, blog_id))
    return render(request, "core/file.html", {"post_id" : post_id, "blog_id" : blog_id})

class CreateUser(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")

class RegisterView(CreateView):

    form_class = CreateUser
    template_name = 'core/registration_form.html'

    def get_success_url(self):
        return reverse('core:login')

    def form_valid(self, form):
        form.save(commit=True)
        return super(RegisterView, self).form_valid(form)