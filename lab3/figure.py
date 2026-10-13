class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите длину прямоугольника: "))

rectangle = Rectangle(width, height)

print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())