# Среднее количество шагов. Браслет для занятий спортом - это носимое устройство,
# которое отслеживает вашу физическую активность, количество сожженных калорий,
# сердечный ритм, модели сна и т. д. Одним из самых распространенных видов физический активности,
# который отслеживает большинство таких устройств, является количество шагов, которые вы делаете каждый день.
# Среди исходного кода главы 6, а также в подпапке data "Решений задач по программированию" соответствующей главы,
# вы найдете файл steps.txt. Файл steps.txt содержит количество шагов, которые человек делал каждый день в течение года.
# В файле имеется 365 строк, и каждая строка содержит количество шагов, сделанных в течение дня.
# (Первая строка- это число шагов, сделанных 1-го января, вторая строка- число шагов,
# сделанных 2 января и т. д.) Напишите программу, которая читает файл и затем выводит
# среднее количество шагов, сделанных в течение каждого месяца. (Данные были записаны в год, который не был високосным,
# и поэтому февраль имеет 28 дней.)

all_count = 0
current_day = 1
current_month = 'января'

with open('steps.txt', 'r', encoding='utf8') as steps_file:
    for line in steps_file:
        if all_count == 31:
            current_day = 1
            current_month = 'февраля'
        elif all_count == 59:
            current_day = 1
            current_month = 'марта'
        elif all_count == 90:
            current_day = 1
            current_month = 'апреля'
        elif all_count == 120:
            current_day = 1
            current_month = 'мая'
        elif all_count == 151:
            current_day = 1
            current_month = 'июня'
        elif all_count == 181:
            current_day = 1
            current_month = 'июля'
        elif all_count == 212:
            current_day = 1
            current_month = 'августа'
        elif all_count == 243:
            current_day = 1
            current_month = 'сентября'
        elif all_count == 273:
            current_day = 1
            current_month = 'октября'
        elif all_count == 304:
            current_day = 1
            current_month = 'ноября'
        elif all_count == 334:
            current_day = 1
            current_month = 'декабря'

        print(f'{current_day} {current_month}: {line.rstrip()} шагов')
        current_day += 1
        all_count += 1
