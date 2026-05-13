import tkinter as tk
from ..entities.client import Client
from ..utils.utils import show_errors_messages
from ..utils.exceptions_logger import ExceptionsLoggerHandler
from ..database.simulated_database import db

exc_logger = ExceptionsLoggerHandler('clients')

def validate_client(parent: tk.Tk, client: Client):
    errors = client.validate()

    if(len(errors) > 0):
        show_errors_messages(parent=parent, title="Failed to create client", errors=errors)
        raise RuntimeError("There were errors in the Client form")


def submit_data(
    parent: tk.Tk,
    first_name: str,
    last_name: str,
    birthdate: str,
):
    client = Client(firstName=first_name, lastName=last_name, birthdate=birthdate)

    exc_logger.handle(
        execute=lambda: validate_client(parent, client),
        onSuccess=lambda: db.save_client(client)
    )


def create_client_window(parent: tk.Tk):
    dialog = tk.Toplevel(parent)
    dialog.title('Register client')
    dialog.geometry('400x500')

    frame = tk.Frame(master = dialog)

    first_name_label = tk.Label(frame, text="First Name:")
    first_name_label.grid(row=0, column=0, padx=10, pady=10)

    first_name_entry = tk.Entry(frame)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tk.Label(frame, text="Last Name:")
    last_name_label.grid(row=1, column=0, padx=10, pady=10)
    
    last_name_entry = tk.Entry(frame)
    last_name_entry.grid(row=1, column=1)

    birthdate_label = tk.Label(frame, text="Birthdate:")
    birthdate_label.grid(row=2, column=0, padx=10, pady=10)
    
    birthdate_entry = tk.Entry(frame)
    birthdate_entry.grid(row=2, column=1)

    submit_btn = tk.Button(frame, text="Save Client", command=lambda: submit_data(dialog, first_name_entry.get(), last_name=last_name_entry.get(), birthdate=birthdate_entry.get()))
    submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

    frame.pack()