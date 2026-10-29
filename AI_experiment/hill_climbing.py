# Objective function to maximize

def objective_fun(x):
    return -(x ** 2) + 8


# Hill climbing function

def hill_climb(start, step_size, max_iterations, min_step=1e-6):
    current = float(start)
    current_val = objective_fun(current)
    best_pos = current
    best_val = current_val

    for _ in range(max_iterations):
        left = current - step_size
        right = current + step_size

        left_value = objective_fun(left)
        right_value = objective_fun(right)

        if left_value > current_val and left_value >= right_value:
            current = left
            current_val = left_value
        elif right_value > current_val and right_value > left_value:
            current = right
            current_val = right_value
        else:
            if step_size <= min_step:
                break
            step_size /= 2.0
            continue

        if current_val > best_val:
            best_pos = current
            best_val = current_val

    return best_pos, best_val



def hill_climbimg(start, step_size, max_iterations, min_step=1e-6):
    return hill_climb(start, step_size, max_iterations, min_step)


# Main program

start = float(input("enter the starting value:"))
step_size = float(input("enter the step size:"))
max_iterations = int(input("enter the maximum number of iterations:"))

best_pos, best_val = hill_climbimg(start, step_size, max_iterations)
print("\nBest position =", best_pos)
print("maximum value =", best_val)