cook_book = {}

with open('recipes.txt', 'r', encoding='utf8') as recipe:
    for line in recipe:
        cook_book[line.strip()] = []
        ingredient_count = recipe.readline()
        for i in range(int(ingredient_count)):
            ingredient_name, quantity, measure = recipe.readline().split(' | ')
            cook_book[line.strip()].append({'ingredient_name': ingredient_name,
                                            'quantity': int(quantity),
                                            'measure': measure.strip()})
        recipe.readline()


def get_shop_list_by_dishes(dishes, person_count):
    list_ingredient = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            list_ingredient[list(ingredient.values())[0]] = {'measure': list(ingredient.values())[2],
                                                             'quantity': list(ingredient.values())[1] * person_count}
    return list_ingredient


print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
