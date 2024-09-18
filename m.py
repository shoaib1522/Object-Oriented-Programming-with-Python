class Mat2by2:
    def _init(self,a11=0,a21=0,a12=0,a22=0):#defining the class#default values are set to zero if no values are provided.# constructor : __init_ takes four parameters (a11, a21, a12, a22).
        self.__a11=a11
        self.__a12=a12
        self.__a21=a21
        self.__a22=a22
    def _str_(self):#printing matrix form
        mstr="|"
        mstr+=str(self.__a11)
        mstr+=","
        mstr+=str(self.__a12)
        mstr+=","
        mstr+=str(self.__a21)
        mstr+=","
        mstr+=str(self.__a22)
        mstr+="|"
        return mstr
    def add(self,mat2):
        added=Mat2by2()
        added._a11=self.a11+mat2._a11
        added._a12=self.a12+mat2._a12
        added._a21=self.a21+mat2._a21
        added._a22=self.a22+mat2._a22
        return added
    def subs(self,mat2):
        sub=Mat2by2()
        sub._a11=self.a11-mat2._a11
        sub._a12=self.a12-mat2._a12
        sub._a21=self.a21-mat2._a21
        sub._a22=self.a22-mat2._a22
        return sub        
    def scalar_multiple(self,k):
        scalar=Mat2by2()
        scalar._a11=k*self._a11
        scalar._a12=k*self._a12
        scalar._a21=k*self._a21
        scalar._a22=k*self._a22
        return scalar        
    def multiplied(self,mat2):
        multiply=Mat2by2()
        multiply._a11=((self.a11*mat2.a11)+(self.a12*mat2._a21))
        multiply._a12=((self.a11*mat2.a12)+(self.a12*mat2._a22))
        multiply._a21=((self.a21*mat2.a11)+(self.a22*mat2._a21))
        multiply._a22=((self.a21*mat2.a12)+(self.a22*mat2._a22))
        return multiply        
    def cofactor(self):
        cofac=Mat2by2()
        cofac._a11=self._a22
        cofac._a12=-self._a21
        cofac._a21=-self._a12
        cofac._a22=self._a11
        return cofac
    def determinant(self):
        determinant=(self._a11*self.a22)-(self.a12*self._a21)
        return determinant
    def adj(self):
        adj=Mat2by2()
        adj._a11=self._a22
        adj._a12=-self._a12
        adj._a21=-self._a21
        adj._a22=self._a11
        return adj        
    def inv(self):
        inv=Mat2by2()
        determinant=self.determinant()
        adj=Mat2by2()
        adj._a11=self._a22
        adj._a12=-self._a12
        adj._a21=-self._a21
        adj._a22=self._a11
        inv._a11=adj._a11/determinant
        inv._a12=adj._a12/determinant
        inv._a21=adj._a21/determinant
        inv._a22=adj._a22/determinant
        return inv        
    def div(self,mat2):
        inv=Mat2by2()
        determinant=self.determinant()
        adj=Mat2by2()
        adj._a11=mat2._a22
        adj._a12=-mat2._a12
        adj._a21=-mat2._a21
        adj._a22=mat2._a11
        inv._a11=adj._a11/determinant
        inv._a12=adj._a12/determinant
        inv._a21=adj._a21/determinant
        inv._a22=adj._a22/determinant
        return inv
        div=Mat2by2()
        div._a11=((self.a11*inv.a11)+(self.a12*inv._a21))
        div._a12=((self.a11*inv.a12)+(self.a12*inv._a22))
        div._a21=((self.a21*inv.a11)+(self.a22*inv._a21))
        div._a22=((self.a21*inv.a12)+(self.a22*inv._a22))
        return div        
    def transpose(self):
        trans=Mat2by2()
        trans._a11=self._a11
        trans._a12=self._a21
        trans._a21=self._a12
        trans._a22=self._a22
        return trans
    def null(self):
        if self._a11==0 and self.a12==0 and self.a21==0 and self._a22==0:
            return True
        return False
    def identity(self):
        if self._a11==1 and self.a12==0 and self.a21==0 and self._a22==1:
            return True
        return False
def main():
    print('--------Please enter co-ordinates of Matrices First---------')
    a=int(input('1st entry of Matrix1:'))#displaying Matrix1
    c=int(input('2nd entry of Matrix1:'))
    b=int(input('3rd entry of Matrix1:'))
    d=int(input('4th entry of Matrix1:'))
    m1=Mat2by2(a,b,c,d)
    print(f'Matrix1:{m1}')
    x=int(input('1st entry of Matrix2:'))#displaying Matrix2
    z=int(input('2nd entry of Matrix2:'))
    y=int(input('3rd entry of Matrix2:'))
    w=int(input('4th entry of Matrix2:'))
    m2=Mat2by2(x,y,z,w)
    print(f'Matrix2:{m2}')
    added_matrix=m1.add(m2)#Add Two Matrices
    print(f'Addition:',end='')
    print(added_matrix)
    subs_matrix=m1.subs(m2)#Substract Two Matrices
    print(f'Substraction:',end='')
    print(subs_matrix)
    print('------Please enter a Scalar number First-------')#Scalar Multiple of Matrix
    k=int(input('Enter scalar of Matrix1:'))
    scalar_multiple=m1.scalar_multiple(k)
    print(f'Scalar Multipication:',end='')
    print(scalar_multiple)
    multiplied_matrix=m1.multiplied(m2)#Multiply Two Matrices
    print(f'Multiplied matrix:',end='')
    print(multiplied_matrix)    
    cofactor_of_matrix=m1.cofactor()#Cofactor of Matrix
    print(f'Co-factor of Matrix1:',cofactor_of_matrix)    
    det1=m1.determinant()#Determinant of Matrix
    print(f'Determinant of Matrix1:{det1}')    
    singular_matrix=m1.determinant()#Singular Matrix
    if singular_matrix==0:
        print('Matrix is Singular')
    else:
        print('Matrix is NOT Singular')        
    adj_matrix=m1.adj()#Adjoint of Matrix
    print(f'Adjoint of Matrix1:{adj_matrix}')    
    inverse_matrix=m1.inv()#Inverse of a Matrix
    print(f'Inverse of Matrix1={inverse_matrix}')
    transpose=m1.transpose()#Transpose of a Matrix
    print(f'Transpose of Matrix1:{transpose}')
    null=m1.null()#Null Matrix
    if m2.null() is True:
        print('Matrix2 is null')
    else:
        print('Matrix1 is not null')
    iden=m1.identity()#Identity Matrix
    if m1.identity() is True:
        print('Matrix1 is Identity Matrix')
    else:
        print('Matrix1 is not Identity Matrix')
    divided=m1.div(m2)#Division of a Matrix by another Matrix
    print(f'Divided Matrix:{divided}')
main()
