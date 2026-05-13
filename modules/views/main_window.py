import tkinter as tk
from .create_client import create_client_window
from .create_service import ServicesDialog
    
class MainWindow(tk.Tk):
    def __init__(
        self,
    ):
        super().__init__()
        self.title("My Application")
        self.geometry("400x300")

        self.options()

    def show_create_service_dialog(self):
        sub = ServicesDialog(self)

    def options(self):
        frame = tk.Frame(master=self)

        register_client_button = tk.Button(frame, text="Register Client", command=lambda: create_client_window(self));
        register_client_button.pack()

        register_service_button = tk.Button(frame, text="Register Service", command=self.show_create_service_dialog);
        register_service_button.pack()

        frame.pack()

    def run(self):
        self.show_create_service_dialog()
        self.mainloop()
    