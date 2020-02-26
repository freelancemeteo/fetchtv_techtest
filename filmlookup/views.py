from django.http import HttpResponse
from django.shortcuts import render

import requests
import json
import pandas as pd
from enum import Enum

# OMDB search type enumeration
class SearchType(Enum):
    Movies = "movie"
    Series = "series"
    Episodes = "episodes"

# OMDB API config
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "c769b385"
OMDB_API_MAX_PAGES = 10

# href to IMDB title pages
IMDB_URL = "http://www.imdb.com/title/"

# required POST vars to denote POST search
POST_VARS = {"search_type", "search_term"}



# Create your views here.

# OMDB lookup page
def index(request):

    context = {"search_types": list(SearchType), "show_results": False, "error": False}

    # if POST is populated (ie incoming search)
    if POST_VARS.issubset(request.POST):

        # update context with search results
        for v in POST_VARS:
            context[v] = request.POST[v]

        # query OMDB API
        (context["results"], context["error"]) = query_external(
            context["search_type"], context["search_term"]
        )

        context["show_results"] = True

    return render(request, "index.html", context)


def query_external(search_type, search_term):
    """ query the OMDB API """

    # API parameters as per http://www.omdbapi.com/
    params = {
        "apikey": OMDB_API_KEY,
        "s": search_term,
        "type": search_type,
        "r": "json",
    }

    # query API page by page up until OMBD_API_MAX_PAGES
    # have been retrieved. Accumulate results.
    try:
        results = []
        for page in range(1, OMDB_API_MAX_PAGES + 1):

            params["page"] = page
            response = requests.get(OMDB_API_URL, params=params)
            assert response.status_code == 200

            # becomes False if no more results available
            if response.json()["Response"] != "True":
                break

            # convert response to dataframe and append
            results.append(pd.DataFrame(response.json()["Search"]))

    except Exception as e:

    	# something's failed, return empty and flag error
        return (pd.DataFrame(), True)


    # concat results tables
    df = pd.concat(results, axis=0)

    # add links to the IMDB website
    df["Link"] = IMDB_URL + df["imdbID"]

    return (df, False)
