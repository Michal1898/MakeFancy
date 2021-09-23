def make_fancy(text: str, n):
    space_on_the_beginning = ""
    while len(text):
        print(space_on_the_beginning, n * text[0])
        space_on_the_beginning += " "
        text = text[1:]


if __name__ == "__main__":
    make_fancy("LOKOMOTIVA", 2)
