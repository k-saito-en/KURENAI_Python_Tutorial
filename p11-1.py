class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"
    
    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation == "/":
            self.result = self.first_term / self.second_term

# ここからメインプログラム
dentaku = Dentaku()
while True:
    f = int(input("First term "))
    dentaku.first_term = f
    o = input("Operation ")
    dentaku.operation = o
    s = int(input("Second term "))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result
    print("Result ", r)


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