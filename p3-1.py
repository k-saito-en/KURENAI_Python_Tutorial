# x の平方根を求める 
x = 2
#
rmew = x
#
r1 = rnew
r2 = x/r1 # 三角形の関係式から図形的に求めている
rnew = (r1 + r2)/2 
print(r1, rnew, r2) 
#
r1 = rnew
r2 = x/r1 
rnew = (r1 + r2)/2 
print(r1, rnew, r2) 
#
r1 = rnew
r2 = x/r1 
rnew = (r1 + r2)/2 
print(r1, rnew, r2) 
#
r1 = rnew
r2 = x/r1 
rnew = (r1 + r2)/2 
print(r1, rnew, r2)

# 出力結果
# 2 1.5 1.0
# 1.5 1.4166666666666665 1.3333333333333333
# 1.4166666666666665 1.4142156862745097 1.411764705882353
# 1.4142156862745097 1.4142135623746899 1.41421143847487

# Traceback (most recent call last):
#   File "/**/KURENAI_Python_Tutorial/p3-1.py", line 6, in <module>
#     r1 = rnew
#          ^^^^
# NameError: name 'rnew' is not defined. Did you mean: 'rmew'?