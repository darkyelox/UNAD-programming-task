import tkinter as tk
from ..utils.utils import build_window_title
from .create_client import CreateClientDialog
from .create_service import ServicesDialog
from .create_reservation import CreateReservationDialog

# main window of the application     
class MainWindow(tk.Tk):
    def __init__(
        self,
    ):
        super().__init__()
        self.title("My Application")
        self.geometry("400x300")

        build_window_title(
            master=self,
            title="Reservation System",
            description="Create clients, services and reservations.",
        )

        # build options
        self.options()

    # shows client dialog
    def show_create_client_dialog(self):
        CreateClientDialog(self)

    # shows service dialog
    def show_create_service_dialog(self):
        ServicesDialog(self)

    # shows reservation dialog
    def show_create_reservation_dialog(self):
        CreateReservationDialog(self)

    def options(self):
        frame = tk.Frame(master=self)

        register_client_button = tk.Button(frame, text="Register Client", command=self.show_create_client_dialog);
        register_client_button.pack()

        register_service_button = tk.Button(frame, text="Register Service", command=self.show_create_service_dialog);
        register_service_button.pack()

        register_reservation_button = tk.Button(frame, text="Create Reservation", command=self.show_create_reservation_dialog);
        register_reservation_button.pack()


        frame.pack()

    def run(self):
        self.mainloop()
    