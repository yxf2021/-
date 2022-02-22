# 自定义感知机

# 实现逻辑和
def AND(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.7
    tem = w1 * x1 + w2 * x2
    if tem <= theta:
        return 0
    return 1


print(AND(1, 1))  # 1
print(AND(1, 0))  # 0
print(AND(0, 0))  # 0


def OR(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.2
    tem = w1 * x1 + w2 * x2
    if tem <= theta:
        return 0
    return 1





def XOR(x1, x2):
    s1 = not AND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(XOR(1, 1))  # 0
print(XOR(1, 0))  # 1
print(XOR(0, 1))  # 1
print(XOR(0, 0))  #
