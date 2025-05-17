import re

# Чтение файла text.txt
with open('text.txt', 'r') as file:
    text = file.read()

# Поиск email-адресов
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)

# Запись email-адресов в файл emails.txt
with open('emails.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')

# Поиск номеров телефонов в формате +7-XXX-XXX-XX-XX
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)

# Запись номеров телефонов в файл phones.txt
with open('phones.txt', 'w') as file:
    for phone in phones:
        file.write(phone + '\n')

# Поиск слов с заглавной буквы
capital_words = re.findall(r'[A-Z][a-z]', text)

# Запись слов с заглавной буквы в файл capital_words.txt
with open('capital_words.txt', 'w') as file:
    for word in capital_words:
        file.write(word + '\n')
