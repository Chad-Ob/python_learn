import re

# 正则表达式练习(需强化练习一周)
# 基本匹配
#   \d:数字  .:匹配任意一个字符(除了下划线) \w:单词字符(字母/数字/下划线) \s:空白字符
# 数量限定
#   *:0次或者多次 +:1次或者多次 ?:零次或一次 {n}:严格匹配前一项n次 {n,m}:匹配n到m次
# 位置锚点
#   ^:匹配字符串开头 $:匹配字符串结尾 \b:单词边界
# 字符集合
#   [abc]:匹配abc中任意一个 [^abc]:不匹配a/b/c [a-z]:字母范围
# 分组或捕获
#   ():捕获分组 (?:):非捕获分组 ':或逻辑
number = "订单号:4200002526202502027350303142 收货人:Anna"
pattear = re.compile(r"\s*(\d{28}).+?收货人:\s*([A-Za-z\u4e00-\u9fa5\s]{1,20})")
match = pattear.search(number)
if match:
    num = match.group(1)
    man = match.group(2)
    print(f"匹配到订单号:{num}收货人:{man}")
