import heapq

from utils import Leaf, Node, get_count_symbols_from_text


def encode(text):
    """
    Кодирование текста

    :param text (str): текст, который нужно закодировать
    :return (dict): словарь {символ: код}
    """
    # инициализируем очередь
    queue = []

    # подсчитываем сколько встречается каждый символ в тексте
    counter = get_count_symbols_from_text(text)
    i = 0
    # Создаем очередь
    for ch, freq in counter.items():
        queue.append((
            freq,  # частота символа
            i,  # счетчик
            Leaf(ch)  # символ
        ))
        i += 1
    heapq.heapify(queue)
    #  счетчик равен длине нашей очереди
    counter = i
    # запускаем цикл пока в очереди есть больше 1 элемента
    while len(queue) > 1:
        # получаем элемент с минимальной частотой (слева)
        freq_1, counter_1, left = heapq.heappop(queue)
        # получаем элемент с максимальной частотой (справа)
        freq_2, counter_2, right = heapq.heappop(queue)
        # добавляем в очередь элемент, у которого частота = сумма частот полученных раннее элементов
        heapq.heappush(
            queue,
            (freq_1 + freq_2, counter, Node(left, right))
        )
        counter += 1
    # словарь кодов символов
    codes = {}
    if queue:
        # вытаскимваем из нашей очереди корень дерева
        [(_, _, root)] = queue
        # начинаем обход дерева с самого начала
        root.walk(codes, '')
    return codes
