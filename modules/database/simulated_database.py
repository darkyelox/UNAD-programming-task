from ..entities.client import Client
from ..entities.service import ServiceInclude, BaseService, SpaService, TurcoService, GymService
from ..entities.reservation import Reservation
from datetime import date

# This is a simulated database that has internal data
# this is useful for handling elements from different types
# utility methods for storing and retrieving data
class SimulatedDB:
    clients: list[Client] = list()
    available_services: list[Client] = list()
    reservations: list[Client] = list()

    def __init__(self):
        self.seed_clients()
        self.seed_services()
        self.seed_reservations()

    # creates example clients
    def seed_clients(self):
        client1 = Client('Hugo', 'Hernandez', date(1998,4,25))
        client2 = Client('Paco', 'Murillo', date(2001,10,17))
        client3 = Client('Luis', 'Valencia', date(1970,6,7))

        self.clients.append(client1)
        self.clients.append(client2)
        self.clients.append(client3)

    # creates example services with includes.
    def seed_services(self):
        spa1 = SpaService('Spa 1')
        spa1.applyIncludes([
            ServiceInclude(name = 'towel', price = 2000),
            ServiceInclude(name = 'massage', price = 5000),
            ServiceInclude(name = 'acupuncture', price = 10_000),
        ])

        turco1 = TurcoService('Turco 1', 20)
        turco1.applyIncludes([
            ServiceInclude(name = 'towel', price = 2000),
            ServiceInclude(name = 'cheese', price = 15_000),
            ServiceInclude(name = 'carbon', price = 20_000),
        ])

        gym1 = GymService('Gym 1', 'platinum')
        gym1.applyIncludes([
            ServiceInclude(name = 'dance', price = 5000),
            ServiceInclude(name = 'equipment', price = 25_000),
            ServiceInclude(name = 'access', price = 30_000),
        ])

        self.available_services.append(spa1)
        self.available_services.append(turco1)
        self.available_services.append(gym1)

    # creates example reservations
    def seed_reservations(self):
        reservation1 = Reservation(
            self.clients[0],
            [
                self.available_services[0]
            ],
            date(2025,5,18),
        )

        reservation2 = Reservation(
            self.clients[1],
            [
                self.available_services[0],
                self.available_services[1]
            ],
            date(2025,5,18)
        )

        self.reservations.append(reservation1)
        self.reservations.append(reservation2)

    # saves the client instance to the DB
    def save_client(self, client: Client):
        self.clients.append(client)

    # saves the service instance to the DB
    def save_service(self, service: BaseService):
        self.available_services.append(service)

    # saves the reservation instance to the DB
    def save_reservation(self, reservation: Reservation):
        self.reservations.append(reservation)

    # gets all client names
    def get_client_names(self):
        names = []
        for client in self.clients:
            names.append(client.firstName)
        
        return names
    
    # gets all services names
    def get_service_names(self):
        names = []
        for service in self.available_services:
            names.append(service.name)
        
        return names
    
    # find a client by first name
    def find_client(self, name: str):
        clientFound: Client = None
        for client in self.clients:
            if client.firstName == name:
                clientFound = client
        
        return clientFound

    # find a service by name
    def find_service(self, name: str):
        serviceFound: BaseService = None
        for service in self.available_services:
            if service.name == name:
                serviceFound = service
        
        return serviceFound

# creates the DB in memory.
db = SimulatedDB()