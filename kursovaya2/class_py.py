

class BasicWord:

    def __init__(self, original_word, word_set):
        self.original_word = original_word
        self.word_set = word_set

    def checking_word(self, new_word):
        if new_word in self.word_set:
            return True
        return False

    def number_subwords(self):
        return len(self.word_set)


class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def get_used_words(self):
        """
        Возвращает использованные слова
        """
        return len(self.used_words)

    def add_word(self, word):
        """
        Добавляет слово в список слов
        """
        self.used_words.append(word)

    def check_word_is_new(self, word):
        """
        Проверяет повторение использования слова
        """
        if word not in self.used_words:
            return True
        return False

    def count_used_words(self):
        """
        Возврат кол-ва использованных слов
        """
        return len(self.used_words)