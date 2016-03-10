#### MapParser (A Simple Counter for Continents and Lands)

#### DESCRIPTION:

This is a coding exercise built in python that analyses the coordinates in a sample map to determine the continents and lands.

#### DEPENDENCIES:

Python 2/3

#### OVERVIEW:

This script serves as a commandline tool that takes in the file path of the .txt sample map, and outputs the following:

a.  Number of continents in a map
b.  Number of lands in each continent

In the context of this exercise, the definition of a continent is any one or more '+'s connected horizontally, vertically or diagonally.

IMPORTANT: Please note that this exercise has been specifically designed for sample maps in the same format as the map.txt and the map_small_sample.txt files saved under test/fixtures directory.


#### USAGE INSTRUCTIONS:

1. `git clone https://github.com/annaconda101/python_continents_lands.git`
2. `cd python_content_lands`
3. `python continent_land_counter.py test/fixtures/map.txt`

Output:

```
There are 3 continents in this map.
Continent 1 has 809 +.
Continent 2 has 368 +.
Continent 3 has 589 +.
```

#### TESTING INSTRUCTIONS:

This project has 11 test examples compatible with unittest. To run:

1. `python -m unittest test.test_filmpond_exercise`

#### DESIGN:

Inspired by: [Graphs in Python](http://www.python-course.eu/graphs_python.php).

1. Create a multidimensional list from textual input (rows x columns)
2. Build up land positions (nodes) and connections (edges) based on specified rules (represented as a dictionary)
3. Traverse continents using recursion, keeping track of visited land positions
