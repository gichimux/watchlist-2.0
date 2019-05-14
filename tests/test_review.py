import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    test class to test the behavior of the movie class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_review = Movie(1234, 'Python must be crazy', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 'Python must be crazy')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_review, Review))

