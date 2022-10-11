def numbers(numbers):
    for number in range(len(numbers)):
        if numbers[number] % 2 == 0:
            print(numbers[number])


numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
