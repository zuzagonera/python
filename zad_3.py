def numberIsEven(number: float) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

result = numberIsEven(66.6)

if(result):
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')