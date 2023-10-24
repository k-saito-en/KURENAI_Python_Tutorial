from turtle import *


def come(x, y):
    # 現在のタートルの座標をタプル型で取得
    (xx, yy) = pos()
    newxy = ((xx + x) / 2, (yy + y) / 2)
    print(x, y)
    goto(newxy)


# 関数そのものを渡してクリック時に実行するので引数を取らないようにする必要がある
onscreenclick(come)
done()
