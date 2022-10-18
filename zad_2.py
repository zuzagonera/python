class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka: {self.city}, {self.street}, {self.zip_code}, {self.open_hours}, {self.phone}'


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
        return f'Pracownik: {self.first_name}, {self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone}'


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka: {self.library}, {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages}'


class Order:
    def __init__(self, employee: Employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie: {self.employee}, {self.student}, {self.books}, {self.order_date}'


class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index

    def __str__(self) -> str:
        return f'Dane studenta: {self.name} {self.surname}, numer indeksu {self.index}'


library0 = Library("Katowice", "Uniczowska 40", "40-748", "9:00 - 17:00", "500500501")
library1 = Library("Katowice", "Adamskiego 50", "40-000", "9:00 - 17:00", "500500502")
employee0 = Employee("Joanna", "Nowak", "03.12.2005", "13.02.1981", "Katowice", "Młyńska", "40-100", "500500503")
employee1 = Employee("Janusz", "Kowalski", "01.01.2006", "14.03.1982", "Katowice", "3 Maja", "40-101", "500500504")
employee2 = Employee("Marek", "Malinowski", "02.02.2007", "15.04.1983", "Katowice", "Mikołowska", "40-102", "500500505")
book0 = Book(library0, "08.10.1999", "Maria", "Kowalczyk", "150")
book1 = Book(library0, "09.11.2000", "Maria", "Kowalczyk", "155")
book2 = Book(library0, "02.01.2001", "Bartosz", "Nowak", "160")
book3 = Book(library1, "03.02.2002", "Bartosz", "Nowak", "165")
book4 = Book(library1, "04.05.2003", "Bartosz", "Nowak", "170")
student0 = Student("Jan", "Kowalski", "14000")
student1 = Student("Anna", "Nowak", "140001")
order0 = Order(employee0, student0, book0, "01.11.2022")
order1 = Order(employee1, student1, book4, "02.11.2022")

print(f'{order0},\n{order1}')

