from abc import ABC,abstractmethod
from tkinter import*
class Shape(ABC):
    t = Tk()
    @abstractmethod
    def area(self):
        pass
    @abstractmethod 
    def perimeter(self):
        pass
    @abstractmethod
    def draw(self):
        pass
class Rectangle(Shape):
    def __init__(self,len,wid):
        self.length=len
        self.width=wid
    def area(self):
        return f"Area of rectangle :{round(self.length*self.width,2)} metre square"
    def perimeter(self):
        return f"Perimeter of rectangle:{round(2*(self.length+self.width),2)} metre"
    def draw(self):
        canvas=Canvas()
        canvas.create_rectangle(self.length,self.width,self.length*2,self.width*2,outline="green",fill="black",width=5)
        canvas.pack()
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"Area :{round(22/7*(self.radius*self.radius),2)} metre square"
    def perimeter(self):
        return f"Perimeter :{round(2*(22/7*self.radius),2)} metre"
    def draw(self):
        canvas=Canvas()
        canvas.create_oval(self.radius,10, self.radius*2, 70, outline="black", fill="white", width=2)
        canvas.pack()
class Square(Rectangle):
    def __init__ (self,len,outline,border_size,fill):
        self.length=len
        self.outline=outline
        self.border_size=border_size
        self.colour=fill
    def area(self):
        return f"Area :{round(self.length*self.length,2)}"
    def perimeter(self):
        return f"Perimeter :{round(2*(self.length+self.length),2)} m"
    def draw(self):
        canvas=Canvas()
        canvas.create_rectangle(self.length,self.length,self.length*2+50,self.length*2+50,outline=self.outline,fill=self.colour,width=self.border_size)
        canvas.pack()
    def __str__(self):
        return f"Area :{round(self.length*self.length,2)}\nOutline :{self.outline}\nBorder_size :{self.border_size}\nColour :{self.colour}"
class Oval(Circle):
    def __init__(self,radius):
       super().__init__(radius)
        # self.outline=outline
        # self.border_size=border_size
        # self.fill=fill
    def perimeter(self):
        return f"Perimeter :{round(2*(22/7*self.radius),2)} m"
    def area(self):
        return f"Area :{round(22/7*(self.radius*self.radius),2)} m**2"
    # def __str__(self):
    #     return f"Area :{round(22/7*self.radius,2)}\nOutline :{self.outline}\nBorder_size :{self.border_size}\nFill :{self.fill}"
    def draw(self):
        canvas = Canvas()
        canvas.create_rectangle(self.radius,self.radius,80,80,outline=self.outline, fill=self.fill, width=self.border_size)
        canvas.pack()
        Shape.t.mainloop()
def main():
    # r=Rectangle(50,70)
    # print(r.area())
    # r.draw()
    # c=Circle(40)
    # print(c.area())
    # c.draw()
    # s=Square(30,"black",3,fill="white")
    # print(s.area())
    # s.draw()
    # print(s)
    # o=Oval(10,"black",3,fill="white")
    # o.draw()
    c=Oval(5)
    print(c.area())
main()
