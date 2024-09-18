from copy import*
from fractions import Fraction

class Polynomial:
    
    def __init__(self,d,var="x"):
        self.var=var
        self.Dict=d
        
        
    @property
    def var(self,var="x"):
        self.__var=var
    var.getter
    def var(self):
        return self.__var
    @property
    def Dict(self,d={}):
        self.__Dict=d
    Dict.getter
    def Dict(self):
        return self.__Dict
    
#Simple setter getters
    def setVar(self,var="x"):
        self.__var=var
    def getVar(self):
        return self.__var
    def setDict(self,d={}):
        self.__Dict=d
    def getDict(self):
        return self.__Dict

    
        
    def __add__(self,p2):
        z=deepcopy(p2.Dict)
        for num in self.Dict:
            if num not in z:
                z[num]=0
                z[num]=self.Dict[num]
            else:
                z[num]+=self.Dict[num]
        return Polynomial(z,self.var)
                
    def __sub__(self,p2):
        z=deepcopy(self.Dict)
        for num in p2.Dict:
            if num not in z:
                z[num]=0
                z[num]=-(p2.Dict[num])
            else:
                z[num]-=p2.Dict[num]
        return Polynomial(z)
    
    @staticmethod            
    def multiply(self,num):
        z=deepcopy(self.Dict)
        for n in z:
            z[n]*=num
        return Polynomial(z,self.var)

    def __mul__(self,p2):
        z={}
        for num in self.Dict:
            for n in p2.Dict:
                r=num+n
                if r not in z:
                    z[r]=0
                z[r]+=self.Dict[num]*p2.Dict[n]
        return Polynomial(z,self.var)
    
    def __truediv__(self,b):
        
        b=b.reciprocal()
       
        c=Polynomial(self.Dict,self.var)*Polynomial(b)
        return c.__fraction()

    def reciprocal(self):
        d={}
        z=0
        r=self.Dict
        for n in r:
            if -n not in d:
                d[-n]=0
            d[-n]+=1/r[n]
 
        return d
    
    def __fraction(self):
        x= dict(sorted(self.Dict.items(),reverse=True))
        acc=0
        s=""
        for num in x:
            if num!=0:
                if str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[1])!="1":
                    s+="{}/{}".format(str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[0]),str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[1]))
                    s+="{}^{}".format(self.var,str(num))
                else:
                    s+="{}".format(str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[0]))
                    s+="{}^{}".format(self.var,str(num)) 
            else:
                s+="{}/{}".format(str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[0]),str(Fraction(self.Dict[num]).limit_denominator().as_integer_ratio()[1]))
            if acc<(len(x)-1):
                s+=" + "
            acc+=1
        return s
    
    def __str__(self):
        x= dict(sorted(self.Dict.items(),reverse=True))
        acc=0
        s=""
        for num in x:
            
            if num!=0:
                s+="{}{}^{}".format(str(self.Dict[num]),self.var,str(num))
            else:
                s+="{}".format(str(self.Dict[num]))
            if acc<(len(x)-1):
                s+=" + "
            acc+=1
        return s
    
    @staticmethod
    def show(q):
        x=q
        return x

    
def dictfunc(l1,l2):
    d={}
    z=0
    for n in l1:
        d[n]=0
        d[n]=l2[z]
        z+=1
    return d


               
def main():
    l1=[7,5,3,0]
    l2=[4,6,4,7]
    l3=[7,6,4,3]
    l4=[4,6,4,7]
    dict1=dictfunc(l1,l2)
    dict2=dictfunc(l3,l4)
    x=Polynomial(dict1,"y")
    y=Polynomial(dict2,"y")
   
    print("Polynomial X:",x)
    print("Polynomial Y:",y)
    print("Y*2: ",Polynomial.multiply(y,2))
    print("X+Y:",x+y)
    print("X-Y:",x-y)
    print("X*Y:",x*y)
    print("X/Y:",x/y)
    z=Polynomial(dict2,"q")
    print("Polynomial Z printed through static method:",Polynomial.show(z))
    
   
  
        

main()
