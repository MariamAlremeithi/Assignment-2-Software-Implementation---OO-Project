# Defines the Museum class
class Museum:
    # Initialising the Museum class with name and location attributes
    def __init__(self, museum_name, location):
        self.museum_name = museum_name
        self.location = location
        # Creating a list to store artworks in the permanent galleries
        self.permanent_galleries = []
        self.exhibition_halls = []
        self.outdoor_spaces = []
        self.artworks = []
        self.exhibitions = []  # Add a list to store exhibitions

    # Method to return the name of the museum
    def get_museum_name(self):
        return self.museum_name

    # Method to set a new name for the museum
    def set_museum_name(self, museum_name):
        self.museum_name = museum_name

    # Method to return the location of the museum
    def get_location(self):
        return self.location

    # Method to set a new location for the museum
    def set_location(self, location):
        self.location = location

    # function to add an artwork to the museum and its specific section
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        if artwork.section_location == "permanent galleries":
            self.permanent_galleries.append(artwork)
        elif artwork.section_location == "exhibition halls":
            self.exhibition_halls.append(artwork)
        elif artwork.section_location == "outdoor spaces":
            self.outdoor_spaces.append(artwork)

    # Method to add an exhibition to the museum
    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    # Method to return all exhibitions of the museum
    def get_all_exhibitions(self):
        return self.exhibitions

    # this searches for a specific section of the museum and return its artworks
    def search_section(self, section):
        if section == "permanent galleries":
            return self.permanent_galleries
        elif section == "exhibition halls":
            return self.exhibition_halls
        elif section == "outdoor spaces":
            return self.outdoor_spaces


# Defines the Artwork class
class Artwork:
    # Initializing the Artwork class with the attributes
    def __init__(self, title, artist, date_of_creation, section_location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.section_location = section_location

    # function to return the title of the artwork
    def get_title(self):
        return self.title

    # function to set a new title for the artwork
    def set_title(self, title):
        self.title = title

    # function to return the artist of the artwork
    def get_artist(self):
        return self.artist

    # function to add the artwork to a museum
    def add_to_museum(self, museum):
        museum.add_artwork(self)

    # function to remove the artwork from a museum
    def remove_from_museum(self, museum):
        museum.artworks.remove(self)

    def set_artist(self, artist):
        self.artist = artist

    # function to display the artwork details
    def display_artwork(self):
        return f"Title: {self.title}, Artist: {self.artist}, Date of Creation: {self.date_of_creation}, Section Location: {self.section_location}"


class Exhibition:
    def __init__(self, name, exhibition_location, start_date, end_date):
        self.name = name
        self.exhibition_location = exhibition_location
        self.start_date = start_date
        self.end_date = end_date
        self.list_of_artworks = []  # Aggregation , whichInitialize an empty list to store artworks in the exhibition

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_days_opened(self):
        return (self.end_date - self.start_date).days

    def add_artwork(self, artwork):  # Artwork objects can exist without an Exhibition object
        self.list_of_artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.list_of_artworks.remove(artwork)


class Employee:
    # Initializing the Employee class with the attributes

    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role

    # function to display the details of the employee

    def display_employee_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}"


class Tour:
    def __init__(self, time_and_date, participating_visitors_num, tour_guide):
        self.time_and_date = time_and_date
        self.participating_visitors_num = participating_visitors_num
        self.tour_guide = tour_guide

    def cancel_tour(self):
        self.tour_guide.end_tour(self)

    def display_tour_info(self):
        return f"Time and Date: {self.time_and_date}, Participants: {self.participating_visitors_num}, Tour Guide: {self.tour_guide.name}"


class TourGuide(Employee):
    def __init__(self, employee_id, name, role, years_of_experience):
        # The constructor method for the TourGuide class
        super().__init__(employee_id, name, role)
        self.years_of_experience = years_of_experience
        self.tours = []  # Composition: TourGuide is composed of Tours

    def start_tour(self, time_and_date, participating_visitors_num):
        tour = Tour(time_and_date, participating_visitors_num, self)  # Creating a Tour object within TourGuide
        self.tours.append(tour)
        return tour

    def end_tour(self, tour):
        self.tours.remove(tour)


class Ticket:
    # The constructor method for the Ticket class
    def __init__(self, ticket_id, adult_price, vat, child_price, student_price, senior_price, group_discount,
                 online_ticket):
        self.ticket_id = ticket_id
        self.online_ticket = online_ticket
        self.pricing = Pricing(adult_price, vat, child_price, student_price, senior_price,
                               group_discount)  # composition

    # This method calculates the final price of the ticket
    def calculate_final_price(self, visitor_type, visitor_age):
        # The calculate_final_price method of the Pricing object is called
        return self.pricing.calculate_final_price(visitor_type, visitor_age)


class Pricing:
    def __init__(self, adult_price, vat, child_price, student_price, senior_price, group_discount):
        self.adult_price = adult_price
        self.vat = vat
        self.child_price = child_price
        self.student_price = student_price
        self.senior_price = senior_price
        self.group_discount = group_discount

    # This function calculates the final price based on the visitor's type and age
    def calculate_final_price(self, visitor_type, visitor_age):
        if visitor_type == "adult":
            return self.adult_price * (1 + self.vat)
        elif visitor_type == "child":
            return self.child_price * (1 + self.vat)
        elif visitor_type == "student":
            return self.student_price * (1 + self.vat)
        elif visitor_type == "senior":
            return self.senior_price * (1 + self.vat)
        elif visitor_type == "group":
            return self.adult_price * (1 + self.vat) * (1 - self.group_discount)


class Visitor:
    def __init__(self, visitor_name, visitor_age):
        self.visitor_name = visitor_name
        self.visitor_age = int(visitor_age)  # Convert to integer
        self.ticket = None  # Aggregation: Visitor has a ticket , currently its set to none becuasde the visitor does not have a ticket

    def buy_ticket(self, ticket, pricing):
        # Buying a ticket for the visitor
        global ticket_price
        self.ticket = ticket
        if 18 <= self.visitor_age <= 60:
            ticket_price = pricing.calculate_final_price("adult", self.visitor_age)  # Pass visitor's age
        elif self.visitor_age < 18 or self.visitor_age >= 60:
            ticket_price = 0  # Free ticket for children, students, and seniors
        return ticket_price

    def return_ticket(self):
        self.ticket = None

    # The name and age of the visitor are returned
    def display_visitor_info(self):
        return f"Visitor Name: {self.visitor_name}, Age: {self.visitor_age}"


# Initiating the creation of a prestigious museum
louvre_abu_dhabi = Museum("Louvre Abu Dhabi", "Abu Dhabi")
print(f"\nWelcome to the {louvre_abu_dhabi.get_museum_name()}!")

# Curating an iconic piece of art
bezique_game = Artwork("The Bezique Game", "Gustave Caillebotte", "1880", "permanent galleries")
print(f"Artwork in our possession: {bezique_game.get_title()} , by the artist {bezique_game.get_artist()} ")

# Adding the artwork to the museum's world-class collection
louvre_abu_dhabi.add_artwork(bezique_game)
print(f"{bezique_game.get_title()} has been added to the museum's Permanent collection since 2018 !.")


