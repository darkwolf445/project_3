from utils import list, statistics

for i in list:
    print(i)
    i.build_question()
    user_response = input() # Ввод пользователя

    if i.is_correct(user_response):
        i.build_positive_feedback()
    else:
        i.build_negative_feedback()

statistics(list)  # Функция статистики
