import tkinter as tk
from ..entities.service import BaseService
from ..entities.reservation import Reservation
from ..utils.exceptions_logger import ExceptionsLoggerHandler
from ..utils.utils import show_errors_messages
from ..database.simulated_database import db


class CreateReservationDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Tk = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.title('Create Reservation')
        self.geometry('500x200')
        self.canceled = False
        self.services: list[BaseService] = [] # services internal list
        self.exc_logger = ExceptionsLoggerHandler('reservations')

        self.build_form()


    # adds the service to the internal list
    def add_service(self, serviceName: str):
        service = db.find_service(serviceName)

        self.services.append(service)

    # validates the reservation object
    # raises an error if the object is not valid.
    def validate_reservation(self, reservation: Reservation):
        errors = reservation.validate()

        if(len(errors) > 0):
            show_errors_messages(parent=self, title="Failed to create reservation", errors=errors)
            raise RuntimeError("There were errors in the Reservation form")

    def cancel(self):
        self.canceled = True
        self.destroy()

    # first gets the client by its name and then validates and saves the 
    # reservation using the simulated DB.
    def save(
        self,
        clientName: str,
        date: str,
    ):
        client = db.find_client(clientName)

        reservation = Reservation(client, self.services, date)

        def onSuccess():
            db.save_reservation(reservation)
            self.destroy()

        self.exc_logger.handle(
            execute=lambda: self.validate_reservation(reservation),
            onSuccess=lambda: onSuccess()
        )
    
    # creates a form for relating a client and services to a reservation.
    def build_form(self):
        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(tuple(range(2)), weight=1)

        client_label = tk.Label(frame, text="Select client:")
        client_label.grid(row=0, column=0, padx=10, pady=10)

        client_entry_value = tk.StringVar(frame)
        client_entry_options = db.get_client_names()
        client_entry = tk.OptionMenu(frame, client_entry_value, *client_entry_options)
        client_entry.grid(row=0, column=1, padx=10, pady=10)

        service_label = tk.Label(frame, text="Select service:")
        service_label.grid(row=1, column=0, padx=10, pady=10)

        service_entry_value = tk.StringVar(frame)
        service_entry_options = db.get_service_names()
        service_entry = tk.OptionMenu(frame, service_entry_value, *service_entry_options)
        service_entry.grid(row=1, column=1, padx=10, pady=10)

        add_service_button = tk.Button(master=frame, text= "Add Service", command=lambda: self.add_service(service_entry_value.get()))
        add_service_button.grid(row=1, column=2, padx=10, pady=10)

        date_label = tk.Label(frame, text="Reservation date(YYYY-MM-DD):")
        date_label.grid(row=2, column=0, padx=10, pady=10)
        
        date_entry = tk.Entry(frame)
        date_entry.grid(row=2, column=1)

        actions_frame = tk.Frame(frame)

        cancel_button = tk.Button(master=actions_frame, text= "Cancel", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, anchor=tk.W)

        save_button = tk.Button(master=actions_frame, text= "Save Reservation", command=lambda: self.save(
            client_entry_value.get(), 
            date_entry.get()
        ))
        save_button.pack(side=tk.RIGHT, anchor=tk.W)

        actions_frame.grid(row=3, column=0, columnspan=3)

        frame.pack()