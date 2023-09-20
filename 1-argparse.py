# python中的argparse模块学习


import sys

# 1.读取命令行中的所有参数
# format : script,和其他参数
print(sys.argv)
print(int(sys.argv[1]) * int(sys.argv[2]))


# 2.处理命令行
# - 添加可选参数
# 没有-号，添加位置参数
import argparse

# 先创建解释器
parser = argparse.ArgumentParser(description="parser *")
# 实现a*b的操作
parser.add_argument("--a", type = int, default=3, help = "operator A")
parser.add_argument("--b", type = int, default=9, help = "operator B")
parser.add_argument("method", type = int)
arg = parser.parse_args()
print(arg.a * arg.b)
