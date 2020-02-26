from django.http import HttpResponse
from django.shortcuts import render

from filmlookup.models import Result, Search, SearchType

# required POST vars to denote POST search
POST_VARS = {"search_type", "search_term"}

# Create your views here.

# OMDB lookup page
def index(request):

    context = {"search_types": list(SearchType), "show_results": False, "error": False}

    # if POST is populated as required to denote an incoming search
    # NB: there is surely a better way to do this
    if POST_VARS.issubset(request.POST):

        # update context with search results
        for v in POST_VARS:
            context[v] = request.POST[v]

        # look for cached results, and grab if present
        try:
            search = Search.objects.get(search_type=context["search_type"], 
                search_term=context["search_term"])
            
            context["results"] = search.results.all()
            context["show_results"] = True
        
        # otherwise query from OMDB API
        except:

            # setup search object
            search = Search(search_type=context["search_type"], 
                            search_term=context["search_term"])

            # source results externally, return error flag
            context["error"] = search.query_external()
            
            # update context if no error encountered
            if not context["error"]:
                context["results"] = search.results.all()
                context["show_results"] = True
            else:
                context["show_results"] = False


    return render(request, "index.html", context)



