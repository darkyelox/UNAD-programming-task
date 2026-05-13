from ..entities.client import Client
from ..entities.service import ServiceInclude, BaseService, SpaService, TurcoService, GymService
from ..entities.reservation import Reservation
from datetime import date

class SimulatedDB:
    clients: list[Client] = list()
    available_services: list[Client] = list()
    reservations: list[Client] = list()

    def __init__(self):
        self.seed_clients()
        self.seed_services()
        self.seed_reservations()

    def seed_clients(self):
        client1 = Client('Hugo', 'Hernandez', date(1998,4,25))
        client2 = Client('Paco', 'Murillo', date(2001,10,17))
        client3 = Client('Luis', 'Valencia', date(1970,6,7))

        self.clients.append(client1)
        self.clients.append(client2)
        self.clients.append(client3)

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

    def seed_reservations(self):
        reservation1 = Reservation(
            self.clients[0],
            [
                self.available_services[0]
            ],
            date(2025,5,18),
            100_000
        )

        reservation2 = Reservation(
            self.clients[1],
            [
                self.available_services[0],
                self.available_services[1]
            ],
            date(2025,5,18),
            200_000
        )

        self.reservations.append(reservation1)
        self.reservations.append(reservation2)

    def save_client(self, client: Client):
        self.clients.append(client)


db = SimulatedDB()