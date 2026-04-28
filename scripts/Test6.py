# 示例1: 简单的try-except语句
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: 除数不能为零。")

# 示例2: 捕获多个异常
try:
    num = int("abc")
except ValueError:
    print("Error: 无法将字符串转换为整数。")
except TypeError:
    print("Error: 类型错误。")

# 示例3: 使用else子句
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: 除数不能为零。")
else:
    print("结果是:", result)

# 示例4: 使用finally子句
try:
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError:
    print("Error: 文件未找到。")
finally:
    print("清理操作完成。")

# 示例5: 自定义异常
class CustomError(Exception):
    pass


try:
    raise CustomError("这是一个自定义异常。")
except CustomError as e:
    print("CustomError:", e)
