# liquidation of a concern
def liquidation_of_a_concern(companys, half_weight):
    OPT = [[0] * (half_weight + 1) for _ in range(len(companys))]

    for i in range(len(OPT)):
        for j in range(1, half_weight + 1):
            if i == 0:
                if j < companys[i]['value']:
                    OPT[i][j] = 0
                else:
                    OPT[i][j] = companys[i]['value']
            else:
                if j < companys[i]['value']:
                    OPT[i][j] = OPT[i - 1][j]
                else:
                    OPT[i][j] = max(OPT[i - 1][j], companys[i]['value'] + OPT[i - 1][j - companys[i]['value']])

    for i in range(len(OPT)):
        print(OPT[i])
    print()
    print(f"Group of companies {[item['value'] for item in companys.values()]}. "
          f"Checking whether the total value of the companies {sum([item['value'] for item in companys.values()])} "
          f"is possible to divide: {sum([item['value'] for item in companys.values()]) / 2 == OPT[i][j]}.")
    print(f"We found a subset sum: {OPT[i][j]}")

companys = {
    0: {'value': 6},
    1: {'value': 3},
    2: {'value': 5},
    3: {'value': 2}
}
half_weight = sum([item['value'] for item in companys.values()]) // 2
liquidation_of_a_concern(companys, half_weight)
