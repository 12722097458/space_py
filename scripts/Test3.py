# 1. if-elif-else 条件语句
x = 10
if x > 10:
    print("x 大于 10")
elif x == 10:
    print("x 等于 10")
else:
    print("x 小于 10")

# 2. for 循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# 4. break 语句
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# 5. continue 语句
for num in numbers:
    if num == 3:
        continue
    print(num)

# 6. pass 语句
for num in numbers:
    if num == 3:
        pass
    print(num)

# 7. try-except-else-finally 异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
else:
    print("没有发生异常，结果是:", result)
finally:
    print("无论是否发生异常，都会执行")

# 使用 for 循环实现循环 10 次
for i in range(10):
    print(f"这是第 {i + 1} 次循环")

# 使用 while 循环实现循环 10 次
count = 0
while count < 10:
    print(f"这是第 {count + 1} 次循环")
    count += 1

# range() 函数常见用法
for i in range(5, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"索引 {i} 对应的水果是: {fruits[i]}")

numbers = list(range(5))
print(numbers)
