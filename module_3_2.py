# Домашняя работа по уроку "Способы вызова функции"
# Задача "Рассылка писем"



def send_email(message, recipient, sender='universiry.help@gmail.com'):
    # Блокировка отправки самому себе
    if sender == recipient:
        print('\nНельзя отправить письмо самому себе')
        return
    else:
        # Проверка адреса на отсутствие @ или домена верхнего уровня
        D = '@'
        end_of_adress = ['.com', '.ru', '.net']
        for i in end_of_adress:
            check1 = True
            check2 = True
            if i not in sender or D not in sender:
                check1 = False
            else:
                check1 = True
            if i not in recipient or D not in recipient:
                check2 = False
            else:
                check2 = True
            if not check1 and not check2:
                print(f'\nНевозможно отправить письмо с адреса {sender} на адрес {recipient}')
                return
            else:
                # Проверка на отправителя
                if sender == 'universiry.help@gmail.com':
                    print(f'\nПисьмо успешно отправлено с адреса {sender} на адрес {recipient}')
                else:
                    print(f'\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
                break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
