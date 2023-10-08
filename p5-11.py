# 演習 5-17 力試し
# inputcheck.py, p5-6.py を組み合わせて以下の条件を満たす平方根を求めるプログ
# ラム作成しなさい. 以下の項目に一度に取り組むのではなく，これまでに学んだどの節が関係するか
# を整理し，1項目づつプログラムを改修しては動作を確認するようにしてくださ い.

# 1. 絶対値の計算には abs() 関数を用いること.
# 2. 平方根を求める数を繰り返し端末から入力できるようにすること.
# 3. 平方根を求める数の入力が数値に変換できない場合は，その旨を示して，次の入力を求めること.
# 4. 平方根を求める数が 0 以下の場合は，その旨を示して，次の入力を求めること.
# できれば以下にも挑戦すること
# 5. 端末からの入力が “end” という文字列なら終了すること.
# 6. 計算精度を絶対精度ではなく，相対精度で 10-6 とすること.これについて大きな数や小さな数(例えば 1010 や 10-10)の平方根を求め，結果を確認する こと.

import math

while True:
    x = input("正の数値を入力して下さい ")
    if x == "end":
        break
    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期しないエラーです")
        exit
    if x < 0:
        print(x, "は正の数値ではありません")
        continue
# 以下は正しい出力が得られた時の処理
    rnew = x
#
    diff = rnew - x / rnew
    if diff < 0:
        diff = math.abs(diff)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = r1 - r2
        if diff < 0:
            diff = math.abs(diff)