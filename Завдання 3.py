text = input("Введіть рядок: ")

words = text.split()

for word in words:
    last = word[-1] # остання літера
    new_word = word.replace(last, "")
    print(new_word)
