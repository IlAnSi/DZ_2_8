file = 'recipes0.txt'
cook_book = {}
list_temp = []



with open(file, encoding="utf-8") as file:
    line1 = str(file.readline())
    print(line1)
    num2 = int(file.readline())
    print(num2, type(num2))
    i = 0
    for line in file.read().split('\n'):
        print(line)
        list_line =line.split(' | ')
        print(list_line)
        dict_ingr = {'ingredient_name': list_line[0], 'quantity': list_line[1], 'measure': list_line[2]}
        print(dict_ingr)
        list_temp.append(dict_ingr)
        i += 1
    print(list_temp)
    cook_book[line1] = list_temp
    print(cook_book)