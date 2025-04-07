# 1.字符串格式化的三种方法
user_name = "赵琛瑜"
user_year = 29
user_phone_number = "17576066350"
# 1.1%-formatring()兼容旧项目
print("用户名:%s年龄:%d电话号码:%s" % (user_name, user_year, user_phone_number))
# 1.2str.format() pythone2.0
print(
    "用户名:{x}年龄:{y}电话号码:{z}".format(
        x=user_name, y=user_year, z=user_phone_number
    )
)
# 1.3f-string pythone3.6以上 推荐
print(f"用户名:{user_name}年龄:{user_year}电话号码:{user_phone_number}")
