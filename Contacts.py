

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone} {self.email}"

    def contact(self):
        print(
            f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name + " " + self.surname)


class BusinessContact(BaseContact):
    def __init__(self, name, surname, email, phone, company_phone, company_name, position):
        super().__init__(name, surname, email, phone)
        self.company_phone = company_phone
        self.company_name = company_name
        self.position = position

    def contact(self):
        print(
            f"Wybieram numer {self.company_phone} i dzwonię do {self.name} {self.surname}")
