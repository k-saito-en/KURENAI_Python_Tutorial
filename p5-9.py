# for i in range(3):
#     for j in range(3):
#         print(i,j)

# # 出力結果
# # 0 0
# # 0 1
# # 0 2
# # 1 0
# # 1 1
# # 1 2
# # 2 0
# # 2 1
# # 2 2

a = [5, 1, 3, 4]
sum = 0
for i in a:
    sum += i
average = sum/len(a)
print(average)

# 出力結果
# 3.25

# 演習 5-13 エラーを体験する(4).
# if 文内で比較演算子 == の代わりに誤って代入演算 = を書いてしまうことはよくある間違いの一つです.
# プログラム 5-9 プログラム 5-1 の 3 行目を if a = 1: と 書いた場合に，どのようなエラーになるかを確かめてください.
# 17 章 「IDLE/Python でのエラーメッセージの読み方」も併せて参照すること.

a = 1 
b = 0
if a == 1: # a = 1
    if b == 0:
        print("YES a == 1 and b == 0")

# 出力結果
#     if a = 1:
#        ^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?