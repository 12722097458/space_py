class Person:
    # 构造方法，在创建对象时自动调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 字符串表示方法，当使用str()或print()函数时调用
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    # 长度方法，当使用len()函数时调用
    def __len__(self):
        return len(self.name)

# 创建一个Person对象
p = Person("Alice", 25)

# 调用__str__方法
print(p)  # 输出: Person(name='Alice', age=25)

# 调用__len__方法
print(len(p))  # 输出: 5