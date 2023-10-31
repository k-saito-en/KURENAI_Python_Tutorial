import tkinter as tk

# 計算機能のための変数とイベント用の関数定義

# ２校演算のモデル
# 入力中の数字
current_number = 0
# 第一項
first_term = 0
# 第二項
second_term = 0
# 結果
result = 0

operation = 0


def do_puls():
    global current_number
    global first_term
    global operation

    operation = 1
    first_term = current_number
    current_number = 0


def do_minus():
    global current_number
    global first_term
    global operation

    operation = 2
    first_term = current_number
    current_number = 0


def do_times():
    global current_number
    global first_term
    global operation

    operation = 3
    first_term = current_number
    current_number = 0


def do_division():
    global current_number
    global first_term
    global operation

    operation = 4
    first_term = current_number
    current_number = 0

def do_eq():
    global second_term
    global result
    global current_number

    second_term = current_number
    if operation == 1:
        result = first_term + second_term
        current_number = 0
    elif operation == 2:
        result = first_term - second_term
        current_number = 0
    elif operation == 3:
        result = first_term * second_term
        current_number = 0
    elif operation == 4:
        if second_term == 0: # 0 を割るという概念はないのでエラー表示
            result = "Error"
        else:
            result = first_term // second_term # 課題指示通りに整数商を求める 演算子 // とする
            current_number = 0


# # 数字キーのコールバック
# def key1():
#     key(1)


# def key2():
#     key(2)


# def key3():
#     key(3)


# def key4():
#     key(4)


# def key5():
#     key(5)


# def key6():
#     key(6)


# def key7():
#     key(7)


# def key8():
#     key(8)


# def key9():
#     key(9)


# def key0():
#     key(0)


# 数字キーを一括処理する関数
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)


def clear():
    global current_number
    current_number = 0
    show_number(current_number)


def plus():
    do_puls()
    show_number(current_number)


def minus():
    do_minus()
    show_number(current_number)


def times():
    do_times()
    show_number(current_number)


def division():
    do_division()
    show_number(current_number)


def eq():
    do_eq()
    show_number(result)



def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))


# tkinter での画面構成

# ウインドウ作成
root = tk.Tk()
# コンテナ作成
f = tk.Frame(root, bg="#ffffc0")
# フレーム割り付け
f.grid()

# ウィジェットの作成

number_buttons = []
for i in range(10):
    button = tk.Button(f, text=str(i), highlightbackground="#ffffff", width=2, command=lambda x=i: key(x))
    number_buttons.append(button)

bc = tk.Button(f, text="C", highlightbackground="#ff0000", width=2, command=clear)
bp = tk.Button(f, text="+", highlightbackground="#00ff00", width=2, command=plus)
bm = tk.Button(f, text="-", highlightbackground="#00ff00", width=2, command=minus)
bt = tk.Button(f, text="x", highlightbackground="#00ff00", width=2, command=times)
bd = tk.Button(f, text="/", highlightbackground="#00ff00", width=2, command=division)
be = tk.Button(f, text="=", highlightbackground="#00ff00", width=2, command=eq)

# Grid 型ジオメトリマネージャによるウィジェットの割り付け

number_buttons[0].grid(row=4,column=0)
number_buttons[1].grid(row=3,column=0)
number_buttons[2].grid(row=3,column=1)
number_buttons[3].grid(row=3,column=2)
number_buttons[4].grid(row=2,column=0)
number_buttons[5].grid(row=2,column=1)
number_buttons[6].grid(row=2,column=2)
number_buttons[7].grid(row=1,column=0)
number_buttons[8].grid(row=1,column=1)
number_buttons[9].grid(row=1,column=2)

bc.grid(row=1,column=3)
be.grid(row=4,column=3)
bp.grid(row=2,column=3)
bm.grid(row=3,column=3)
bt.grid(row=4,column=2)
bd.grid(row=4,column=1)

# 数値を表示するウィジェット

e = tk.Entry(f, font=("Helvetica", 14))
e.grid(row=0, column=0, columnspan=4)
clear()

# ここから GUI がスタート

# mainloop メソッドで GUI の処理に移る
root.mainloop()