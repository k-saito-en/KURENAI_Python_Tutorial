# x の平方根を求める 
x = 2
#
rnew = x
rnew_list = [rnew]
#
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
rnew_list.append(rnew)
#
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
rnew_list.append(rnew)
#
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
rnew_list.append(rnew)
#
r1 = rnew
r2 = x/r1
rnew = (r1 + r2)/2
print(r1, rnew, r2)
rnew_list.append(rnew)
print(rnew_list)

# 出力
# 2 1.5 1.0
# 1.5 1.4166666666666665 1.3333333333333333
# 1.4166666666666665 1.4142156862745097 1.411764705882353
# 1.4142156862745097 1.4142135623746899 1.41421143847487
# [2, 1.5, 1.4166666666666665, 1.4142156862745097, 1.4142135623746899]