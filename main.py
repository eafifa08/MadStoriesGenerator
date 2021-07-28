# Mad Stories Generator by Meshkov Sergey
# Генератор забавных историй(на английском проще - нет стольких окончаний)

def generate_first_story():
    name = input('Введите имя:')
    verb = input('Введите глагол(инфинитив - плыть, бежать и т.д.):')
    place = input('Введите место:')
    adverb = input('Введите наречие:')
    second_name = input('Введите второе имя:')
    time = input('Введите время(11:47):')
    thing = input('Введите вещь:')
    result = f'Однажды {name} захотел немного {verb} c {second_name}.' + \
             f'Они встретились в {place} в {time}, взяли {thing} и начали ' +\
             f'{adverb} {verb}'
    return result


def go():
    print(generate_first_story())


if __name__ == '__main__':
    go()