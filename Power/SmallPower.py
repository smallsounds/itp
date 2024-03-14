def get_power(x, n):
    return x ** n

def print_graph(n):
    for i in range(-8, 9):
        x = i
        y = get_power(x, 2)
        if y > 0:
            print('*' * (n * y))
        elif y == 0:
            print('' * n)
print_graph(1)