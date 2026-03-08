text = input("Введіть рядок: ")
position = text.rfind('?')# повертає індекс останнього елемента

if position != -1:
    print("Позиція останнього зкаку питання: ", position)
else:
    print("Знаку питання немає у цьому рядку")
    

