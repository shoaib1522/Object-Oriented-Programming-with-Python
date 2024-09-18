from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Oval import Oval
from Shape import Outline
from Shape import Point
def main():
    # SHAPE 1:
    Sq_1_outline=Outline(True) 
    Sq_1_point=Point("Center")
    Sq_1=Square("Shape 1",Sq_1_outline,"Red","White",'Square',Sq_1_point,5)
    print(Sq_1)
main()