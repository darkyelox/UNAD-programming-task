import tkinter as tk
from ..entities.client import Client
from ..utils.utils import show_errors_messages
from ..utils.exceptions_logger import ExceptionsLoggerHandler
from ..database.simulated_database import db

class CreateClientDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Tk = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.title('Register Client')
        self.geometry('300x200')
        self.canceled = False # just to track if the window was canceled
        self.exc_logger = ExceptionsLoggerHandler('clients') # registers the exception handler

        # builds the form
        self.build_form()

    # validates the user object if there is an error it raises an exception
    def validate_client(self, client: Client):
        errors = client.validate()

        if(len(errors) > 0):
            show_errors_messages(parent=self, title="Failed to create client", errors=errors)
            raise RuntimeError("There were errors in the Client form") # raises error should not close the app


    # on cancel closes the dialog
    def cancel(self):
        self.canceled = True
        self.destroy()

    # saves the client
    def save(
        self,
        first_name: str,
        last_name: str,
        birthdate: str,
    ):
        # creates client instance
        client = Client(firstName=first_name, lastName=last_name, birthdate=birthdate)

        # when no error then save the user in the simulated db
        def onSuccess():
            db.save_client(client)
            self.destroy()

        # handles the execution and errors, if there is an error it is written into a log
        # otherwise executes the onSuccess handler
        self.exc_logger.handle(
            execute=lambda: self.validate_client(client),
            onSuccess=lambda: onSuccess()
        )


    # builds the form using plain TkInter
    def build_form(self):
        frame = tk.Frame(master = self)

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

        actions_frame = tk.Frame(frame)

        cancel_button = tk.Button(master=actions_frame, text= "Cancel", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, anchor=tk.W)

        save_button = tk.Button(master=actions_frame, text= "Save Client", command=lambda: self.save(
            first_name_entry.get(), 
            last_name=last_name_entry.get(), 
            birthdate=birthdate_entry.get()
        ))
        save_button.pack(side=tk.RIGHT, anchor=tk.W)

        actions_frame.grid(row=3, column=0, columnspan=2)

        frame.pack()