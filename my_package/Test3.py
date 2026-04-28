class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} 汪汪叫。")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} 喵喵叫。")

# 创建对象
dog = Dog("旺财")
dog.speak()

cat = Cat("咪咪")
cat.speak()