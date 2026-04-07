words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

long_words = []
for word in unique_words:
    if len(word) > 4:
        long_words.append(word)

upper_words = []
for word in long_words:
    upper_words.append(word.upper())

if "BANANA" in upper_words:
    print("Так, BANANA є у списку!")

print(f"Унікальні слова: {unique_words}")
print(f"Слова у верхньому регістрі (>4 символів): {upper_words}")
