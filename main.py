def make_fancy(text, n):
    pointer = 0
    for i in text:
        print(pointer * " ", n * i)
        pointer += 1


if __name__ == "__main__":
    make_fancy("KOKOT", 7)
