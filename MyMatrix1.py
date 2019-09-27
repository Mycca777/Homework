import copy
class MyMatrix:
#-------------------------------------------------------------------------------------------
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
 #-------------------------------------------------------------------------------------------       
    def __repr__(self):
        str1 = []
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                str1.append(self.__data[i][j])
                str2 = str(str1)
        str2 = str2.replace(',', ' ')
        str2 = str2.replace(']', '')
        str2 = str2.replace('[', '')
        return str2
#---------------------------------------------------------------------------------------------
#+#
    def size(self):
        a = str(len(self.__data))
        b = str(len(self.__data[0]))
        return "(" + a +"," + b +")"
#---------------------------------------------------------------------------------------------
    def flip_up_down(self):
        for i in range(len(self.__data)//2):
            self.__data[i],self.__data[-i-1] = self.__data[-i-1],self.__data[i]
        return self.__data
#---------------------------------------------------------------------------------------------
    
    def flip_left_right(self):
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i]) // 2):
                self.__data[i][j],self.__data[i][-j - 1] = self.__data[i][- j- 1],self.__data[i][j]
        return self.__data

 #---------------------------------------------------------------------------------------------   
#+#    
    def flipped_up_down(self):
        fup = copy.deepcopy(self.__data)
        fup = MyMatrix(fup)
        s0 = fup.flip_up_down()
        return s0
#----------------------------------------------------------------------------------------------
 #+#
    def flipped_left_right(self):
        flr = copy.deepcopy(self.__data)
        flr = MyMatrix(flr)
        s1 = flr.flip_left_right()
        return s1
#-----------------------------------------------------------------------------------------------
    def transpose(self):
        fi = []
        fj = []
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                fj.append(j)
            fi.append(j)
        f1 = max(fj)
        f2 = max(fi)
        sub = f1 - f2
        if f1 > f2:
            f2 = f2 + sub
            self.__data[f2][f1],self.__data[f1][f2] = self.__data[f1][f2],self.__data[f2][f1]
        else:
            f1 = f1 + sub
            self.__data[f2][f1],self.__data[f1][f2] = self.__data[f1][f2],self.__data[f2][f1]
#-----------------------------------------------------------------------------------------------
 #+#
    def transposed(self):
        tr = copy.deepcopy(self.__data)
        tr = MyMatrix(tr)
        s2 = tr.transpose()
        return s2
#-----------------------------------------------------------------------------------------------
    def get_data(self):
        return self.__data
#-------------------------------------------------------------------------------
    def add(self, other):
        """Return self + other"""
        sum = []
        result = []
        for i in range(len(self.__data)):
          for j in range(len(self.__data[i])):
              sum.append(self.__data[i][j] + other.__data[i][j])
        result.append(sum)
        return result
#-------------------------------------------------------------------------------
    def subtract(self, other):
        """Return self - other."""
        sub = []
        result2 = []
        for i in range(len(self.__data)):
          for j in range(len(self.__data[i])):
              sub.append(self.__data[i][j] - other.__data[i][j])
        result2.append(sub)
        return result2