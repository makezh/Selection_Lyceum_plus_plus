from math import sin, cos, log


def simple(x, a):
    ans = a * (x ** (a - 1))
    print(ans)


def degree(a, x):
    ans = (a ** x) * log(a)
    print("%.3f" % ans)


def tg(x):
    ans = 1 / (cos(x) ** 2)
    print("%.3f" % ans)


def ctg(x):
    ans = (-1) / (sin(x) ** 2)
    print("%.3f" % ans)


def ln(x):
    ans = 1 / x
    print("%.3f" % ans)


def main():
    func = input()
    x = int(input())
    if func[0] == "x" and func[1] == "^":
        a = int(func[2:])
        simple(x, a)
    elif func[-1] == "x" and func[-2] == "^":
        a = int(func[:-2])
        degree(a, x)
    elif func == "tg(x)":
        tg(x)
    elif func == "ctg(x)":
        ctg(x)
    elif func == "ln(x)":
        ln(x)


if __name__ == '__main__':
    main()
