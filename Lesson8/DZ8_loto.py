import random


class LotoCard:
    def __init__(self, player):
        self.player = player
        self.card = []
        card_numbers = random.sample(range(1, 91), k=15)  # Генерация 15 случайных чисел для карточки
        print(card_numbers)
        for i in range(3):  # Цикл по строкам карточки
            row = ['  '] * 9  # Создается пустая строка
            # Следующие пять чисел сортируются по возрастанию и записываются в случайные ячейки строки:
            for m, el in zip(sorted(random.sample(range(9), k=5)), sorted(card_numbers[i * 5:i * 5 + 5])):
                row[m] = el
            self.card.append(row)
        self.quant = 15  # Количество оставшихся в карточке чисел

    def __str__(self):
        return '\n'.join(' '.join(str(el).ljust(2, ' ') for el in row) for row in self.card) + \
               '\n' + '_' * 26

    def del_num(self, num):  # Функция для удаления числа из карточки
        for row in self.card:
            if num in row:
                row[row.index(num)] = '  '
                self.quant -= 1
                return self.quant
        # Если число не найдено, то возвращается -1. В остальных случаях возвращается количество чисел в карточке.
        return -1


class LotoGame:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

    def start(self):
        kegs = [el for el in range(1, 91)]
        num_kegs = 90
        while True:
            keg = random.choice(kegs)
            num_kegs -= 1
            kegs.remove(keg)
            # Вывод нового бочонка и текущих карточек
            print(f"\nНовый бочонок: {keg} (осталось {num_kegs})")
            print('-' * 5 + ' Ваша карточка: ' + '-' * 5)
            print(self.human_player)
            print('-' * 2 + ' Карточка компьютера: ' + '-' * 2)
            print(self.computer_player)
            while True:
                step = input('Зачеркнуть число? (y / n) ')
                if step in ('y', 'n'):
                    break
            res_computer = computer_player.del_num(keg)
            res_human = human_player.del_num(keg)
            if step == 'y' and res_human == -1 or step == 'n' and res_human != -1:
                print('Вы проиграли!')
                break
            if res_computer == 0 and res_human == 0:
                print('Ничья!')
                break
            elif res_computer == 0:
                print('Компьютер выиграл!')
                break
            elif res_human == 0:
                print('Вы выиграли!')
                break


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
