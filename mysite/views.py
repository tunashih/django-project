from datetime import datetime
from django.shortcuts import render

from .forms import SearchForm
from .models import Hotel

year = datetime.today().year


def home(request):
    form = SearchForm
    context = {
        'hotels': Hotel.objects.all().order_by('?')[:3],
        'form': form
    }
    return render(request, 'mysite/home.html', context)


def about(request):
    return render(request, 'mysite/about.html', {'title': 'About'})


def search(request):
    form = SearchForm()
    return render(request, 'mysite/search.html', {'title': 'Search', 'form': form})


def search_results(request):
    query_string = ''
    found_entries = None
    if ('year' in request.GET) and request.GET['year'].strip():
        query_string = request.GET['year']
        hotels = Hotel.objects.filter(year_opened=query_string)
        return render(request, 'mysite/search_results.html', {'query_string': query_string, 'hotels': hotels})
    else:
        return render(request, 'mysite/search_results.html',
                      {'query_string': 'Null', 'found_entries': 'Enter a search term'})
