from main import Museum, Artwork, Exhibition, Visitor, Ticket, Pricing
from datetime import datetime


# The addition of new art to the museum.
def test_add_new_art():
    # Create a museum instance
    louvre = Museum("Louvre Museum", "Paris")

    # Create artworks
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "permanent galleries")
    artwork2 = Artwork("Starry Night", "Vincent van Gogh", datetime(1889, 1, 1), "exhibition halls")
    artwork3 = Artwork("The Thinker", "Auguste Rodin", datetime(1904, 1, 1), "outdoor spaces")

    # Add artworks to the museum
    artwork1.add_to_museum(louvre)
    artwork2.add_to_museum(louvre)
    artwork3.add_to_museum(louvre)

    # Assertion
    assert len(louvre.artworks) == 3
    assert len(louvre.permanent_galleries) == 1
    assert len(louvre.exhibition_halls) == 1
    assert len(louvre.outdoor_spaces) == 1

    print(f"\nAll Artworks in the Museum:")
    for artwork in louvre.artworks:
        print(artwork.display_artwork())


# The opening of a new exhibition or event at the museum.
def test_open_new_exhibition():
    # Create a museum instance
    louvre = Museum("Louvre Museum", "Abu Dhabi")

    # Create artworks
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "permanent galleries")
    artwork2 = Artwork("Starry Night", "Vincent van Gogh", datetime(1889, 1, 1), "exhibition halls")

    # Create exhibitions
    exhibition1 = Exhibition("Spring Art Exhibition", "outdoor spaces", datetime(2024, 5, 1), datetime(2024, 5, 15))
    exhibition2 = Exhibition("Modern Art Exhibition", "exhibition halls", datetime(2024, 4, 1), datetime(2024, 5, 1))

    # Add artworks to exhibitions
    exhibition1.add_artwork(artwork1)
    exhibition2.add_artwork(artwork2)

    # Add exhibitions to the museum
    louvre.add_exhibition(exhibition1)
    louvre.add_exhibition(exhibition2)

    # Print exhibitions and associated artworks
    print("\nAll Exhibitions in the Museum:")
    for exhibition in louvre.get_all_exhibitions():
        print(f"\nExhibition: {exhibition.name}")
        print("Artworks:")
        for artwork in exhibition.list_of_artworks:
            print(f"- {artwork.title}: {artwork.section_location}")


# The purchase of tickets by an individual or tour group for an event.
def test_purchase_tickets():
    # Define pricing
    pricing = Pricing(adult_price=63, vat=0.05, child_price=0, student_price=0, senior_price=0, group_discount=0.5)

    # Define ticket
    ticket = Ticket(ticket_id=1, adult_price=63, vat=0.05, child_price=0, student_price=0, senior_price=0,
                    group_discount=0.5, online_ticket=True)

    # Define visitor
    visitor = Visitor("Mariam", 30)

    # Purchase ticket
    ticket_price = visitor.buy_ticket(ticket, pricing)

    # Assertion
    assert ticket_price == 63 * (1 + 0.05)  # Adult ticket price + VAT

    print(f"\nTicket Price: {ticket_price}")


def test_display_payment_receipts():
    # Define pricing
    pricing = Pricing(adult_price=63, vat=0.05, child_price=0, student_price=0, senior_price=0, group_discount=0.5)

    # Define tickets for adult and child
    ticket1 = Ticket(ticket_id=1, adult_price=63, vat=0.05, child_price=0, student_price=0, senior_price=0,
                     group_discount=0.5, online_ticket=True)  # Adult ticket
    ticket2 = Ticket(ticket_id=2, adult_price=0, vat=0, child_price=0, student_price=0, senior_price=0,
                     group_discount=0, online_ticket=True)  # Child ticket

    # Define visitors
    visitor1 = Visitor("Mariam ", 10)
    visitor2 = Visitor("Afra", 30)

    # Purchase tickets
    total_bill = visitor1.buy_ticket(ticket1, pricing) + visitor2.buy_ticket(ticket2, pricing)

    # Display payment receipt
    print(f"Total Bill: {total_bill}")


if __name__ == "__main__":
    test_add_new_art()
    test_open_new_exhibition()
    test_purchase_tickets()
    test_display_payment_receipts()

