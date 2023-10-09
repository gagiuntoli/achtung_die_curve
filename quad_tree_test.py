from quad_tree import quad_tree

TOL = 1.0e-10

def test_init_quad_tree():
    tree = quad_tree([0.0, 4.0, 0.0, 4.0], 1.0)

    assert tree.get_height() == 3
    assert tree.leaves[0].rectangle == [0.0, 2.0, 0.0, 2.0]
    assert tree.leaves[0].leaves[0].rectangle == [0.0, 1.0, 0.0, 1.0]

def test_insert_point():
    radius = 1.0e-3
    tree = quad_tree([0.0, 2.0, 0.0, 2.0], 1.0, radius)

    tree.insert_point([0.2, 0.1]) # -> leaf 0
    tree.insert_point([1.2, 0.1]) # -> leaf 2
    tree.insert_point([1.2, 1.1]) # -> leaf 3
    tree.insert_point([0.2, 1.1]) # -> leaf 1
    tree.insert_point([0.2, 1.2]) # -> leaf 1

    assert tree.insert_point([0.2, 2.2]) == None
    assert tree.insert_point([-0.2, 2.2]) == None

    assert tree.leaves[0].points == [[0.2, 0.1]]
    assert tree.leaves[1].points == [[0.2, 1.1], [0.2, 1.2]]
    assert tree.leaves[2].points == [[1.2, 0.1]]
    assert tree.leaves[3].points == [[1.2, 1.1]]

def test_check_collision():
    radius = 1.0e-3
    tree = quad_tree([0.0, 2.0, 0.0, 2.0], 1.0, radius)

    tree.insert_point([0.2, 0.1]) # -> leaf 0
    tree.insert_point([1.2, 0.1]) # -> leaf 2
    tree.insert_point([1.2, 1.1]) # -> leaf 3
    tree.insert_point([0.2, 1.1]) # -> leaf 1
    tree.insert_point([0.2, 1.2]) # -> leaf 1

    assert tree.check_collision([0.2, 1.2], radius) == True
    assert tree.check_collision([1.2, 0.1], radius) == True
    assert tree.check_collision([1.2, 1.1], radius) == True
    assert tree.check_collision([0.2, 1.1], radius) == True
    assert tree.check_collision([0.2, 1.2], radius) == True

    assert tree.check_collision([0.3, 1.2], radius) == False
    assert tree.check_collision([1.3, 0.1], radius) == False
    assert tree.check_collision([1.3, 1.1], radius) == False
    assert tree.check_collision([0.2, 1.3], radius) == False
    assert tree.check_collision([0.2, 1.3], radius) == False

def test_check_collision_when_point_is_in_border():
    radius = 1.0e-3
    tree = quad_tree([0.0, 2.0, 0.0, 2.0], 1.0, radius)

    tree.insert_point([1.00001, 0.99999]) # -> 2

#    assert(tree.leaves[2].points == [[1.00001, 0.99999]]) # leaf 2
#
#    assert(tree.check_collision([0.99999, 0.99999], 1.0e-1) == True) # leaf 0
#    assert(tree.check_collision([0.99999, 1.00001], 1.0e-1) == True) # leaf 1
#    assert(tree.check_collision([1.00006, 0.99999], 1.0e-1) == True) # leaf 2
#    assert(tree.check_collision([1.00006, 1.00001], 1.0e-1) == True) # leaf 3