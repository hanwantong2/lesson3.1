# 初始化一个空字符串
result = ""

# 从键盘输入字数
num_words = int(input("请输入要输入的单词数量："))

# 循环输入每一个单词并连接到结果字符串
for i in range(num_words):
    word = input(f"请输入第{i + 1}个单词：")
    result += word + " "

# 打印结果字符串
print("连接后的字符串是：", result.strip())

# 初始化一个空字符串
result = ""

# 循环输入每一个单词并连接到结果字符串
while True:
    word = input("请输入一个单词（输入“停止”结束）：")

    # 检查用户是否输入“停止”，如果是则跳出循环
    if word == "停止":
        break

    result += word + " "

# 打印结果字符串
print("连接后的字符串是：", result.strip())

import random

# 初始化错误计数器
wrong_count = 0
correct_count = 0

while wrong_count < 3:
    # 生成两个随机数字
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # 显示表达式
    expression = f"{num1} + {num2} = "

    # 获取用户输入的答案
    user_answer = input(expression)

    # 计算正确答案
    correct_answer = num1 + num2

    # 检查答案是否正确
    if user_answer == str(correct_answer):
        print("正确！")
        correct_count += 1
    else:
        print("错误答案")
        wrong_count += 1

# 显示游戏结束消息和正确答案数量
print(f"游戏结束。正确答案{correct_count}个。")