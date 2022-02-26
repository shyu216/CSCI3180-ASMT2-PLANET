class Circle:
    def __init__(self, radius):


        self._radius = radius
    @property
    def radius(self):


        return self._radius
    @radius.setter
    def radius(self, radius):


        if radius > 0:
            self._radius = radius
        else:
            self._radius = 0


circle = Circle(1)

print(circle.radius)

circle.radius = -1 
print(circle.radius) 

circle.radius = 3
print(circle.radius) 