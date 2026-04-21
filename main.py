from random import choice

from unicodedata import category

menu = [

{ "назва": "Борщ",
  "ціна": 120.0,
  "опис": "Традиційний український борщ з яловичиною та сметаною",
  "категорія": "супи"
  },

{ "назва": "Вареники",
  "ціна": 95.0,
  "опис": "З картоплею та смаженою цибулею",
  "категорія": "основні"
  },

{"назва": "Узвар",
 "ціна": 40.0,
 "опис": "Напій із сухофруктів",
 "категорія": "сухофрукти"
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
    category = input("Категорія: ")

    menu.append({"назва": name, "ціна": price, "опис": descr, "категорія": category})
    print(f"Страву '{name}' успішно додано!")

def edit_dish():
    """"Редагування страви"""
    print("\n--- Редагувати страву --- ")
    name = input("Введіть назву страви дя редагування: ")

    found = False

    for dish in menu:
        if dish['назва'].lower() == name.lower():
            found = True
            print('Знайдено! Що хочеш змінити?')
            print('1. Ціна')
            print('2. Опис')
            print('3. Категорія')

            choice = input('Оберіть: ')

            if choice == '1':
                try:
                    new_prise = float(input('Нова ціна: '))
                    if new_prise < 0:
                        print("Ціна не може бути від'ємною")
                    else:
                        dish['ціна'] = new_prise
                        print('Ціну змінено')
                except:
                    print('Помилка вводу')

            elif choice == '2':
                new_descr = input('Новий опис: ')
                dish['опис'] = new_descr
                print('Опис зміненно')

            elif choice == '3':
                new_cat = input('Нова категорія: ')
                dish['категорія'] = new_cat
                print('Категорію змінено')

            else:
                print('Невірний вибір')

    if not found:
        print("Такої страви не існує!")

def show_menu():
    """Красивий вивід списку страв (Завдання А)"""
    print("\n" + "="*40)
    print(f"{'МЕНЮ РЕСТОРАНУ':^40}")
    print("="*40)
    
    if not menu:
        print("Меню порожнє.")
    else:
        categories = []
        for dish in menu:
            if dish['категорія'] not in categories:
                categories.append(dish['категорія'])

        for cat in categories:
            print(f"\n=== {cat.upper()} ===")

        for i, dish in enumerate(menu, 1):
            print(f"{i}. {dish['назва'].upper()} — {dish['ціна']} грн")
            print(f"   {dish['опис']}")
            print("-" * 20)
    print("="*40)

def main():
    
    while True:
        print("\n1. Додати страву (Add)")
        print("2. Редагувати страву (Edit)")
        print("4. Показати меню (Show)")
        print("0. Вихід (Exit)")
        
        choice = input("Оберіть дію: ")
        
        if choice == '1':
            add_dish()
        elif choice == '2':
            edit_dish()
        elif choice == '4':
            show_menu()
        elif choice == '0':
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()

