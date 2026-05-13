from .client import Client
from .service import BaseService
from datetime import date
import re

class Reservation:
    def __init__(
        self,
        client: Client,
        services: list[BaseService],
        date: date,
    ):
        self.client = client
        self.services = services
        self.date = date

    def calculate_total(self):
        services_price = 0

        for service in self.services:
            services_price += service.calculate_price()

        return services_price
    
    def validate(self):
        errors: list[str] = []
        
        if(self.client == None):
            errors.append('The client should not be empty')

        if(len(self.services) == 0):
            errors.append('The services are empty')

        date_pattern = r"\d{4}-\d{2}-\d{2}"
        if(not re.fullmatch(date_pattern, self.date)):
            errors.append("The reservation date should have the format YYYY-MM-DD");

        return errors