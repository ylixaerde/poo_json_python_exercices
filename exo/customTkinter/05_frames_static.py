import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="checkbox 3")
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        
    def get(self):
        checked_checkboxes = []
        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(self.checkbox_1.cget("text"))
        if self.checkbox_2.get() == 1:
            checked_checkboxes.append(self.checkbox_2.cget("text"))
        if self.checkbox_3.get() == 1:
            checked_checkboxes.append(self.checkbox_3.cget("text"))
        return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("APP Maestro")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

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

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())



app = App()
app.mainloop()