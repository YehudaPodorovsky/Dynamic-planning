# stressful tasks

def stressful_tasks(l, h):
    n = len(l)
    OPT = [0] * n

    OPT[0] = max(l[0], h[0])
    for i in range(1, n):
        OPT[i] = max(OPT[i - 1] + l[i], OPT[i - 2] + h[i])
    print(OPT)

l = [10, 1, 10, 10]
h = [5, 50, 5, 1]
stressful_tasks(l, h)
