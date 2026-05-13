import tkinter as tk
from tkinter import messagebox
from ..entities.service import ServiceInclude, SpaService, TurcoService, GymService, BaseService
from ..utils.utils import show_errors_messages
from ..utils.exceptions_logger import ExceptionsLoggerHandler
from ..database.simulated_database import db
from .create_include import CreateIncludeDialog
from ..utils.utils import GlobalEffects

exc_logger = ExceptionsLoggerHandler('services')

class ServicesDialog(tk.Toplevel):
    def __init__(
        self,
        master: tk.Tk = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        self.title('Create Service')
        self.geometry('500x400')
        self.includes: list[ServiceInclude] = [ServiceInclude('test', 123)]
        self.effects = GlobalEffects()
        self.exc_logger = ExceptionsLoggerHandler('services')
        self.service: BaseService = None

        self.build_form()

    # Shows a dialog for deleting includes.
    def show_delete_dialog(self, includeToRemove: ServiceInclude):
        result = messagebox.askokcancel(
            parent=self, title="Delete include", message="¿Are you sure you want to remove this include?"
        )

        if result:
            self.includes.remove(includeToRemove)
            self.effects.exec_effect('update_grid')

    def build_service_includes_table(self, parent: tk.Tk):
        container_frame = tk.Frame(master=parent)
            
        # builds the headers of the datatable
        headers_frame = tk.Frame(master=container_frame)
        headers_frame.rowconfigure(0, weight=1)
        headers_frame.columnconfigure(tuple(range(3)), weight=1)
        headers_frame.columnconfigure(0, minsize=200)
        headers_frame.columnconfigure(1, minsize=100)
        headers_frame.columnconfigure(2, minsize=100)

        titles_font = ("Arial", 10, "bold")
        serial_title = tk.Label(master=headers_frame, text="Serial", font=titles_font)
        serial_title.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")
        hourly_price_title = tk.Label(
            master=headers_frame, text="Precio hora", font=titles_font
        )
        hourly_price_title.grid(row=0, column=1, padx=0, pady=10, sticky="nsew")
        
        actions_title = tk.Label(master=headers_frame, text="Acciones", font=titles_font)
        actions_title.grid(row=0, column=5, padx=0, pady=10, sticky="nsew", columnspan=3)
        headers_frame.pack(fill=tk.X)

        grid_frame: tk.Frame = None

        def build_grid():
            nonlocal grid_frame

            grid_frame = tk.Frame(
                master=container_frame,
            )

            if len(self.includes) == 0:
                grid_frame.columnconfigure(0, weight=1)
                empty_message = tk.Label(
                    master=grid_frame,
                    text="There are not includes...",
                    justify=tk.CENTER,
                )
                empty_message.grid(row=0, column=0, pady=30, sticky="nsew")

            # loop for creating datatable rows by each bycicle.
            for include in self.includes:
                row_frame = tk.Frame(master=grid_frame)
                row_frame.rowconfigure(0, weight=1)
                row_frame.columnconfigure(tuple(range(2)), weight=1)
                row_frame.columnconfigure(0, minsize=100)
                row_frame.columnconfigure(1, minsize=100)

                base_cell_frame = {
                    "master": row_frame,
                    "relief": tk.RAISED,
                    "borderwidth": 1,
                    "bg": "white",
                }

                name_frame = tk.Frame(**base_cell_frame)
                name_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
                name_label = tk.Label(
                    master=name_frame, text=include.name, bg="white"
                )
                name_label.pack(fill=tk.X, padx=10, pady=10)

                price_frame = tk.Frame(**base_cell_frame)
                price_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
                price_label = tk.Label(
                    master=price_frame, text=include.price, bg="white"
                )
                price_label.pack(fill=tk.X, padx=10, pady=10)

                        

                delete_button_icon = tk.PhotoImage(file="delete.png")
                delete_button = tk.Button(
                    master=row_frame,
                    image=delete_button_icon,
                    command=lambda: self.show_delete_dialog(
                        includeToRemove=include
                    ),
                )
                delete_button.image = delete_button_icon
                delete_button.grid(row=0, column=7, padx=0, pady=0, sticky="nsew")

                row_frame.pack(fill=tk.X)
            grid_frame.pack(fill=tk.X)

        build_grid()
        container_frame.grid(row=2, column=0, columnspan=2)

         # effect function to rebuild the grid.
        def on_update():
            nonlocal grid_frame

            if grid_frame:
                grid_frame.destroy()
                build_grid()

        # registers a function for rebuilding the grid when required.
        self.effects.add_effect('update_grid', on_update) 
        

    def open_add_include_form(self):
        dialog = CreateIncludeDialog(master = self)
        dialog.wait_window()
        if not dialog.canceled:
            self.includes.append(dialog.include)
            self.effects.exec_effect('update_grid')

    def validate_service(self, service: BaseService):
        errors = service.validate_service()

        if(len(errors) > 0):
            show_errors_messages(parent=self, title="Failed to create service", errors=errors)
            raise RuntimeError("There were errors in the Service form")

    def cancel(self):
        self.canceled = True
        self.destroy()

    def save(self, name: str, type: str, plan: str, duration: str):
        service: BaseService = None

        def onSuccess():
            self.service = service
            self.destroy()

        match type:
            case 'Spa':
                service = SpaService(name)
            case 'Turco':
                service = TurcoService(name, duration)
            case 'Gym':
                service = GymService(name, plan)

        self.exc_logger.handle(
            execute=lambda: self.validate_service(service),
            onSuccess=lambda: onSuccess()
        )

    def build_form(self):
        frame = tk.Frame(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(tuple(range(2)), weight=1)

        name_label = tk.Label(frame, text="Service Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        name_entry = tk.Entry(frame)
        name_entry.grid(row=0, column=1)

        include_actions_frame = tk.Frame(frame)

        add_button = tk.Button(master=include_actions_frame, text= "Add Include", command=self.open_add_include_form)
        add_button.pack(side=tk.LEFT, anchor=tk.W)

        include_actions_frame.grid(row=1, column=0, columnspan=2)

        self.build_service_includes_table(frame)

        type_label = tk.Label(frame, text="Service Type:")
        type_label.grid(row=3, column=0, padx=10, pady=10)

        

        type_entry_variable = tk.StringVar(frame)
        plan_entry_variable = tk.StringVar(frame)

        duration_frame = tk.Frame(master=frame)
        
        duration_label = tk.Label(duration_frame, text="Duration:")
        duration_label.grid(row=0, column=0, padx=10, pady=10)

        duration_entry = tk.Entry(duration_frame)
        duration_entry.grid(row=0, column=1)

        plan_frame = tk.Frame(master=frame)
        
        plan_label = tk.Label(plan_frame, text="Plan:")
        plan_label.grid(row=0, column=0, padx=10, pady=10)

        plan_entry_options=['gold', 'platinum']
        plan_entry = tk.OptionMenu(plan_frame, plan_entry_variable, *plan_entry_options)
        plan_entry.grid(row=0, column=1)

        def on_type_change(value):
            duration_frame.grid_forget()
            plan_frame.grid_forget()
            match value:
                case 'Turco':
                    duration_frame.grid(row=4, column=0, columnspan=2)
                case 'Gym':
                    plan_frame.grid(row=4, column=0, columnspan=2)


        type_entry_options=['Spa', 'Turco', 'Gym']
        type_entry = tk.OptionMenu(frame, type_entry_variable, *type_entry_options, command=on_type_change)
        type_entry.grid(row=3, column=1, padx=10, pady=10)

        actions_frame = tk.Frame(frame)

        cancel_button = tk.Button(master=actions_frame, text= "Cancel", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, anchor=tk.W)

        save_button = tk.Button(master=actions_frame, text= "Save", command=lambda: self.save(
            name_entry.get(),
            type_entry_variable.get(),
            plan_entry_variable.get(),
            duration_entry.get()
        ))
        save_button.pack(side=tk.RIGHT, anchor=tk.W)

        actions_frame.grid(row=5, column=0, columnspan=2)

        frame.pack()

