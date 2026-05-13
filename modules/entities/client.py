from datetime import date
import re

class Client:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        birthdate: date,
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.birthdate = birthdate
    
    def validate(self):
        errors: list[str] = [];
        if(self.firstName == ''):
            errors.append("The first name should not be empty");
        if(self.lastName == ''):
            errors.append("The last name should not be empty");
        if(self.birthdate == ''):
            errors.append("The birthdate should not be empty");

        date_pattern = r"\d{4}-\d{2}-\d{2}"
        if(not re.fullmatch(date_pattern, self.birthdate)):
            errors.append("The birthdate should have the format YYYY-MM-DD");

        return errors;



