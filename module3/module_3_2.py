
def send_email(message, recipient, sender="university.help@gmail.com"):

    domains = [".com",".ru", ".net"]
    is_recipient_contain_true_domain = False
    is_recipient_contain_mail_separator = False
    is_sender_contain_true_domain = False
    is_sender_contain_mail_separator = False

    for word in domains:
        if word in recipient:
            is_recipient_contain_true_domain = True
        if word in sender:
            is_sender_contain_true_domain = True

    if '@' in recipient:
        is_recipient_contain_mail_separator = True
    if '@' in sender:
        is_sender_contain_mail_separator = True

    if is_recipient_contain_true_domain == False or is_recipient_contain_mail_separator == False or is_sender_contain_true_domain == False or is_sender_contain_mail_separator == False :
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
