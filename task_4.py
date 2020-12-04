# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


user_input = int(input("Введите целое положительное число: "))
max_number = user_input % 10
while user_input >= 1:
    user_input //= 10
    if user_input % 10 > max_number:
        max_number = user_input % 10
    if user_input > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_number)
        break


