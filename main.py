menu = [
    {
        "назва": "Борщ", 
        "ціна": 120.0, 
        "опис": "Традиційний український борщ з яловичиною та сметаною"
    },
    {
        "назва": "Вареники", 
        "ціна": 95.0, 
        "опис": "З картоплею та смаженою цибулею"
    },
    {
        "назва": "Узвар", 
        "ціна": 40.0, 
        "опис": "Напій із сухофруктів"
    }
]

def add_dish():
    """Додавання нової страви (Завдання А)"""
    print("\n--- Додати нову страву ---")
    name = input("Назва: ")
    try:
        price = float(input("Ціна: "))
        
        if price < 0:
            print("Помилка! Ціна не може бути від'ємною.")
            return
    except ValueError:
        print("Помилка! Введіть число.")
        return
    descr = input("Опис: ")
    
    menu.append({"назва": name, "ціна": price, "опис": descr})
    print(f"Страву '{name}' успішно додано!")

def show_menu():
    """Красивий вивід списку страв (Завдання А)"""
    print("\n" + "="*40)
    print(f"{'МЕНЮ РЕСТОРАНУ':^40}")
    print("="*40)
    
    if not menu:
        print("Меню порожнє.")
    else:
        for i, dish in enumerate(menu, 1):
            print(f"{i}. {dish['назва'].upper()} — {dish['ціна']} грн")
            print(f"   {dish['опис']}")
            print("-" * 20)
    print("="*40)

def main():
    
    while True:
        print("\n1. Додати страву (Add)")
        print("4. Показати меню (Show)")
        print("0. Вихід (Exit)")
        
        choice = input("Оберіть дію: ")
        
        if choice == '1':
            add_dish()
        elif choice == '4':
            show_menu()
        elif choice == '0':
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()
