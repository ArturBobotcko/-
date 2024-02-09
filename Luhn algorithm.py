import random

def luhn_alg(num):
    num_copy = str(num)
    num_copy = list(num_copy)
    sum = 0
    for i in range(len(num_copy)):
        # Числа на нечетных позициях умножаем на 2. Примечание: индексы списков начинаются с 0
        if i % 2 == 0:
            number = int(num_copy[i])
            num_copy[i] = str(number * 2)
    for i in range(len(num_copy)):
        # Если число двузначное, вычитаем из него 9
        if len(num_copy[i]) == 2:
            number = int(num_copy[i])
            num_copy[i] = str(number - 9)
        # Считаем сумму цифр
        sum += int(num_copy[i])
    # Если число делится на 10 без остатка, то номер карты верный
    if sum % 10 == 0:
        return 1
    else:
        return 0

def choose_number(num):
    # Перебираем цифры от 0 до 9 и по алгоритму Луна определяем какое из них подохдящее
    for i in range(10):
        new_num = int(str(num) + str(i))
        if luhn_alg(new_num) == 1:
            return new_num

if __name__ == "__main__":
    num = random.randint(100000000000000,999999999999999)
    print(num)
    num = choose_number(num)
    print(num)