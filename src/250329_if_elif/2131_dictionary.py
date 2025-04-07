import timeit
import time

# 2131_dictionary
# 字典可以替代if-elif语句,提升代码可读性和效率
"""
oprations = {
    "1": lambda x, y: x + y,
    "2": lambda x, y: x - y,
    "3": lambda x, y: x * y,
    "4": lambda x, y: x / y,
}

# 实现计算器
while True:
    mode = input("1.加法2.减法3.乘法4.除法5.退出\n")
    if mode == "5":
        break
    x = int(input("请输入第一个数字"))
    y = int(input("请输入第二个数字"))
    func = oprations.get(mode, lambda *_: "输入错误")
    print(func(x, y))

# ‌练习‌：实现一个单位转换器菜单，支持以下选项：

1.公里转英里(1公里≈0.6214英里）
2.摄氏度转华氏度（℉=℃*1.8+32)
3.千克转磅(1千克≈2.2046磅）
4.要求使用字典映射实现核心逻辑。
dicationary = {
    "1": lambda x: x * 0.6214,
    "2": lambda x: x * 1.8 + 32,
    "3": lambda x: x * 2.2046,
}

while True:
    mode = input("1.公里转英里2.摄氏度转华氏度3.千克转磅4.退出\n")
    if mode == "4":
        break
    func = dicationary.get(mode, lambda *_: "没有这个功能")
    number = float(input("请输入你的数字:\n"))
    print(func(number))

# 循环优化
# 1.相同情况下优先使用for循环,for循环比while循环效率更高,
# 2.避免重复计算:在循环前预结算固定值
# 3.提前终止条件‌,控制内存,小心内存溢出

# 编写一个寻找质数的方法


def find_primes(max_numble):
    primes = []
    max = max_numble + 1

    # 选择for循环
    for num in range(2, max):
        number2 = int(num**0.5) + 1
        for num_a in range(2, number2):
            if num % num_a == 0:
                break
        else:
            primes.append(num)
    return primes


number = int(input("请输入最大数:\n"))
print(find_primes(number))
"""


# ‌练习‌：优化以下代码，使其运行效率提升至少 50%：
# 原低效代码
star = time.perf_counter()
numbers = list(range(1, 100001))
total = 0

for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
end = time.perf_counter()
text_time = end - star
print(f"消耗时间为{text_time}秒")
