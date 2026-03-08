text = input("Введіть речення: ")

text = text.replace(",", "").replace(".", "")
words = text.split()

min_count = len(words)

for word in set(words):
    count = words.count(word)
    if count < min_count:
        min_count = count

print("Слова, які зустрічаються найменше разів:")

for word in set(words):
    if words.count(word) == min_count:
        print(word)
