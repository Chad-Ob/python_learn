import re

# 今日练习
"""
任务1身份证信息解释器
要求:
    1.输入18位身份证号(需校验长度和数字)
    2.解析并输出
        -出生日期(YYYY-MM-DD格式)
        -性别(第17位数是奇数为男反之为女)
        -校验位验证结果(最后校验码验证)
    3.对非法输入进行友好提示



def verify_idnumber(txt):
    pat = re.compile(
        r"^[1-9]\d{5}((19|20)\d{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{2}(\d{1})([\dX])$"
    )
    if pat:
        return pat.search(txt)


txt = input("请输入身份证号:")
result = verify_idnumber(txt)
years = result.group(1)
month = result.group(3)
day = result.group(4)
if int(result.group(5)) % 2 == 0:
    sex = "女"
else:
    sex = "男"
    last = result.group(6)
print(f"出生日期:{years}年{month}月{day}日.性别为:{sex}校验码为:{last}")
"""

"""
任务2日志清洗工具
要求:
1.使用正则提取:
    -日志级别(ERROP/WRANING/INFO)
    -时间戳(转为datetime对象)
    -错误描述
    -重试次数(如果有)
2.返回结构化字典
"""
"""
log_txt = "[ERROR] 2023-10-05 14:30:45 - Connection timeout (retry=3)"


def log_cleaning(txt):
    pat = re.compile(
        r"^\[([A-Z]+)\] ((19|20)\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\s([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s-\s(.*)\((retry=\d+)\)$" #转义字符\(是将(转义
    )
    if pat:
        return pat.search(txt)
    else:
        print("未匹配到数据")


result_log = log_cleaning(log_txt)
level = result_log.group(1)
timestamp_year = result_log.group(2)
timestamp_month = result_log.group(4)
timestamp_day = result_log.group(5)
timestamp_hour = result_log.group(6)
timestamp_minute = result_log.group(7)
timestamp_second = result_log.group(8)
timestamp_message = result_log.group(9)
timestamp_retries = result_log.group(10)

print("匹配完成")
"""
a = "431121199612176517"

pat = re.compile(
    r"^[1-9]\d{5}((19|20)\d{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{2}(\d{1})([\dX])$"
)

if pat:
    result = pat.search(a)
    year = result.group(1)
    math = result.group(3)
    day = result.group(4)
    if int(result.group(5)) % 2 == 0:
        sex = "女"
    else:
        sex = "男"
    check = result.group(6)

    print(f"出生时间为:{year}年{math}月{day}日;性别:{sex};校验码:{check}")
