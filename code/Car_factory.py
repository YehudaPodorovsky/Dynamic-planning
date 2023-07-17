# Car factory
import copy

def car_factory(costs):
    n = len(costs)
    OPT = copy.deepcopy(costs)

    for i in range(1, n):
        if i == 1:
            OPT[i]['S1'] += costs[i - 1]['S1']
            OPT[i]['S2'] += costs[i - 1]['S2']
        else:
            OPT[i]['S1'] = costs[i]['S1'] + min(OPT[i - 1]['S1'], OPT[i]['t1'] + OPT[i - 1]['S2'])
            OPT[i]['S2'] = costs[i]['S2'] + min(OPT[i - 1]['S2'], OPT[i]['t2'] + OPT[i - 1]['S1'])
        del OPT[i]['t1']
        del OPT[i]['t2']

    print("OPT table")
    for j in OPT:
        print(j, OPT[j])

    path = []
    for i in range(n - 1, -1, -1):
        if i == 0:
            path.insert(0, 'e1' if OPT[i + 1]['S1'] < OPT[i + 1]['S2'] else 'e2')
        elif i == n - 1:
            path.insert(0, 'x1' if OPT[i]['S1'] < OPT[i]['S2'] else 'x2')
        elif i == n - 2:
            path.insert(0, 'a ' + str(i) + ',1' if OPT[i + 1]['S1'] < OPT[i + 1]['S2'] else 'a ' + str(i) + ',2')
        else:
            path.insert(0, 'a ' + str(i) + ',1' if OPT[i]['S1'] < OPT[i]['S2'] else 'a ' + str(i) + ',2')
    print()
    print(f"A plan that costs minimal {path} will cost {min(OPT[n-1]['S1'], OPT[n-1]['S2'])}")

monthly_costs = {
    0: {'S1': 2, 'S2': 4},
    1: {'S1': 7, 'S2': 8, 't2': float('inf'), 't1': float('inf')},
    2: {'S1': 9, 'S2': 5, 't2': 2, 't1': 2},
    3: {'S1': 3, 'S2': 6, 't2': 3, 't1': 1},
    4: {'S1': 4, 'S2': 4, 't2': 1, 't1': 2},
    5: {'S1': 8, 'S2': 5, 't2': 3, 't1': 1},
    6: {'S1': 3, 'S2': 6, 't2': float('inf'), 't1': float('inf')}
}
car_factory(monthly_costs)
