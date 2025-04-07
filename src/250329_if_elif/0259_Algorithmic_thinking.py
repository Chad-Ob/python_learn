from functools import lru_cache

# 0259_Algorithmic_thinking 递归和迭代
# 递归是从上至下的视角,从顶到下逐步缩小问题规模的方式
#!递归需要设置边界,要不会出现无线递归,栈溢出的现象
# 迭代是从底到顶逐步积累的效果,迭代往往比递归内存性能更好
# 波菲那契函数 F(N) = F(n-1) + F(n+2)


# 递归实现
# 通过缓存减少重复计算,极大提升函数性能,原理是缓存同一参数固定答案的答案,减少计算.
# 需要纯函数,参数可哈希,列表和字典不能使用 可通过参数调整内存和性能
@lru_cache(maxsize=128)
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
    # 查询缓存 CacheInfo(hits=34, misses=36, maxsize=None, currsize=36)
    # hits:缓存命中次数,musses:缓存未命中次数,maxsize:缓存容量,currsize:当前缓存量
    print(fibonacci.cache_info())
    fibonacci.cache_clear()  # 重置缓存


# 迭代实现
def fib_iter(n):
    a = 0  # F(0)
    b = 1  # F(1)
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib_rec(4))
print(fib_iter(4))


# 冒泡排序
def bubble_sort(arr, mode_version=False, compare_func=None):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for e in range(n - 1 - i):
            a, b = arr[e], arr[e + 1]
            if compare_func:
                if mode_version:
                    result = compare_func(b, a)
                else:
                    result = compare_func(a, b)
                should_swap = result > 0
            else:
                # 默认比较方式
                if mode_version:
                    should_swap = a < b
                else:
                    should_swap = a > b
            if should_swap:
                arr[e], arr[e + 1] = b, a
    return arr


def compare_length(a, b):
    return len(a) - len(b)


arr = ["apple", "banana", "cherry", "date"]
print(bubble_sort(arr, mode_version=True, compare_func=compare_length))
# ‌练习‌：
# 修改斐波那契递归函数，加入缓存装饰器 @lru_cache 提升性能
# 优化冒泡排序，使其支持降序排序和自定义比较函数
