from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)


def create_record(request):
    # phone = Phone(id = '1', name = 'e', price = '5', image = 'e', release_date = 'e', lte_exists = 'e', slug = 'e')
    # phone.save()
    return HttpResponse(f'done! new record {phone.name}, {phone.price}')

