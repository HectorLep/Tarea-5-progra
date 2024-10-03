import customtkinter as ctk
import tkinter as tk 
from .ventana_interfaz import New_ventana

class Nose(New_ventana):
    def __init__(self, parent):
        super().__init__(parent, 'black')
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color='black', corner_radius=0)
        self.sub.pack(fill='both', expand=True)
        
        self.label = ctk.CTkLabel(self.sub, text='Hola, soy una ventana nose', bg='black', fg='white')
        self.label.pack(fill='both', expand=True)
        