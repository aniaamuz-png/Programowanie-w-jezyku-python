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
