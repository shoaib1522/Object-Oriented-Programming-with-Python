class shape(object):
    def __init__(self, nam, ol, bc):
        self.name = nam
        self.outline = ol
        self.background = bc
    def __str__(self):
        return f"{self.name}, {self.outline}, {self.background}"

class rectangle(shape):
    def __init__(self, nam, ol, bc, ln, wd):
        super().__init__(nam, ol, bc)
        self.length = ln
        self.width = wd
    def __str__(self):
        return f"{super().__str__()}, {self.length}, {self.width}"
    def area(self):
        return self.length * self.width

class square(rectangle):
    def __init__(self, nam, ol, bc, sl):
        super().__init__(nam, ol, bc, sl, sl)


def main():
    s = shape('sh1', True, 'yellow')
    print(s)
    rtg = rectangle('rg1', True, 'blue', 3, 4)
    print(rtg)
    print("Area", rtg.area())
    sqr = square('sq1', False, 'golden', 5)
    print(sqr)
    print("Area", sqr.area())
main()
