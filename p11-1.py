class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.current_number = 0
        self.operation = "+"
    
    def do_operation(self):
        self.second_term = self.current_number
        if self.operation == "+":
            self.result = self.first_term + self.second_term
            self.current_number = 0
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
            self.current_number = 0
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
            self.current_number = 0
        elif self.operation == "/":
            if self.second_term == 0:  # 0 を割るという概念はないのでエラー表示
                self.result = 0000
        else:
            self.result = self.first_term // self.second_term  # 課題指示通りに整数商を求める 演算子 // とする
            self.current_number = 0


# ここからメインプログラム
dentaku_plus = Dentaku()
dentaku_minus = Dentaku()
while True:
    f = int(input("First term "))
    dentaku_plus.first_term = f
    o = input("Operation ")
    dentaku_plus.operation = o
    s = int(input("Second term "))
    dentaku_plus.second_term = s
    dentaku_plus.do_operation()
    r = dentaku_plus.result
    print("Result ", r)
    dentaku_minus.first_term = dentaku_plus.result
    dentaku_minus.second_term = dentaku_plus.second_term
    if dentaku_plus.first_term == dentaku_minus.first_term - dentaku_minus.second_term:
        print("加算結果は正しいです")

# 実行結果
# First term 1
# Operation +
# Second term 2
# Result  3
# First term ^CTraceback (most recent call last):
#   File "/Users/kotarosaito/Documents/個人開発/KURENAI_Python_Tutorial/p11-1.py", line 17, in <module>
#     f = int(input("First term "))
#             ^^^^^^^^^^^^^^^^^^^^
# KeyboardInterrupt