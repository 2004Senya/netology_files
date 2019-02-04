def create_cook_book(file):
    cook_book = {}
    f = open(file, "r")
    line = f.readlines()

    line_count = []

    i = 0
    while i < i + 1:
        try:
            rec_count = int(line[sum(line_count) + 1]) + 3
            line_count.append(rec_count)
            i += 1
        except IndexError:
            break

    # print("Количество блюд:", len(line_count))

    ingre = []

    i = 0
    while i < len(line_count):
        i2 = 0
        while i2 < line_count[i] - 3:
            if (i2 == 0):
                cook_book[line[sum(ingre)].replace("\n", "")] = [{'ingridient_name': line[sum(ingre) + i2 + 2].split(" | ")[0], 'quantity': line[sum(ingre) + i2 + 2].split(" | ")[1], 'measure': line[sum(ingre) + i2 + 2].split(" | ")[2].replace("\n", "")}]
            else:
                cook_book[line[sum(ingre)].replace("\n", "")] += [{'ingridient_name': line[sum(ingre) + i2 + 2].split(" | ")[0], 'quantity': line[sum(ingre) + i2 + 2].split(" | ")[1], 'measure': line[sum(ingre) + i2 + 2].split(" | ")[2].replace("\n", "")}]
            i2 += 1
            if (i2 % (line_count[i] - 3) == 0):
                ingre.append(line_count[i])
        i += 1

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        i = 0
        while i < 1:
            i2 = 0
            while i2 < len(cook_book[dish]):
                shop_list[cook_book[dish][i2]["ingridient_name"]] = {'quantity': (int(cook_book[dish][i2]["quantity"]) * person_count), 'measure': cook_book[dish][i2]["measure"]}
                i2 += 1
            i += 1
    return shop_list
            
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, create_cook_book("recipes.txt")))

