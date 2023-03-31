class Circle(): 
    # class object
    pi = 3.1416
    # create instace of class attributes
    def __init__(self, radius=1): 
        self.radius = radius
        
# method
    def area(self): 
        return self.radius*self.radius*self.pi
    def perimeter(self): 
        # you can use the Classname instead of self while want to access the class object
        return 2*self.radius*Circle.pi
my_circle = Circle(radius = 5)
print(my_circle.area())
print(my_circle.perimeter())