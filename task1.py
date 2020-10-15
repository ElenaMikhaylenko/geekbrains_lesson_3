dividend = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))



def my_func(dividend, divisor):
    try:
        return dividend/divisor

    except ZeroDivisionError:
        print("На ноль делить нельзя!")

print(my_func(dividend, divisor))

