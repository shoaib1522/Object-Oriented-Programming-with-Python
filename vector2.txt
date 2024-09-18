# Introduction of user defined type, here named Vector, a class
# the concept of data members of class

class Vector:
    pass

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
    r = Vector()
    r.x = t.x+b.x
    r.y = t.y+b.y
    r.z = t.z+b.z
    print(f"t+b: ({r.x}, {r.y}, {r.z})")

    # s is stp ==>  t . m x b
    s = t.x * (m.y*b.z - b.y*m.z) - t.y * (m.x*b.z - b.x*m.z) + t.z * (m.x*b.y - b.x*m.y)
    print(f"stp: {s}")

main()