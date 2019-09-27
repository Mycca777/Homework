from MyMatrix1 import MyMatrix
def test_repr():
    m = [[12,2,3]]
    matrix = MyMatrix(m)
    assert(repr(matrix) == '12 2 3')
#-------------------------------------------------------
def test_size():
	 m = [[12,3,4]]
	 matrix = MyMatrix(m)
	 assert(matrix.size() == '(1,3)')
#-------------------------------------------------------
def test_transpose():
    m = MyMatrix([[1, 2], [3, 4], [5, 6]])
    m.transpose()
    assert(m == [[1, 3, 5],[2, 4, 6]])
    assert(m.get_data() == [[1, 3, 5], [2, 4, 6]])
def test_transposed():
    m1 = MyMatrix([[1, 2], [3, 4], [5, 6]])
    m2 = m1.transpose()
    assert(m2 == [[1, 3, 5],[2, 4, 6]])
    assert(m1.get_data() == [[1, 3, 5], [2, 4, 6]])
#-------------------------------------------------------
def test_flip_up_down():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m = MyMatrix(some_list)
    m.flip_up_down()
    assert(m == [[1, 2, 3],[4, 5, 6]])
    assert(m.get_data() == some_list)
def test_flipped_up_down():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m1 = MyMatrix(some_list)
    m2 = m1.flipped_up_down()
    assert(m2 == [[1, 2, 3],[4, 5, 6]])
    assert(m1.get_data() == some_list)
#--------------------------------------------------------
def test_flip_rihgt_left():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m = MyMatrix(some_list)
    m = m.flip_right_left()
    assert(m == [[6, 5, 4],[3, 2, 1]])
    assert(m.get_data() == some_list)
def test_flipped_right_left():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m1 = MyMatrix(some_list)
    m2 = m1.flipped_right_left()
    assert(m2 == [[6, 5, 4],[3, 2, 1]])
    assert(m1.get_data() == some_list)
#--------------------------------------------------------
def test_add():
	m1 = [[2,4,7],[5,1,0]]
	m2 = [[1,2,3],[4,5,6]]
	assert(add(m1,m2) == [[3,6,10],[9,6,6]])
#--------------------------------------------------------
def test_subtract():
	m1 = [[2,4,7],[5,1,0]]
	m2 = [[1,2,3],[4,5,6]]
	assert(subtract(m1,m2) == [[1,2,4],[1,-4,-6]])