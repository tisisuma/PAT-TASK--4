class Circle:
    # member variable
    pi = 3.141


    # constructor method
    def __init__(self, radius):
        self.radius = radius


    # method to calculate Area of a circle
    def AreaCircle(self):
        area = self.pi * self.radius * self.radius
        return area
   
    # function for perimeter of a circle
    def PerimeterCircle(self):
        perimeter = 2 * self.pi * self.radius
        return perimeter
    
radius_list= [10,501,22,37,100,999,87,351]  
for radius in radius_list:
    # #object defined. The name of the object is circle_object

    circl=Circle(radius)
    print("Radius: ",circl.radius)

    print("Area of Circle: ",circl.AreaCircle())
    print("Perimeter of Circle: ",circl.PerimeterCircle())
   

