from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html'), context
