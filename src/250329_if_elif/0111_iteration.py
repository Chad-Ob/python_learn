from itertools import zip_longest
from decimal import Decimal, getcontext

# 0111_iteration 迭代工具 enumerate()和zip()
a = [1, 2, 3, 4, 5, 6]
b = ["a", "b", "c", "d", "e"]
# enumerate()产生一个带序号的元组,返回一个迭代器
iteration1 = enumerate(b)
for k, v in iteration1:
    print(f"键为{k},值为{v}")
# zip()将多个可迭代对象转换成一个元素,返回一个迭代器
data = {k: v for k, v in zip(a, b)}
print(data)

#!zip()在调用两个长度不同的可迭代对象时,根据较短的对象生成元组,可通过zip_longest补全
data2 = list(zip_longest(a, b, fillvalue="空"))
print(data2)

# ‌‌练习‌：给定两个列表：
fruits = ["apple", "banana", "cherry"]
prices = [4.5, 2.8, 6.3]
# 1.使用 enumerate 输出带编号的价格表（如 "1. apple: $4.5"）
for k, (name, price) in enumerate(zip(fruits, prices)):
    print(f"{k}.{name}:${price}")
# 2.用 zip 找出价格最高的水果名称
max_price = 0
max_price_name = ""
getcontext().prec = 6  # 设置精度等于6
for k, v in zip(fruits, prices):
    count = Decimal(v)
    if count > max_price:
        max_price = v
        max_price_name = k
print(f"最贵的水果是:{max_price_name},价格:${max_price}")

# 推导式实战
"""
    1.列表推导式
    2.生成器表达式
    3.字典推导式
"""
# 统计高频单词
text = "apple banana apple cherry apple banana"
words = text.split()  # 将字符串以空格的港式分割
english_set = {word: words.count(word) for word in set(words)}
print(english_set)

## 生成器表达式计算大文件总行数（节省内存）
line_count = sum(
    1
    for line in open(
        "D:/pythonfactory/250329_python_learn/requirements.txt", encoding="UTF-16"
    )
)
print(f"共有:{line_count}行")

# ‌练习‌：
# 用列表推导式生成 1-100 中所有能被7整除或包含数字7的数
list1 = [i for i in range(1, 101) if i % 7 == 0 or i % 10 == 7 or i // 7 == 7]
print(list1)
# 用集合推导式找出两段文本中共同的单词：
text1 = "Python is an interpreted high-level programming language"
text2 = "High-level programming languages abstract away machine details"
english_set2 = text1.split()
english_set3 = text2.split()

english_txt = {t for t1 in english_set3 for t in english_set2 if t == t1}
print(english_txt)
