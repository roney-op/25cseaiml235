from itertools import permutations

def tsp(g, s):
    n = len(g)
    p = permutations([i for i in range(n) if i != s])
    ans = float('inf')
    path = []

    for i in p:
        c = [s] + list(i) + [s]
        d = sum(g[c[j]][c[j+1]] for j in range(n))
        if d < ans:
            ans = d
            path = c

    print("Path:", path)
    print("Minimum Cost:", ans)

g = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(g, 0)