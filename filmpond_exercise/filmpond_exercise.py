class FilmpondChallenge:
    def foo(self):
        return 'bar'
    
    def get_connections(self, map, position, res):
        row = position[0]
	column = position[1]

	connections = [ 
	    (row - 1, column - 1),
	    (row - 1, column),
	    (row - 1, column + 1),
	    (row, column + 1),
	    (row + 1, column + 1),
	    (row + 1, column),
	    (row + 1, column - 1),
	    (row, column - 1)
	 ]

	res[position] = [pos for pos in connections if map[pos[0]][pos[1]] == '+']
