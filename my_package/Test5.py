class MyClass:
    # 类变量
    class_variable = 0
    def __init__(self, instance_variable):
        # 实例变量
        self.instance_variable = instance_variable
        MyClass.class_variable += 1
    # 实例方法
    def instance_method(self):
        return f'实例变量: {self.instance_variable}, 类变量: {MyClass.class_variable}'
    # 类方法
    @classmethod
    def class_method(cls):
        return f'类变量: {cls.class_variable}'
    # 静态方法
    @staticmethod
    def static_method():
        return '这是一个静态方法'
# 创建实例
obj1 = MyClass(1)
obj2 = MyClass(2)
obj3 = MyClass(3)
# 调用实例方法
print(obj1.instance_method())
# 调用类方法
print(MyClass.class_method())
# 调用静态方法
print(MyClass.static_method())