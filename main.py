
menu = []

def add_dish():
    name = input("Назва страви: ")
    try:
        price = float(input("Ціна: "))
    except ValueError:
        print("Помилка! Введіть число.")
        return
    descr = input("Опис: ")
    menu.append({"назва": name, "ціна": price, "опис": descr})
    print(f"Страву {name} додано!")

def show_menu():
    print("\n--- МЕНЮ РЕСТОРАНУ ---")
    if not menu:
        print("Меню порожнє.")
    for dish in menu:
        print(f"{dish['назва']} | {dish['ціна']} грн | {dish['опис']}")

def main():
    while True:
        print("\n1. Додати страву (А)\n4. Показати меню (А)\n0. Вихід")
        choice = input("Оберіть дію: ")
        if choice == '1': add_dish()
        elif choice == '4': show_menu()
        elif choice == '0': break

if __name__ == "__main__":
    main()

#Гравець Г
def total_sum(menu):
    total = sum(dish['price'] for dish in menu)
    print(f"Загальна вартість усіх страв: {total} грн")

def category_sum(menu, category_name):
    total = sum(dish['price'] for dish in menu if dish.get('category') == category_name)
    print(f"Вартість категорії {category_name}: {total} грн")

def sort_menu(menu, reverse_order):
    sorted_list = sorted(menu, key=lambda x: x['price'], reverse=reverse_order)
    for dish in sorted_list:
        print(f"{dish['name']} — {dish['price']} грн")