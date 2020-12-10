from pprint import pprint

def get_input():
    with open("input.txt", "r") as file:
        return file.read()

def quiz1(data):
    couples = ["0, 0"]
    x = y = 0
    for c in data:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1
        couples.append(f"{x}, {y}")
    print(len(set(couples)))

def quiz2(data):
    couples = ["0, 0"]
    x = y = x2 = y2 = 0
    i = 0
    for c in data:
        x_c = y_c = None
        if i % 2 == 0:
            x_c = x
            y_c = y
        else:
            x_c = x2
            y_c = y2
        if c == '^':
            y_c += 1
        elif c == 'v':
            y_c -= 1
        elif c == '<':
            x_c -= 1
        elif c == '>':
            x_c += 1

        couples.append(f"{x_c}, {y_c}")
        if i % 2 == 0:
            x = x_c
            y = y_c
        else:
            x2 = x_c
            y2 = y_c
        i += 1
    print(len(set(couples)))

if __name__ == "__main__":
    data = get_input()
    quiz1(data)
    quiz2(data)