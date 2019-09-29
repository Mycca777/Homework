from mymatrix import MyMatrix
some_list = [[1, 2], [3, 4], [5, 6]]
def test_repr():
    m = [[12,2,3]]
    matrix = MyMatrix(m)
    assert(repr(matrix) == '12 2 3')
def test_size():
    m = [[12,3,4]]
    matrix = MyMatrix(m)
    assert(matrix.size() == (1, 3))
def test_transpose():
    matrix = MyMatrix(some_list)
    matrix1 = matrix.transpose()
    assert(matrix1.size() == (2, 3))
    assert(matrix1.get_data() == [[1, 3, 5], [2, 4, 6]])

    empty_matrix = MyMatrix([])
    empty_matrix.transpose()
    assert(empty_matrix.size() == (0, 0))
    assert(matrix.data == [])

def test_transposed():
    m1 = MyMatrix([[1, 2], [3, 4], [5, 6]])
    m2 = m1.transposed()
    assert(m1.get_data() == [[1, 2], [3, 4], [5, 6]])
    assert(m2.get_data() == [[1, 3, 5],[2, 4, 6]])

def test_flip_up_down():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m = MyMatrix(some_list)
    m.flip_up_down()
    assert(m == [[1, 2, 3],[4, 5, 6]])
    assert(m.get_data() == some_list)

    empty_matrix = MyMatrix([])
    empty_matrix.flip_up_down()
    assert(empty_matrix.size() == (0, 0))
    assert(matrix.data == [])

def test_flipped_up_down():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m1 = MyMatrix(some_list)
    m2 = m1.flipped_up_down()
    assert(m2 == [[1, 2, 3],[4, 5, 6]])
    assert(m1.get_data() == some_list)
def test_flip_left_right():
    some_list = [[4, 5, 6], [1, 2, 3]]
    m = MyMatrix(some_list)
    m = m.flip_left_right()
    assert(m == [[6, 5, 4],[3, 2, 1]])
    assert(m.get_data() == some_list)

    empty_matrix = MyMatrix([])
    empty_matrix.flip_left_right()
    assert(empty_matrix.size() == (0, 0))
    assert(matrix.data == [])

def test_flipped_left_right():
    matrix = MyMatrix(some_list)
    new_matrix = matrix.flipped_left_right()
    assert(new_matrix.size() == (3, 2))
    assert(new_matrix.data == [[2, 1], [4, 3], [6, 5]])

    assert(matrix.size() == (3, 2))
    assert(matrix.data == some_list)
def test___add__():
    m1 = MyMatrix([[2,4,7],[5,1,0]])
    m2 = MyMatrix([[1,2,3],[4,5,6]])
    m3 = m1 + m2
    assert(m1.get_data() == [[2,4,7],[5,1,0]])
    assert(m2.get_data() == [[1,2,3],[4,5,6]])
    assert(m3.get_data() == [
    	                     [3,6,10],
    	                     [9,6,6],
    	                    ])


def test___sub__():
    m1 = MyMatrix([[2,4,7],[5,1,0]])
    m2 = MyMatrix([[1,2,3],[4,5,6]])
    m3 = m1 - m2
    assert(m1.get_data() == [[2,4,7],[5,1,0]])
    assert(m2.get_data() == [[1,2,3],[4,5,6]])
    assert(m3.get_data() == [
    	                      [1,2,4],
    	                      [1,-4,-6],
    	                    ])
def test___iadd__():
    m1 = MyMatrix([[2,4,7],[5,1,0]])
    m2 = MyMatrix([[1,2,3],[4,5,6]])
    
    assert(m1.get_data() == [[2,4,7],[5,1,0]])\
    m1 += m2
    assert(m2.get_data() == [[1,2,3],[4,5,6]])
    assert(m1.get_data() == [
                             [3,6,10],
                             [9,6,6],
                            ])
def test___isub__():
    m1 = MyMatrix([[2,4,7],[5,1,0]])
    m2 = MyMatrix([[1,2,3],[4,5,6]])
    assert(m1.get_data() == [[2,4,7],[5,1,0]])
    m1 -= m2
    assert(m2.get_data() == [[1,2,3],[4,5,6]])
    assert(m1.get_data() == [
                             [1,2,4],
                             [1,-4,-6],
                            ])
