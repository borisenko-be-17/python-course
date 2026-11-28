room = "lobby"
has_artifact = False
flashlight = False
flash = False
alarm = 0

print("Добро пожаловать на ночную смену в музее!")
print("Цель: найдите пропажу и выйдите через служебный выход.")
print("Введите help, чтобы узнать список команд.")
while True:
    command = input ("\nВведите команду: ").strip().lower()
    if command == "help":
        print ("Доступные команды: look, go <зал>, take <предмет>, use <предмет>, exit")
    elif command == "exit":
        print ("Вы закончили игру")
        break
    elif command == "look":
        if room == "lobby":
            if flashlight == False:
                print ("Вы в лобби (lobby). Свет горит только тут. На столе лежит фонарик (flashlight) Пути: paintings (зал живописи), sculptures (зал скульптур), backdoor (служебный выход).")
            else:
                print ("Вы в лобби (lobby). Свет горит только тут. Пути: paintings (зал живописи), sculptures (зал скульптур), backdoor (служебный выход).")
        elif room == "paintings":
            print ("Вы в зале живописи (paintings). Пути: lobby (лобби), archeo (зал археологии).")
        elif room == "sculptures":
            print ("Вы в зале скульптур (sculptures). Пути: lobby (лобби).")
        elif room == "archeo":
            print ("Вы в зале археологии (archeo). Пути: paintings (зал живописи), storage (хранилище).")
        elif room == "storage":
            if has_artifact == False:
                print ("Вы в хранилище (storage). На столе лежит пропавший артефакт! Пути: archeo.")
            else:
                print("В хранилище ничего нет. Пути: archeo.")
        elif room == "backdoor":
            print("Вы у служебного выхода (backdoor). Пути: lobby.")

#go
    elif command.startswith("go "):
        if room == "lobby":
            if command == "go paintings":
                if flashlight == True:
                    if flash == True:
                        room = "paintings"
                        print("Вы перешли в зал живописи (paintings).")
                    else:
                        print ("Фонарик выключен, ничего не видно. Включите фонарик.")
                else:
                    print ("Возьмите фонарик.")
            elif command == "go sculptures":
                if flashlight == True:
                    if flash == True:
                        room = "sculptures"
                        print("Вы перешли в зал скульптур (sculptures).")
                    else:
                        print ("Фонарик выключен, ничего не видно. Включите фонарик.")
                else:
                    print ("Возьмите фонарик.")
            elif command == "go backdoor":
                if flashlight == True:
                    if flash == True:
                        room = "backdoor"
                        if has_artifact == True:
                            print("Вы вынесли артефакт через служебный выход! Победа!")
                            break
                        else:
                            print("Вы подошли к служебному выходу (backdoor). Артефакта нет, заберите его")
                    else:
                        print ("Фонарик выключен, ничего не видно. Включите фонарик.")
                else:
                    print ("Возьмите фонарик")
            elif command == "go archeo" or command =="go storage":
                alarm +=1
                print ("Из лобби нельзя пойти в эту комнату. Уровень тревоги: ", alarm)
            else:
                alarm+=1
                print ("Такой комнаты не существует. Уровень тревоги: ", alarm)

    
        elif room == "paintings":
            if command == "go lobby":
                room = "lobby"
                print("Вы вернулись в лобби (lobby).")
            elif command == "go archeo":
                if flash == True:
                    room = "archeo"
                    print("Вы перешли в зал археологии (archeo).")
                else:
                    print ("Фонарик выключен, ничего не видно. Включите фонарик.")
            elif command == "go backdoor" or command == "go storage" or command == "go scultures":
                alarm += 1
                print ("Из зала живописи нельзя пойти в эту комнату. Уровень тревоги: ", alarm)
            else:
                alarm +=1
                print ("Такой комнаты не существует. Уровень тревоги: ", alarm)


        elif room == "sculptures":
            if command == "go lobby":
                room = "lobby"
                print("Вы вернулись в лобби (lobby).")
            elif command == "go archeo" or command == "go storage" or command == "go backdoor" or command == "go paintings":
                alarm += 1
                print ("Из зала скульптур нельзя пойти в эту комнату. Уровень тревоги: ", alarm)
            else:
                alarm += 1
                print ("Такой комнаты не существует. Уровень тревоги: ", alarm)


        elif room == "archeo":
            if command == "go paintings":
                if flash == True:
                    room = "paintings"
                    print("Вы вернулись в зал живописи (paintings).")
                else:
                    print ("Фонарик выключен, ничего не видно. Включите фонарик.")
            elif command == "go storage":
                if flash == True:
                    room = "storage"
                    print("Вы вошли в хранилище (storage).")
                else:
                    print ("Фонарик выключен, ничего не видно. Включите фонарик.")
            elif command == "go lobby" or command == "go backdoor" or command == "go sculptures":
                alarm +=1
                print ("Из зала археологии нельзя пойти в эту комнату. Уровень тревоги: ", alarm)
            else:
                alarm += 1
                print ("Такой комнаты не существует. Уровень тревоги: ", alarm)


        elif room == "storage":
            if command == "go archeo":
                if flash == True:
                    room = "archeo"
                    print("Вы вернулись в зал археологии (archeo).")
                else:
                    print ("Фонарик выключен, ничего не видно. Включите фонарик.")
            elif command == "go lobby" or command =="go backdoor" or command == "go sculptures" or command == "go paintings":
                alarm +=1
                print ("Из хранилища нельзя пойти в эту комнату. Уровень тревоги: ", alarm)
            else:
                alarm += 1
                print ("Такой комнаты не существует. Уровень тревоги: ", alarm)


        else: 
            if room == "backdoor":
                if command == "go lobby":
                    room = "lobby"
                    print ("Вы вернулись в лобби.")
                elif command == "go sculptures" or command == "go paintings" or command == "go storage" or command == "go archeo":
                    alarm += 1
                    print ("Из служебного выхода нельзя пойти в эту комнату. Уровень тревогии: ", alarm)
                else:
                    alarm += 1
                    print ("Такой комнаты не существует. Уровень тревоги: ", alarm)

#take
    elif command.startswith("take "):
        if command == "take artifact":
            if room == "storage":
                if has_artifact == False:
                    has_artifact = True
                    print("Вы забрали артефакт!")
                else:
                    print("Вы уже забрали артефакт, в хранилище ничего нет.")
            else:
                alarm = alarm + 1
                print("Тут нет артефакта.", "Уровень тревоги: ", alarm)
        elif command == "take flashlight":
            if room == "lobby":
                if flashlight == False:
                    flashlight = True
                    print ("Вы подобрали фонарик.")
                else:
                    print ("Фонарик уже у вас.")
            else:
                alarm = alarm + 1
                print("Тут нет фонарика. Уровень тревоги: ", alarm)
        else:
            alarm +=1
            print ("Нет такой команды. Уровень тревоги: ", alarm)
     
    elif command.startswith("use "):
        if command == "use flashlight":
            if flashlight == True:
                if flash == False:
                    flash = True
                    print ("Фонарик включен.")
                else:
                    flash = False
                    print ("Фонарик выключен.")
            else:
                print ("У вас нет фонарика.")
        else:
            alarm+=1
            print ("Нет такой команды. Уровень тревоги: ", alarm)
    else:
        alarm +=1
        print ("Нет такой команды. Уровень тревоги: ", alarm)
    if alarm >= 5:
        print("Сработала сигнализация! Уровень тревоги достиг 5. Поражение!")
        break