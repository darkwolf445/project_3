
def plus(a, b):
    return a + b

new_list = []

while True:
    num = input()
    if num == 'стоп':
        break
    else:
        new_list.append(num)

print(new_list[1])