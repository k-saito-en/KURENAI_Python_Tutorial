# is_A, is_B, is_C のいずれかが True の場合に True と判定する関数
conditions = [is_A, is_B, is_C]


def checkABC():
    for c in conditions:
        if c:
            return True
    return False
