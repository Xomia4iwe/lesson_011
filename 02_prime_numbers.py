# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.n:
            for number in range(2, self.n + 1):
                for prime in self.prime_numbers:
                    if number % prime == 0:
                        break
                else:
                    self.prime_numbers.append(number)
                    return number
        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

#
# def prime_numbers_generator(n):
#     i = 0
#     prime_numbers = []
#     while True:
#         i += 1
#         if i >= n:
#             break
#         else:
#             number = 1 + i
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 prime_numbers.append(number)
#                 yield number
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True

def lucky_number(number):
    str_number = str(number)
    if len(str_number) % 2 == 0:
        left_side_numbers = str_number[:len(str_number) // 2]
        right_side_numbers = str_number[len(str_number) // 2:]
    else:
        left_side_numbers = str_number[:len(str_number) // 2]
        right_side_numbers = str_number[len(str_number) // 2 + 1:]
    return sum(list(map(int, left_side_numbers))) == sum(list(map(int, right_side_numbers)))



# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

def palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]


def prime_numbers_generator(n, func):
    i = 0
    prime_numbers = []
    while True:
        i += 1
        if i >= n:
            break
        else:
            number = 1 + i
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
                if func(number):
                    yield number







for number in prime_numbers_generator(n=10000, func=lucky_number):
    print(number)


