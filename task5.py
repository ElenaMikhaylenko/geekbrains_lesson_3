s = 0
need_to_stop = False
while True:
    number = input("Введите строку чисел: ")
    for el in number.split():
        if el == "end":
            need_to_stop = True
            break
        s += int(el)
    print(s)
    if need_to_stop:
        break
