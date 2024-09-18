# Introduction of user defined type, here named Vector, a class
# getters/setters and decorators

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.setX(x)
        self.setX(x)
        self.setY(y)
        self.setZ(z)
        return
    def setX(self, d):
        self.__x = d
        return
    def getX(self):
        return self.__x
    def setY(self, d):
        self.__y = d
        return
    def getY(self):
        return self.__y
    def setZ(self, d):
        self.__z = d
        return
    def getZ(self):
        return self.__z
    def __str__(self):
        return "(" + str(self.getX()) + "," + str(self.getY()) + "," + str(self.getZ()) + ")"
    def __add__(lhs, rhs):
        v = Vector()
        v.setX(lhs.getX() + rhs.getX())
        v.setY(lhs.getY() + rhs.getY())
        v.setZ(lhs.getZ() + rhs.getZ())
        return v
    @staticmethod
    def stp(v1, v2, v3):
        v = v1.getX() * (v2.getY() * v3.getZ() - v2.getZ() * v3.getY())
        v -= v1.getY() * (v2.getX() * v3.getZ() - v2.getZ() * v3.getX())
        v += v1.getZ() * (v2.getX() * v3.getY() - v2.getY() * v3.getX())
        return v

def main():
    t = Vector(2,1,5)
    m = Vector(3,-2,4)
    b = Vector(4,-1,-2)
    print("t: " + str(t))
    print("m: " + str(m))
    print("b: " + str(b))
    print("t+b: " + str(t+b))
    print("stp: " + str(Vector.stp(t,m,b)))

main()