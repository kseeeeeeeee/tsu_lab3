
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def main():
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите длину прямоугольника: "))

    rectangle = Rectangle(width, height)

    print("Площадь прямоугольника:", rectangle.area())
    print("Периметр прямоугольника:", rectangle.perimeter())


if __name__ == "__main__":
    main()
