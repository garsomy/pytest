#pytest
#1
# def num(x):
#     try:
#         if x < 0:
#             return ('yes')
#         else:
#             return ('no')
#     except TypeError:
#         return 'TypeError'
#     except ValueError:
#         return 'ValueError'
#    except(IndexError):
#        return 'Список пуст'
#
# num(10)

#2
# def num(x):
#     try:
#         if x % 2 == 0:
#             return ('yes')
#         else:
#             return ('no')
#     except TypeError:
#         return ('TypeError')
#     except ValueError:
#         return ('ValueError')
#     except ZeroDivisionError:
#         return 'на 0 нельзя делить'
#     except(IndexError):
#         return 'Список пуст'

# num(53)

#3
# def num(nums):
#     try:
#         quantity = len(str(nums))
#         return quantity
#     except ValueError:
#         return 'Введено некорректное значение'
#     except(IndexError):
#         return 'Список пуст'
#
# num(764286)

#4
# def num(nums):
#     try:
#         return sum(nums)
#     except ValueError:
#         return 'Введено некорректное значение'
#     except ArithmeticError:
#         return 'Арифметическая ошибка'
#     except(IndexError):
#         return 'Список пуст'
#
# num([1, 2, 3, 4, 5, 6])

#5
# def num(nums):
#     try:
#         numbs = [int(x) for x in nums.split(',')]
#         summ = sum(numbs)
#         return summ
#     except ValueError:
#         return 'Введено некорректное значение.'
#     except(IndexError):
#         return 'Список пуст'
#
# nums = '12,34,56'


# Unittest
# 1
# def num(date):
#     try:
#         day, month, year = date.split('-')
#         return tuple((year, month, day))
#     except ValueError:
#         return 'Некорректный формат даты.'
#
# num('2025-12-31')

# 2
# try:
#     a = 0
#     while list != 0:
#         list = int(input('Введите числа и 0 для завершения ввода: '))
#         a += list
# except (ValueError, Exception):
#     print('Не корректно введены данные. Ошибка:', Exception)
# except(IndexError):
#     print('Список пуст')
#
# print('Работа завершена. Сумма введных чисел равна: ', a)

# 3
# def num(nums):
#     try:
#         half = len(nums) // 2
#         first_half = nums[:half]
#         second_half = nums[half:]
#
#         sum_first = sum(first_half)
#         sum_second = sum(second_half)
#
#         return sum_first / sum_second
#
#     except ZeroDivisionError:
#         return 'Ошибка: деление на ноль'
#     except IndexError:
#         return 'Ошибка индекса: ', IndexError
#
#
# print(num([1,6,3,86,2,7,24,7,4]))

#4
# def num(nums, nums2):
#     try:
#         nums.update(nums2)
#         return nums
#     except ValueError:
#         return 'Введено некорректное значение.'
#     except(IndexError):
#         return 'Список пуст'
#
#
# print(num(nums = {'a': 1, 'b': 2}, nums2 = {'c': 8, 'd': 4}))

#5.1
# def num(nums):
#     try:
#         sum = 0
#
#         for key1 in nums:
#             for key2 in nums[key1]:
#                 sum += nums[key1][key2]
#
#         return sum
#
#     except:
#         return 'Ошибка: неправильная структура словаря'
#
# nums = {
# 1: {
# 1: 1,
# 2: 1,
# 3: 1,
# },
# 2: {
# 1: 5,
# 2: 1,
# 3: 61,
# },
# 3: {
# 1: 1,
# 2: 14,
# 3: 1,
# },
# }
#
# res = num(nums)
# print(res)

#5.2
# def num(nums):
#     try:
#         if len(nums) == 0:
#             raise ValueError('Список пустой')
#
#         max = nums[0]
#         min = nums[0]
#
#         for num in nums:
#             if num > max:
#                 max = num
#
#         if num < min:
#             min = num
#
#         res = {'max': max, 'min': min}
#
#         return res
#
#     except ValueError as ve:
#         return 'Ошибка: ', ve
#
#
# nums = [1, 337, 5, 73, 9, 4]
# print(num(nums))

#6
# def replace(nums):
#     res = []

#     for num in nums:
#         try:
#             num = int(num)
#             divisors = []

#             for i in range(1, num + 1):

#                 if num % i == 0:
#                     divisors.append(i)
#                     res.append(divisors)

#         except ValueError as ve:
#             return 'Ошибка: ', ve
#         except IndexError as ie:
#             return 'Ошибка: ', ie
#     return res
#
#
# nums = [10, 15, 20]
# res = replace(nums)
# print(res)

#7
# import random
#
# def list(N, start, end):
#     res = []
#     try:
#         start = int(start)
#         end = int(end)
#
#         if start > end:
#             raise ValueError('Ошибка: Начало больше конца', ValueError)
#         elif N > (end - start + 1):
#             raise ValueError('Ошибка: Нарушен диапозон числа N', ValueError)
#         elif N <= 0 or start < 0 or end < 0:
#             raise ValueError('Ошибка: Начало и конец должны быть положительными и целыми числами.', ValueError)
#         else:
#             for i in range(N):
#                 num = random.randint(start, end)
#
#                 if res and res[-1] == num:
#
#                     while res[-1] == num:
#                         num = random.randint(start, end)
#                         res.append(num)
#                         return res
#     except ValueError as ve:
#         return ve
#
# N = 10
# start = 1
# end = 10
# res = list(N, start, end)
# print(res)

#8
# import random
#
# def color():
#     colors = ['зеленый', 'оранжевый', 'красный', 'синий', 'желтый']
#     random_c = random.choice(colors)
#     return random_c
#
# random_c = color()
# print('Цвет:', random_c)

#9
#Нужно скачать pyphen: pip install pyphen
# import pyphen
#
# def slog(word):
#     s = pyphen.Pyphen(lang='ru')
#     list_s = s.inserted(word).split('-')
#     return list_s
#
# word = input('Введите слово: ')
# print('Все слоги:', slog(word))

#10
# import random
#
# def shuffle(list):
#     random.shuffle(list)
#     return list
#
# list_s = [1, 2, 3, 4, 5]
# shuffled_l = shuffle(list_s)
# print('Рандомный список: ', shuffled_l)