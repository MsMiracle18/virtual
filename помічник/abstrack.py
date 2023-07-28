from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_notes(self, notes):
        pass

    @abstractmethod
    def show_help(self, commands):
        pass

#клас ConsoleInterface, реалізує інтерфейс користувача в консолі
class ConsoleInterface(UserInterface):

    def show_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def show_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(f"Title: {note['title']}, Content: {note['content']}")

    def show_help(self, commands):
        print("Available commands:")
        for command, description in commands.items():
            print(f"{command}: {description}")

# Список контактів і нотаток
contacts = [
    {"name": "Valeriia Tovstenko", "phone": "123-456-7890"},
    {"name": "Vladyslav Sukhatskyi", "phone": "987-654-3210"}
]

notes = [
    {"title": "List products", "content": "1. Milk, 2. Eggs, 3. Bread"},
    {"title": "Zoom", "content": "Remember the 7:30 PM zoom with the team."}
]

commands = {
    "add_contact": "Add a new contact.",
    "delete_contact": "Delete an existing contact.",
    "add_note": "Add a new note.",
    "delete_note": "Delete an existing note.",
    "help": "Show available commands."
}

# Створила б'єкт консольного інтерфейсу
console_interface = ConsoleInterface()

# Виведення контактів
console_interface.show_contacts(contacts)

# Виведення нотаток
console_interface.show_notes(notes)

# Виведення доступних команд
console_interface.show_help(commands)
