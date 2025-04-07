# 第三天函数设计与模块化编程实战
# 0038_function_paramete  函数参数解析
# 1.参数传递机制:不可变对象传值(int,str,tuple),可变对象传引用(list,dict)
def modify(num, lst):
    num += 2
    lst.append(99)


a = 5
b = [1, 2]
modify(a, b)
print(a, b)  # 5 [1, 2, 99] 说明可变类型传参鬼被一同更改,不可变类型传参不会


# 2.可变参数实战
def dynamic_args(a, *args, **kwargs):
    print(f"固定参数:{a}")
    print(f"元组:{args}")
    print(f"字典:{kwargs}")


dynamic_args(1, 5, 6, 8, name="小明", age=89)


# 练习
# 实现通用平均值计算函数 avg()，支持任意数量参数和异常处理：


def raise_type_error():
    raise TypeError("参数类型错误")


def avg_not_variable_parameter(*args):
    if not args:
        raise ValueError("至少需要一个参数")
    return sum(args) / len(args)


def avg_variable_parameter(iterable):
    total = 0
    count = 0
    for item in iterable:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            raise_type_error()
    if count == 0:
        raise ValueError("可迭代对象中无有效数字")
    return total / count


def avg(*args):
    # 处理多参数（如 avg(1, 2, 3)）
    if len(args) > 1:
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise_type_error()
        return avg_not_variable_parameter(*args)

    # 处理单参数（如 avg([1,2,3])）
    arg = args
    type_name = type(arg).__name__

    if type_name in ("list", "set"):
        return avg_variable_parameter(arg)
    elif type_name in ("int", "float"):
        return avg_not_variable_parameter(arg)
    else:
        raise_type_error()


print(avg(1, 2, 3))  # 输出 2.0
print(avg("a", 2, 3))  # 提示"参数类型错误"
