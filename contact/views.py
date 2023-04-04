from django.shortcuts import render, redirect
from .forms import ContactForm, NewsletterForm


def index(request):
    form = ContactForm(request.POST or None)
    form1 = NewsletterForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user.profile.full_name
            obj.save()
            return redirect('.')
    else:
        if form.is_valid():
            form.save()
            return redirect('.')
    if form1.is_valid():
        form1.save()
        return redirect('.')
    ctx = {
        'form': form,
        'form1': form1,
    }
    return render(request, 'podcast/contact.html', ctx)
