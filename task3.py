def my_func(p_1=6, p_2=8, p_3 = 9):
    return sum((sorted([p_1, p_2, p_3], reverse=True) [:2]))
print(my_func())
