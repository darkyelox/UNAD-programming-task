from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
from collections.abc import Callable

#
def show_errors_messages(parent:tk.Tk, title:str, errors: list[str]):
    message = "\n * ".join(errors)
    messagebox.showerror(parent=parent, title=title, message=message)


# Builds a title and description frame.
def build_window_title(master: tk.Misc, title: str, description: str):
    title_frame = tk.Frame(master=master, pady=25)

    custom_font = tkFont.Font(family="Arial", size=25)

    title_label = tk.Label(
        master=title_frame,
        text=title,
        font=custom_font,
    )
    title_label.pack(fill=tk.X)

    description_label = tk.Label(
        master=title_frame,
        text=description,
        font=("Arial", "18", "italic"),
    )
    description_label.pack(fill=tk.X)

    title_frame.pack(fill=tk.X)

# A class for holding effects, it serve as a store for 
# function references with a given name that can be
# executed in other places.
class GlobalEffects:
    # Dict for registering functions for updates
    # this is a good option for preventing parameter drilling.
    __effects: dict[str, Callable]

    def __init__(self):
        self.__effects = dict()

    # Adds the effect to the dict with a given name
    # the effect is a function reference.
    def add_effect(self, name: str, func: Callable):
        self.__effects[name] = func

    # Executes the effect with the given name.
    def exec_effect(self, name: str):
        self.__effects[name]()