from django.shortcuts import render, get_object_or_404

from . models import Snippets

def all_snippets(request):
    snippet = Snippets.objects
    return render(request, 'snippets/all_snippets.html', {'snippets':snippets})

def snippets_detail(request, snippet_id):
    # pass in the model (Snippets) and the primary key in the db
    snippet_detail = get_object_or_404(Snippets, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet':snippet_detail})
