FILENAME = 'dictionary.txt'


def load_dict_from_file(filename):
    etu = {}
    ute = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split('=')  # ['eng','ukr']
            if len(parts) == 2:
                eng, ukr = parts

                etu[eng] = ukr
                ute[ukr] = eng

    return etu, ute


def save_word(filename, eng, ukr):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{eng}={ukr}\n')


eng_to_ukr, ukr_to_eng = load_dict_from_file(FILENAME)

while True:
    word = input('Enter your word \n')

    if word in ('quit', 'end', 'exit'):
        print('pa pa!')
        break

    if word in eng_to_ukr:
        print(f'Translation: {eng_to_ukr[word]}')
        continue

    if word in ukr_to_eng:
        print(f'Translation: {ukr_to_eng[word]}')
        continue

    print('word not found')

    answer = input('Додати переклад? (y/n):').strip()
    if answer == 'y':
        eng = input('Enter english word: ')
        ukr = input('Enter ukrainian translation : ')

        eng_to_ukr[eng] = ukr
        ukr_to_eng[ukr] = eng

        save_word('dictionary.txt', eng, ukr)
        print('Word saved.')
