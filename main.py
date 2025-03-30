def main():
    # Ввод списка от пользователя
    input_list = input("Введите элементы списка через пробел: ").split()

    processed_list = []
    all_numbers = True

    # Преобразование элементов и проверка на числа
    for item in input_list:
        try:
            num = float(item)
            processed_list.append(num)
        except ValueError:
            processed_list.append(item)
            all_numbers = False

    # 1. Проверка наличия хотя бы одного положительного числа
    has_positive = any(isinstance(x, (int, float)) and x > 0 for x in processed_list)
    print(f"1. Список содержит хотя бы одно положительное число: {has_positive}")

    # 2. Проверка, что все элементы - числа
    print(f"2. Все элементы списка являются числами: {all_numbers}")

    # 3. Сортировка списка
    try:
        sorted_list = sorted(processed_list)
        print(f"3. Отсортированный список: {sorted_list}")
    except TypeError:
        print("3. Невозможно отсортировать список, так как элементы разных типов")


if __name__ == "__main__":
    main()