import math 
class Vector:
    def __init__(self,list):
        self.vector=list
    def __str__(self):
        index=0
        vector=""
        for element in self.vector:
            if element >=0:
                vector+=f"+{element}x{index}"
            else:
                vector += f"{element}x{index}"
            index+=1
        return f"Vector : {vector}"
    def __getitem__(self, index):
        return self.vector[index]
    def __setitem__(self, index, value):
        self.vector[index]=value
    def magnitude(self):
        magnitude=0
        for element in self.vector:
            magnitude+=element**2
        mag=round(math.sqrt(magnitude),2)
        return f"Magnitude :{mag}"
    def dot_product(self,other):
        if len(self.vector)> len(other.vector) or len(self.vector) < len(other.vector):
            return "Dot product is not possible (Only possible for same dimensional vector)"
        dot_product=0
        for i in range(len(self.vector)):
            dot_product+=self.vector[i]*other.vector[i]
        return f"(Va.Vb):{dot_product}"
    def __mul__(self,constant):
        Scalar_vector=Vector([0]*len(self.vector))
        for i in range(len(self.vector)):
            Scalar_vector[i]=(self.vector[i] * constant)
        return f'After Scalar Multiplication {Scalar_vector.__str__()}'
    def __neg__(self):
        negative_of_vector=Vector([0]*len(self.vector))
        for i in range(len(self.vector)):
            negative_of_vector.vector[i] = (self.vector[i] * -1)
        return negative_of_vector.__str__()
    def __add__(self, other):
        Addition=Vector([0]*len(self.vector))
        if len(self.vector) > len(other.vector) or len(self.vector) < len(other.vector):
            return "Addition is not possible (Only possible for same dimensional vector)"
        for i in range(len(self.vector)):
            Addition.vector[i] = (self.vector[i] +other.vector[i])
        return Addition.__str__()
    def __sub__(self, other):
        Subtraction=Vector([0]*len(self.vector))
        if len(self.vector) > len(other.vector) or len(self.vector) < len(other.vector):
            return "Subtraction is not possible  (Only possible for same dimensional vector)"
        for i in range(len(self.vector)):
            Subtraction.vector[i] = (self.vector[i] - other.vector[i])
        return Subtraction.__str__()
    def cross_product(self, other):
        if len(self.vector) != 3 or len(other.vector) != 3:
            return "Cross product is only defined for 3-dimensional vectors."
        cross_product = Vector([self.vector[1]*other.vector[2] - self.vector[2]*other.vector[1],
                           self.vector[2]*other.vector[0] - self.vector[0]*other.vector[2],
                           self.vector[0]*other.vector[1] - self.vector[1]*other.vector[0]])
        return f"Cross Product: {cross_product}"
    def unit_vector(self):
        magnitude = math.sqrt(sum(element**2 for element in self.vector))
        unit_vector = Vector([round(element / magnitude,3) for element in self.vector])
        return f"Unit Vector: {unit_vector}"
    def component_wise_multiply(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same dimensions for component-wise multiplication.")
        result_vector = [self.vector[i] * other.vector[i] for i in range(len(self.vector))]
        return Vector(result_vector)
    def component_wise_divide(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same dimensions for component-wise division.")
        result_vector = [round(self.vector[i] / other.vector[i],3) for i in range(len(self.vector))]
        return Vector(result_vector)
    def scalar_divide(self, scalar):
        result_vector = [round(element / scalar,3) for element in self.vector]
        return Vector(result_vector)
    def __eq__(self, other):
        return self.vector == other.vector
def main():
    v=Vector([1,2,3])
    d=Vector([1,4,5])
    print('The First Vector',v.magnitude())
    print('Negative of first',-v)
    print(v*3)
    print(v+d)
    print(v.dot_product(d))
    print(v-d)
    print(v.magnitude())
    print(d.magnitude())
    print(v.cross_product(d))
    print(v.unit_vector())
    print(v.component_wise_multiply(d))
    print(v.component_wise_divide(d))
    print(v.scalar_divide(5))
    print('Comparison Of equality: ',v==d)
main()