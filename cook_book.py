from pprint import pprint

with open('recipes.txt', encoding='UTF-8') as f:
    cook_book = {}
    for line in f.read().split("\n\n"):
        name, *args = line.split("\n")
        # print(line)
        # print(' ')
        dish_name, *ingredients = line.split("\n")
        cook_lst = []
        for ingredient in ingredients[1:]:
            ingredient_name, quantity, measure = ingredient.split("|")
            cook_lst.append(
                {
                    "ingredient_name": ingredient_name,
                    "quantity": int(quantity),
                    "measure": measure,
                }
            )
        # print(cook_lst)
        # print(' ')
        cook_book[dish_name] = cook_lst
        # cook_book = {cook_book}
    print(f"cook_book = {cook_book}")


def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                name, quantity, measure = ingredient.values()
                new_cook.setdefault(name, {"measure": measure, "quantity": 0})
                new_cook[name]["quantity"] += quantity * person_count
    print(new_cook)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
