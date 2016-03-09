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
    
    def test_edge_land_connections(self):
        map = [
            [' ','+','+'],
            [' ','+','+'],
            ['+',' ','+']
        ]
        fp = FilmpondChallenge()
        res = {}
        fp.get_connections(map, (0,2), res)
        self.assertEqual(res, { 
                                (0,2): [(1,2),(1,1),(0,1)]
                              }
                        )
    
    def test_all_land_connections_without_gaps(self):
        map = [
            ['+','+','+'],
            ['+','+','+'],
            ['+','+','+']
        ]
        fp = FilmpondChallenge()
        res = {}
        fp.get_all_connections(map, res)
        self.assertEqual(res, { 
                                (0,0): [(0,1),(1,1),(1,0)],
                                (0,1): [(0,2),(1,2),(1,1),(1,0),(0,0)],
                                (0,2): [(1,2),(1,1),(0,1)],
                                (1,0): [(0,0),(0,1),(1,1),(2,1),(2,0)],
                                (1,1): [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)],
                                (1,2): [(0,1),(0,2),(2,2),(2,1),(1,1)],
                                (2,0): [(1,0),(1,1),(2,1)],
                                (2,1): [(1,0),(1,1),(1,2),(2,2),(2,0)],
                                (2,2): [(1,1),(1,2),(2,1)]
                              }
                        )

    def test_all_land_connections_with_gaps(self):
        map = [
            [' ','+','+'],
            [' ','+','+'],
            ['+',' ','+']
        ]
        fp = FilmpondChallenge()
        res = {}
        fp.get_all_connections(map, res)
        self.assertEqual(res, { 
                                (0,1): [(0,2),(1,2),(1,1)],
                                (0,2): [(1,2),(1,1),(0,1)],
                                (1,1): [(0,1),(0,2),(1,2),(2,2),(2,0)],
                                (1,2): [(0,1),(0,2),(2,2),(1,1)],
                                (2,0): [(1,1)],
                                (2,2): [(1,1),(1,2)]
                              }
                        )

    def test_single_continent(self): 
        map = [
            ['+','+','+'],
            ['+','+','+'],
            ['+','+','+']
        ]
        fp = FilmpondChallenge()
        connections = {}
        fp.get_all_connections(map, connections)
        positions = []
        fp.get_continent(connections, (0,0), positions)
        self.assertEqual(positions, [ (0,0), (0,1), (0,2), (1,2), (2,2), (1,1), (2,1), (1,0), (2,0) ])

    def test_multiple_continents(self):
        map = [
            ['+','+',' ','+'],
            ['+',' ',' ','+'],
            ['+','+',' ',' '],
            [' ',' ',' ',' '],
            ['+','+','+',' '],
            ['+','+','+',' ']
        ]
        fp = FilmpondChallenge()
        connections = {}
        fp.get_all_connections(map, connections)
        continents = []
        fp.get_continents(connections, continents)
        self.assertEqual(continents, [[(0, 1), (1, 0), (0, 0), (2, 1), (2, 0)], [(5, 2), (4, 1), (4, 2), (5, 1), (4, 0), (5, 0)], [(1, 3), (0, 3)]])
