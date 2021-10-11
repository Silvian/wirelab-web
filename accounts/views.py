from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    """Login view."""

    template_name = "web/login.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.GET.get('logout', False):
            context['logout'] = True
            context['msg'] = "You are now logged out successfully."
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def authenticate_user(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])

        if user is not None:
            # the password is verified for the user
            if user.is_active:
                login(request, user)
                return redirect('/')

            else:
                context['msg'] = "Your account has been disabled. Please contact your system administrator."
                return render(request, "web/login.html", context)

        else:
            # the authentication system was unable to verify the username and password
            context['msg'] = "Invalid credentials provided."
            return render(request, "web/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login/?logout=true')
