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
for i in range(len(a)):
    sum += a[i]
average = sum/len(a)
print(average)

# 出力結果
# 3.25