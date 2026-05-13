from abc import ABC, abstractmethod 

class ServiceInclude:
    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def validate(self):
        errors: list[str] = []
        
        if(self.name == ''):
            errors.append('Name should not be empty')

        if(self.price == ''):
            errors.append('Price should not be empty')

        if(self.price == '0'):
            errors.append('Price should not be zero')

        return errors

class BaseService(ABC):
    includes: list[ServiceInclude]
    
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @abstractmethod
    def describe_service(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def validate_service(self) -> list[str] :
        pass

    def applyIncludes(self, includes: list[ServiceInclude]):
        self.includes = includes

class SpaService(BaseService):
    def __init__(self, name: str):
        super().__init__(name)
        
    def describe_service(self):
        return "This is the more complete SPA service you would buy in your life!!!"
    
    def calculate_price(self):
        total_price = 0

        for include in self.includes:
            total_price += include.price

        return total_price + total_price * 0.2
    
    def validate_service(self):
        errors: list[str] = []
        
        if(self.name == ''):
            errors.append('Name should not be empty')

        return errors
    
class TurcoService(BaseService):
    def __init__(self, name: str, duration: int):
        super().__init__(name)
        self.duration = duration

    def describe_service(self):
        return "We have the best turco in town, de-intoxicate yourself!!!"
    
    def calculate_price(self):
        total_price = 0

        for include in self.includes:
            total_price += include.price

        total_price += 100 * self.duration

        return total_price
    
    def validate_service(self):
        errors: list[str] = []
        
        if(self.name == ''):
            errors.append('Name should not be empty')

        if(self.duration == '' or self.duration == '0'):
            errors.append('Duration should not be empty or zero')
        
        return errors
    
class GymService(BaseService):
    def __init__(self, name: str, plan: str):
        super().__init__(name)
        self.plan = plan

    def describe_service(self):
        return "Don't be a wimp, train yourself until you are the strongest!!!"
    
    def calculate_price(self):
        total_price = 0

        for include in self.includes:
            total_price += include.price

        if self.plan == 'gold':
            total_price -= total_price * 0.2

        if self.plan == 'platinum':
            total_price -= total_price * 0.3

        return total_price
    
    def validate_service(self):
        errors: list[str] = []
        
        if(self.name == ''):
            errors.append('Name should not be empty')

        if(self.plan == ''):
            errors.append('Plan should not be empty')
        
        return errors