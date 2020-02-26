from django.db import models

import requests
import json
import pandas as pd
from enum import Enum


# OMDB API config
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "c769b385"
OMDB_API_MAX_PAGES = 10

# href to IMDB title pages
IMDB_URL = "http://www.imdb.com/title/"

# OMDB search type enumeration
class SearchType(Enum):
    Movies = "movie"
    Series = "series"
    Episodes = "episode"

# populate choices as enumerated
SEARCH_TYPE = ((v.name, v.value) for v in SearchType)


class Result(models.Model):

    title = models.TextField(default="")
    ftype = models.CharField(max_length=100, choices=SEARCH_TYPE)
    year = models.TextField(default="")
    link = models.TextField(default="")

    def __str__(self):
        return f'{self.title} | {self.ftype} | {self.year}'


class Search(models.Model):

    search_type = models.CharField(max_length=100, choices=SEARCH_TYPE)
    search_term = models.TextField()
    results = models.ManyToManyField(Result) #, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.search_type} | {self.search_term}'


    def query_external(self):
        """ query the OMDB API and save results """

        # API parameters as per http://www.omdbapi.com/
        params = {
            "apikey": OMDB_API_KEY,
            "s": self.search_term,
            "type": self.search_type,
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

            # results will be empty for a dud search
            if len(results) == 0:
                return True

            # concat all results pages/dataframes
            df = pd.concat(results, axis=0)

            # add links to the IMDB website
            df["Link"] = IMDB_URL + df["imdbID"]

            # need to save before use in many-to-many relationships with
            # results
            self.save()

            # create and link results to search and save to cache db
            for (_, r) in df.iterrows():
                result = Result(title=r['Title'], ftype=r['Type'], 
                                year=r['Year'], link=r['Link'])
                result.save()
                self.results.add(result)

            # save again with results updated
            self.save()

            return False

        except Exception as e:
            return True

