def make_fancy(text:str, n):
    letters_list = list(text)
    space_on_the_beginning=""
    while len(letters_list):
        one_letter=letters_list.pop(0)
        print(space_on_the_beginning,n*one_letter)
        space_on_the_beginning += " "

if __name__ == "__main__":
    make_fancy("LOKOMOTIVA", 2)
