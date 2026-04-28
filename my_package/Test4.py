class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

# 定义一个函数，接受一个 Shape 对象并调用其 area 方法
def print_area(shape):
    print(f"该图形的面积是 {shape.area()}。")

# 创建对象
rectangle = Rectangle(5, 3)
circle = Circle(2)

# 调用 print_area 函数
print_area(rectangle)
print_area(circle)