# initializing the all entities of matrix with 0 in __init__ function
class matrix:
    def __init__(self,x11=0,x12=0,x21=0,x22=0):
        self.__x11=x11
        self.__x12=x12
        self.__x21=x21
        self.__x22=x22
    # the matrix is written as we use in matlab
    def __str__(self):
        string = "["
        string += str(self.__x11)
        string += ","
        string += str(self.__x12)
        string += " ; "
        string += str(self.__x21)
        string += ","
        string += str(self.__x22)
        string += "]"
        return string
    # passing the parameters 0 in all the calling classes within the function of a class like the private member
    def addition(m1,m2):
        add=matrix(x11=0,x12=0,x21=0,x22=0)
        add.__x11=m1.__x11+m2.__x11
        add.__x12=m1.__x12+m2.__x12
        add.__x21=m1.__x21+m2.__x21
        add.__x22=m1.__x22+m2.__x22
        return add
    staticmethod(addition) #making an static function
    def subtraction(m1,m2):
        sub=matrix(x11=0,x12=0,x21=0,x22=0)
        sub.__x11=m1.__x11-m2.__x11
        sub.__x12=m1.__x12-m2.__x12
        sub.__x21=m1.__x21-m2.__x21
        sub.__x22=m1.__x22-m2.__x22
        return sub
    staticmethod(subtraction)
    def scalar_multiple(n,m):
        multi=matrix(x11=0,x12=0,x21=0,x22=0)
        multi.__x11=m.__x11*n
        multi.__x12=m.__x12*n
        multi.__x21=m.__x21*n
        multi.__x22=m.__x22*n 
        return multi
    staticmethod(scalar_multiple)
    def multiply(m1,m2):
        multiplication=matrix(x11=0,x12=0,x21=0,x22=0)
        multiplication.__x11=m1.__x11*m2.__x11+m1.__x12*m2.__x21
        multiplication.__x21=m1.__x21*m2.__x11+m1.__x22*m2.__x21
        multiplication.__x12=m1.__x11*m2.__x12+m1.__x12*m2.__x22
        multiplication.__x22=m1.__x21*m2.__x12+m1.__x22*m2.__x22
        return multiplication
    staticmethod(multiply)
    def cofactor_matrix(i,j,m2):
        cofactor=m2.__x22
        if i==1 and j==2:
            cofactor=(-1)*m2.__x21
        if i==2 and j==1:
            cofactor=(-1)*m2.__x12
        if i==2 and j==2:
            cofactor=m2.__x11
        return cofactor
    def determinant(m):
        det=m.__x11*m.__x22-m.__x12*m.__x21
        return det 
    def inverse(m):
        det=m.__x11*m.__x22-m.__x12*m.__x21
        inverse=matrix()
        inverse.__x11=round(m.__x22/det,2)
        inverse.__x12=round(-1*(m.__x12)/det,2)
        inverse.__x21=round(-1*(m.__x21)/det,2)
        inverse.__x22=round(m.__x11/det,2)
        return inverse
    staticmethod(inverse)
    def null(m):
        null='Not a Null matrix'
        if m.__x11==0 and m.__x12==0 and m.__x21==0 and m.__x22==0:
            null='YES it is a null matrix'
        return null
    def division(m1,m2):
        division=matrix(x11=0,x12=0,x21=0,x22=0)
        division.__x11=round(m1.__x11/m2.__x11,2)
        division.__x12=round(m1.__x12/m2.__x12,2)
        division.__x21=round(m1.__x21/m2.__x21,2)
        division.__x22=round(m1.__x22/m2.__x22,2)
        return division
    staticmethod(division)
    def identity(m1):
        identity="No it is not an Identity matrix"
        if m1.__x11==1 and m1.__x12==1 and m1.__x21==0 and m1.__x22==1:
            identity="Yes it is an Identity matrix"
        return identity
    def transpose(m1):
        transpose=matrix(x11=0,x12=0,x21=0,x22=0)
        transpose.__x11=m1.__x11
        transpose.__x12=m1.__x21
        transpose.__x21=m1.__x12
        transpose.__x22=m1.__x22
        return transpose
    staticmethod(transpose)
def main():
    m1=matrix(1,5-8,3)
    m2=matrix(4,12,-11,1)
    print(f'm1 = {m1}')
    print(f'm2 = {m2}')
    # addition
    add=matrix.addition(m1,m2)
    print(f'm1 + m2 = {add}')
    # subtraction
    sub=matrix.subtraction(m1,m2)
    print(f'm1 - m2 = {sub}')
    # scalar multiple
    num=int(input('Enter the number for scalar multiple: '))
    scalar_multiple=matrix.scalar_multiple(num,m1)
    print(f'n x m1 = {scalar_multiple}')
    # multiplication
    multiplication=matrix.multiply(m1,m2)
    print(f'm1 x m2 = {multiplication}')
    i=int(input('Enter the value for the cofactor i: '))
    j=int(input('Enter the value for the cofactor j: '))
    # cofactor of a matrix
    cofactor=matrix.cofactor_matrix(i,j,m2)
    print(f'Cofactor of m{i}{j} is : {cofactor}')
    #determinant
    determinant=matrix.determinant(m1)
    print(f'|m1| = {determinant}')
    #singular
    if determinant==0:
        singular_matrix='Yes it is a singular matrix'
    else:
        singular_matrix='No it is not a singular matrix'
    print(f'|m1| = {singular_matrix}')
    determinant=matrix.determinant(m2)
    print(f'|m2| = {determinant}')
    if determinant==0:
        singular_matrix='Yes it is a singular matrix'
    else:
        singular_matrix='No it is not a singular matrix'
    print(f'|m2| = {singular_matrix}')
    #null
    null_matrix=matrix.null(m1)
    print(f'|m1| shows {null_matrix}')
    null_matrix=matrix.null(m2)
    print(f'|m2| shows {null_matrix}')
    #identity
    identity= matrix.identity(m1)
    print(f'm1 = {identity}')
    identity= matrix.identity(m2)
    print(f'm2 = {identity}')
    #inverse
    inverse=matrix.inverse(m1)
    print(f'm1^-1 = {inverse}')
    inverse=matrix.inverse(m2)
    print(f'm2^-1 = {inverse}')
    # division
    division=matrix.division(m1,m2)
    print(f'm1 / m2 = {division}')
    # transpose
    transpose=matrix.transpose(m1)
    print(f'Transpose of m1 = {transpose}')
    transpose=matrix.transpose(m2)
    print(f'Transpose of m2 = {transpose}')
main()