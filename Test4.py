# 以下是一个简单的Python函数示例

# 定义一个函数，用于计算两个数的和
def add_numbers(a, b):
    """
    计算两个数的和。

    :param a: 第一个数
    :param b: 第二个数
    :return: 两个数的和
    """
    return a + b

# 调用函数并打印结果
result = add_numbers(3, 5)
print(result)

# 定义一个函数，用于打印欢迎信息
# def greet(name):
#     """
#     打印欢迎信息。

#     :param name: 用户名
#     """
#     print(f"欢迎, {name}!")

# # 调用函数
# greet("张三")

# 在Python中，函数参数有多种写法，以下是常见的几种：

# 1. 位置参数（Positional Arguments）
# 这是最常见的参数类型，调用函数时，参数按照定义的顺序依次传递。
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# 2. 默认参数（Default Arguments）
# 可以为参数提供默认值，这样在调用函数时，如果没有传递该参数，就会使用默认值。
def greet(name, message="欢迎"):
    print(f"{message}, {name}!")

greet("张三")  # 使用默认消息
greet("李四", "你好")  # 提供自定义消息

# 3. 可变位置参数（Variable Positional Arguments）
# 使用 *args 来接收任意数量的位置参数，这些参数会被收集到一个元组中。
def sum_numbers(*args):
    print(f"type args is {type(args)}")
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)

# 4. 关键字参数（Keyword Arguments）
# 在调用函数时，可以使用参数名来指定参数的值，这样可以不按照定义的顺序传递参数。
def describe_person(name, age):
    print(f"{name} 今年 {age} 岁。")

describe_person(age=25, name="王五")

# 5. 可变关键字参数（Variable Keyword Arguments）
# 使用 **kwargs 来接收任意数量的关键字参数，这些参数会被收集到一个字典中。
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="赵六", age=30, city="北京")

# 6. 仅限位置参数（Positional-Only Arguments）
# 在Python 3.8及以后的版本中，可以使用 / 来指定仅限位置参数。
def add_positional(a, b, /):
    return a + b

result = add_positional(2, 3)
print(result)

# 7. 仅限关键字参数（Keyword-Only Arguments）
# 使用 * 来指定后面的参数为仅限关键字参数。
def greet_keyword(*, name, message="欢迎"):
    print(f"{message}, {name}!")

greet_keyword(name="孙七")

# 匿名函数示例
# 定义一个匿名函数，用于计算两个数的和
add = lambda a, b: a + b
# 调用匿名函数
result = add(3, 5)
print("匿名函数计算结果:", result)

# 闭包示例
def outer_function(x):
    """
    外部函数，用于创建闭包。

    :param x: 外部函数的参数
    :return: 内部函数
    """
    def inner_function(y):
        """
        内部函数，使用了外部函数的变量 x。

        :param y: 内部函数的参数
        :return: 两个数的和
        """
        return x + y
    return inner_function

# 创建一个闭包
closure = outer_function(10)
# 调用闭包
result = closure(5)
print("闭包计算结果:", result)

# 演示局部变量和全局变量

# 全局变量
global_variable = 10

def test_variables():
    # 局部变量
    local_variable = 20
    print(f"局部变量: {local_variable}")
    # 访问全局变量
    print(f"全局变量: {global_variable}")

# 调用函数
test_variables()

# 尝试访问局部变量（这会导致错误）
# print(local_variable)

# 修改全局变量
def modify_global_variable():
    global global_variable
    global_variable = 30
    print(f"修改后的全局变量: {global_variable}")

# 调用修改全局变量的函数
modify_global_variable()

# 验证全局变量是否已被修改
print(f"全局变量现在的值: {global_variable}")