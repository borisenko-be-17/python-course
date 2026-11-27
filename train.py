command = input("Введите команду: ").strip().lower()

if command == "ключ":
    print("Вы взяли ключ!")
elif command == "выход":
    print("Пока!")
else:
    print("Неизвестная команда!")