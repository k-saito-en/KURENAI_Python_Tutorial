while True:
    x = input("正の数値を入力して下さい ")
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
    print(x)

# 出力内容
# 正の数値を入力して下さい a
# a は数値に変換できません
# 正の数値を入力して下さい -1
# -1.0 は正の数値ではありません
# 正の数値を入力して下さい 1
# 1.0