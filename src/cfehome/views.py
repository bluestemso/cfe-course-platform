from django.shortcuts import render

from emails.forms import EmailForm

def home_view(request, *args, **kwargs):
    template_name = 'home.html'
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        'message': None,
    }
    if form.is_valid():
        form.save()
        context['form'] = EmailForm()
        context['message'] = "Success! Check your email for a verification link."
    return render(request, template_name, context)