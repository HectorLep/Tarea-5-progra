import customtkinter as ctk
from customtkinter import *

from .Ventana_nose import Nose  
from . import util_ventana

class Main(ctk.CTk):  
    def __init__(self):
        super().__init__()
        self.title("Prueba nose hola")
        self.geometry("800x600")
        util_ventana.centrar_ventana(self, 800, 600)
        self.config_window()

    def config_window(self):
        self.iconbitmap('.\Semana 8\Ventanas\gato.ico') 
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def open_nose(self):
        Nose(self)

        
