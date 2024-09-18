# Introduction of user defined type, here named Vector, a class
# the concept of __init__, __str__, static member functions of class

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def __str__(self):
        vstr = "("
        vstr += str(self.__x)
        vstr += ", "
        vstr += str(self.__y)
        vstr += ", "
        vstr += str(self.__z)
        vstr += ")"
        return vstr
        
    def add(v1, v2):
        r = Vector()
        r.__x = v1.__x+v2.__x
        r.__y = v1.__y+v2.__y
        r.__z = v1.__z+v2.__z
        return r
    staticmethod(add)

    def stp(v1, v2, v3):
        s = v1.__x * (v2.__y*v3.__z - v3.__y*v2.__z) - v1.__y * (v2.__x*v3.__z - v3.__x*v2.__z) + v1.__z * (v2.__x*v3.__y - v3.__x*v2.__y)
        return s
    staticmethod(stp)

def main():
    # t is 2i+j+5k
    t = Vector(2,1,5)

    # m is 3i-2j+4k
    m = Vector(3,-2,4)

    # b is 4i-j-2k
    b = Vector(4, -1, -2)
    
    print(f"t: {t}")
    print(f"m: {m}")
    print(f"b: {b}")

    # r is t+b
    r = Vector.add(t, b)   # calling a static member function
    print(f"t+b: {r}")

    # s is stp ==>  t . m x b
    s = Vector.stp(t,m,b)   # calling a static member function
    print(f"stp: {s}")

main()