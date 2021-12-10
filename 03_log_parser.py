# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def read_file(file):
    with open(file, 'r') as file:
        for line in file:
            yield line


def log_generator(file):
    stat = {}
    file_data = read_file(file)
    for line in file_data:
        event_statistic = line[1:17]
        if 'NOK' in line:
            if event_statistic in stat:
                stat[event_statistic] += 1
            else:
                stat[event_statistic] = 1
    for key, value in stat.items():
        yield key, value


grouped_events = log_generator(file='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
