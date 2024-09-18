class Polynomial:
    __coefficients=[]
    def __new__(cls,coefficients=[]):
        obj=super().__new__(cls)
        return obj
    def __init__(self,coefficients=[]):
        self.__coefficients=coefficients
    @property
    def coefficients(self,get_index):
        return self.__coefficients[get_index]
    @coefficients.setter
    def coefficients(self,set_index):
        return self.__coefficients[set_index]
    def __str__(self):
        string=''
        for i in range (len(self.__coefficients)):
            if self.__coefficients[i]!=0:
                if self.__coefficients[i]>=0:
                    string+='+{}x^{}'.format(self.__coefficients[i],len(self.__coefficients)-i-1)
                else:
                    string+='{}x^{}'.format(self.__coefficients[i],len(self.__coefficients)-i-1)
        return string
    def degree(self):
        # It Returns the degree of the polynomial
        return (len(self.__coefficients)-1)
    def __del__(self):
        print(f'{self.__coefficients} deleted after Execution to keep optimization in our code')
        return
    def evaluate(self,value):
        result=0
        for i in range(len(self.__coefficients)):
            result+=self.__coefficients[i]*(value**((len(self.__coefficients)-i-1)))
        return result
    def __add__(self,other):
        if len(self.__coefficients)>len(other.__coefficients):
            added_list=[]
            for j in range(len(self.__coefficients)-len(other.__coefficients)):
                added_list.append(self.__coefficients[j])
            i=len(self.__coefficients)-len(other.__coefficients)
            while i<=len(other.__coefficients):
                added_list.append(self.__coefficients[i]+other.__coefficients[i-1])
                i+=1
        elif len(self.__coefficients)<len(other.__coefficients):
            added_list=[]
            for j in range(len(other.__coefficients)-len(self.__coefficients)):
                added_list.append(other.__coefficients[j])
            i=len(other.__coefficients)-len(self.__coefficients)
            while i<=len(self.__coefficients):
                added_list.append(self.__coefficients[i-1]+other.__coefficients[i])
                i+=1
        elif len(self.__coefficients)==len(other.__coefficients):
            for i in range(len(other.__coefficients)):
                added_list.append(self.__coefficients[i]+other.__coefficients[i])
        return Polynomial(added_list)
    def __sub__(self,other):
        sub_list=[]
        if len(self.__coefficients)>len(other.__coefficients):
            for append in range(len(self.__coefficients)-len(other.__coefficients)):
                sub_list.append(self.__coefficients[append])
            i=len(self.__coefficients)-len(other.__coefficients)
            while i<=len(other.__coefficients):
                sub_list.append(self.__coefficients[i]-other.__coefficients[i-1])
                i+=1
        elif len(self.__coefficients)<len(other.__coefficients):
            for append in range(len(other.__coefficients)-len(self.__coefficients)):
                sub_list.append(other.__coefficients[append])
            i=len(other.__coefficients)-len(self.__coefficients)
            while i<=len(self.__coefficients):
                sub_list.append(self.__coefficients[i-1]-other.__coefficients[i])
                i+=1
        elif len(self.__coefficients)==len(other.__coefficients):
            for i in range(len(other.__coefficients)):
                sub_list.append(self.__coefficients[i]-other.__coefficients[i])
        return Polynomial(sub_list)
    # def __mul__(self,other):
    #     multiply_list=[0]*(len(self.__coefficients)*len(other.__coefficients))
    #     for i in range(len(self.__coefficients)):
    #         for j in range(len(other.__coefficients)):
    #             index=(len(self.__coefficients)-1-i)+(len(other.__coefficients)-1-j)
    #             multiply_list.insert(index,(multiply_list[index]+self.__coefficients[i]*other.__coefficients[j]))
    #     return Polynomial(multiply_list)
    def __mul__(self, other):
     # Multiply two polynomials and return a new polynomial.
        result_degree = len(self.__coefficients) + len(other.__coefficients) - 2
        result = [0] * (result_degree + 1)
        for i in range(len(self.__coefficients)):
            for j in range(len(other.__coefficients)):
                result[i + j] += self.__coefficients[i] * other.__coefficients[j]
        return Polynomial(result)



    

            

    
