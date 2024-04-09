class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def calculate_dist(self, point):
        dist = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return dist
    

point1 = Point(1, 2)
point2 = Point(3, 4)

print(point1.calculate_dist(point2))

point1.set_x(5)
print(point1.get_x())
point1.set_y(5)
print(point1.get_y())

