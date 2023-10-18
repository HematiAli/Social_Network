from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, self.template_name, 'success')
            return redirect('home:home')

        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
