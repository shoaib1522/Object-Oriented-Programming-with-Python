class rational:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def show(self):
        print(f'The ratio is= {self.numerator} : {self.denominator}')
    def multiply_ratio(self,r2):
        self.numerator=self.numerator*r2.numerator
        self.denominator=self.denominator*r2.denominator
        return f'After multiplication of r1*r2 = {self.numerator} : {self.denominator}'
    def real_ratio(self,r2)

def main():
    r1=rational(5,6)
    r1.show()
    r2=rational(9,16)
    r2.show()
    print(r1.multiply_ratio(r2))
main()