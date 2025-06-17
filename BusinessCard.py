from faker import Faker


class BusinessCard:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

    def create_fake_card():
        fake = Faker()
        name = fake.name().split()
        company = fake.company()
        position = fake.job()
        email = fake.email()
        return BusinessCard(name[0], name[1], company, position, email)
