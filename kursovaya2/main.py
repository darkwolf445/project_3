from class_py import Player
from utils import load_random_word

user_name = input("Ввведите имя игрока\n")

player_name = Player(user_name)
load_random_word()

original_word = load_random_word()
subword_count = original_word.number_subwords()

print(f"Привет, {player_name.user_name}!")
print(f'Составьте {subword_count} слов из слова {original_word.original_word.upper()}')
print("Слова должны быть не короче 3 букв")
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print("Поехали, ваше первое слово?")

while player_name.count_used_words() < subword_count:

    user_input = input().lower()
    if user_input == "stop" or user_input == "стоп":
        break

    if len(user_input) < 3:
        print("Слово какое-то короткое, уходи")
        continue

    if original_word.checking_word(user_input) and player_name.check_word_is_new(user_input):
        print("Такое слово есть!")
        player_name.add_word(user_input)
    else:
        print("Такого слова нет или оно было использовано!")

print(f"Игра завершена, вы угадали {player_name.get_used_words()} слов!")