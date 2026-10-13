
class MathUtils:
    @staticmethod
    def square(number):
        return number * number


number = float(input("Введите число: "))

result = MathUtils.square(number)

print("Квадрат числа:", result)
