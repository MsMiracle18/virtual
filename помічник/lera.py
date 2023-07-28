import re
from datetime import datetime
import json
from pathlib import Path

# 1) зберігати контакти з іменами, адресами, номерами телефонів, email та днями 
# народження до книги контактів;

class AddressBook():
    contacts = {}

    dir_path = Path(__file__).parent
    filename = Path(fr'{dir_path}\addressbook.json')

    def unpackaging(self):
        with open(self.filename, 'r') as f:
            self.contacts.update(json.load(f))
    
    def packaging(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def input_error(func):
            def inner(*args):
                try:
                    return func(*args)
                except (KeyError, ValueError, IndexError):
                    print('\nCommand was entered incorrectly, please try again.\n') 
            return inner

    greeting = re.compile('hello', flags=re.IGNORECASE)
    add = re.compile('add', flags=re.IGNORECASE)
    change = re.compile('change', flags=re.IGNORECASE)
    phone = re.compile('phone', flags=re.IGNORECASE)
    show_all = re.compile('show all', flags=re.IGNORECASE)
    goodbye = re.compile(r'(good bye|close|exit)', flags=re.IGNORECASE)

    @input_error
    def hello():
        print("\nHow can i help you?\n")

    @input_error
    def adding(self, command):
        words = command.split(' ')
        name = words[1]
        args = words[2:]
        self.contacts[name] = args
        print('\nCompleted!\n')

# 2) виводити список контактів, у яких день народження через задану кількість 
#днів від поточної дати;

def days_to_bday(self, command):
        words = command.split(' ')
        n = words[1]
        BDAY_REGEX = re.compile(r"\d{2}\.\d{2}\.\d{4}")
        for name, args in self.contacts.items():
            for date in args:
                if re.search(BDAY_REGEX, date):
                    d, m, y = date.split('.')
                    now = datetime.now()
                    some_day = datetime(year=now.year, month=int(m), day=int(d))
                    diff = some_day - now
                    if diff.days <= n and diff.days >= 0:
                        print(f"{name}: {', '.join(args)}")

# 3) здійснення пошуку контактів серед контактів книги;
def search_contacts(self, search_term):
    print("Результати пошуку:")
    for contact in self.contacts:
        if search_term.lower() in contact.name.lower() or \
                search_term.lower() in contact.address.lower() or \
                search_term.lower() in contact.phone_number.lower() or \
                search_term.lower() in contact.email.lower():
            print("Ім'я: {}".format(contact.name))
            print("Адреса: {}".format(contact.address))
            print("Номер телефону: {}".format(contact.phone_number))
            print("Email: {}".format(contact.email))
            print("День народження: {}".format(contact.birthday.strftime("%Y-%m-%d")))
            print("---")

# 4) перевірка на правильність введеного номера телефону та email під час 
# створення або редагування запису та повідомляти користувача у разі 
# некоректного введення;

def add_contact(self, name, address, phone_number, email, birthday):
    if not self.validate_phone_number(phone_number):
        print("Некоректний номер телефону. Будь ласка, перевірте формат та спробуйте знову.")
        return
    if not self.validate_email(email):
        print("Некоректний email. Будь ласка, перевірте формат та спробуйте знову.")
        return

    contact = Contact(name, address, phone_number, email, birthday)
    self.contacts.append(contact)
    print("Контакт успішно доданий!")

def edit_contact(self, index, name, address, phone_number, email, birthday):
    if not self.validate_phone_number(phone_number):
        print("Некоректний номер телефону. Будь ласка, перевірте формат та спробуйте знову.")
        return
    if not self.validate_email(email):
        print("Некоректний email. Будь ласка, перевірте формат та спробуйте знову.")
        return

    if index < 0 or index >= len(self.contacts):
        print("Неправильний індекс контакту.")
        return

    contact = self.contacts[index]
    contact.name = name
    contact.address = address
    contact.phone_number = phone_number
    contact.email = email
    contact.birthday = birthday
    print("Контакт успішно відредагований!")

def validate_phone_number(self, phone_number):
    # Перевірка формату номера телефону за допомогою регулярного виразу
    pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$"
    return bool(re.match(pattern, phone_number))

def validate_email(self, email):
    # Перевірка формату email за допомогою регулярного виразу
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


#5) редагувати та видаляти записи з книги контактів;
def changing(self, command):
        words = command.split(' ')
        name = words[1]
        args = words[2:]
        self.contacts[name] = args
        print('\nCompleted!\n')

def deleting(self, command):
    arguments = command.split(' ')
    name = arguments[1]
    self.contacts(name)
    print('\nCompleted!\n')


address_book = AddressBook()
address_book.adding("add John Doe john.doe@example.com 1234567890")
print(address_book.contacts)

address_book = AddressBook()
address_book.contacts = {
    'John Doe': ['john.doe@example.com', '1234567890', '01.01.1990'],
    'Jane Smith': ['jane.smith@example.com', '9876543210', '02.02.1995']
}
address_book.days_to_bday("days_to_bday 7")
