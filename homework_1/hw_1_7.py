#7

class Circle():
    
    def area(self,radius):
        return radius**2*3.14
    
    def perimeter(self,radius):
        return 2*radius*3.14


radius = int(input("Enter the radius of circle: "))

print("Circle Area:", Circle().area(radius))
print("Circle perimeter:", Circle().perimeter(radius))
