import random as rn

while slct := int(input("\nОберіть дію:")):

    match slct:
        case 1:
            N = int(input("Введіть кількість елементів : "))
            some_list = [int(item) for item in input("Введіть елементи списку : ").split()][:N]
            max_number = max(some_list)

            print("\nTask 1")
            print(f"Максимальний елемент списку: {max_number}\n"
                  f"Реверсивний список: {some_list[::-1]}\n")

        case 2:
            N = int(input("Введіть кількість елементів : "))
            some_list = [int(item) for item in input("Введіть елементи списку : ").split()][:N]
            positive_list = [i for i in some_list if i >= 0]
            negative_list = [i for i in some_list if i < 0]

            print("\nTask 2")
            print(f"Список додатніх: {positive_list}\n"
                  f"Список від'ємних: {negative_list}\n")

        case 3:
            some_list = list(map(lambda x: rn.randint(-20, 20), range(20)))
            sum_odd = sum(some_list[::2])

            print("\nTask 3")
            print(f"Сумма непарних елеменів: {sum_odd}")
            print(f"Наш список: {some_list}")

        case 4:
            some_list = list(map(lambda x: rn.randint(-100, 100), range(30)))
            max_number = max(some_list)
            odd_list = [i for i in some_list if i % 2 != 0]

            print("\nTask 4")
            print(f"Список елементів:{some_list}"
                  f"\nМаксимальний елемент - {max_number}"
                  f"\nІндекс максимального елемента - {some_list.index(max_number)}")

            if len(odd_list):
                print(f"Список непарних : {odd_list}")
            else:
                print("Списку не існує")

            some_list.sort(reverse=True)

            print(f"Список у порядку зменшення елементів: {some_list}")

        case 5:
            some_list = list(map(lambda x: rn.randint(-100, 100), range(30)))

            print("\nTask 5")
            print(f"Згенерований список: {some_list}"
                  f"\nВід'ємні елементи що стоять поруч")

            for i in range(len(some_list)-1):
                print(some_list[i], some_list[i+1]) if some_list[i] < 0 and some_list[i+1] < 0 else None

        case 6:
            some_list = [int(item) for item in input("Введіть елементи списку : ").split()][:10]
            square_list = []

            for i in some_list:
                if i < max(some_list):
                    square_list.append(i**2)

            square_list.sort(reverse=True)

            print(f"\nTask 6")
            print(f"Вихідний масив: {square_list}")
            print(f"Максимальний елемент: {max(some_list)}")

        case 7:
            some_list = list(map(lambda x: rn.randint(-100, 99) + rn.random().__round__(2), range(30)))
            help_list = [abs(i) for i in some_list]
            some_list.sort()

            print("\nTask 7")
            print(f"Мінімальний за модулем елемент: {min(help_list)}"
                  f"\nВідсортований список: {some_list}")

        case 8:
            # розіб'ємо список за допомогою генератору
            def gen(list_type, size_slice):
                for i in range(0, len(list_type), size_slice):
                    yield list_type[i:i + size_slice]

            # Функція ключ для сортування
            def abs_sum(list_type):
                return sum([abs(i) for i in list_type])

            some_list = list(map(lambda x: rn.randint(-100, 99) + rn.random().__round__(2), range(30)))
            slice_list = list(gen(some_list, 3))
            slice_list.sort(key=abs_sum)

            print(f"Згенерований список: {some_list}")
            print(f"Відсортований та нарізаний список: {slice_list}")
