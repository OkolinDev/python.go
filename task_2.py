# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_input = int(input())
sec_in_day = 86400
min = 60
hour = 3600
hh = user_input // hour
mm = (user_input % hour) // min
sec = (user_input % hour) % min
print(f"{hh:d}:{mm:02d}:{sec:02d}")