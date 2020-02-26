from django.test import TestCase

from filmlookup.models import Search, Result

# Create your tests here.


class QueryExternalTestCase(TestCase):
    """ query external OMDB API calls """

    def setUp(self):
        pass

    def test_known_query(self):
        search = Search(search_type="movie", search_term="dancer in the dark")
        error = search.query_external()

        self.assertEqual(error, False)
        self.assertEqual(search.results.first().year, "2000")

    def test_noresults_query(self):
        search = Search(search_type="episode", search_term="qwerty")
        error = search.query_external()

        self.assertEqual(error, True)
