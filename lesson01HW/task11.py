# Очки книжного клуба. Прозорливая книготорговая фирма владеет книжным клубом,
# который присуждает своим клиентам очки, основываясь на количестве книг, приобре-
# тенных ими ежемесячно. Очки присуждаются следующим образом:
# • если клиент приобретает О книг, то зарабатывает О очков;
# • если клиент приобретает 2 книги, то зарабатывает 5 очков;
# • если клиент приобретает 4 книги, то зарабатывает 15 очков;
# • если клиент приобретает 6 книг, то зарабатывает 30 очков;
# • если клиент приобретает 8 книг или больше, то зарабатывает 60 очков.
# Напишите программу, которая просит пользователя ввести количество книг, приобре-
# тенных им в этом месяце, и затем выводит присужденное количество очков.

amount = int(input('Введите количество книг\n'))

if amount < 2:
    print('0 очков')
elif amount < 4:
    print('5 очков')
elif amount < 6:
    print('15 очков')
elif amount < 8:
    print('30 очков')
elif amount >= 8:
    print('60 очков')
