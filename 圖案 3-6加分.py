# 打印上半部分
for i in range(1, 4):
    print(" " * (3 - i) + "*" * (2 * i - 1))

# 打印中間的星號
print("*" * 5)

# 打印下半部分
for i in range(3, 0, -1):
    print(" " * (3 - i) + "*" * (2 * i - 1))