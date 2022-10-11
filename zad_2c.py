def numbers(number, number1, number2, number3, number4, number5, number6, number7, number8, number9):
    numbers_list = [number, number1, number2, number3, number4, number5, number6, number7, number8, number9]
    for number in numbers_list:
        if number % 2 == 0:
            print(number)


numbers(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
