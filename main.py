from BusinessCard import BusinessCard

business_cards = []

for i in range(5):
    card = BusinessCard.create_fake_card()
    business_cards.append(card)

for card in business_cards:
    print(f"Name: {card.name}, Surname: {card.surname}, Company: {card.company}, "
          f"Position: {card.position}, Email: {card.email}")
