num = input()
num = num.split()
new_list = []

for i in num:
    new_list.append(int(i))

new_list.reverse()
print(new_list)