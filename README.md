In order to see the output for each of the three questions, simply run the main.py file


Overview:

* route.py - Contains a function for retrieving data from an MBTA endpoint and route using an HTTP request
* operations/routes.py - Contains all relevant functions needed to retrieve data regarding routes using route.py
* operations/stops.py - Contains all relevant functions needed to retrieve data regarding stops using route.py
* views/routes.py - Contains all relevant functions needed for simplifying/deconstructing data regarding routes retrieved from operations
* views/stops.py - Contains all relevant functions needed for simplifying/deconstructing data regarding stops retrieved from operations
* algorithm.py - Contains an algorithm that finds a path between two nodes on a graph given a starting point, ending point, and an adjacency list representation of the graph
* tests.py - Contains tests that are relevant for ensuring the validity of the path finding algorithm in algorithm.py
* main.py - Contains all the relevant code for solving each of the questions based on the above defined general purpose functions
