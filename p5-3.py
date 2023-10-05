# for i in range(10): 
#     # i = 1 ならば、ブッロク内の処理を一周分スキップする
#     if i == 1:
#         continue 
#     # i = 8 ならば、10週目を待たずしてこのブロックから離脱する
#     if i== 8:
#         break
#     print(i)

# # 出力結果
# # 0
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7

a = list(range(10))
b = list(range(3, 10))
c = list(range(3, 10, 2))
print(a)
print(b)
print(c)

# 出力結果
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3, 4, 5, 6, 7, 8, 9]
# [3, 5, 7, 9]