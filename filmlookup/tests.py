from django.test import TestCase

from filmlookup.views import query_external

# Create your tests here.

class QueryExternalTestCase(TestCase):
	""" query external OMDB API calls """

	def setUp(self):
		pass

	def test_known_query(self):
		(df, success) = query_external("movie", "dancer in the dark")

		self.assertEqual(success, True)
		self.assertEqual(df.iloc[0]['Year'], '2000')


	def test_noresults_query(self):
		(df, success) = query_external("episode", "qwerty")

		self.assertEqual(success, True)
		self.assertEqual(len(df), 0)






