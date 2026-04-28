def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(result)


def add(a, b):
    return a + b


result = add(3, 5)
print(result)


def greet(name, message="欢迎"):
    print(f"{message}, {name}!")


greet("张三")
greet("李四", "你好")


def sum_numbers(*args):
    print(f"type args is {type(args)}")
    return sum(args)


result = sum_numbers(1, 2, 3, 4, 5)
print(result)


def describe_person(name, age):
    print(f"{name} 今年 {age} 岁。")


describe_person(age=25, name="王五")


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="赵六", age=30, city="北京")


def add_positional(a, b, /):
    return a + b


result = add_positional(2, 3)
print(result)


def greet_keyword(*, name, message="欢迎"):
    print(f"{message}, {name}!")


greet_keyword(name="孙七")

add = lambda a, b: a + b
result = add(3, 5)
print("匿名函数计算结果:", result)


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_function(10)
result = closure(5)
print("闭包计算结果:", result)

global_variable = 10


def test_variables():
    local_variable = 20
    print(f"局部变量: {local_variable}")
    print(f"全局变量: {global_variable}")


test_variables()


def modify_global_variable():
    global global_variable
    global_variable = 30
    print(f"修改后的全局变量: {global_variable}")


modify_global_variable()
print(f"全局变量现在的值: {global_variable}")
