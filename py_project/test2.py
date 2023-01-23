s = 'Python is the most powerful language'
words = s.split()
print(words)

numbers = [8, 9, 10, 11]

numbers[1] = 17

print(numbers)

numbers.extend([4, 5, 6])

print(numbers)

numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers = numbers * 2
numbers[3] = 25
print(numbers)