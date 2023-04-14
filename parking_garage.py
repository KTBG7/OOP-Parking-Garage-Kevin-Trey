class ParkingGarage:
    def __init__(self, tickets: int):
        self.tickets = [i for i in range(tickets)]
        self.parkingSpaces = [i for i in range(tickets)]
        self.currentTicket = {}
        self.active_tickets = []

    def takeTicket(self):
        ticket_number = self.tickets.pop()
        parking_number = self.parkingSpaces.pop()
        self.active_tickets.insert(0,"ticket"+ str(ticket_number))
        self.currentTicket["ticket"+ str(ticket_number)] = 'Occupied'
        print(f'Your ticket number is {ticket_number}, your parking number is {parking_number} ')
    def payForParking(self):
        parking_number = input("Please pay 20 dollars")
        if len(parking_number) >= 1:
            print("you have 15 minutes to leave your ticket has been paid")
            self.currentTicket[self.active_tickets.pop()] = "Paid"
        while len(parking_number)< 1:
            parking_number = input("Please pay 20 dollars")
        print("you have 15 minutes to leave your ticket has been paid")
        self.currentTicket[self.active_tickets.pop()] = "Paid"

my_garage = ParkingGarage(50)

my_garage.takeTicket()
my_garage.payForParking()