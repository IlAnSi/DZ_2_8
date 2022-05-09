
def read_cook_book(file, cook_book_):
    list_temp = []
    line1 = str(file.readline().strip())
    num2 = int(file.readline())
    i = 0
    while i < num2:
        line = file.readline()
        list_line = line.split(' | ')
        dict_ingr = {'ingredient_name': list_line[0],
                     'quantity': int(list_line[1]),
                     'measure': list_line[2].strip()}
        list_temp.append(dict_ingr)
        i += 1
    cook_book_[line1] = list_temp
    return cook_book_

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_order = {}
    for dish in dish_order:
        ing_ord = cook_book[dish]
        for ingr in ing_ord:
            measure_quantity = {}
            measure = ingr.get('measure')
            measure_quantity['measure'] = measure
            quantity = ingr.get('quantity')*pers_count
            measure_quantity['quantity'] = quantity
            ing = list(ingredient_order.keys())
            ingr_key = ingr.get('ingredient_name')
            if ing.count(ingr_key) > 0:
                ingredient_order.get(ingr_key)
                del(ingredient_order[ingr_key])
                quantity_rep = ingr.get('quantity') * pers_count
                measure_quantity['quantity'] = quantity + quantity_rep
            ingredient_order[ingr_key] = measure_quantity
    return ingredient_order


file_ = 'recipes.txt'
cook_book = {}

with open(file_, encoding="utf-8") as file_:
    read_cook_book(file_, cook_book)
    for line in file_:
        read_cook_book(file_, cook_book)

dish_order = ['Омлет', 'Фахитос']
pers_count = 3

order = get_shop_list_by_dishes(dish_order, pers_count)
print(order)