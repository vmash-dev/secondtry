text = "Програмування на мові Python це дуже цікаво та корисно"

words = text.split()

shortest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"Список слів: {words}")
print(f"Найкоротше слово: '{shortest_word}' (довжина: {len(shortest_word)})")
print(f"Найдовше слово: '{longest_word}' (довжина: {len(longest_word)})")