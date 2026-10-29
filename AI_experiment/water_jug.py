from collections import deque

def water_jug(a, b, target):
    q = deque([(0, 0)])
    vis = set()

    while q:
        x, y = q.popleft()

        if (x, y) in vis:
            continue

        vis.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Solution found")
            return

        q.extend([
            (a, y),
            (x, b),
            (0, y),
            (x, 0),
            (max(0, x - (b - y)), min(b, x + y)),
            (min(a, x + y), max(0, y - (a - x)))
        ])

    print("No solution")

water_jug(4, 3, 2)