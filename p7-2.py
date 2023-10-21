def myabs(x):
    if x < 0:
        return -x
    return x


while True:
    a = float(input("> "))
    print(a, myabs(a))