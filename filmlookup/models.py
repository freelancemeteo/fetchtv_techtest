from django.db import models

from filmlookup.views import SearchType

# Create your models here.


class Search(models.Model):

    # populate choices as enumerated elsewhere
    SEARCH_TYPE = ((v.name, v.value) for v in SearchType)

    search_type = models.CharField(max_length=100, choices=SEARCH_TYPE)
    search_term = models.TextField()


class Results(models.Model):

    search = models.ForeignKey(Search, on_delete=models.CASCADE)
    title = models.TextField(default="")
    year = models.TextField(default="")
    link = models.TextField(default="")
