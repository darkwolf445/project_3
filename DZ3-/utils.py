import json
from question import Question

list = []


def load_json():
    """
    Чтение данных из JSON файла
    """
    with open("question.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def generations():
    """
    Запись в список
    """
    for i in load_json():
        abc = Question(i["q"], i["d"], i["a"])
        list.append(abc)

generations()

def statistics(list: list):
    """
    Статистика
    """
    correct_answer = 0 # Счётчик верных ответов
    points = 0 # Счётчик баллов
    for i in list:
        if i.is_question_asked == True:
            correct_answer += 1
            points += i.get_points()

    print("\nВот и всё!")
    print(f"Отвечено {correct_answer} вопроса из {len(list)}")
    print(f"Набрано баллов: {points}")

