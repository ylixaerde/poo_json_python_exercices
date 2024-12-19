import customtkinter as ctk
import tkinter as tk
from typing import Union, Callable

class FloatSpinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # modification de la taille de l'ui en fonction de la résolution de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        screen_resolution = screen_height * screen_width
        print("Résolution de l'écran :", screen_width, "x", screen_height)
        standard_screen_width = 1920
        standard_screen_height = 1080
        standard_screen_resolution = standard_screen_height * standard_screen_width
        scale_value = (screen_resolution/standard_screen_resolution)
        print(f"Scale value : {scale_value}")
        ctk.set_widget_scaling(scale_value)
        ctk.set_window_scaling(scale_value)

        # Brand Label
        self.brandLabel = ctk.CTkLabel(self, text="Marque")
        self.brandLabel.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        # Brand Entry Field
        self.brandEntry = ctk.CTkEntry(self, placeholder_text="Toyota")
        self.brandEntry.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="ew")
        # Model Label
        self.modelLabel = ctk.CTkLabel(self, text="Modèle")
        self.modelLabel.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        # Model Entry Field
        self.modelEntry = ctk.CTkEntry(self, placeholder_text="Corolla GR")
        self.modelEntry.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="ew")
        # Année Label
        self.yearLabel = ctk.CTkLabel(self, text="Année")
        self.yearLabel.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        # Année option menu
        year_list = list(range(2025, 1995, -1))
        year_list_str = [str(year) for year in year_list]
        year_list_str.append("Ancêtre")
        self.yearOptionMenu = ctk.CTkOptionMenu(self, values=year_list_str)
        self.yearOptionMenu.grid(row=2, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        # Couleurs Label
        self.colorLabel = ctk.CTkLabel(self, text="Couleurs")
        self.colorLabel.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        # Couleurs checkbox
        self.checkboxVar = tk.StringVar(value="Choice 1")
        self.choice1 = ctk.CTkCheckBox(self, text="Noir", variable=self.checkboxVar, onvalue="choice1", offvalue="c1")
        self.choice1.grid(row=3, column=1, padx=20, pady=10, sticky="ew")
        self.choice2 = ctk.CTkCheckBox(self, text="Blanc", variable=self.checkboxVar, onvalue="choice2", offvalue="c2")							 
        self.choice2.grid(row=3, column=2, padx=20, pady=10, sticky="ew")
        self.choice3 = ctk.CTkCheckBox(self, text="Rouge", variable=self.checkboxVar, onvalue="choice3", offvalue="c3")							 
        self.choice3.grid(row=3, column=3, padx=20, pady=10, sticky="ew")
        # Puissance moteur - Label
        self.powerLabel = ctk.CTkLabel(self, text="Puisance du moteur en ch")
        self.powerLabel.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        # Puissance du moteur - Spinbox        
        self.power_spinbox = FloatSpinbox(self, width=150, step_size=10)
        self.power_spinbox.grid(row=4, column=1, padx=20, pady=10, sticky="ew")
        self.power_spinbox.set(100)
        # Cylindrée moteur - Label
        self.engineLabel = ctk.CTkLabel(self, text="Cylindrée du moteur")
        self.engineLabel.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        # Cylindrée du moteur - Spinbox        
        self.engineLabel = FloatSpinbox(self, width=150, step_size=100)
        self.engineLabel.grid(row=5, column=1, padx=20, pady=10, sticky="ew")
        self.engineLabel.set(1600)
        # Prix - Label
        self.priceLabel = ctk.CTkLabel(self, text="Prix du véhicule en €")
        self.priceLabel.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        # Prix - Spinbox        
        self.price_spinbox = FloatSpinbox(self, width=150, step_size=500)
        self.price_spinbox.grid(row=6, column=1, padx=20, pady=10, sticky="ew")
        self.price_spinbox.set(20000)
        # Fuel consumption Label
        self.fuelLabel = ctk.CTkLabel(self, text="Consommation (l/100km)")
        self.fuelLabel.grid(row=7, column=0, padx=20, pady=10, sticky="ew")
        # Fuel consumption Entry Field
        self.fuelEntry = ctk.CTkEntry(self, placeholder_text="")
        self.fuelEntry.grid(row=7, column=1, columnspan=2, padx=20, pady=10, sticky="ew")
        # Encode Button
        self.encodeResultsButton = ctk.CTkButton(self, text="Enregistrer",command=self.encodeResults)
        self.encodeResultsButton.grid(row=10, column=1, columnspan=2, padx=20,pady=10, sticky="ew")

    def encodeResults(self):
            print("Test button")

if __name__ == "__main__":
    # gestion de l'apparence Dark mode et couleur verte
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")

    app = App()
    app.title("Gestion de voitures")
    appWidth, appHeight = 700, 600    
    app.geometry(f"{appWidth}x{appHeight}")
    app.mainloop()