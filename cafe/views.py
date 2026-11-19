from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, MenuItem, GalleryImage
from .forms import ReservationForm, ContactForm


def build_context(**extra):
    ctx = {
        "featured": MenuItem.objects.filter(featured=True, available=True)[:6],
        "gallery": GalleryImage.objects.all()[:6],
        "categories": Category.objects.prefetch_related('items'),
        "reservation_form": ReservationForm(auto_id='res_%s'),
        "contact_form": ContactForm(auto_id='con_%s'),
    }
    ctx.update(extra)
    return ctx


def home(request):
    return render(request, "home.html", build_context())


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, auto_id='res_%s')
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your reservation request has been received.")
            return redirect('/#reserve')
        return render(request, "home.html", build_context(reservation_form=form))
    return redirect('/#reserve')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, auto_id='con_%s')
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent. We'll get back to you soon.")
            return redirect('/#contact')
        return render(request, "home.html", build_context(contact_form=form))
    return redirect('/#contact')