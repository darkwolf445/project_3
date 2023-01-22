import requests
import json
from class_py import BasicWord
from random import randint


def load_random_word():
    """""
    Функция принимающая json файл с внешнего ресурса.
    1. Загадываем рандомное число, зависит от - количества слов в списке
    2. Получаем original_word и word_set из списка по ранд. числу
    """""
    response = requests.get("https://www.jsonkeeper.com/b/8JFK")

    response_json = json.loads(response.text)
    random_number = randint(0, len(response_json) - 1)
    original_word = response_json[random_number]["word"]
    word_set = response_json[random_number]["subwords"]
    return BasicWord(original_word, word_set)
