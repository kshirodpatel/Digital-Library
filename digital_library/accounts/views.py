# from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm

# from django.contrib.auth import login
# from django.contrib.auth.models import User
# from django.views.generic.edit import CreateView
# from .forms import CustomUserCreationForm
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import DetailView
# from django.contrib.auth.forms import UserCreationForm

def RegisterUser(request):
    form = MyUserCreationForm()
    context = {"form":form}

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
        

    context = {"form":form}
    return render(request, "accounts/register.html", context)

# def RegisterView(request):
#     form = UserCreationForm()
#     return render(request, "accounts/register.html", {"form":form})
#     # form_class = CustomUserCreationForm
#     # success_url = reverse_lazy('accounts:login')
#     # template_name = "accounts/register.html"

#     # def dispatch(self, request, *args, **kwargs):
#     #     if request.user.is_authenticated:
#     #         return redirect("/")
#     #     return super().dispatch(request, *args, **kwargs)

#     # def form_valid(self, form):
#     #     response = super().form_valid(form)
#     #     login(self.request, self.object)
#     #     return redirect("/")


# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'accounts/profile.html'
#     context_object_name = 'profile_user'

#     def get_object(self):
#         return self.request.user

# class MyLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     redirect_authenticated_user = True  # Prevents logged-in users from seeing login page