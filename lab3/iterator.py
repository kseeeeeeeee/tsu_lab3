
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration

        number = self.current
        self.current -= 1
        return number


start = int(input("Введите начальное число: "))

countdown = Countdown(start)

for number in countdown:
    print(number)
