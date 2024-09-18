# Introduction of user defined type, here named Vector, a class
# functions with UDTs as parameters and return values

class Vector:
    pass

def add(v1, v2):
    r = Vector()
    r.x = v1.x+v2.x
    r.y = v1.y+v2.y
    r.z = v1.z+v2.z
    return r

#def stp(v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z):
def stp(v1, v2, v3):
    s = v1.x * (v2.y*v3.z - v3.y*v2.z) - v1.y * (v2.x*v3.z - v3.x*v2.z) + v1.z * (v2.x*v3.y - v3.x*v2.y)
    return s

def main():
    # t is 2i+j+5k
    t = Vector()
    t.x = 2
    t.y = 1
    t.z = 5

    # m is 3i-2j+4k
    m = Vector()
    m.x = 3
    m.y = -2
    m.z = 4

    # b is 4i-j-2k
    b = Vector()
    b.x = 4
    b.y = -1
    b.z = -2

    print(f"t: ({t.x}, {t.y}, {t.z})")
    print(f"m: ({m.x}, {m.y}, {m.z})")
    print(f"b: ({b.x}, {b.y}, {b.z})")

    # r is t+b
    r = add(t,b)
    print(f"t+b: ({r.x}, {r.y}, {r.z})")

    # s is stp ==>  t . m x b
    s = stp(t,m,b)
    print(f"stp: {s}")

main()