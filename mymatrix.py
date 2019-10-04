import copy

class MyMatrix:
    def __init__(self, data):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        self.__data = copy.deepcopy(data)
        
    def __repr__(self):
        str1 = []
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                str1.append(self.__data[i][j])
                str2 = str(str1)
        str2 = str2.replace(',', '')
        str2 = str2.replace(']', '')
        str2 = str2.replace('[', '')
        return str2
    
    def size(self):
        a = len(self.__data)
        if self.__data == []:
            korteh = (0, 0)
        else:
            b = len(self.__data[0])
            korteh = (a, b)
        return korteh
    
    def flip_up_down(self):
        for i in range(len(self.__data)//2):
            self.__data[i],self.__data[-i-1] = self.__data[-i-1],self.__data[i]
        return self
    
    def flip_left_right(self):
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i]) // 2):
                self.__data[i][j],self.__data[i][-j - 1] = self.__data[i][- j- 1],self.__data[i][j]
        return self

    def flipped_up_down(self):
        fup = copy.deepcopy(self.__data)
        fup = MyMatrix(fup)
        s0 = fup.flip_up_down()
        return s0
    
    def flipped_left_right(self):
        flr = copy.deepcopy(self.__data)
        flr = MyMatrix(flr)
        s1 = flr.flip_left_right()
        return s1
    
    def transpose(self):
        some_matrix = []
        k = 0
        for i in range(len(self.__data)):
             while k < len(self.__data[i]):
                matrix = []
                for j in range(len(self.__data)):
                    matrix.append(self.__data[i][k])
                some_matrix.append(matrix)
                k += 1
        return some_matrix

    def transposed(self):
        tr = copy.deepcopy(self.__data)
        tr = MyMatrix(tr)
        s2 = tr.transpose()
        return s2
    
    def get_data(self):
        self1 = copy.deepcopy(self.__data)
        return self1
    
    def __add__(self, other):
        m1 = MyMatrix(self.__data)
        m2 = MyMatrix(other.__data)
        sum0 = []
        result = []
        for i in range(len(self.__data)):
           for j in range(len(self.__data[i])):
               sum0.append(self.__data[i][j] + other.__data[i][j])
        result.append(sum0)
        return result
    def __sub__(self, other):
        m1 = MyMatrix(self.__data)
        m2 = MyMatrix(other.__data)
        sub0 = []
        result = []
        for i in range(len(self.__data)):
           for j in range(len(self.__data[i])):
               sub0.append(self.__data[i][j] - other.__data[i][j])
        result.append(sub0)
        return result

    def __iadd__(self, other):
        some_matrix = add(self.__data, other.__data)
        return some_matrix

    def __isub__(self, other):
        some_matrix = sub(self.__data, other.__data)
        return some_matrix
