def str2arr(string):
    m = list(string.split(", "))
    return m

def str2int(str1):
    list1 = str1
    list2 = list1[:-1]
    list3 = int(list2)
    return list3
    
def Mat_Data(mat1):
    mat2 = Matrix_Convert(mat1)
    mat3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range (3):
        for j in range (3):
            m1 = str2int(mat2[i][j])
            mat3[i][j] = m1
        
    return mat3


def Matrix_Convert(matrix1):
    matrix = str2arr(matrix1)
    
    if(matrix[0] == 'matr'):
        return ([[matrix[1], matrix[2], matrix[3]], [matrix[4], matrix[5], matrix[6]], [matrix[7], matrix[8], matrix[9]]])
     
    if(matrix[0] == 'sym'):
        return ([[matrix[1], matrix[2], matrix[3]], [matrix[2], matrix[4], matrix[5]], [matrix[3], matrix[5], matrix[6]]])
     
    if(matrix[0] == 'skew'):     
        return ([[0, -1*matrix[3], matrix[2]], [matrix[3], 0, -1*matrix[1]], [-1*matrix[2], matrix[1], 0]])
     
    if(matrix[0] == 'diag'):
        return ([[matrix[1], "0.", "0."], ["0.", matrix[2], "0."], ["0.", "0.", matrix[3]]])
    
    if(matrix[0] == 'eye'):
        return ([["1.", "0.", "0."], ["0.", "1.", "0."], ["0.", "0.", "1."]])

    if(matrix[0] == 'null'):
        return ([["0.", "0.", "0."], ["0.", "0.", "0."], ["0.", "0.", "0."]])


class Matrix_Multiply:
    def __init__(self, matrix1, matrix2):
        self.mat1 = Mat_Data(matrix1)
        self.mat2 = Mat_Data(matrix2) 
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.result[i][j] = self.result[i][j] + (self.mat1[i][k] * self.mat2[k][j])
        
    def __str__(self):
        s ='\nmatr, '+ str(self.result[0][0]) + '., ' + str(self.result[0][1]) + '., ' + str(self.result[0][2]) + '.,'
        s = s + str(self.result[1][0]) + '., ' + str(self.result[1][1]) + '., ' + str(self.result[1][2]) + '., '
        s = s + str(self.result[2][0]) + '., ' + str(self.result[2][1]) + '., ' + str(self.result[2][2]) + '.;'
        return s
        
        
class Matrix_Addition:
    def __init__(self, mat1, mat2):
        self.m1 = Mat_Data(mat1)
        self.m2 = Mat_Data(mat2)
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.result[i][j] = (self.m1[i][j] + self.m2[i][j])
        
    def __str__(self):
        s ='\nmatr, '+ str(self.result[0][0]) + '., ' + str(self.result[0][1]) + '., ' + str(self.result[0][2]) + '.,'
        s = s + str(self.result[1][0]) + '., ' + str(self.result[1][1]) + '., ' + str(self.result[1][2]) + '., '
        s = s + str(self.result[2][0]) + '., ' + str(self.result[2][1]) + '., ' + str(self.result[2][2]) + '.;'
        return s


        
class Matrix_Substraction:
    def __init__(self, mat1, mat2):
        self.m1 = Mat_Data(mat1)
        self.m2 = Mat_Data(mat2)
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.result[i][j] = (self.m1[i][j] - self.m2[i][j])
        
    def __str__(self):
        s ='\nmatr, '+ str(self.result[0][0]) + '., ' + str(self.result[0][1]) + '., ' + str(self.result[0][2]) + '.,'
        s = s + str(self.result[1][0]) + '., ' + str(self.result[1][1]) + '., ' + str(self.result[1][2]) + '., '
        s = s + str(self.result[2][0]) + '., ' + str(self.result[2][1]) + '., ' + str(self.result[2][2]) + '.;'
        return s

      
class pluginVAR:
    def __init__(self, idx1, idx2, mass, string1, string2):
        self.idx1 = idx1
        self.idx2 = idx2
        self.mass = mass
        self.string1 = string1
        self.string2 = string2
    def __str__(self):
        s = '\nset:  [node, ' + self.idx1 + ', '+ self.mass + ', structural, string="' + str(self.string1) + '"];\n' 
        s = s +  '\nset:  [node, ' + self.idx2 + ', '+ self.mass + ', structural, string="' + str(self.string2) + '"];\n' 
        return s


class Reference:
    def __init__(self, idx, ori, vel, refvel, position):
        self.idx = idx
        self.ori = ori
        self.vel = vel
        self.refvel = refvel
        self.position = position
    def __str__(self):
        s = '\nreference:\t' + str(self.idx) + ',\n'
        s = s +'\t'+ str(self.position) + ',\n'
        s = s +'\t'+ str(self.ori)+ ',\n'
        s = s +'\t'+ str(self.vel)+ ',\n'
        s = s +'\t'+ str(self.refvel)+ ';\n'
        return s


class JointRH:
    def __init__(self, idx, node1, node2, ref, orientation, positions = Position('', 'node')):
        self.idx = idx
        self.node1 = node1
        self.node2 = node2
        self.ref = ref
        self.positions = positions
        self.orientation = orientation
    def __str__(self):
        s = '\njoint:\t' + str(self.idx) + ',\n\trevolute hinge,\n'
        s = s +'\t'+ str(self.node1) + ',\n'
        s = s + '\t\treference, ' + str(self.ref)+', '+ str(self.positions) +',\n'
        s = s + '\t\thinge, reference, '+str(self.ref) +', ' + str(self.orientation) +',\n'
        s = s +'\t'+ str(self.node2) + ',\n'
        s = s + '\t\treference, ' + str(self.ref)+', '+ str(self.positions)  +',\n'
        s = s + '\t\thinge, reference, '+str(self.ref) +', ' + str(self.orientation) +';\n'
        return s

