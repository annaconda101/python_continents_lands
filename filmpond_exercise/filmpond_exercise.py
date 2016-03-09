class FilmpondChallenge:
    def foo(self):
        return 'bar'
    
    def get_all_connections(self, map, res): 
        for i,row in enumerate(map):
            for x,pos in enumerate(row):
	        self.get_connections(map, (i,x), res)
    
    def get_connections(self, map, position, res):
        row = position[0]
	column = position[1]

	connections = []
	num_columns = len(map[0])
	num_rows = len(map)

	if (row -1 >= 0) and (column -1 >= 0):
	    connections.append((row - 1, column - 1))

        if (row -1 >= 0):
	    connections.append((row - 1, column))

	if (row -1 >= 0) and (column + 1 < num_columns):
	    connections.append((row - 1, column + 1))

	if (column + 1 < num_columns):
	    connections.append((row, column + 1))

	if (row + 1 < num_rows) and (column + 1 < num_columns):
	    connections.append((row + 1, column + 1))

	if (row + 1 < num_rows):
	    connections.append((row + 1, column))
	 
	if (row + 1 < num_rows) and (column - 1 >= 0):
	    connections.append((row + 1, column - 1))
	
	if (column - 1 >= 0):
	    connections.append((row, column - 1))

	res[position] = [pos for pos in connections if map[pos[0]][pos[1]] == '+']

	# print res[position]

	# res[position] = connections

