from django.conf import settings
from django.contrib.auth import login as auth_login, views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View


class ResisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        context = {"form": UserCreationForm()}
        return TemplateResponse(request, "accounts/register.html", context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            return TemplateResponse(request, "accounts/register.html", {"form": form})
        user = form.save()
        auth_login(request, user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


register = ResisterView.as_view()


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/login.html"


login = LoginView.as_view()
