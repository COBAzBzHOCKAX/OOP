class Cat:
    def __init__(self, name):
        self.name = name

class Dog(Cat):
    def __init__(self, name, gender, age):
        super().__init__(name)
        self.gender = gender
        self.age = age

    def get_pet(self):
        return f'{self.name} {self.age}'

dog_1 = Dog("Felix", "boy", 2)
print(dog_1.get_pet())