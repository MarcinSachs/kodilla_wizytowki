from contacts import BaseContact, BusinessContact
from faker import Faker

contacts = []


def create_contacts(type='private', qty=1):
    for i in range(qty):
        fake = Faker(locale='pl_PL', providers=None)
        name = fake.name().split()
        email = fake.email()
        phone = fake.phone_number()
        if type == 'business':
            company_name = fake.company()
            company_phone = fake.phone_number()
            position = fake.job()
            contacts.append(BusinessContact(
                name[0], name[1], email, phone, company_phone, company_name, position))
    else:
        contacts.append(BaseContact(name[0], name[1], phone, email))
