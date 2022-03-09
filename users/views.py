from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm,LoginForm,UpdateProfileForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'profile_form': profile_form})

class RegisterView(View):
  form_class = RegisterForm
  initial = {'key':'value'} 
  template_name = 'users/register.html'

  def get(self,request,*args,**kwargs):
    form = self.form_class(initial = self.initial)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def sendMail(request):
    if request.method == 'POST':
        sender = settings.EMAIL_HOST_USER
        receiver = request.POST['receiver']
        subject = request.POST['sub']
        content = request.POST['content']

        mail = send_mail(subject, content, sender, [receiver], fail_silently=False)
        if mail:
            messages.success(request, 'Email has been sent.')
            return redirect('home')
        else:
            return HttpResponse('message not sent')
    else:
        return redirect('home')