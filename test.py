import os
print("__________________________________________________")
print("欢迎使用个人财务管理系统V1.0")
print("By Jianling Gao")
print("__________________________________________________")

filename = "money.txt"
zero = 0
# 检查文件是否存在
if not os.path.exists(filename):
    # 如果文件不存在，则创建文件
    with open(filename, 'w') as file:
        file.write("")  # 创建一个空文件
    with open(filename, 'w') as file:
        file.write(str(zero))
    print(f"文件'{filename}'已创建。")
else:
    print(f"文件'{filename}'已存在。")



while True:
    print("1.查询当前余额")
    print("2.存钱")
    print("3.消费")
    print("4.退出系统")
    num = int(input("请输入要执行的操作："))
    os.system('cls')
    if num == 4:
        print("已退出，欢迎再次使用")
        break
    elif num == 2:
        innum = float(input("请输入要存入的金额"))
        # 打开并读取文件
        with open(filename, 'r') as file:
            content = file.read().strip()  # 读取文件内容并去除首尾空白字符

        # 尝试将读取的内容转换为整数
        now = float(content)
        now = now + innum
        with open(filename, 'w') as file:
            file.write(str(now))  # 将数字转换为字符串后写入文件

        print("已存入"+ str(innum) +"￥")

    elif num == 3:
        innum = float(input("请输入消费金额"))
        # 打开并读取文件
        with open(filename, 'r') as file:
            content = file.read().strip()  # 读取文件内容并去除首尾空白字符

        # 尝试将读取的内容转换为整数
        now = float(content)
        now = now - innum
        with open(filename, 'w') as file:
            file.write(str(now))  # 将数字转换为字符串后写入文件

        print("已消费"+ str(innum) +"￥")

    elif num == 1:
        # 打开并读取文件
        with open(filename, 'r') as file:
            content = file.read().strip()  # 读取文件内容并去除首尾空白字符
        print("余额为" + str(content) + "￥")

    else:
        print("数字不正确，请重新输入")