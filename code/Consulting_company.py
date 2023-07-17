# Consulting company
import copy

def consulting_company(costs, M):
    n = len(costs)
    OPT = copy.deepcopy(costs)

    for i in range(2, n + 1):
        OPT[i]['NY'] = costs[i]['NY'] + min(OPT[i - 1]['NY'], M + OPT[i - 1]['SF'])
        OPT[i]['SF'] = costs[i]['SF'] + min(OPT[i - 1]['SF'], M + OPT[i - 1]['NY'])

    print("Monthly costs\t\t\t", "OPT table")
    for j in OPT:
        print(j, costs[j], "\t", j, OPT[j])

    path = []
    for i in range(n, 0, -1):
        path.insert(0, 'NY' if OPT[i]['NY'] < OPT[i]['SF'] else 'SF')
    print()
    print(f"A plan that costs minimal {path} will cost {min(OPT[n]['NY'], OPT[n]['SF'])}")

monthly_costs = {
    1: {'NY': 1, 'SF': 50},
    2: {'NY': 3, 'SF': 20},
    3: {'NY': 20, 'SF': 2},
    4: {'NY': 30, 'SF': 4}
}
M = 10
consulting_company(monthly_costs, M)
