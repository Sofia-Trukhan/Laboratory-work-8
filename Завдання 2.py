text = input("Введіть текст: ")
group = input("Введіть номер групи: ")

words = text.split()

for word in words:
    if word.count(group) >= 2:
        print(word)
