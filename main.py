import customtkinter as ctk
from Ventanas.ventana_principal import SistemaGestionUniversitaria

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = SistemaGestionUniversitaria()
    app.mainloop()
