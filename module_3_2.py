def send_email(massage, recipient, *,sender = "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender \
            or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)

mail = str(send_email(massage=input("Введите текст: "),
                            recipient=input("Введите адрес получателя: "),
                            sender=input("Введите свой адрес ")))