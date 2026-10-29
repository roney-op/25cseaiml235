import math


def alpha_beta(depth, node, height, maximizing_player, values, alpha, beta):

    # If we reach the leaf node
    if depth == height:
        return values[node]

    # MAX player
    if maximizing_player:

        best = -math.inf

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                height,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best

    # MIN player
    else:

        best = math.inf

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                height,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best


# Main program

height = int(input("Enter the height of the tree: "))

n = 2 ** height

values = []

print("Enter the values of the leaf nodes:")

for i in range(n):
    value = int(input("Enter value " + str(i + 1) + ": "))
    values.append(value)

alpha = -math.inf
beta = math.inf

result = alpha_beta(
    0,
    0,
    height,
    True,
    values,
    alpha,
    beta
)

print("Optimal value:", result)