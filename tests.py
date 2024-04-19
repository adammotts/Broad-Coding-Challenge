from algorithm import find_path

# Tests for the pathfinding algorithm
def tests():

    adjacency_list = {
        'Red Line':
            {'Green Line D', 'Orange Line', 'Green Line B', 'Mattapan Trolley', 'Green Line E', 'Green Line C'},
        'Mattapan Trolley':
            {'Red Line'},
        'Orange Line':
            {'Green Line D', 'Blue Line', 'Green Line E', 'Red Line'},
        'Green Line B':
            {'Green Line D', 'Blue Line', 'Green Line E', 'Red Line', 'Green Line C'},
        'Green Line C':
            {'Green Line D', 'Blue Line', 'Green Line B', 'Green Line E', 'Red Line'},
        'Green Line D':
            {'Blue Line', 'Orange Line', 'Green Line B', 'Green Line E', 'Red Line', 'Green Line C'},
        'Green Line E':
            {'Green Line D', 'Blue Line', 'Orange Line', 'Green Line B', 'Red Line', 'Green Line C'},
        'Blue Line':
            {'Green Line D', 'Orange Line', 'Green Line B', 'Green Line E', 'Green Line C'}
    }
    
    # Start and end are the same
    assert "Red Line" in find_path('Red Line', 'Red Line', adjacency_list)
    assert "Green Line D" in find_path('Green Line D', 'Green Line D', adjacency_list)
    assert "Orange Line" in find_path('Orange Line', 'Orange Line', adjacency_list)
    
    # Path between adjacent routes must include start and end
    assert "Red Line" in find_path('Red Line', 'Orange Line', adjacency_list)
    assert "Orange Line" in find_path('Red Line', 'Orange Line', adjacency_list)
    assert "Red Line" in find_path('Red Line', 'Green Line D', adjacency_list)
    assert "Green Line D" in find_path('Red Line', 'Green Line D', adjacency_list)
    
    # Path between non-adjacent routes must include intermediate routes
    assert "Red Line" in find_path('Mattapan Trolley', 'Orange Line', adjacency_list)
    assert "Red Line" in find_path('Mattapan Trolley', 'Green Line D', adjacency_list)
    assert "Red Line" in find_path('Mattapan Trolley', 'Blue Line', adjacency_list)