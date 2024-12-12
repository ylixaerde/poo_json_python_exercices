import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Obtenir la résolution de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        screen_resolution = screen_height * screen_width
        print("Résolution de l'écran :", screen_width, "x", screen_height)
        standard_screen_width = 1920
        standard_screen_height = 1080
        standard_screen_resolution = standard_screen_height * standard_screen_width
        scale_value = (screen_resolution/standard_screen_resolution)
        print(f"Scale value : {scale_value}")
        customtkinter.set_widget_scaling(scale_value)  # widget dimensions and text size
        customtkinter.set_window_scaling(scale_value)  # window geometry dimensions

        self.title("APP Maestro")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()