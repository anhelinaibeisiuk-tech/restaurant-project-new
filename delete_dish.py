def delete_dish(menu):
    """Функція Учасника В: Видалення та підрахунок"""
    if not menu:
        print("❌ Меню порожнє, видаляти нічого.")
        return

    mode = input("\nВиберіть режим видалення:\n1 - За назвою\n2 - За категорією\nВаш вибір: ")

    if mode == '1':
        name_to_delete = input("Введіть назву страви: ").strip().lower()
        initial_len = len(menu)

        # Використовуємо menu[:] щоб змінити оригінальний список
        menu[:] = [dish for dish in menu if dish.get('name', '').lower() != name_to_delete]

        if len(menu) < initial_len:
            print(f"✅ Страву '{name_to_delete}' видалено.")
        else:
            print(f"⚠️ Страву з назвою '{name_to_delete}' не знайдено.")

    elif mode == '2':
        cat_to_delete = input("Введіть назву категорії: ").strip().lower()
        initial_len = len(menu)

        menu[:] = [dish for dish in menu if dish.get('category', '').lower() != cat_to_delete]

        removed = initial_len - len(menu)
        print(f"🔥 Видалено страв у категорії: {removed}")

    else:
        print("❌ Помилка: оберіть 1 або 2.")

    # Обов'язкова умова завдання: підрахунок залишку
    print(f"📊 Залишилося страв у меню: {len(menu)}")