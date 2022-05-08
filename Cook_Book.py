file = 'recipes0.txt'
cook_book = {}
list_temp = []



with open(file, encoding="utf-8") as file:

    line1 = str(file.readline())
    num2 = int(file.readline())

    for line in file.read().split('\n'):
        list_line =line.split(' | ')
        dict_ingr = {'ingredient_name': list_line[0], 'quantity': list_line[1], 'measure': list_line[2]}
        list_temp.append(dict_ingr)
    cook_book[line1] = list_temp
    print(cook_book)