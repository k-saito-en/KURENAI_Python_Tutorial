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

# tk.Frame を継承した MyFrame というクラスを作り
# その中でウィジェットやコールバック関数(メソッド)を設定する
# tkinter をつかう定番

class MyFrame(tk.Frame):
#   __init__はクラスオブジェクトを作る際の初期化メソッド
    def __init__(self, master = None):
        super().__init__(master)
# 後で参照しないウィジェットの作成、ローカル変数
        b1 = tk.Button(self,text='1', command=lambda:self.key(1))
        b2 = tk.Button(self,text='2', command=lambda:self.key(2))
        b3 = tk.Button(self,text='3', command=lambda:self.key(3))
        b4 = tk.Button(self,text='4', command=lambda:self.key(4))
        b5 = tk.Button(self,text='5', command=lambda:self.key(5))
        b6 = tk.Button(self,text='6', command=lambda:self.key(6))
        b7 = tk.Button(self,text='7', command=lambda:self.key(7))
        b8 = tk.Button(self,text='8', command=lambda:self.key(8))
        b9 = tk.Button(self,text='9', command=lambda:self.key(9))
        b0 = tk.Button(self,text='0', command=lambda:self.key(0))
        bc = tk.Button(self,text='c', command=self.clear)
        bp = tk.Button(self,text='+', command=self.plus)
        be = tk.Button(self,text='=', command=self.eq)
        bm = tk.Button(self,text='-', command=self.minus)
        bt = tk.Button(self,text='x', command=self.times)
        bd = tk.Button(self,text='/', command=self.division)

# Grid 型ジオメトリーマネージャによるウィジェットの割り付け
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=1, column=0)
        b8.grid(row=1, column=1)
        b9.grid(row=1, column=2)
        b0.grid(row=4, column=0)
        bc.grid(row=1,column=3)
        bp.grid(row=2,column=3)
        be.grid(row=4,column=3)
        bm.grid(row=3,column=3)
        bt.grid(row=4,column=2)
        bd.grid(row=4,column=1)

# 他のメソッドで参照する数値を表示するウィジェット,
# クラスオブジェクトの変数として作成,頭に self. がつく
        self.e = tk.Entry(self)
        self.e.grid(row=0, column=0, columnspan=4)

# クラスの定義ではメソッドの最初の引数は self, 中でクラスオブジェクトの変数, メソッドは self をつけて参照
    def key(self, n):
        global current_number
        current_number = current_number * 10 + n
        self.show_number(current_number)

    
    def clear(self):
        global current_number
        current_number = 0
        self.show_number(current_number)


    def plus(self):
        do_puls()
        self.show_number(current_number)


    def minus(self):
        do_minus()
        self.show_number(current_number)


    def times(self):
        do_times()
        self.show_number(current_number)


    def division(self):
        do_division()
        self.show_number(current_number)


    def eq(self):
        do_eq()
        self.show_number(result)



    def show_number(self, num):
        self.e.delete(0, tk.END)
        self.e.insert(0, str(num))


# tkinter での画面構成

# ウインドウ作成
root = tk.Tk()
# コンテナ作成
f = MyFrame(root)
# フレーム割り付け
f.pack()
f.mainloop()


