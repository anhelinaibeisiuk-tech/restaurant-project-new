
menu = []


def main():
    while True:
        print("\n--- МЕНЮ РЕСТОРАНУ ---")
        print("1. Додати страву (A)")
        print("2. Редагувати страву (Б)")
        print("3. Видалити страву (В)")
        print("4. Показати список страв (A)")
        print("5. Загальна ціна (Г)")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        if choice == '1':
            add_dish()
        elif choice == '4':
            show_menu()
        elif choice == '0':
            break


def add_dish():

    pass


def show_menu():

    pass


if __name__ == "__main__":
    main()