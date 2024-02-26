import csv

with (open('game.csv', encoding='utf8') as file):
    reader = list(csv.reader(file, delimiter='$'))[1:]

    for row in reader:

        print(
            f'У персонажа {row[1]} в игре {row[0]} нашлась ошибка с кодом: {row[2]}. Дата фиксации: {row[3]}')
        if row[2] == '55':
            nameError = 'Done'
            date = '0000-00-00'

with open('game_new.csv', encoding='utf8') as file:
    writer = csv.writer(file, delimiter='$')
    writer.writerow('GameName', 'characters', 'nameError', 'date')
    writer.writerows(reader)
