# The backpack problem
def backpack_problem(items, bag_weight):
    OPT = [[0] * (bag_weight + 1) for _ in range(len(items))]

    for i in range(len(OPT)):
        for j in range(1, bag_weight + 1):
            if i == 0:
                if j < items[i]['weight']:
                    OPT[i][j] = 0
                else:
                    OPT[i][j] = items[i]['value']
            else:
                if j < items[i]['weight']:
                    OPT[i][j] = OPT[i - 1][j]
                else:
                    OPT[i][j] = max(OPT[i - 1][j], items[i]['value'] + OPT[i - 1][j - items[i]['weight']])

    for i in range(len(OPT)):
        print(OPT[i])
    print(f"The maximum weight of items that we can put in a {bag_weight} kilo bag is {OPT[i][j]}.")

items = {
    0: {'weight': 6, 'value': 30},
    1: {'weight': 3, 'value': 14},
    2: {'weight': 4, 'value': 18},
    3: {'weight': 2, 'value': 9}
}
bag_weight = 10
backpack_problem(items, bag_weight)
