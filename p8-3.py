from turtle import *


def drawStar(n):
    for _ in range(n):
        forward(100)
        left(360 * (n - 4) / n)
    done()


# 正七角形
drawStar(7)

# # 正九角形
drawStar(9)