
list_of_numbers = [8, 6, 10]

choice = int(input('# - '))

if choice == 1:
    minimum = list_of_numbers[0]
    for number in list_of_numbers:
        if number < minimum:
            minimum = number
    print(f'Minimum-{minimum}')
elif choice == 2:
    maximum = list_of_numbers[0]
    for number in list_of_numbers:
        if number > maximum:
            maximum = number
    print(f'Maximum-{maximum}')
elif choice == 3:
    odd_numbers = []
    for number in list_of_numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    print(f'Odd-numbers: {odd_numbers}')
elif choice == 4:
    even_numbers = []
    for number in list_of_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(f'Even-numbers: {even_numbers}')
elif choice == 5:
    sum_of_numbers = 0
    for number in list_of_numbers:
        sum_of_numbers += number
    print(f'Sum-of-numbers: {sum_of_numbers}')
elif choice == 6:
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]

    print(f'Sorted-list [ascending]: {list_of_numbers}')
elif choice == 7:
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_numbers[j + 1] > list_of_numbers[j]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
    print(f'Sorted-list [descending]: {list_of_numbers}')
else:
    print('Invalid choice!')