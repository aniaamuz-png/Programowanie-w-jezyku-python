class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
       return f'Library in {self.city} {self.street} {self.zip_code} open on: {self.open_hours}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f'Employee data {self.first_name}'

class Book:
    def __init__(self, library: Library, publication_date, author_name: str, author_surname: str, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f' Book data {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}'

class Order:
    def __init__(self, employee: Employee, student: str, books: list[Book], order_date) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f'Book {self.books} shipped by {self.employee} to {self.student}'

from datetime import date
# === Biblioteki ===
library1 = Library(
    city="Warszawa",
    street="Krakowskie Przedmieście 10",
    zip_code="00-001",
    open_hours="8:00-18:00",
    phone="111222333"
)

library2 = Library(
    city="Kraków",
    street="Rynek Główny 1",
    zip_code="30-001",
    open_hours="9:00-17:00",
    phone="444555666"
)

# === Pracownicy ===
employee1 = Employee(
    "Jan", "Kowalski",
    date(2020, 5, 1),
    date(1990, 3, 15),
    "Warszawa", "Mickiewicza 5", "01-234", "999888777"
)

employee2 = Employee(
    "Anna", "Nowak",
    date(2019, 4, 10),
    date(1988, 7, 22),
    "Kraków", "Długa 12", "30-002", "888777666"
)
# === Studenci ===
student1 = "Maria Wiśniewska"
student2 = "Tomasz Lewandowski"
student3 = "Katarzyna Kaczmarek"

# === Książki ===
book1 = Book(library1, date(2010, 1, 1), "Adam", "Mickiewicz", 350)
book2 = Book(library1, date(2015, 6, 10), "Henryk", "Sienkiewicz", 420)
book3 = Book(library2, date(2005, 3, 20), "Bolesław", "Prus", 280)
book4 = Book(library2, date(2018, 9, 5), "Stanisław", "Lem", 310)
book5 = Book(library1, date(2020, 12, 12), "Olga", "Tokarczuk", 290)

# === Zamówienia ===
order1 = Order(
    employee=employee1,
    student=student1,
    books=[book1, book2, book5],
    order_date=date.today()
)

order2 = Order(
    employee=employee2,
    student=student2,
    books=[book3, book4],
    order_date=date.today()
)
print(order1)
print("\n" + "=" * 50 + "\n")
print(order2)