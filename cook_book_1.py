from pprint import pprint
import json as json
from pprint import pformat


# def make_cook_book():
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
    # return cook_book
    # format_cook_book = pformat(cook_book)
    # print(f"cook_book = ")
    pprint(cook_book, width=100)
    # pprint(format_cook_book)
    print(' ')


def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                name, quantity, measure = ingredient.values()
                new_cook.setdefault(name, {"measure": measure, "quantity": 0})
                new_cook[name]["quantity"] += quantity * person_count

    pprint(new_cook)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }


# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
