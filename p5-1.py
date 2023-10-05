# x の平方根を求める
x = 2
#
rnew = x
#
for i in range(10):
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2)/ 2
print(r1, rnew, r2)

# 出力結果
# 1.414213562373095 1.414213562373095 1.4142135623730951