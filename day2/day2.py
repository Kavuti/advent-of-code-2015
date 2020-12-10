from itertools import permutations

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def get_area(w, h, l):
    return 2*(w*h + h*l + w*l) + min(w*h, h*l, w*l)


def get_ribbon(w, h, l):
    s = sorted([w, h, l])
    return 2*(s[0]+s[1])+(w*h*l)


def quiz1(data):
    print(sum([get_area(*d) for d in data]))

def quiz2(data):
    print(sum([get_ribbon(*d) for d in data]))

if __name__ == "__main__":
    data = [[int(n) for n in l.split("x")] for l in get_input().splitlines()]
    quiz1(data)
    quiz2(data)
