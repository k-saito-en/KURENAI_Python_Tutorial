# 交差点名を格納する空の配列を作成しておく
cross_table = []
# 材料を用意
tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "鳥丸", "河原町"]
# for文で格納していく
for i in range(len(tozai)):
    street = []
    for j in range(len(nanboku)):
        cross = tozai[i] + nanboku[j]
        street.append(cross)
    cross_table.append(street)

print(cross_table)

# 出力結果
# [['三条堀川', '三条鳥丸', '三条河原町'], ['四条堀川', '四条鳥丸', '四条河原町'], ['五条堀川', '五条鳥丸', '五条河原町']]