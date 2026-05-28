from utils_homework_12 import average, foo_check, foo_vowels

res_avg = average(10, 5, 8)
print(f"Середнє значення: {res_avg}")

res_bool1 = foo_check(12)
res_bool2 = foo_check(8)
print(f"Число 12 парне і > 10?: {res_bool1}")
print(f"Число 8 парне і > 10?: {res_bool2}")

res_vowels = foo_vowels("Beautiful Apple")
print(f"Кількість голосних у тексті: {res_vowels}")