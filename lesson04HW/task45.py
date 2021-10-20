# В приведенной ниже функции применен цикл. Перепишите ее как рекурсивную функцию,
# которая выполняет ту же самую операцию.
def traffic_sign(n):
    while n > 0:
        print('Не парковаться')
        n = n - 1


def traffic_sign_req(n):
    if n > 0:
        print('Не парковаться')
        traffic_sign_req(n - 1)


# traffic_sign(3)
traffic_sign_req(3)