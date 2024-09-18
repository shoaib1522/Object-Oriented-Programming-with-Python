class shape(object):
    def __init__(self, nam, ol, bc):
        self.name = nam
        self.outline = ol
        self.background = bc
    def __str__(self):
        return f"{self.name}, {self.outline}, {self.background}"

class square(shape):
    def __init__(self, nam, ol, bc, sl):
        super().__init__(nam, ol, bc)
        self.length = sl
    def __str__(self):
        return f"{super().__str__()}, {self.length}"
    def area(self):
        return self.length ** 2

class rectangle(square):
    def __init__(self, nam, ol, bc, ln, wd):
        super().__init__(nam, ol, bc, ln)
        self.width = wd
    def __str__(self):
        return f"{super().__str__()}, {self.width}"
    def area(self):
        return self.length * self.width

def main():
    s = shape('sh1', True, 'yellow')
    print(s)
    sqr = square('sq1', False, 'golden', 5)
    print(sqr)
    print("Area", sqr.area())
    rtg = rectangle('rg1', True, 'blue', 3, 4)
    print(rtg)
    print("Area", rtg.area())


main()
