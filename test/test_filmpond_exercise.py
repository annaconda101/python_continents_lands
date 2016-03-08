import unittest

from filmpond_exercise.filmpond_exercise import FilmpondChallenge

class TestFilmpondChallenge(unittest.TestCase):
    def test_foo(self):
        fp = FilmpondChallenge()
	res = fp.foo() 
	self.assertEqual(res, 'bar')
