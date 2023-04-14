class ParkingGarage:
    def __init__(self, tickets: int):
        self.tickets = [i for i in range(tickets)]
        self.parkingSpaces = [i for i in range(tickets)]
        self.currentTicket = {}
    
    def takeTicket(self):
        ticket_number = self.tickets.pop()
        parking_number = self.parkingSpaces.pop()
        self.currentTicket[str(ticket_number)] = 'Occupied'
        print(f'Your ticket number is {ticket_number}, your parking number is {parking_number}. Your ticket status is {self.currentTicket[str(ticket_number)]}')

        


my_garage = ParkingGarage(50)

my_garage.takeTicket();