class ParkingGarage:
    """
        We initialized the class with tickets and parking which will be based off of the user's input or it'll default to 5.
        Then we initialize the currentTicket dict as well as the active tickets dict.
    """
    def __init__(self, tickets: int = 5):
        self.tickets = [i for i in range(tickets)]
        self.parkingSpaces = [i for i in range(tickets)]
        self.currentTicket = {}
        self.active_tickets = []
    """
        We grab the last values from both the ticket number and the parking number. Then we insert that number to the front
        of the active_tickets list, this is because if we have multiple tickets/parking numbers the pop will grab the largest value
        i.e if theres 50 tickets itll grab 49 and if we grab another we want to put 48 in front of the 49 to keep the numbers in the
        active ticket list ascending.
        Then we set the key = to ticket+ num and set it to occupied.
        finally we print their ticket and parking number.
    """
    def takeTicket(self):
        ticket_number = self.tickets.pop()
        parking_number = self.parkingSpaces.pop()
        self.active_tickets.insert(0,"ticket"+ str(ticket_number))
        self.currentTicket["ticket"+ str(ticket_number)] = 'Occupied'
        print(f'Your ticket number is {ticket_number}, your parking number is {parking_number} ')

    """
        We first ask for a payment, if they pay the first time aka the input is non empty we print out that they paid and set
        the currentTicket value to paid. Else we run a while loop that'll keep asking until the input is non empty, the rest stays
        the same once they satisfy the conditions.
    """
    def payForParking(self):
        parking_number = input("Please pay 20 dollars: ")
        if len(parking_number) >= 1:
            print("you have 15 minutes to leave your ticket has been paid")
            self.currentTicket[self.active_tickets.pop()] = "Paid"
        else:
            while len(parking_number)< 1:
                parking_number = input("Please pay 20 dollars: ")
                print("you have 15 minutes to leave your ticket has been paid")
                self.currentTicket[self.active_tickets.pop()] = "Paid"
    
    """
        We check if the first ticket grabbed has been paid if it has then we thank them and 
        we add back the tickets and parking spaces.
    """
    def leaveGarage(self):
        if self.currentTicket["ticket"+str(len(self.tickets))] == 'Paid':
            print('Thank you, have a nice day.')
            self.tickets.append(len(self.tickets))
            self.parkingSpaces.append(len(self.parkingSpaces))