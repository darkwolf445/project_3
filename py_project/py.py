# put your python code here
# text = input()
# text = text.split()
#
# count = 0
#
# for i in text:
#     if i == 'a' or i == 'an' or i == 'the':
#         count += 1
#
# print(f"Общее количество артиклей: {count}")

text = input().lower().split()

print("Общее количество артиклей: ", text.count('a') + text.count('an') + text.count('the'))