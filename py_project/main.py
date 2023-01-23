from test import plus

for i in range(1, 10):
    if i >= 9:
        print(i)
    else:
        print(i, end=', ')

a = 5
b = 3

print(plus(a, b))