
class Question:

    def __init__(self, text, difficult, correct_answer, is_question_asked=False, user_response=None):
        self.text = text
        self.difficult = difficult
        self.correct_answer = correct_answer
        self.is_question_asked = is_question_asked
        self.user_response = user_response


    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        points = int(self.difficult) * 10
        return points

    def is_correct(self, user_response):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if self.correct_answer == user_response:
            self.is_question_asked = True
            return True

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        print(f"Вопрос {self.text}\nСложность {self.difficult}/5")

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        print(f"Ответ верный, получено {Question.get_points(self)} баллов")

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        print(f"Ответ неверный, верный ответ {self.correct_answer}")
