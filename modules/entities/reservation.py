from .client import Client
from .service import BaseService
from datetime import date

class Reservation:
    def __init__(
        self,
        client: Client,
        services: list[BaseService],
        date: date,
        price: int,
    ):
        self.client = client
        self.services = services
        self.date = date
        self.price = price

    def calculate_total(self):
        services_price = 0

        for service in self.services:
            services_price += service.calculate_price()

        return services_price + self.price