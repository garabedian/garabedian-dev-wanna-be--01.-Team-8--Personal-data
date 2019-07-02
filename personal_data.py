
""" Изчитане на файла """
personal_records = []
with open("personal_data.txt") as file_object:
    """ Opens a file as object """
    lines = file_object.readlines()
    for line in lines:
        """ Stores data in a list [personal_records] """
        personal_record = list(map(str, line.strip().split(", ")))
        personal_records.append(personal_record)

cin = None

while True:

    if cin == 0:
        break

    """ Избор от меню """
    print()
    print("Изберете опция от следното меню: 0 = Изход от програмата ")
    print("                                 1 = Търси по име        ")
    print("                                 2 = Търси по град       ")
    print("                                 3 = Търси по номер      ")
    print("                                 4 = Виж всички контакти ")
    print("                                 5 = Добави нов контакт  ")

    cin = input("Моля, въведете Вашия избор ==> ")

    """ Проверка за валидност на избора """
    try:
        cin = int(cin)
    except ValueError:
        print("\nХайде, моля Ви да въведете число!\n")
        continue
    else:
        if not 0 <= cin <= 5:
            print("\nХайде отново, защото числото трябва да бъде от нула до пет!\n")
            continue

    name_of_person = ""
    town_of_person = ""
    phone_of_person = ""
    filtered_records = []

    if cin == 1:
        """ Търси по име """
        key_word = input("Въведете критерий за търсене - име  : ").lower()
        filtered_records = list(filter(lambda element: element[0] == key_word, personal_records))
        if filtered_records:
            for record in filtered_records:
                if key_word == record[0]:
                    print('\n' + ', '.join(str(x.title()) for x in record))
        else:
            if [personal_record for personal_record in personal_records if key_word in personal_record]:
                print("\nКлючът съществува, но е различен атрибут! ")
            else:
                print("\nКлючът HE съществува в Базата Данни! ")
        continue
    elif cin == 2:
        """ Търси по град """
        key_word = input("Въведете критерий за търсене - град : ").lower()
        filtered_records = list(filter(lambda element: element[1] == key_word, personal_records))
        if filtered_records:
            for record in filtered_records:
                if key_word == record[1]:
                    print('\n' + ', '.join(str(x.title()) for x in record))
        else:
            if [personal_record for personal_record in personal_records if key_word in personal_record]:
                print("\nКлючът съществува, но е различен атрибут! ")
            else:
                print("\nКлючът HE съществува в Базата Данни! ")
        continue
    elif cin == 3:
        """ Търси по номер """
        key_word = input("Въведете критерий за търсене - тел.№ ").lower()
        filtered_records = list(filter(lambda element: element[2] == key_word, personal_records))
        if filtered_records:
            for record in filtered_records:
                if key_word == record[2]:
                    print('\n' + ', '.join(str(x.title()) for x in record))
        else:
            if [personal_record for personal_record in personal_records if key_word in personal_record]:
                print("\nКлючът съществува, но е различен атрибут! ")
            else:
                print("\nКлючът HE съществува в Базата Данни! ")
        continue
    elif cin == 4:
        """ Виж всички контакти """
        for record in range(1, len(personal_records)):
            print('\n' + ', '.join(str(x.title()) for x in personal_records[record]))
        break
    elif cin == 5:
        """ Добави нов контакт """
        name_of_person = input("Име   : ").lower()
        town_of_person = input("Град  : ").lower()
        phone_of_person = input("Teл. № ").lower()
        """ Добавяне на записа """
        personal_records.append([name_of_person, town_of_person, phone_of_person])
        """ Записване на файла """
        with open("personal_data.txt", 'w') as file_object:
            """ Opens a file in write mode as object """
            for line in personal_records:
                """ Stores each element in a single line """
                file_object.write(", ".join(str(x) for x in line)+'\n')
        break
