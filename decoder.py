def decode(encoded_text, codes):
    """
    Декодирование текста

    :param encoded: encoded_text
    :param codes: коды символов
    :return: декодированный текст
    """
    res = []
    encoded_symbols = ''
    # идем по всем символам
    for symbol in encoded_text:
        # добавляем текущий символ к формируемой строке
        encoded_symbols += symbol
        # идем по всем кодам
        for code in codes:
            # если закодированный символ есть в списке наших кодов
            if codes.get(code) == encoded_symbols:
                # добавляем значение раскодированного символа к списку раскодированной строки
                res.append(code)
                encoded_symbols = ''
                break
    return ''.join(res)
