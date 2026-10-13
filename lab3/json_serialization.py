
import json


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])


student = Student("Ксения", 20)

# Преобразуем объект в JSON и сохраняем в файл.
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student.to_dict(), file, ensure_ascii=False, indent=4)

print("Объект сохранён в student.json")

# Читаем JSON из файла.
with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Восстанавливаем объект Student из прочитанных данных.
loaded_student = Student.from_dict(data)

print("Имя:", loaded_student.name)
print("Возраст:", loaded_student.age)
