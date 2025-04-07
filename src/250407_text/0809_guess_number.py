import random
import re

# 猜数字游戏
"""
    完善猜数字游戏
    核心需求:
        1.记录玩家猜测次数,限制最多10次
        2.游戏失败时显示正确答案
        3.增加输入验证(防止非数字输入崩溃)

    升级任务:
        1.添加难度选择(简单模式15次/困难模式5次)
        2.记录历史猜测数字并显示趋势(如:23->30->提示持续上升)        
"""


def guess_number():
    target = random.randint(1, 100)
    guess_list = []
    while True:
        game_mode = input("1.简单模式(15次机会)2.困难模式(5次机会),请选择:\n")
        if game_mode != "1" and game_mode != "2":
            print("输入错误,请重新输入")
        else:
            break
    max_attempts = 15 if game_mode == "1" else 5
    print(f"=== 猜数字游戏(1-100) ===\n您有{max_attempts}次机会")
    for attempt in range(1, max_attempts + 1):
        try:
            guess = input(f"\n第{attempt}次尝试 > 输入数字:")
            pat = re.compile(r"^(100|[1-9][0-9]?)$")
            if pat:
                result = pat.search(guess)
                guess = int(result.group(1))
        except AttributeError:
            print("检测到非法输入!请输入数字!")
            continue
        guess_list.append(guess)
        if guess == target:
            print(f"正确!您用了{attempt}次猜中!")
            return
        elif guess > target:
            print("猜大了")
        else:
            print("猜小了")
        # 趋势分析
        if len(guess_list) > 1:
            last = guess_list[len(guess_list) - 2]
            (
                print("持续偏离")
                if (guess > target and guess > last)
                or (guess < target and guess < last)
                else print("调整方向")
            )
    print(f"机会用尽!正确答案是{target}")


if __name__ == "__main__":
    guess_number()
