# 算术运算符
a = 10
b = 3

# 加法
addition = a + b
print(f"加法结果: {addition}")

# 减法
subtraction = a - b
print(f"减法结果: {subtraction}")

# 乘法
multiplication = a * b
print(f"乘法结果: {multiplication}")

# 除法
division = a / b
print(f"除法结果: {division}")

# 取整除法
floor_division = a // b
print(f"取整除法结果: {floor_division}")

# 取模
modulus = a % b
print(f"取模结果: {modulus}")

# 幂运算
power = a ** b
print(f"幂运算结果: {power}")

# 比较运算符
print(f"等于比较: {a == b}")
print(f"不等于比较: {a != b}")
print(f"大于比较: {a > b}")
print(f"小于比较: {a < b}")
print(f"大于等于比较: {a >= b}")
print(f"小于等于比较: {a <= b}")

# 赋值运算符
c = 5
c += a  # 等同于 c = c + a
print(f"加法赋值后 c 的值: {c}")
c -= a  # 等同于 c = c - a
print(f"减法赋值后 c 的值: {c}")
c *= a  # 等同于 c = c * a
print(f"乘法赋值后 c 的值: {c}")
c /= a  # 等同于 c = c / a
print(f"除法赋值后 c 的值: {c}")
c //= a  # 等同于 c = c // a
print(f"取整除法赋值后 c 的值: {c}")
c %= a  # 等同于 c = c % a
print(f"取模赋值后 c 的值: {c}")
c **= a  # 等同于 c = c ** a
print(f"幂运算赋值后 c 的值: {c}")

# 逻辑运算符
x = True
y = False
print(f"逻辑与: {x and y}")
print(f"逻辑或: {x or y}")
print(f"逻辑非: {not x}")

# 位运算符
p = 5  # 二进制: 0101
q = 3  # 二进制: 0011
print(f"按位与: {p & q}")
print(f"按位或: {p | q}")
print(f"按位异或: {p ^ q}")
print(f"按位取反: {~p}")
print(f"左移: {p << 1}")
print(f"右移: {p >> 1}")

# 成员运算符
list_example = [1, 2, 3, 4, 5]
print(f"成员存在: {a in list_example}")
print(f"成员不存在: {b not in list_example}")

# 身份运算符
m = [1, 2, 3]
n = [1, 2, 3]
o = m
print(f"身份相同: {m is o}")
print(f"身份不同: {m is not n}")
