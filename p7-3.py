#
def get_positive_numeral(element1, element2):
    diff = element1 - element2
    if diff < 0:
        return -diff
    else:
        return diff


def square_root(x):
    "引数 x の平方根を求める"
    rnew = x
    #
    diff = get_positive_numeral(rnew, x / rnew)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = get_positive_numeral(r1, r2)
        if diff < 0:
            diff = -diff
    return rnew


# ここからメインプログラム
v = 2
r = square_root(v)
print("結果は ", r)