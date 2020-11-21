class Node:
    """
    Класс для передвижения по дереву
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, res):
        # если идем влево, то добавляем 0
        self.left.walk(code, f'{res}0')
        # если идем влево, то добавляем 1
        self.right.walk(code, f'{res}1')


class Leaf:
    """
    Класс 'Лист дерева' для хранения симовла
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def walk(self, code, res):
        # обрабатываем условие, когда 1 символ всего
        if not res:
            code[self.symbol] = '0'
        else:
            code[self.symbol] = res


def get_count_symbols_from_text(text):
    """
    Подсчет сколько встречается каждый символ в тексте
    :param text: текст
    :return: словарь сопоставления букв и их кол-ва в тексте
    """
    res = {}
    for symbol in text:
        if symbol in res.keys():
            res[symbol] += 1
        else:
            res[symbol] = 1
    return res
