
def read_cook_book(file, cook_book_):
    list_temp = []
    line1 = str(file.readline().strip())
    num2 = int(file.readline())
    i = 0
    while i < num2:
        line = file.readline()
        list_line = line.split(' | ')
        dict_ingr = {'ingredient_name': list_line[0],
                     'quantity': list_line[1],
                     'measure': list_line[2].strip()}
        list_temp.append(dict_ingr)
        i += 1
    cook_book_[line1] = list_temp
    return cook_book_

file_ = 'recipes.txt'
cook_book = {}

with open(file_, encoding="utf-8") as file_:
    read_cook_book(file_, cook_book)
    for line in file_:
        read_cook_book(file_, cook_book)
print(cook_book)