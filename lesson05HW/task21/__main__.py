# Имитация игры в блек-джек. Ранее в этой главе вы рассмотрели программу
# card_dealer.py, которая имитирует раздачу игральных карт из колоды на руки. Усовершенствуйте программу так,
# чтобы она имитировала упрощенную версию игры в блекджек между двумя виртуальными игроками.
# Карты имеют приведенные ниже значения.
# • Числовым картам присвоено значение, которое на них напечатано. Например,
# значение двойки пик равняется 2, значение пятерки бубей равняется 5.
# • Валетам, дамам и королям присвоено значение 1 О.
# • Тузам присвоено значение 1 или 11 в зависимости от выбора игрока.
# Программа должна раздавать карты каждому игроку до тех пор, пока карты на руках
# у одного из игроков не превысят 21 очко. Когда это происходит, другой игрок становится победителем.
# (Может возникнуть ситуация, когда карты на руках у обоих игроков
# превысят 21 очко; в этом случае победителя нет.) Программа должна повторяться до тех
# пор, пока все карты не будут розданы.
# Если игроку сдан туз, то программа должна определить значение этой карты согласно
# следующему правилу: туз равняется 11 очкам, если в результате добавления этой карты
# стоимость комбинации карт на руках у игрока не превысит 21 очко. В противном случае
# туз равняется 1 очку.

import random


def main():
    deck = create_deck()
    deal_cards(deck)


def create_deck():
    deck = {
        'Туз пик': 1, '2 пик': 2, '3 пик': 3,
        '4 пик': 4, '5 пик': 5, '6 пик': 6,
        '7 пик': 7, '8 пик': 8, '9 пик': 9,
        '10 пик ': 10, 'Валет пик': 10,
        'Дама пик': 10, 'Король пик': 10,
        'Туз червей': 1, '2 червей': 2, '3 червей': 3,
        '4 червей': 4, '5 червей': 5, '6 червей': 6,
        '7 червей': 7, '8 червей': 8, '9 червей': 9,
        '10 червей': 10, 'Валет червей': 10,
        'Дама червей': 10, 'Король червей': 10,
        'Туз треф': 1, '2 треф ': 2, '3 треф': 3,
        '4 треф': 4, '5 треф': 5, '6 треф': 6,
        '7 треф': 7, '8 треф': 8, '9 треф': 9,
        '10 треф': 10, 'Валет треф': 10,
        'Дама треф ': 10, 'Король треф': 10,
        'Туз бубей': 1, '2 бубей': 2, '3 бубей': 3,
        '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
        '7 бубей': 7, '8 бубей': 8, '9 бубей': 9,
        '10 бубей': 10, 'Валет бубей': 10,
        'Дама бубей': 10, 'Король бубей': 10
    }
    return deck


def deal_cards(deck):
    player1 = 0
    player2 = 0

    while len(deck) > 0:

        key_list = list(deck.keys())

        if player1 < 21:
            value1 = deck.pop(random.choice(key_list))
            player1 += value1
            if value1 == 1 and player1 + 10 < 21:
                player1 += 10
        if player2 < 21:
            value2 = deck.pop(random.choice(key_list))
            player2 += value2
            if value2 == 1 and player2 + 10 < 21:
                player2 += 10

        print(player1, player2)

        if player1 > 21 and player2 > 21:
            print('Draw')
            break
        if player1 > 21:
            print('Player 2 wins')
            break
        if player2 > 21:
            print('Player 1 wins')
            break


main()
