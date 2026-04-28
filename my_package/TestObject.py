class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁。")

# 创建对象
person1 = Person("张三", 25)
person1.introduce()