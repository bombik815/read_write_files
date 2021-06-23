from pprint import pprint

''' Задача №1
Должен получится следующий словарь

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }'''
cook_book = {}
ing_book = {}
new_list = []
with open('recipes.txt', 'r', encoding='utf-8') as book_file:
    for line in book_file:
        dish_name = line.strip() # выводим имя блюда
        qty_ingredient = book_file.readline().strip() # выводим кол-во ингредиентов
        new_list = []

        for i in range(int(qty_ingredient)):
            list_ing = book_file.readline().strip().split("|") # получаем список ингредиента
            ing_book['ingredient_name'] = list_ing[0] # добавим к ключу значение из списока
            ing_book['quantity'] = list_ing[1]
            ing_book['measure'] = list_ing[2]
            new_list.append(ing_book)  # добавим в список словарь ингредиентов
            ing_book = {}

        emp_str = book_file.readline().strip() # получаем пустую строку
        cook_book[dish_name] = new_list # записываем в словарь cook_book

''' Задача №2 '''
def get_shop_list_by_dishes(dishes, person_count):
    result = []
    new_result = {}
    for dish in dishes:
        if dish in cook_book.keys(): result = cook_book.get(dish)
        for value in result:
                value['quantity'] = int(person_count) * int(value['quantity'])
                new_value = value['ingredient_name']
                del value['ingredient_name']
                new_result[new_value] = value
    pprint(new_result)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет','Утка по-пекински'], 3)