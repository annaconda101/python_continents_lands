import unittest

from filmpond_exercise.filmpond_exercise import FilmpondChallenge

class TestFilmpondChallenge(unittest.TestCase):
    def test_foo(self):
        fp = FilmpondChallenge()
        res = fp.foo() 
        self.assertEqual(res, 'bar')
    
    def test_all_land_connections(self):
        map = [
            ['+','+','+'],
            ['+','+','+'],
            ['+','+','+']
        ]
        fp = FilmpondChallenge()
        res = {}
        fp.get_connections(map, (1,1), res)
        self.assertEqual(res, { 
                                (1,1): [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)]
                              }
                        )
    
    def test_some_land_connections(self):
        map = [
            [' ','+','+'],
            [' ','+','+'],
            ['+',' ','+']
        ]
        fp = FilmpondChallenge()
        res = {}
        fp.get_connections(map, (1,1), res)
        self.assertEqual(res, { 
                                (1,1): [(0,1),(0,2),(1,2),(2,2),(2,0)]
                              }
                        )
