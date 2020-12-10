def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(data):
    print(data.count("(") - data.count(")"))


def quiz2(data):
    count = 0
    for i, p in enumerate(data):
        if p == ("("):
            count += 1
        if p == (")"):
            count -= 1 
        if count == -1:
            print(i+1)
            break


if __name__ == "__main__":
    data = get_input()
    quiz1(data)
    quiz2(data)