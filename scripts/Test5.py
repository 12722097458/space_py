# 1. 列表 (List)
# 列表是一种可变的有序序列，可以包含不同类型的元素。

# 创建列表
my_list = [1, 2, 3, 4, 5]

# 查：访问列表元素
print("列表中索引为2的元素:", my_list[2])

# 增：添加元素
my_list.append(6)
print("添加元素后的列表:", my_list)

# 改：修改元素
my_list[2] = 10
print("修改元素后的列表:", my_list)

# 删：删除元素
del my_list[2]
print("删除元素后的列表:", my_list)

# 2. 元组 (Tuple)
my_tuple = (1, 2, 3, 4, 5)
print("元组中索引为2的元素:", my_tuple[2])

# 3. 集合 (Set)
my_set = {1, 2, 3, 4, 5}
print("元素3是否在集合中:", 3 in my_set)
my_set.add(6)
print("添加元素后的集合:", my_set)
my_set.remove(3)
print("删除元素后的集合:", my_set)

# 4. 字典 (Dictionary)
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("字典中键 'name' 对应的值:", my_dict['name'])
my_dict['job'] = 'Engineer'
print("添加键值对后的字典:", my_dict)
my_dict['age'] = 31
print("修改键值对后的字典:", my_dict)
del my_dict['city']
print("删除键值对后的字典:", my_dict)
