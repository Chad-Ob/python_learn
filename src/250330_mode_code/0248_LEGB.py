# 0248_LEGB 作用域和闭包
"""
python中的作用域从小到大分别为
L(local):局部作用域,E(enclosing)嵌套作用域,G(global)全局作用域,B(built-in)内置作用域
LEGB法则:系统读取变量时通过L->E->G->B顺序读取,读到就停止
"""
# 全局作用域
x = 5


def counter():
    count = 0  # 局部作用域

    def _increment():
        nonlocal count  # 声明非局部变量,嵌套作用域
        count += 1
        return count

    return _increment


c = counter()
print(c(), c(), c())  # 输出 1 2 3

# ‌练习‌：
# 实现缓存装饰器 @cache，存储函数最近 3 次调用结果：
"""
from collections import OrderedDict
import functools

def cache(func):
    缓存装饰器，保存函数最近 3 次不同参数的调用结果
    cache_store = OrderedDict()  # 用有序字典存储缓存

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 生成唯一缓存键（处理参数顺序和关键字参数）
        key = args + tuple(sorted(kwargs.items()))
        
        # 如果命中缓存，刷新使用顺序并返回结果
        if key in cache_store:
            cache_store.move_to_end(key)  # 标记为最近使用
            return cache_store[key]
        
        # 未命中缓存，执行函数并存储结果
        result = func(*args, **kwargs)
        cache_store[key] = result
        
        # 缓存超过 3 项时，删除最久未使用的项
        if len(cache_store) > 3:
            cache_store.popitem(last=False)
        
        return result

    return wrapper
"""
