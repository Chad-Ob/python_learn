import re
import json
import phonenumbers
from phonenumbers import geocoder, timezone, carrier

# 简易通讯录系统
"""
    功能需求:
        1.使用字典存储联系人(姓名:电话)
        2.支持功能:
            ·添加联系人(姓名不可重复)
            ·查询联系人
            ·显示全部联系人
            ·删除联系人
        3.数据持久化(可选):退出时保存到contacts.txt

    高级挑战:
        1.实现数据持久化(使用json模块保存/读取)        
        2.添加电话号码归属地查询功能(例如前三位判断运营商)
"""

# 功能方法
contact_function = {
    "1": lambda: add_contact(),
    "2": lambda: search_contact(),
    "3": lambda: search_contact_location(),
    "4": lambda: remove_contact(),
    "5": lambda: show_all_contact(),
}

# 校验规则
verify_txt = {
    "phone_verify": r"^(1[3-9]\d{9})$",
    "user_name_verify": r"^([\u4e00-\u9fa5a-zA-Z0-9](2,20))$",
    "mode_verify": r"^([1-6])$",
}

# 文件读取
file_full_name = {"contact": "contacts.json"}


# c初始化通讯录
def init_contacts():
    try:
        with open(file_full_name.get("contact"), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # 文件不存在时返回空字典
    except Exception as e:
        print(
            f"初始化失败:{str(e)}"
        )  # 初始化指为某个变量,系统或设备设置初始状态和默认值的过程
        return {}


# 保存数据
def save_contact(contacts):
    try:
        with open(file_full_name.get("contact"), "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存失败:{str(e)}")
    return False


# 校验名称
def validate_name():
    for _ in range(3):
        contact_name = input("请输入联系人姓名\n")
        try:
            contact_name = (
                re.compile(verify_txt.get("user_name_verify"))
                .search(contact_name)
                .group(1)
            )
        except Exception as e:
            print(f"姓名格式错误:{str(e)}")
            continue
        return contact_name
    return None


# 校验手机号码
def validata_phone_number():
    for _ in range(3):
        phone_number = input("请输入手机号码\n")
        try:
            phone_number = (
                re.compile(verify_txt.get("phone_verify")).search(phone_number).group(1)
            )
        except Exception as e:
            print(f"手机格式错误:{e}")
            continue
        return phone_number
    return None


# 添加数据
def add_contact():
    loaded_data = init_contacts()
    phone_number = validata_phone_number()
    contact_name = validate_name()
    if contact_name == None or phone_number == None:
        return None
    loaded_data[contact_name] = phone_number
    # 持久化逻辑
    save_contact(loaded_data)
    return "保存成功"


# 查询联系人
def search_contact():
    contact_name = validate_name()
    if contact_name == None:
        return None
    loaded_data = init_contacts()
    return loaded_data[contact_name]


# 查询号码归属地
def search_contact_location():
    phone_number = validata_phone_number()
    if phone_number == None:
        return None
    # 字典匹配归属地并返回
    #!!有缺陷归属地现在只显示中国
    try:
        num = phonenumbers.parse(f"+86{phone_number}", "CN")
        if not phonenumbers.is_valid_number(num):
            return "无效的手机号码"
        tz = timezone.time_zones_for_geographical_number(num)[0]
        operator = geocoder.description_for_number(num, "zh")
        return f"{tz}|{operator}"
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return f"查询异常:{str(e)}"


# 展示所有联系人
def show_all_contact():
    loaded_data = init_contacts()
    if loaded_data == None:
        return None
    return loaded_data


# 删除联系人
def remove_contact():
    contact_name = validate_name()
    loaded_data = init_contacts()
    if contact_name == None or loaded_data == None:
        return None
    if contact_name in loaded_data:
        del loaded_data[contact_name]  # 删除数据时也应该进行校验
    else:
        print("联系人不存在")
    save_contact(loaded_data)
    return "删除成功"


# 控制台
def main_menu():
    print("欢迎来到通讯录系统")
    while True:
        #!↓
        mode_id = input(
            f"本系统提供1.添加联系人;2.查询联系人;3.查询号码归属地;4.删除联系人;5.显示全部联系人;6.退出系统;请选择\n"
        )
        try:
            re.compile(verify_txt.get("mode_verify")).search(mode_id).group(1)
        except:
            print("暂时没有此项功能,敬请期待")
            continue
        if mode_id == "6":
            print("感谢使用")
            break
        # 数据准备
        func = contact_function.get(mode_id)
        # 核心逻辑
        result = func()
        if result == None:
            continue
        print(result)
    return


if __name__ == "__main__":
    main_menu()
