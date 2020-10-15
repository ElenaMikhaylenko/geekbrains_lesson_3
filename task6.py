def int_func(text="nice авп ъghj jапро hjjпаро вапрghgh cool"):
    words = text.split(maxsplit=1)
    if len(words) > 1:
        return words[0].title() + " " + int_func(words[1])
    return words[0].title()
print(int_func())