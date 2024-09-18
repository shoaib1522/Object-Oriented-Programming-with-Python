class Circle:
    def __init__(self, x, y, r):
        self.__cx = x
        self.__cy = y
        self.__radius = r
        
    def __str__(self):
        
    def __repr__(self):
        
    def __reduce__(self):
        
    def __eq__(self, other):   # for equal matrices
        
    def __ne__(self, other):    # for unequal matrices

    # other relational/condition operations <, <=, >, >=
        
    @property
    def cx(self):  
    @x.setter
    def cx(self, x):

    @property
    def cy(self):   
    @y.setter
    def cy(self, y):

    @property
    def radius(self):    
    @radius.setter
    def radius(self, r):

    @property
    def area(self):    

    @property
    def diameter(self):   # return 2 * radius 

    @property
    def circumference(self):    

    @property
    def isPointCircle(self):    # return true when radius is zero

    @property
    def isUnitCircle(self):    # return true when radius is one

    def isCircleOfRadius(self, r):    # return true when radius is r

    def isCocentricwith(self, c):   # return true when have same center

    def haveSameCenter(self, c):    # return true if center and radius are same

    def isOfEqualRadius(self, c):    # return true when radius are equal
    
    def set(self, x, y, r):
    
    def setCenter(self, x, y):
    
    def setRadius(self, r):
        
    def moveCenterAt(self, x, y):
    
    def moveCenterBy(self, x, y):
    
    def increaseRadiusBy(self, c):
    
    def decreaseRadiusBy(self, c):
    
    #some more of your choice      