
from django.core.management.base import BaseCommand
from filmlookup.models import Search, Result

class Command(BaseCommand):

    help = 'Update searches with fresh OMDB data'

    def handle(self, **options):
        """ update searches with fresh OMDB data """

        for search in Search.objects.all():
            search.query_external()
            self.stdout.write(self.style.SUCCESS(f'Updated search {search}'))