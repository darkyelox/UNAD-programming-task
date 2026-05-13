import tkinter as tk
from ..entities.service import ServiceInclude
from ..utils.exceptions_logger import ExceptionsLoggerHandler
from ..utils.utils import show_errors_messages

class CreateIncludeDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Tk = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.title('Create Include')
        self.geometry('300x200')
        self.include = None
        self.canceled = False
        self.exc_logger = ExceptionsLoggerHandler('includes')

        self.build_form()

    def cancel(self):
        self.canceled = True
        self.destroy()

    def validate_include(self, include: ServiceInclude):
        errors = include.validate()

        if(len(errors) > 0):
            show_errors_messages(parent=self, title="Failed to create include", errors=errors)
            raise RuntimeError("There were errors in the Include form")

    def add_include(self, name: str, price: int):
        include = ServiceInclude(name, price)

        def onSuccess():
            self.include = include
            self.destroy()

        self.exc_logger.handle(
            execute=lambda: self.validate_include(include),
            onSuccess=lambda: onSuccess()
        )

    
    def build_form(self):
        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(tuple(range(2)), weight=1)

        name_label = tk.Label(frame, text="Include Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        name_entry = tk.Entry(frame)
        name_entry.grid(row=0, column=1)

        price_label = tk.Label(frame, text="Price:")
        price_label.grid(row=1, column=0, padx=10, pady=10)

        price_entry = tk.Entry(frame)
        price_entry.grid(row=1, column=1)

        actions_frame = tk.Frame(frame)

        cancel_button = tk.Button(master=actions_frame, text= "Cancel", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, anchor=tk.W)

        save_button = tk.Button(master=actions_frame, text= "Add Include", command=lambda: self.add_include(
            name_entry.get(),
            price_entry.get()
        ))
        save_button.pack(side=tk.RIGHT, anchor=tk.W)

        actions_frame.grid(row=2, column=0, columnspan=2)

        frame.pack()
