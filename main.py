from encoder import encode
from decoder import decode


def get_info_about_encoded_text(text, codes):
    """
    Получение информации по закодированному тексту
    """
    # Выводим сопоставления какие символы кодировались какими значениями
    for symbol in codes.keys():
        print(f'{symbol}: {codes[symbol]}')
    return ''.join(codes[symbol] for symbol in text)


if __name__ == '__main__':
    text = input('Введите текст, который хотите закодировать: ')
    codes = encode(text)
    encoded_text = get_info_about_encoded_text(text=text, codes=codes)

    print(f'Закодированный текст: {encoded_text}')
    print(f'Раскодированный текст: {decode(encoded_text, codes)}')
