import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("APP Maestro")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="click here", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()