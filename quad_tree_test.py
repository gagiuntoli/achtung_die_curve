from quad_tree import quad_tree

TOL = 1.0e-10

def test_init_quad_tree():
    tree = quad_tree(4.0, 4.0, 1.0)

    assert(abs(tree.height - 4.0) < TOL)
    assert(abs(tree.width - 4.0) < TOL)

    assert(abs(tree.leaves[0].height - 2.0) < TOL)
    assert(abs(tree.leaves[0].width - 2.0) < TOL)

    assert(abs(tree.leaves[0].leaves[0].height - 1.0) < TOL)
    assert(abs(tree.leaves[0].leaves[0].width - 1.0) < TOL)

def test_insert_point():
    tree = quad_tree(2.0, 2.0, 1.0)

    tree.insert_point([0.2, 0.1]) # -> 0
    tree.insert_point([1.2, 0.1]) # -> 2
    tree.insert_point([1.2, 1.1]) # -> 3
    tree.insert_point([0.2, 1.1]) # -> 1
    tree.insert_point([0.2, 1.2]) # -> 1

    assert(tree.insert_point([0.2, 2.2]) == None)
    assert(tree.insert_point([-0.2, 2.2]) == None)

    assert(tree.points == [])
    assert(tree.leaves[0].points == [[0.2, 0.1]])
    assert(tree.leaves[1].points == [[0.2, 1.1], [0.2, 1.2]])
    assert(tree.leaves[2].points == [[1.2, 0.1]])
    assert(tree.leaves[3].points == [[1.2, 1.1]])

def test_insert_point():
    tree = quad_tree(2.0, 2.0, 1.0)

    tree.insert_point([0.2, 0.1]) # -> 0
    tree.insert_point([1.2, 0.1]) # -> 2
    tree.insert_point([1.2, 1.1]) # -> 3
    tree.insert_point([0.2, 1.1]) # -> 1
    tree.insert_point([0.2, 1.2]) # -> 1

    assert(tree.check_collision([0.2, 1.2], 1.0e-10) == True)
    assert(tree.check_collision([0.2, 1.21], 1.0e-10) == False)
    assert(tree.check_collision([1.2, 0.1], 1.0e-10) == True)
    assert(tree.check_collision([1.2, 1.1], 1.0e-10) == True)
    assert(tree.check_collision([0.2, 1.1], 1.0e-10) == True)
    assert(tree.check_collision([0.2, 1.2], 1.0e-10) == True)
    assert(tree.check_collision([0.21, 1.21], 1.0e-2) == True)
    assert(tree.check_collision([0.21, 1.21], 1.0e-4) == False)
